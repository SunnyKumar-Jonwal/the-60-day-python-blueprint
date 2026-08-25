import os
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = "day-55/exercises/exercise_3.db"

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


# TODO: add GET /notes/{note_id} that returns the note, or raises a 404
# HTTPException if it doesn't exist


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
