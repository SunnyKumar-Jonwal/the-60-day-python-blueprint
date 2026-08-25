import os
import sqlite3

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

DB_PATH = "day-58/examples/app.db"

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

router = APIRouter(prefix="/books", tags=["books"])


class Book(BaseModel):
    title: str
    author: str


@router.post("", status_code=201)
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


@router.get("")
def list_books():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM books").fetchall()
    connection.close()
    return [dict(row) for row in rows]


@router.get("/{book_id}")
def read_book(book_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(row)
