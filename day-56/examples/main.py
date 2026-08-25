import os
import sqlite3

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

DB_PATH = "day-56/examples/app.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str


@app.post("/books", status_code=201)
def create_book(book: Book):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (book.title, book.author),
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "title": book.title, "author": book.author}


@app.get("/books")
def list_books():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM books").fetchall()
    connection.close()
    return [{"id": row["id"], "title": row["title"], "author": row["author"]} for row in rows]


@app.get("/books/{book_id}")
def read_book(book_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": row["id"], "title": row["title"], "author": row["author"]}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    connection = get_connection()
    result = connection.execute(
        "UPDATE books SET title = ?, author = ? WHERE id = ?",
        (book.title, book.author, book_id),
    )
    connection.commit()
    connection.close()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book_id, "title": book.title, "author": book.author}


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    connection = get_connection()
    result = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status_code=204)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
