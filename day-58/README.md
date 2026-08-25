# Day 58: Review & polish

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- Organizing a growing FastAPI app into multiple files
- `APIRouter` for splitting routes out of a single `main.py`
- A quick recap of everything Module 6 has built so far
- What's ahead in the capstone

## Explanation

### The problem with one giant `main.py`

Days 51-57 kept everything — models, database helpers, and every route — in
a single `main.py`, which was the right call while learning one concept at a
time. A real project's API grows past what's comfortable in one file. Today
is a light "consolidate and organize" day before the capstone, with no major
new library.

### `APIRouter` — splitting routes into their own file

```python
# routers/books.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/books", tags=["books"])


class Book(BaseModel):
    title: str
    author: str


@router.get("/")
def list_books():
    ...


@router.get("/{book_id}")
def read_book(book_id: int):
    ...
```

```python
# main.py
from fastapi import FastAPI

from routers.books import router as books_router

app = FastAPI()
app.include_router(books_router)
```

`APIRouter` works almost exactly like `FastAPI()` for defining routes
(`@router.get(...)` instead of `@app.get(...)`), and `app.include_router(...)`
wires it into the main app. `prefix="/books"` means every route in that
router is automatically under `/books/...`, so `@router.get("/{book_id}")`
becomes `/books/{book_id}` — you don't repeat `/books` in every route.

This course's day folders (hyphenated names, Day 51's constraint) make a
full multi-file package layout awkward to demonstrate cleanly across
separate numbered days, so **the capstone (Days 59-60)** is where you'll see
this pattern used for real, in one project that's allowed to have its own
proper internal structure.

### Recap: what Module 6 built, day by day

- **Day 51**: a FastAPI app, one endpoint, running it, the auto-generated docs.
- **Day 52**: path parameters, query parameters, request bodies via Pydantic.
- **Day 53**: status codes, `HTTPException` for expected errors.
- **Day 54**: SQLite — tables, parameterized queries, why they matter.
- **Day 55**: connecting FastAPI to SQLite, a connection-per-request pattern.
- **Day 56**: a complete CRUD API (`POST`/`GET`/`PUT`/`DELETE`) for one resource.
- **Day 57**: testing all of it with `TestClient`, no live server needed.

### What's ahead

The capstone combines everything from this entire course: OOP (Module 3) for
modeling the domain, pandas (Module 5) or SQLite for data, and this module's
FastAPI skills for serving it over real endpoints — plus real tests. It's
meant to feel like a small, complete project, not another isolated day of
exercises.

## Worked example / Exercises

No new code today — instead, revisit and clean up one of your own Module 6
day's solutions:

1. Pick any solution from Days 55-56 (SQLite-backed FastAPI app).
2. Split it into at least two files: an `APIRouter`-based routes file and a
   `main.py` that includes it, following the pattern above.
3. Re-run its `curl` checks (or its Day 57-style tests, if you wrote any) to
   confirm it still behaves identically after the split.

See [`examples/`](examples/) for a worked version of this split, based on
Day 56's `books` API.

## Common Gotchas

- **Splitting too early.** For a single-file app with three routes, the
  split adds ceremony without benefit — reach for `APIRouter` once a file
  genuinely feels too large to navigate, not by default.
- **Forgetting `app.include_router(...)`.** Defining routes on a `router`
  object does nothing until the main app actually includes it — a very easy
  step to forget while refactoring.
- **Duplicating the `prefix` in both the router and each route.** With
  `APIRouter(prefix="/books")`, individual routes should be relative
  (`"/"`, `"/{book_id}"`), not `"/books/{book_id}"` again — that would
  produce `/books/books/{book_id}`.
- **Losing track of what changed during a refactor.** After splitting files,
  re-run your actual checks (`curl`, or better, Day 57's `TestClient` tests)
  rather than assuming the split preserved behavior — refactors are exactly
  where automated tests earn their keep.
