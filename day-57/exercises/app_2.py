from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str


@app.post("/items", status_code=201)
def create_item(item: Item):
    items.append(item.name)
    return {"id": len(items), "name": item.name}
