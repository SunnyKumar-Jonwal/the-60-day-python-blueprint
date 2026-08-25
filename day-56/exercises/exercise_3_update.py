import os
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = "day-56/exercises/exercise_3.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()

app = FastAPI()


class Movie(BaseModel):
    title: str
    director: str
    year: int


@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO movies (title, director, year) VALUES (?, ?, ?)",
        (movie.title, movie.director, movie.year),
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}


@app.get("/movies")
def list_movies():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM movies").fetchall()
    connection.close()
    return [dict(row) for row in rows]


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM movies WHERE id = ?", (movie_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return dict(row)


# TODO: add PUT /movies/{movie_id} that updates title/director/year, checking
# result.rowcount and raising a 404 if nothing was updated


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
