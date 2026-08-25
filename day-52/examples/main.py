from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class ItemOut(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/search")
def search(query: str, limit: int = 10):
    return {"query": query, "limit": limit}


@app.post("/items", response_model=ItemOut)
def create_item(item: Item):
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
