import os
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = "day-55/examples/app.db"

# Start each run of this demo from a clean database, so re-running it gives
# the same output every time -- a real app would NOT do this on every startup.
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create_item(item: Item):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO items (name, price) VALUES (?, ?)",
        (item.name, item.price),
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "name": item.name, "price": item.price}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row["id"], "name": row["name"], "price": row["price"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
