from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    priceFrom: str
    rating_point: float
    number_of_reviews: int
    number_of_sales: int
    username_reviews: str
    product_description: str
