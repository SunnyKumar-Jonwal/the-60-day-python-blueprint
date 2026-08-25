# Day 57: API testing (pytest + TestClient)

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- Why testing an API by hand with `curl` doesn't scale
- `TestClient` — calling your FastAPI app directly, with no server needed
- Writing pytest tests for each CRUD operation
- Testing both success and error paths

## Explanation

### The problem with manual `curl` testing

Every FastAPI day so far, you verified endpoints by starting the server and
running `curl` commands by hand. That's fine for a first check, but exactly
like [Day 47](../day-47/README.md)'s point about manual verification in
general — it doesn't scale, and nobody re-runs a page of `curl` commands
before every change.

### `TestClient`

FastAPI ships with a `TestClient` (built on `httpx`, already in this repo's
`requirements.txt`) that lets you call your app's endpoints **directly in
Python, with no live server, no `uvicorn.run()`, no network involved at
all**:

```python
from fastapi.testclient import TestClient

from main import app   # your FastAPI app object, imported directly

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
```

`client.get(...)`, `client.post(...)`, `client.put(...)`, `client.delete(...)`
mirror `requests`' API from [Day 41](../day-41/README.md) almost exactly —
`response.status_code`, `response.json()` work the same way. The difference
is `TestClient` talks to your app in-process, so tests run instantly and
never depend on a port being free or a server being started first.

### Testing CRUD, success and error paths

Reusing Day 56's `books` API:

```python
def test_create_book():
    response = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Dune"
    assert "id" in body


def test_read_missing_book_returns_404():
    response = client.get("/books/99999")
    assert response.status_code == 404
```

`json={...}` on `client.post(...)` handles the JSON encoding and
`Content-Type` header automatically — the equivalent of `requests`' `json=`
parameter, if you used it on Day 41.

### A clean database per test run: `conftest.py`

Testing against the same database file every run can leave stale data
between test runs, causing flaky results. A simple fix: point the app at a
fresh, dedicated test database *before* it's even imported.

`conftest.py` is a special filename pytest recognizes automatically — code
in it runs before pytest imports any test file in the same folder (or
below), which makes it the right place for setup like this:

```python
# conftest.py
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))   # so "from main import app" can find main.py

TEST_DB = "day-57/examples/test.db"
if os.path.exists(TEST_DB):
    os.remove(TEST_DB)

os.environ["DB_PATH_OVERRIDE"] = TEST_DB
```

The app then reads this optional environment variable when picking its
database path (see [`examples/main.py`](examples/main.py)), so the test file
transparently gets a fresh, isolated database — no changes needed inside
`test_main.py` itself.

## Worked example

See [`examples/main.py`](examples/main.py) (a small CRUD API) and
[`examples/test_main.py`](examples/test_main.py) (its tests). Run the tests
with:

```bash
pytest day-57/examples/test_main.py -v
```

No server needs to be running — `TestClient` handles everything.

## Exercises

Each exercise has its `main.py` already complete — write the tests in the
matching `test_*.py` file.

1. **`test_1_get_endpoints.py`** — test `GET /` and a `GET /items/{id}` for
   both an existing and a missing item.
2. **`test_2_post_endpoint.py`** — test `POST /items` returns `201` and the
   correct body.
3. **`test_3_full_crud.py`** — test create, read, update, and delete in
   sequence against the same resource.
4. **`test_4_validation_errors.py`** — test that `POST /items` with a
   missing required field returns `422` (FastAPI's automatic validation from
   Day 52).

## Common Gotchas

- **Importing the app before pointing it at a test database.** If `main.py`
  connects to its database at import time (like Day 55-56's `init_db()`),
  you must redirect it *before* importing — importing first locks in the
  real database path.
- **Tests that depend on each other's order.** A test that assumes a
  previous test already created `id=1` breaks if run alone, or in a
  different order — each test should set up what it needs, or the file
  should reset its database between tests.
- **Testing only the success path.** Exactly like Day 53's reminder — always
  also test `404`s, `422`s, and other error cases, not just "it worked."
- **Forgetting `TestClient` doesn't need a running server.** Starting
  `uvicorn` in the background before running `pytest` isn't necessary (and
  isn't what makes these tests work) — `TestClient` calls the app directly.
