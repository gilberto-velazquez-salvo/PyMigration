from ctypes.wintypes import DOUBLE
from sqlalchemy import DECIMAL, TIMESTAMP, Column, Date, Float, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
import configuration as config

from sqlalchemy import create_engine

connection_string="mysql+pymysql://"+config.MYSQL_USER+":"+config.MYSQL_PASS+"@"+config.MYSQL_HOST+":"+config.MYSQL_PORT+"/"+config.MYSQL_DATABASE
engine = create_engine(connection_string)
Base = declarative_base()

class currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    symbol = Column(String(10))
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class exchangePlatform(Base):
    __tablename__ = 'exchangePlatform'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    platformExchangePairs=relationship("platformExchangePair")
    def __init__(self, name):
        self.name = name

class setOfRequest(Base):
    __tablename__ = 'setOfRequest'
    id = Column(Integer, primary_key=True)
    timestamp=Column(TIMESTAMP)
    requestTimestamp=relationship("bidPrice")

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


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)