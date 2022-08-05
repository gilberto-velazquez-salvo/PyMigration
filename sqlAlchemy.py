from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import globalConfig as config
from sqlalchemy import create_engine

connection_string="mysql+pymysql://"+config.MYSQL_USER+":"+config.MYSQL_PASS+"@"+config.MYSQL_HOST+":"+config.MYSQL_PORT+"/"+config.MYSQL_DATABASE
engine = create_engine(connection_string)
Base = declarative_base()


class Listing(Base):
    __tablename__ = 'listings_sqlalchemy'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    
    host_id = Column(Integer)
    host_name = Column(String(50))
    
    neighbourhood_group = Column(String(20))
    neighbourhood = Column(String(20))
    
    latitude = Column(Float)
    longitude = Column(Float)
    
    room_type = Column(String(20))
    price = Column(Integer)
    minimum_nights = Column(Integer)
    
    number_of_reviews = Column(Integer)
    last_review = Column(Date, nullable=True)
    reviews_per_month = Column(Integer)
    calculated_host_listings_count = Column(Integer)
    availability_365 = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)