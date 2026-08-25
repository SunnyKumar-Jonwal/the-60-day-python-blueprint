import os
import sqlite3

import pandas as pd
from models import Book, BookNotFoundError

DB_PATH = os.environ.get("DB_PATH_OVERRIDE", "day-59/project/library.db")

# Start each run from a clean database, so re-running the app gives the same
# seeded data every time -- a real app would NOT do this on every startup.
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


class BookRepository:
    def __init__(self, db_path=None):
        self.db_path = db_path or DB_PATH
        self._init_db()

    def _get_connection(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _init_db(self):
        connection = self._get_connection()
        connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                year INTEGER NOT NULL,
                copies_available INTEGER NOT NULL
            )
        """)
        connection.commit()
        connection.close()

    def _row_to_book(self, row):
        return Book(
            row["id"],
            row["title"],
            row["author"],
            row["genre"],
            row["year"],
            row["copies_available"],
        )

    def load_from_csv(self, csv_path):
        records = pd.read_csv(csv_path).to_dict("records")
        connection = self._get_connection()
        for record in records:
            connection.execute(
                """INSERT INTO books (title, author, genre, year, copies_available)
                   VALUES (?, ?, ?, ?, ?)""",
                (
                    record["title"],
                    record["author"],
                    record["genre"],
                    int(record["year"]),
                    int(record["copies_available"]),
                ),
            )
        connection.commit()
        connection.close()

    def add(self, book):
        connection = self._get_connection()
        cursor = connection.execute(
            """INSERT INTO books (title, author, genre, year, copies_available)
               VALUES (?, ?, ?, ?, ?)""",
            (book.title, book.author, book.genre, book.year, book.copies_available),
        )
        connection.commit()
        book.id = cursor.lastrowid
        connection.close()
        return book

    def get(self, book_id):
        connection = self._get_connection()
        row = connection.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
        connection.close()
        if row is None:
            raise BookNotFoundError(f"No book with id {book_id}")
        return self._row_to_book(row)

    def list_all(self):
        connection = self._get_connection()
        rows = connection.execute("SELECT * FROM books").fetchall()
        connection.close()
        return [self._row_to_book(row) for row in rows]

    def update(self, book_id, title, author, genre, year, copies_available):
        connection = self._get_connection()
        result = connection.execute(
            """UPDATE books SET title = ?, author = ?, genre = ?, year = ?, copies_available = ?
               WHERE id = ?""",
            (title, author, genre, year, copies_available, book_id),
        )
        connection.commit()
        connection.close()
        if result.rowcount == 0:
            raise BookNotFoundError(f"No book with id {book_id}")
        return self.get(book_id)

    def delete(self, book_id):
        connection = self._get_connection()
        result = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        connection.close()
        if result.rowcount == 0:
            raise BookNotFoundError(f"No book with id {book_id}")

    def checkout(self, book_id):
        book = self.get(book_id)
        book.checkout()
        connection = self._get_connection()
        connection.execute(
            "UPDATE books SET copies_available = ? WHERE id = ?", (book.copies_available, book_id)
        )
        connection.commit()
        connection.close()
        return book

    def search(self, query):
        connection = self._get_connection()
        rows = connection.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
            (f"%{query}%", f"%{query}%"),
        ).fetchall()
        connection.close()
        return [self._row_to_book(row) for row in rows]

    def get_stats(self):
        books = self.list_all()
        records = [
            {
                "genre": book.genre,
                "year": book.year,
                "copies_available": book.copies_available,
            }
            for book in books
        ]
        df = pd.DataFrame(records)
        return {
            "total_books": len(df),
            "average_year": round(df["year"].mean(), 1),
            "total_copies_available": int(df["copies_available"].sum()),
            "books_by_genre": df.groupby("genre").size().to_dict(),
        }
