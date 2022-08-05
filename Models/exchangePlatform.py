
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class exchangePlatform(Base):
    __tablename__ = 'exchangePlatform'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    #platformExchangePairs=relationship("platformExchangePair")
    def __init__(self, name):
        self.name = name