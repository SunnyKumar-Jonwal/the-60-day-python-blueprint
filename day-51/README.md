# Day 51: FastAPI basics & first endpoint

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- What a web framework is, and what FastAPI specifically gives you
- Creating a FastAPI app and your first endpoint
- Running it and hitting it with a real request
- The automatic interactive docs

## Explanation

### From client to server

[Day 41](../day-41/README.md) you were the **client** — using `requests` to
call someone else's API. Today you build the **server** — the thing that
receives a request and sends back a response. **FastAPI** is a modern,
third-party Python web framework (`pip install fastapi uvicorn`, already in
this repo's `requirements.txt`) chosen for this course specifically because
it's built entirely around the type hints you've been writing since
[Day 9](../day-09/README.md) — FastAPI reads your function signatures to
validate requests and generate documentation automatically.

FastAPI itself only describes *what* should happen for each request — it
needs an **ASGI server** to actually run and listen for connections.
`uvicorn` is that server.

### Your first endpoint

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

- `app = FastAPI()` creates the application.
- `@app.get("/")` registers a **route**: "when a `GET` request comes in for
  path `/`, run the function below."
- The function's return value (here, a dict) is automatically converted to
  JSON (Day 42) in the response — no manual `json.dumps()` needed.

### Running it

A normal FastAPI tutorial runs `uvicorn main:app --reload` from the
terminal — but that requires importing your file by a dotted module path
(`main:app`), and this course's day folders are named `day-51`, `day-52`,
etc., which **aren't valid Python identifiers** (hyphens aren't allowed in
import paths). So instead, every FastAPI example in this course runs
directly as a script, starting the server from inside the file itself:

```python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
```

```bash
python day-51/examples/main.py
```

This starts a live server on `http://127.0.0.1:8000` that keeps running
until you stop it (Ctrl+C). In a second terminal, or a browser, you can then
hit it:

```bash
curl http://127.0.0.1:8000/
# {"message":"Hello, FastAPI!"}
```

If you have your own real project (not this course's day-XX folders), the
standard `uvicorn main:app --reload` command works fine — `--reload` restarts
the server automatically whenever you save a change, which the object-based
`uvicorn.run(app, ...)` form used here doesn't support.

### Automatic interactive docs

FastAPI generates interactive API documentation for free, from your route
definitions and type hints. With the server running, visit:

- `http://127.0.0.1:8000/docs` — Swagger UI, where you can try each endpoint
  right in the browser.
- `http://127.0.0.1:8000/redoc` — an alternative documentation view.

This is one of FastAPI's headline features, and it only gets more useful as
you add path/query parameters and request bodies from
[Day 52](../day-52/README.md) onward — FastAPI documents all of it
automatically.

## Worked example

See [`examples/main.py`](examples/main.py). Run it with:

```bash
python day-51/examples/main.py
```

Then, in another terminal:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/ping
```

Stop the server with Ctrl+C when you're done.

## Exercises

Each has its own `main.py` you run and hit with `curl` (or a browser),
exactly like the worked example above.

1. **`exercise_1_hello.py`** — a single `GET /` endpoint returning
   `{"message": "Hello, World!"}`.
2. **`exercise_2_multiple_routes.py`** — two endpoints: `GET /` and
   `GET /about`, each returning a different message.
3. **`exercise_3_status_endpoint.py`** — a `GET /health` endpoint returning
   `{"status": "healthy"}`, a common real-world pattern for checking a
   service is running.
4. **`exercise_4_dynamic_response.py`** — a `GET /random` endpoint that
   returns a different number each time it's called, using the `random`
   module (standard library — `import random`).

## Common Gotchas

- **Forgetting to install `uvicorn` alongside `fastapi`.** FastAPI describes
  the app; `uvicorn` is what actually runs it — you need both.
- **The server blocks the terminal it's running in.** `python
  day-51/examples/main.py` doesn't return control to your terminal until you
  stop it — you need a second terminal (or run it in the background) to send
  it requests while it's up.
- **Port already in use.** If a previous server is still running on port
  8000, starting another one on the same port fails — stop the old one
  first (Ctrl+C), or use a different port.
- **Trying to `uvicorn main:app` this course's files directly.** As
  explained above, the hyphenated `day-XX` folder names break that syntax
  here — always run this course's FastAPI examples as `python
  day-XX/.../main.py`.
