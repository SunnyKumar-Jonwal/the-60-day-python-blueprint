import os
import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel

DB_PATH = "day-55/solutions/exercise_4.db"

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


class Note(BaseModel):
    text: str


@app.post("/notes")
def create_note(note: Note):
    connection = get_connection()
    cursor = connection.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "text": note.text}


@app.get("/notes")
def list_notes():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM notes").fetchall()
    connection.close()
    return [{"id": row["id"], "text": row["text"]} for row in rows]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
