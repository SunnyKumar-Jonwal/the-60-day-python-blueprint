# Day 53: Status codes & error handling

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- Setting a custom success status code
- Raising `HTTPException` for expected error cases
- Choosing the right status code for the situation
- How this connects to Day 28's exceptions

## Explanation

### Custom success status codes

By default, FastAPI returns `200 OK` for a successful `GET`, `POST`, etc.
Override it with `status_code` on the route decorator:

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created"}
```

`201 Created` is the conventional status code for "a `POST` successfully
created something" — using `status.HTTP_201_CREATED` (a named constant) is
clearer than the bare number `201` and less error-prone.

### `HTTPException` — expected errors

For error cases your API needs to signal deliberately (not found, bad
input), `raise` an `HTTPException` — this is Day 28's `raise` pattern,
specialized for HTTP:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_items = {1: "Widget", 2: "Gadget"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in fake_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": fake_items[item_id]}
```

```bash
curl -i http://127.0.0.1:8000/items/1
# HTTP/1.1 200 OK
# {"item_id":1,"name":"Widget"}

curl -i http://127.0.0.1:8000/items/999
# HTTP/1.1 404 Not Found
# {"detail":"Item not found"}
```

Unlike a plain Python exception (Day 28), `HTTPException` is specifically
understood by FastAPI: it stops the function and sends back a proper HTTP
error response with the given status code and a JSON body containing
`detail`.

### Choosing a status code

| Code | Meaning | When |
|---|---|---|
| `200` | OK | Successful `GET`/`PUT`/`PATCH` |
| `201` | Created | Successful `POST` that created something |
| `204` | No Content | Successful `DELETE` (no body to return) |
| `400` | Bad Request | The client sent something invalid |
| `401` | Unauthorized | Missing/invalid authentication |
| `403` | Forbidden | Authenticated, but not allowed to do this |
| `404` | Not Found | The resource doesn't exist |
| `422` | Unprocessable Entity | FastAPI's automatic validation failure (Day 52) |
| `500` | Internal Server Error | An unhandled bug on the server |

You've already seen `422` happen automatically (Day 52's type validation);
`404`/`400`/`403` are the ones you'll raise deliberately most often.

## Worked example

See [`examples/main.py`](examples/main.py). Run it with:

```bash
python day-53/examples/main.py
```

Then, in another terminal:

```bash
curl -i -X POST http://127.0.0.1:8000/items
curl -i http://127.0.0.1:8000/items/1
curl -i http://127.0.0.1:8000/items/999
```

## Exercises

1. **`exercise_1_created_status.py`** — a `POST /notes` endpoint returning
   status `201`.
2. **`exercise_2_not_found.py`** — a `GET /books/{book_id}` endpoint that
   raises a `404` `HTTPException` for any `book_id` not in a small hardcoded
   dict.
3. **`exercise_3_bad_request.py`** — a `POST /divide` endpoint (query params
   `a: float`, `b: float`) that raises a `400` `HTTPException` with detail
   `"Cannot divide by zero"` when `b == 0`.
4. **`exercise_4_multiple_errors.py`** — a `GET /users/{user_id}` endpoint
   that raises `404` if the user doesn't exist, and `403` if `user_id == 0`
   (representing a blocked/banned account, checked before the not-found
   check).

## Common Gotchas

- **Using a plain `raise ValueError(...)` instead of `HTTPException`.**
  Without `HTTPException`, FastAPI treats it as an unhandled server error —
  the client gets a generic `500` instead of the specific, informative status
  code you intended.
- **Forgetting `status_code=` returns a *default* success code, not an
  error.** `status_code=404` on the route decorator itself would claim
  *every* response from that endpoint is a 404 — for conditional errors, use
  `raise HTTPException(status_code=404, ...)` inside the function instead.
- **Returning `200` for something that clearly failed.** Silently returning
  `{"error": "not found"}` with a `200` status makes clients' error-handling
  code (which typically checks the status code) miss the failure entirely.
- **Overusing `500`.** A `500` should mean "the server has a bug" — an
  expected failure case like bad input or a missing resource should almost
  always be a `4xx` code you raise deliberately, not a crash that becomes a
  `500`.
