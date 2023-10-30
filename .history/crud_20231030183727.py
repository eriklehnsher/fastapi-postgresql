# crud.py
from sqlalchemy.orm import Session
from models import Product

# Tạo sản phẩm mới
def create_product(db: Session, product: Product):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Đọc danh sách sản phẩm
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

# Đọc sản phẩm theo ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Cập nhật sản phẩm
def update_product(db: Session, product_id: int, updated_product: Product):
    db_product = get_product(db, product_id)
    if db_product:
        for field, value in updated_product.dict().items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    return None

# Xóa sản phẩm
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product
    return None
