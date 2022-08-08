import globalConfig as config

from Models.exchangePlatform import exchangePlatform
from Models.currency import currency
from Models.setOfRequest import setOfRequest
from Models.platformExchangePair import platformExchangePair
from Models.bitfin_ticker import bitfin_ticker
from Models.cexio_ticker import cexio_ticker
from Models.kraken_ticker import kraken_ticker

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import desc
import datetime, time

connection_string = (
    "mysql+pymysql://"
    + config.MYSQL_USER
    + ":"
    + config.MYSQL_PASS
    + "@"
    + config.MYSQL_HOST
    + ":"
    + config.MYSQL_PORT
    + "/"
    + config.MYSQL_DATABASE
)
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)


def getPlaftormExchangePair():
    with Session() as session:
        # currencies=session.query(currency).filter(currency.name=="BITCOIN").all()
        return session.query(platformExchangePair).all()


def getCurrencies():
    with Session() as session:
        return session.query(currency).all()


def getValidCurrencies():
    with Session() as session:
        return session.query(currency).filter(currency.scan == 1).all()


def getExchangePlatform():
    with Session() as session:
        return session.query(exchangePlatform).all()


def storeStimestamp():
    with Session() as session:
        # timestamp1="NOW()"
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

        # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timsnow = setOfRequest(timestamp)
        session.add(timsnow)
        session.commit()
        # session.close()


def getLatestSetOfRequest():
    with Session() as session:
        # timestamp1="NOW()"
        return session.query(setOfRequest).order_by(setOfRequest.id.desc()).first()


def persistBitfinex(jsonBitfinex):
    setOfRequestObtained = getLatestSetOfRequest().id
    with Session() as session:
        for element in jsonBitfinex:
            bitelement = bitfin_ticker(
                element[0][1:],
                element[1],
                element[2],
                element[3],
                element[4],
                element[5],
                element[6],
                element[7],
                element[8],
                element[9],
                element[10],
                setOfRequestObtained,
            )
            session.add(bitelement)
        session.commit()


def persistCexio(arrayOfCurrencies, jsonCexio):
    setOfRequestObtained = getLatestSetOfRequest().id
    with Session() as session:
        for element in jsonCexio["data"]:
            symbol = element["pair"].split(":")[0] + element["pair"].split(":")[1]
            if symbol in arrayOfCurrencies:
                cexioElement = cexio_ticker(
                    symbol,
                    element["low"],
                    element["high"],
                    element["last"],
                    element["volume"],
                    element["volume30d"],
                    element["priceChange"],
                    element["priceChangePercentage"],
                    element["bid"],
                    element["ask"],
                    setOfRequestObtained,
                )
                session.add(cexioElement)
        session.commit()


def persistKraken(symbol, jsonKraken):
    setOfRequestObtained = getLatestSetOfRequest().id
    dictParameters = jsonKraken["result"][list(jsonKraken["result"].keys())[0]]
    with Session() as session:
        krakenElem = kraken_ticker(
            symbol,
            dictParameters["a"][0],
            dictParameters["a"][1],
            dictParameters["a"][2],
            dictParameters["b"][0],
            dictParameters["b"][1],
            dictParameters["b"][2],
            dictParameters["c"][0],
            dictParameters["c"][1],
            dictParameters["v"][0],
            dictParameters["p"][0],
            dictParameters["t"][0],
            dictParameters["l"][0],
            dictParameters["h"][0],
            dictParameters["o"][0],
            setOfRequestObtained,
        )

        session.add(krakenElem)
        session.commit()
