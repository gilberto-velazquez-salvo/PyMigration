
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class platformExchangePair(Base):
    __tablename__ = 'platformExchangePair'
    id = Column(Integer, primary_key=True)
    exchangePlatform_id = Column(Integer, ForeignKey("exchangePlatform.id"))
    currencyA_id=Column(Integer, ForeignKey("currency.id"))
    currencyB_id=Column(Integer, ForeignKey("currency.id"))
    pairSymbol = Column(String(200))
    #bidPricePlatform=relationship("bidPrice")