# Day 41: The `requests` library & real APIs

**Module:** 5 — Real-World Libraries

## What you'll learn

- What an API is, in practical terms
- Making a GET request with `requests`
- Status codes, `.json()`, `.text`
- Query parameters
- Basic error handling for network calls

## Explanation

### What's an API, briefly?

An **API** (Application Programming Interface) here means a web service you
can send an HTTP request to and get structured data back — instead of a
human-readable web page, you get something like JSON (Day 42) meant for
programs to read. This course uses
[JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free, public,
fake REST API made specifically for learning and testing — no signup, no API
key, no rate-limit worries.

### Installing `requests`

`requests` is a third-party package (Day 2, Day 38) — not part of the
standard library, so it needs `pip install requests` (already in this repo's
root `requirements.txt` from this point onward).

### A basic GET request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)   # 200 -- HTTP status code; 200 means success
print(response.json())          # the response body, parsed into a Python dict
```

`requests.get(url)` sends an HTTP GET request (the kind your browser sends
when you visit a page) and returns a **response object** with everything you
need: the status code, headers, and body.

### Status codes

| Code | Meaning |
|---|---|
| `200` | OK — the request succeeded |
| `201` | Created — a POST succeeded and created something |
| `404` | Not Found — the URL/resource doesn't exist |
| `500` | Server Error — something broke on the server's end |

```python
response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
print(response.status_code)   # 404 -- no user with that id
```

### `.json()` vs `.text`

```python
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.text)   # the raw response body as a string
print(response.json()) # the same body, parsed into a Python dict/list automatically
```

`.json()` only works when the response body is actually valid JSON — calling
it on something else raises an error.

### Query parameters

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
)
print(response.url)   # https://jsonplaceholder.typicode.com/posts?userId=1
posts = response.json()
print(len(posts))       # however many posts belong to user 1
```

Passing a `params` dict is the correct way to build a query string —
`requests` handles the `?key=value&...` formatting and escaping for you,
rather than you concatenating strings by hand.

### Basic error handling

Network calls can fail in ways your own code never does — the site could be
down, the network could drop, the URL could be wrong. Wrap requests in
`try`/`except` (Day 28), catching `requests.exceptions.RequestException`:

```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
    response.raise_for_status()   # raises an exception for 4xx/5xx status codes
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
```

`timeout=5` caps how long to wait before giving up — always set one; without
it, a request can hang indefinitely if the server never responds.
`raise_for_status()` turns an unsuccessful status code (like `404`) into a
Python exception, so your `except` block handles both network failures and
bad responses in one place.

## Worked example

See [`examples/api_basics.py`](examples/api_basics.py). Run it with:

```bash
python day-41/examples/api_basics.py
```

This makes real network requests — you'll need an internet connection.

## Exercises

1. **`exercise_1_get_request.py`** — GET
   `https://jsonplaceholder.typicode.com/todos/1` and print its status code
   and JSON body.
2. **`exercise_2_query_params.py`** — GET
   `https://jsonplaceholder.typicode.com/comments` with `params={"postId":
   1}`, and print how many comments came back.
3. **`exercise_3_not_found.py`** — GET a URL you know doesn't exist
   (`.../users/99999`) and print its status code, without raising an error.
4. **`exercise_4_error_handling.py`** — wrap a request in `try`/`except`
   catching `requests.exceptions.RequestException`, using `timeout=5` and
   `raise_for_status()`.

## Common Gotchas

- **Forgetting `timeout=`.** Without it, a hung server can freeze your
  program indefinitely — always pass a `timeout` in real code.
- **Calling `.json()` on a non-JSON or failed response.** A `404` page's body
  might not be valid JSON at all — check `response.status_code` (or use
  `raise_for_status()`) before trusting `.json()` to work.
- **Building query strings by hand.** `url + "?userId=" + str(user_id)`
  breaks on special characters and is easy to get wrong — always use the
  `params=` dict instead.
- **Assuming the network always works.** Real code that talks to APIs should
  always be prepared for `requests.exceptions.RequestException` — timeouts,
  DNS failures, and connection errors are normal, expected possibilities.
