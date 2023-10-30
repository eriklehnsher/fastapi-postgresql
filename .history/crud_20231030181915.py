from databases import Database
from sqlalchemy import select

from database import database
from models import Product, ProductModel

async def create_product(product: ProductModel):
    query = Product.insert().values(**product.dict())
    product_id = await database.execute(query)
    return {**product.dict(), "id": product_id}

async def read_product(product_id: int):
    query = select([Product]).where(Product.c.id == product_id)
    product = await database.fetch_one(query)
    return product

async def read_products(skip: int = 0, limit: int = 10):
    query = select([Product]).offset(skip).limit(limit)
    products = await database.fetch_all(query)
    return products
