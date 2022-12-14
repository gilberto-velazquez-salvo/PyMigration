from ctypes.wintypes import DOUBLE
from decimal import Decimal
from sqlalchemy import DECIMAL, TIMESTAMP, Boolean, Column, Date, Float, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
import configuration as config

from sqlalchemy import create_engine

connection_string="mysql+pymysql://"+config.MYSQL_USER+":"+config.MYSQL_PASS+"@"+config.MYSQL_HOST+":"+config.MYSQL_PORT+"/"+config.MYSQL_DATABASE
engine = create_engine(connection_string)
Base = declarative_base()

class setOfRequest(Base):
    __tablename__ = 'setOfRequest'
    id = Column(Integer, primary_key=True)
    timestamp=Column(TIMESTAMP)
    requestTimestamp=relationship("bidPrice")
    bidPricePlatform=relationship("bitfin_ticker")
class currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    symbol = Column(String(10))
    scan = Column (Integer)
    def __init__(self, name, symbol, scan):
        self.name = name
        self.symbol = symbol
        self.scan = scan

class exchangePlatform(Base):
    __tablename__ = 'exchangePlatform'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    platformExchangePairs=relationship("platformExchangePair")
    def __init__(self, name):
        self.name = name

class platformExchangePair(Base):
    __tablename__ = 'platformExchangePair'
    id = Column(Integer, primary_key=True)
    exchangePlatform_id = Column(Integer, ForeignKey("exchangePlatform.id"))
    currencyA_id=Column(Integer, ForeignKey("currency.id"))
    currencyB_id=Column(Integer, ForeignKey("currency.id"))
    pairSymbol = Column(String(200))
    bidPricePlatform=relationship("bidPrice")
    

class bidPrice(Base):
    __tablename__ = 'bidPrice'
    id = Column(Integer, primary_key=True)
    setOfRequest_id = Column(Integer, ForeignKey("setOfRequest.id"))
    platformExchangePair_id=Column(Integer, ForeignKey("platformExchangePair.id"))
    bidPrice=Column(DECIMAL(16,3))
    askPrice=Column(DECIMAL(16,9))
    lastPrice=Column(DECIMAL(16,9))
    lowPrice=Column(DECIMAL(16,9))
    highPrice=Column(DECIMAL(16,9))
    volumePrice=Column(DECIMAL(16,9))


class bitfin_ticker(Base):
    __tablename__='bitfin_ticker'
    id=Column(Integer, primary_key=True)
    symbol=Column(String(100))
    bid=Column(DECIMAL(20,12))
    bid_size=Column(DECIMAL(20,12))
    ask=Column(DECIMAL(20,12))
    ask_size=Column(DECIMAL(20,12))
    daily_change=Column(DECIMAL(20,12))
    daily_change_relative=Column(DECIMAL(20,12))
    last_price=Column(DECIMAL(20,12))
    volume=Column(DECIMAL(20,12))
    high=Column(DECIMAL(20,12))
    low=Column(DECIMAL(20,12))
    setOfRequest_id = Column(Integer, ForeignKey("setOfRequest.id"))


class cexio_ticker(Base):
    __tablename__='cexio_ticker'
    id=Column(Integer, primary_key=True)   
    symbol=Column(String(100))
    low=Column(DECIMAL(20,12))
    high=Column(DECIMAL(20,12))
    last=Column(DECIMAL(20,12))
    volume=Column(DECIMAL(20,12))
    volume30d=Column(DECIMAL(20,12))
    priceChange=Column(DECIMAL(20,12))
    priceChangePercentage= Column(DECIMAL(20,12))
    bid=Column(DECIMAL(20,12))
    ask=Column(DECIMAL(20,12))
    setOfRequest_id = Column(Integer, ForeignKey("setOfRequest.id"))


class kraken_ticker(Base):
    __tablename__='kraken_ticker'
    id=Column(Integer, primary_key=True)   
    symbol=Column(String(100))
    ask=Column(DECIMAL(20,12))
    ask_whole_volume=Column(DECIMAL(20,12))
    ask_lot_volume=Column(DECIMAL(20,12))
    bid=Column(DECIMAL(20,12))
    bid_whole_volume=Column(DECIMAL(20,12))
    bid_lot_volume=Column(DECIMAL(20,12))
    last_trade_price=Column(DECIMAL(20,12))
    last_trade_volume=Column(DECIMAL(20,12))
    volume=Column(DECIMAL(20,12))
    volume_weighted_average_price=Column(DECIMAL(20,12))
    trades=Column(DECIMAL(20,12))
    low=Column(DECIMAL(20,12))
    high=Column(DECIMAL(20,12))
    opening_price=Column(DECIMAL(20,12))   
    setOfRequest_id = Column(Integer, ForeignKey("setOfRequest.id"))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)