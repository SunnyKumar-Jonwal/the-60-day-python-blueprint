# Day 52: Path/query parameters, request & response models

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- Path parameters, and how FastAPI validates them using type hints
- Query parameters, including optional ones with defaults
- Request bodies with **Pydantic** models
- The `response_model` parameter

## Explanation

### Path parameters

A part of the URL itself can be a variable, captured with `{curly_braces}`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

```bash
curl http://127.0.0.1:8000/items/42
# {"item_id":42}
curl http://127.0.0.1:8000/items/not-a-number
# 422 error -- automatically rejected, because item_id: int doesn't match "not-a-number"
```

This is FastAPI's headline feature in action: because `item_id` is
type-hinted `int` (Day 9), FastAPI automatically converts and validates it —
no manual `int(...)` and no manual "is this actually a number" check.

### Query parameters

Any function parameter that *isn't* part of the path becomes a **query
parameter** — the `?key=value` part of a URL:

```python
@app.get("/search")
def search(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
```

```bash
curl "http://127.0.0.1:8000/search?query=python"
# {"query":"python","limit":10} -- limit uses its default, wasn't provided
curl "http://127.0.0.1:8000/search?query=python&limit=5"
# {"query":"python","limit":5}
```

A parameter with no default (`query: str`) is **required**; one with a
default (`limit: int = 10`) is **optional**.

### Request bodies with Pydantic

For `POST`/`PUT` requests that send structured data, define a model using
**Pydantic**'s `BaseModel` — this is exactly what a class looks like
(Day 21), just inheriting from `BaseModel` to get automatic validation:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True   # default value -- becomes optional


@app.post("/items")
def create_item(item: Item):
    return {"received": item}
```

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'
# {"received":{"name":"Widget","price":9.99,"in_stock":true}}
```

FastAPI parses the JSON request body, validates it against `Item`'s type
hints, and gives you back a real `Item` instance — `item.name`, `item.price`
work exactly like any object's attributes (Day 21). If the body is missing
`name` or has the wrong type for `price`, FastAPI automatically rejects it
with a `422` error before your function even runs.

### `response_model`

You can also declare the *shape of the response*, separate from what your
function internally works with — useful for hiding internal fields:

```python
class ItemOut(BaseModel):
    name: str
    price: float


@app.post("/items", response_model=ItemOut)
def create_item(item: Item):
    return item   # any extra fields on `item` not in ItemOut are dropped from the response
```

## Worked example

See [`examples/main.py`](examples/main.py). Run it with:

```bash
python day-52/examples/main.py
```

Then, in another terminal:

```bash
curl http://127.0.0.1:8000/items/42
curl "http://127.0.0.1:8000/search?query=python&limit=5"
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Widget", "price": 9.99}'
```

## Exercises

1. **`exercise_1_path_param.py`** — a `GET /users/{user_id}` endpoint
   (`user_id: int`) returning `{"user_id": user_id}`.
2. **`exercise_2_query_params.py`** — a `GET /products` endpoint with query
   parameters `category: str` (required) and `page: int = 1` (optional).
3. **`exercise_3_request_body.py`** — a `Task` Pydantic model (`title: str`,
   `done: bool = False`) and a `POST /tasks` endpoint that returns what it
   received.
4. **`exercise_4_response_model.py`** — a `POST /users` endpoint with an
   input model including a `password` field, and a `response_model` that
   excludes it from the response.

## Common Gotchas

- **Query parameter order matters for required vs. optional.** In Python, a
  parameter with a default can't come before one without — same rule as any
  function (Day 8), so required query params must be listed before optional
  ones in the function signature.
- **Forgetting `Content-Type: application/json` when POSTing with `curl`.**
  Without it, FastAPI may not parse the body as JSON correctly — always
  include that header when sending a JSON body manually.
- **Confusing a path parameter with a query parameter.** `{item_id}` in the
  route path (`@app.get("/items/{item_id}")`) must also appear as a matching
  function parameter name — anything else in the signature becomes a query
  parameter instead.
- **Expecting `response_model` to change what your function returns
  internally.** It only affects what's sent back in the *response* — your
  function still works with the full object internally; `response_model`
  filters at the boundary.
