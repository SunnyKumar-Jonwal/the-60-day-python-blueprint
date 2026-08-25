# Day 55: Connecting FastAPI to SQLite

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- Structuring a FastAPI app backed by a real database instead of an
  in-memory dict
- A simple pattern for getting a fresh connection per request
- Combining Pydantic models (Day 52) with SQLite rows (Day 54)
- Setting up the database once, on startup

## Explanation

### Why not just a Python dict?

[Day 53](../day-53/README.md)'s `fake_items` dict lived only in memory —
every restart of the server wiped it out. A real API backs its data with a
database, so it survives restarts and can be queried, filtered, and updated
properly. Today combines [Day 51-53](../day-51/README.md)'s FastAPI with
[Day 54](../day-54/README.md)'s SQLite.

### A connection-per-request pattern

The simplest reliable pattern: open a fresh SQLite connection at the start
of each route function, and close it when done. SQLite handles this well
since it's just a local file, not a network service you need to keep a
persistent connection to:

```python
import sqlite3

DB_PATH = "day-55/examples/app.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row   # rows behave like dicts, not just tuples
    return connection
```

`row_factory = sqlite3.Row` is new — it makes each row support `row["name"]`
access (like a dict, Day 13) in addition to `row[0]` (like a tuple, Day 12),
which is far more readable than remembering column positions.

### Setting up the database once

Create the table when the app starts, not on every request:

```python
def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()


init_db()   # runs once, when this module is imported/run
```

### Combining it all in an endpoint

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create_item(item: Item):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO items (name, price) VALUES (?, ?)",
        (item.name, item.price),
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "name": item.name, "price": item.price}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    connection = get_connection()
    row = connection.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row["id"], "name": row["name"], "price": row["price"]}
```

`cursor.lastrowid` gives you the auto-generated `id` of the row you just
inserted — useful for building the response without a second query.
`connection.execute(...)` is a shortcut that creates a cursor and runs the
query in one step (equivalent to `cursor = connection.cursor();
cursor.execute(...)` from Day 54, just more concise).

## Worked example

See [`examples/main.py`](examples/main.py). Run it with:

```bash
python day-55/examples/main.py
```

Then, in another terminal:

```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Widget", "price": 9.99}'
curl http://127.0.0.1:8000/items/1
curl http://127.0.0.1:8000/items/999
```

## Exercises

Each has its own database file created fresh on startup.

1. **`exercise_1_setup.py`** — set up `get_connection()`/`init_db()` for a
   `notes` table (`id`, `text`), calling `init_db()` at import time.
2. **`exercise_2_create_endpoint.py`** — a `POST /notes` endpoint (Pydantic
   model with `text: str`) that inserts into the database and returns the
   new row's `id` and `text`.
3. **`exercise_3_read_endpoint.py`** — a `GET /notes/{note_id}` endpoint that
   returns the note or raises a `404`.
4. **`exercise_4_list_endpoint.py`** — a `GET /notes` endpoint that returns
   every row in the table as a list.

## Common Gotchas

- **Forgetting `row_factory = sqlite3.Row`.** Without it, rows come back as
  plain tuples — `row["name"]` fails, you'd need `row[1]` and have to
  remember exactly which position each column is in.
- **Leaving connections open across requests.** Opening one connection at
  import time and reusing it for every request can cause problems under
  concurrent access — the connection-per-request pattern here, while not the
  most efficient possible approach, is simple and safe to reason about.
- **Calling `init_db()` inside every request handler.** `CREATE TABLE IF NOT
  EXISTS` is safe to repeat, but there's no reason to re-run it on every
  single request — call it once, when the module loads.
- **Forgetting to close the connection before returning/raising.** If an
  endpoint raises `HTTPException` (Day 53) before reaching
  `connection.close()`, the connection leaks — for anything beyond this
  course's simple examples, real projects typically use FastAPI's
  dependency-injection system (`Depends`) to guarantee cleanup, which is
  beyond what this course covers.
