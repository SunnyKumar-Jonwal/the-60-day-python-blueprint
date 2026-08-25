import os
import sqlite3

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

DB_PATH = "day-58/solutions/app.db"

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

router = APIRouter(prefix="/notes", tags=["notes"])


class Note(BaseModel):
    text: str


@router.post("", status_code=201)
def create_note(note: Note):
    connection = get_connection()
    cursor = connection.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "text": note.text}


@router.get("")
def list_notes():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM notes").fetchall()
    connection.close()
    return [dict(row) for row in rows]


@router.get("/{note_id}")
def read_note(note_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return dict(row)
