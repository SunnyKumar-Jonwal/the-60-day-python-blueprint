# Exercise: this is a complete, working, single-file API for a "notes"
# resource -- exactly the shape every Day 51-57 example has been.
#
# TODO: split this into two files:
#   1. day-58/exercises/routers/notes.py -- an APIRouter with prefix="/notes",
#      holding the Note model, the database helpers, and all three routes
#      (with their paths relative to the prefix, e.g. "" and "/{note_id}")
#   2. day-58/exercises/main.py -- a FastAPI() app that imports and
#      include_router()s it (see day-58/examples/ for the pattern to follow)
#
# Once split, running "python day-58/exercises/main.py" and hitting the same
# endpoints should behave identically to running this file directly.

import os
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = "day-58/exercises/starting_point.db"

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


@app.post("/notes", status_code=201)
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
    return [dict(row) for row in rows]


@app.get("/notes/{note_id}")
def read_note(note_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return dict(row)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
