from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class cexio_ticker(Base):
    __tablename__='cexio_ticker'
    id=Column(Integer, primary_key=True)   
    symbol=Column(String(100))
    low=Column(DECIMAL(20,3))
    high=Column(DECIMAL(20,3))
    last=Column(DECIMAL(20,3))
    volume=Column(DECIMAL(20,3))
    volume30d=Column(DECIMAL(20,3))
    priceChange=Column(DECIMAL(20,3))
    priceChangePercentage= Column(DECIMAL(20,3))
    bid=Column(DECIMAL(20,3))
    ask=Column(DECIMAL(20,3))
    setOfRequest_id = Column(Integer)
    def __init__(self, symbol, low, high, last, volume, volume30d, priceChange, priceChangePercentage, bid, ask, setOfRequestId):
        self.symbol = symbol
        self.bid = low
        self.high = high
        self.last=last
        self.volume=volume
        self.volume30d=volume30d
        self.priceChange=priceChange
        self.priceChangePercentage=priceChangePercentage
        self.bid=bid
        self.ask=ask
        self.setOfRequest_id=setOfRequestId