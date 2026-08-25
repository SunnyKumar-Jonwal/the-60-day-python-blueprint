import os
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = os.environ.get("DB_PATH_OVERRIDE", "day-57/examples/app.db")

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
            name TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()

app = FastAPI()


class Item(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/items", status_code=201)
def create_item(item: Item):
    connection = get_connection()
    cursor = connection.execute("INSERT INTO items (name) VALUES (?)", (item.name,))
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "name": item.name}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return dict(row)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
