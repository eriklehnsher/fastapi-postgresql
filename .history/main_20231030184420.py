# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Product
from schemas import Product as ProductPydantic

app = FastAPI()

# Tuyến API để tạo sản phẩm mới
@app.post("/products/", response_model=ProductPydantic)
def create_product(product: ProductPydantic, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Tuyến API để đọc danh sách sản phẩm
@app.get("/products/", response_model=list[ProductPydantic])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products
