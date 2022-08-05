
from sqlalchemy import DECIMAL,  Column, Integer,  ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

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
