from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

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