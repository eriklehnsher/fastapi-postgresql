from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    priceFrom = Column(String)
    rating_point = Column(Float)
    number_of_reviews = Column(Integer)
    number_of_sales = Column(Integer)
    username_reviews = Column(String)
    product_description = Column(String)
