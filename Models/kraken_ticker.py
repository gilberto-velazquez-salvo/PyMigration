from sqlalchemy import DECIMAL, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class kraken_ticker(Base):
    __tablename__ = "kraken_ticker"
    id = Column(Integer, primary_key=True)
    symbol = Column(String(100))
    ask = Column(DECIMAL(20, 12))
    ask_whole_volume = Column(DECIMAL(20, 12))
    ask_lot_volume = Column(DECIMAL(20, 12))
    bid = Column(DECIMAL(20, 12))
    bid_whole_volume = Column(DECIMAL(20, 12))
    bid_lot_volume = Column(DECIMAL(20, 12))
    last_trade_price = Column(DECIMAL(20, 12))
    last_trade_volume = Column(DECIMAL(20, 12))
    volume = Column(DECIMAL(20, 12))
    volume_weighted_average_price = Column(DECIMAL(20, 12))
    trades = Column(DECIMAL(20, 12))
    low = Column(DECIMAL(20, 12))
    high = Column(DECIMAL(20, 12))
    opening_price = Column(DECIMAL(20, 12))
    setOfRequest_id = Column(Integer)

    def __init__(
        self,
        symbol,
        ask,
        ask_whole_volume,
        ask_lot_volume,
        bid,
        bid_whole_volume,
        bid_lot_volume,
        last_trade_price,
        last_trade_volume,
        volume,
        volume_weighted_average_price,
        trades,
        low,
        high,
        opening_price,
        setOfRequestId,
    ):
        self.symbol = symbol
        self.ask = ask
        self.ask_lot_volume = ask_lot_volume
        self.ask_whole_volume = ask_whole_volume
        self.bid = bid
        self.bid_whole_volume = bid_whole_volume
        self.bid_lot_volume = bid_lot_volume
        self.last_trade_price = last_trade_price
        self.last_trade_volume = last_trade_volume
        self.volume = volume
        self.volume_weighted_average_price = volume_weighted_average_price
        self.trades = trades
        self.low = low
        self.high = high
        self.opening_price = opening_price
        self.setOfRequest_id = setOfRequestId
