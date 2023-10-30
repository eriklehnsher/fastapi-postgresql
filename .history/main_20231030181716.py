from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import Base, engine, database
from models import Product, ProductModel

app = FastAPI()




Base.metadata.create_all(bind=engine)


@app.post("/products/", response_model=ProductModel)
async def create_product(product: ProductModel):
    query = Product.insert().values(**product.model_dump())
    product_id = await database.execute(query)
    return {**product.model_dump(), "id": product_id}

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
