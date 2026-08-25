from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


@app.post("/products", status_code=201)
def create_product(product: Product):
    return product
