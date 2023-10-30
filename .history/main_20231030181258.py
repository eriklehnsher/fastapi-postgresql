from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "postgresql://username:password@localhost/dbname"

database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ProductModel(BaseModel):
    product_name: str
    priceFrom: str
    rating_point: float
    number_of_reviews: int
    number_of_sales: int
    username_reviews: str
    product_description: str

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

Base.metadata.create_all(bind=engine)

class ProductInDB(ProductModel):
    id: int

@app.post("/products/", response_model=ProductModel)
async def create_product(product: ProductModel):
    query = Product.insert().values(**product.dict())
    product_id = await database.execute(query)
    return {**product.dict(), "id": product_id}

@app.get("/products/{product_id}", response_model=ProductModel)
async def read_product(product_id: int):
    query = Product.select().where(Product.c.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/", response_model=List[ProductModel])
async def read_products(skip: int = 0, limit: int = 10):
    query = Product.select().offset(skip).limit(limit)
    products = await database.fetch_all(query)
    return products
