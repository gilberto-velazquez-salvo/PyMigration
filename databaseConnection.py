import globalConfig as config

from Models.exchangePlatform import exchangePlatform
from Models.currency import currency
from Models.setOfRequest import setOfRequest
from Models.platformExchangePair import platformExchangePair
from Models.bidPrice import bidPrice
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


connection_string="mysql+pymysql://"+config.MYSQL_USER+":"+config.MYSQL_PASS+"@"+config.MYSQL_HOST+":"+config.MYSQL_PORT+"/"+config.MYSQL_DATABASE
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)

def getPlaftormExchangePair():
        with Session() as session:
        #currencies=session.query(currency).filter(currency.name=="BITCOIN").all()
            return session.query(platformExchangePair).all()

def getCurrencies():
        with Session() as session:
            return session.query(currency).all()

def getValidCurrencies():
        with Session() as session:
            return session.query(currency).filter(currency.scan==1).all()

def getExchangePlatform():
        with Session() as session:
            return session.query(exchangePlatform).all()


with Session() as session:
    #currencies=session.query(currency).filter(currency.name=="BITCOIN").all()
    currencies=session.query(currency).all()


    print('### Recent currencies:')
    for movie in currencies:
        print(f'{movie.symbol} name')
    print('')


