# Library API — Capstone

A FastAPI + SQLite library management API, seeded from a CSV, with full
CRUD, a checkout action with real business rules, search, and a
pandas-powered stats endpoint. This is the course capstone (Days 59-60) —
one complete project rather than a new day of isolated exercises.

## Setup

Nothing beyond the repo's root setup (see the [root README](../../README.md)) —
every dependency (`fastapi`, `uvicorn`, `pandas`, `pytest`, `httpx`) is
already in the root `requirements.txt`.

## Run it

From the **repository root**:

```bash
python day-59/project/main.py
```

This seeds a fresh `library.db` from [`books.csv`](books.csv) (15 books
across 5 genres) every time it starts — see the comment in
[`repository.py`](repository.py) for why a real production app wouldn't do
this.

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Welcome message |
| `GET` | `/books` | List every book |
| `GET` | `/books/stats` | Summary statistics (pandas-powered) |
| `GET` | `/books/search?query=...` | Search by title or author (substring match) |
| `GET` | `/books/{id}` | Get one book |
| `POST` | `/books` | Create a book |
| `PUT` | `/books/{id}` | Update a book |
| `DELETE` | `/books/{id}` | Delete a book |
| `POST` | `/books/{id}/checkout` | Check out one copy (decrements `copies_available`) |

Visit `http://127.0.0.1:8000/docs` while it's running for interactive docs.

## Sample session

```
$ curl http://127.0.0.1:8000/books/1
{"id":1,"title":"Dune","author":"Frank Herbert","genre":"Sci-Fi","year":1965,"copies_available":3}

$ curl http://127.0.0.1:8000/books/stats
{"total_books":15,"average_year":1956.5,"total_copies_available":34,
 "books_by_genre":{"Classic":3,"Fantasy":3,"Mystery":3,"Non-Fiction":3,"Sci-Fi":3}}

$ curl "http://127.0.0.1:8000/books/search?query=Tolkien"
[{"id":4,"title":"The Hobbit","author":"J.R.R. Tolkien","genre":"Fantasy","year":1937,"copies_available":4}]

$ curl -X POST http://127.0.0.1:8000/books/1/checkout
{"id":1,"title":"Dune","author":"Frank Herbert","genre":"Sci-Fi","year":1965,"copies_available":2}

$ curl -i -X POST http://127.0.0.1:8000/books/6/checkout
HTTP/1.1 409 Conflict
{"detail":"No copies of 'The Name of the Wind' are available"}
```

`books.csv` seeds "The Name of the Wind" with 0 copies specifically to
demonstrate that last case — a real domain rule (`Book.checkout()`) being
enforced, not just a database constraint.

## How it's built

- **[`models.py`](models.py)** — the domain layer. `Book` is a plain class
  (Day 21) with a `checkout()` method that enforces the actual business rule
  (can't check out a book with 0 copies left); `LibraryError` and its two
  subclasses are a custom exception hierarchy (Day 29), completely
  independent of any web or database concern.
- **[`repository.py`](repository.py)** — the persistence layer.
  `BookRepository` wraps every SQLite operation (Days 54-56) and is the only
  place that knows about the database — everything else in the project works
  with `Book` objects, never raw rows or SQL. `load_from_csv()` reads
  [`books.csv`](books.csv) with `pd.read_csv()` (Day 45) and inserts each
  row with a parameterized query. `get_stats()` builds a small DataFrame and
  uses `groupby()` (Day 46) for the per-genre breakdown.
- **[`routers/books.py`](routers/books.py)** — the API layer (Day 58's
  `APIRouter` pattern). Translates between the domain (`Book`,
  `BookNotFoundError`, ...) and HTTP (Pydantic models, `HTTPException`,
  status codes) — this file is the only place that knows about FastAPI.
- **[`main.py`](main.py)** — wires it together: seeds the database, creates
  the app, includes the router.
- **[`test_books.py`](test_books.py)** — 10 pytest tests via `TestClient`
  (Day 57), covering the full CRUD cycle, the checkout success and conflict
  paths, search, and stats, run against a completely separate test database
  (see [`conftest.py`](conftest.py)).

One small piece of new syntax appears in `routers/books.py`:
`raise HTTPException(...) from error` inside each `except` block. The
`from error` explicitly links the new `HTTPException` to the domain
exception that caused it, which keeps the original error visible in
tracebacks during debugging — a small but genuinely useful habit whenever
you convert one exception into another, as every route handler here does.

## Stretch goal

Pick one (or more) to extend the capstone once the core works:

- **Pagination**: add `?skip=` and `?limit=` query params to `GET /books`
  (Day 52).
- **A `return` action**: the mirror of checkout — `POST
  /books/{id}/return` that increments `copies_available` back up.
- **Author stats**: extend `get_stats()` to also report the most-represented
  author.
- **A `Member` resource**: add a second table/router tracking who has
  checked out which book, turning `checkout` into a real loan record instead
  of just decrementing a counter.
