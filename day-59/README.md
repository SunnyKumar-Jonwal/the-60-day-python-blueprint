# Day 59: Capstone (part 1) — Library API

**Module:** 6 — Web APIs & Capstone

## What you're building

A **Library API**: a FastAPI service backed by SQLite, seeded from a CSV of
books, with full CRUD, a checkout action with real domain rules, search, and
a pandas-powered stats endpoint — plus a full pytest test suite. This is the
capstone: one project pulling together the entire course, not another
isolated day of exercises.

Full instructions, code, and the write-up live in [`project/`](project/) —
start there. [Day 60](../day-60/README.md) continues the same project with
polish and interview prep, rather than starting a new one.

## What this exercises

Practically everything:

- **OOP** ([Module 3](../day-21/README.md)) — `Book` is a real class with
  behavior (`checkout()`), not just a data bag; `models.py` defines a small
  custom exception hierarchy (`LibraryError` → `BookNotFoundError` /
  `NoCopiesAvailableError`).
- **File handling & pandas** ([Module 2](../day-17/README.md),
  [Module 5](../day-45/README.md)) — the database is seeded from
  [`books.csv`](project/books.csv) via `pd.read_csv()`; the stats endpoint
  uses `groupby()` for real aggregation.
- **SQLite** ([Days 54](../day-54/README.md)-[56](../day-56/README.md)) — a
  `BookRepository` class wraps all persistence, with parameterized queries
  throughout.
- **FastAPI** ([Days 51](../day-51/README.md)-[58](../day-58/README.md)) —
  an `APIRouter`-based structure (Day 58), Pydantic request models,
  `HTTPException` mapped from the custom domain exceptions, and a real
  non-CRUD action endpoint (`POST /books/{id}/checkout`).
- **pytest + `TestClient`** ([Day 57](../day-57/README.md)) — 10 tests
  covering success paths, `404`s, and a `409` conflict.

## Run it

```bash
python day-59/project/main.py
pytest day-59/project/test_books.py -v
```

See [`project/README.md`](project/README.md) for the full write-up, every
endpoint, a sample session, and the stretch goal.
