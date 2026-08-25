import os
import sqlite3

from fastapi import FastAPI

DB_PATH = "day-55/exercises/exercise_1.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    pass
    # TODO: create a "notes" table with columns id (INTEGER PRIMARY KEY
    # AUTOINCREMENT) and text (TEXT NOT NULL), commit, close


init_db()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Notes API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
