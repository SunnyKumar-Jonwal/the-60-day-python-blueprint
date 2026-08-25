import os
import sqlite3

from fastapi import FastAPI

DB_PATH = "day-55/solutions/exercise_1.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Notes API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
