# Day 56: Building a full REST API (CRUD)

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- What CRUD means, and the REST convention for each operation
- Building all four operations for one resource, end to end
- `PUT` for full updates
- `DELETE` and `204 No Content`

## Explanation

### CRUD and REST

**CRUD** = Create, Read, Update, Delete — the four things you generally do
to any piece of stored data. **REST** is a convention for mapping these onto
HTTP methods and URLs, which you've been building toward since Day 51:

| Operation | HTTP method | URL | Status on success |
|---|---|---|---|
| Create | `POST` | `/books` | `201 Created` |
| Read (all) | `GET` | `/books` | `200 OK` |
| Read (one) | `GET` | `/books/{id}` | `200 OK` |
| Update | `PUT` | `/books/{id}` | `200 OK` |
| Delete | `DELETE` | `/books/{id}` | `204 No Content` |

The **resource** (`books`) is a noun, and the HTTP method says what to do
with it — you've already built `POST`/`GET` pairs like this on Days 53 and
55; today adds `PUT` and `DELETE` to complete the set for one resource.

### `PUT` for full replacement

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    connection = get_connection()
    result = connection.execute(
        "UPDATE books SET title = ?, author = ? WHERE id = ?",
        (book.title, book.author, book_id),
    )
    connection.commit()
    if result.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Book not found")
    connection.close()
    return {"id": book_id, "title": book.title, "author": book.author}
```

`result.rowcount` tells you how many rows the `UPDATE` actually affected —
`0` means no row had that `id`, so it's a `404`, not a silent no-op.

### `DELETE` and `204 No Content`

```python
from fastapi import Response


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    connection = get_connection()
    result = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status_code=204)
```

`204 No Content` means "it worked, and there's deliberately nothing to send
back" — the conventional response for a successful `DELETE`. Returning a
plain `Response(status_code=204)` (rather than a dict) avoids sending an
empty JSON body that no client expects.

### A shortcut for converting a row to a dict

Since `row_factory = sqlite3.Row` (Day 55) makes each row dict-like, you can
convert one straight into a plain dict with `dict(row)` instead of listing
out every column by hand:

```python
row = connection.execute("SELECT * FROM books WHERE id = ?", (1,)).fetchone()
print(dict(row))   # {"id": 1, "title": "Dune", "author": "Frank Herbert"}
```

This is handy once a table has more than a couple of columns — no need to
repeat every field name when building the response dict.

## Worked example

See [`examples/main.py`](examples/main.py), a complete CRUD API for a
`books` resource. Run it with:

```bash
python day-56/examples/main.py
```

Then, in another terminal:

```bash
curl -X POST http://127.0.0.1:8000/books -H "Content-Type: application/json" -d '{"title": "Dune", "author": "Frank Herbert"}'
curl http://127.0.0.1:8000/books
curl http://127.0.0.1:8000/books/1
curl -X PUT http://127.0.0.1:8000/books/1 -H "Content-Type: application/json" -d '{"title": "Dune Messiah", "author": "Frank Herbert"}'
curl -i -X DELETE http://127.0.0.1:8000/books/1
curl -i http://127.0.0.1:8000/books/1
```

## Exercises

Build a complete CRUD API for a `movies` resource (`title: str`,
`director: str`, `year: int`) across these four files — treat them as one
progressively-built app, each adding to the last.

1. **`exercise_1_create_read.py`** — `POST /movies` and `GET /movies/{id}`.
2. **`exercise_2_list.py`** — adds `GET /movies` (list all).
3. **`exercise_3_update.py`** — adds `PUT /movies/{id}`.
4. **`exercise_4_delete.py`** — adds `DELETE /movies/{id}` returning `204`.

## Common Gotchas

- **Forgetting to check `rowcount` on `UPDATE`/`DELETE`.** SQLite doesn't
  error when a `WHERE` clause matches nothing — `UPDATE`/`DELETE` on a
  nonexistent `id` "succeeds" silently unless you explicitly check
  `rowcount` and raise a `404` yourself.
- **Returning a body with a `204` response.** A `204 No Content` response is
  specifically defined to have no body — returning a dict there is
  inconsistent with the status code's meaning; use `Response(status_code=204)`.
- **Using `POST` for updates.** `POST` conventionally means "create a new
  thing" — using it to update an existing resource works technically but
  breaks the REST convention that `PUT`/`PATCH` exist for.
- **Not testing the "not found" path.** It's easy to only test the happy
  path (valid `id`) — always also check what happens with an `id` that
  doesn't exist, exactly like Day 53's error-handling exercises.
