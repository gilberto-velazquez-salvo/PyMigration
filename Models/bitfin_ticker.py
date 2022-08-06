from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

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
    setOfRequest_id = Column(Integer)
    def __init__(self, symbol, bid, bid_size, ask, ask_size, daily_change, daily_change_relative, last_price, volume, high, low, setOfRequestId):
        self.symbol = symbol
        self.bid = bid
        self.bid_size = bid_size
        self.ask=ask
        self.ask_size=ask_size
        self.daily_change=daily_change
        self.daily_change_relative=daily_change_relative
        self.last_price=last_price
        self.volume=volume
        self.high=high
        self.low=low
        self.setOfRequest_id=setOfRequestId
