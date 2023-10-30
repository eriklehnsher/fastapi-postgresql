# router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Product
import crud

router = APIRouter()

# Tạo sản phẩm mới
@router.post("/products/", response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# Đọc danh sách sản phẩm
@router.get("/products/", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

# Đọc sản phẩm theo ID
@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Cập nhật sản phẩm
@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = crud.update_product(db, product_id, updated_product)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Xóa sản phẩm
@router.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
