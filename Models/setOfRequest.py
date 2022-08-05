from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class setOfRequest(Base):
    __tablename__ = 'setOfRequest'
    id = Column(Integer, primary_key=True)
    timestamp=Column(TIMESTAMP)
    def __init__(self, timestamp):
        self.timestamp=timestamp