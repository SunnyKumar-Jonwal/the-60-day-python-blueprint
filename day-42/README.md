# Day 42: JSON handling

**Module:** 5 — Real-World Libraries

## What you'll learn

- What JSON is, and how it maps to Python types
- `json.dumps()` and `json.loads()`
- Reading and writing `.json` files
- Handling nested JSON structures

## Explanation

### What JSON is

**JSON** (JavaScript Object Notation) is a text format for structured data —
the format the API responses from [Day 41](../day-41/README.md) were already
in. It maps almost directly onto Python's own data types:

| JSON | Python |
|---|---|
| object `{...}` | `dict` |
| array `[...]` | `list` |
| string `"..."` | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

This close mapping is exactly why `response.json()` on Day 41 could just hand
you back a Python dict — the library converts JSON text into Python objects
following this table automatically.

### The `json` module

`json` is part of the standard library — `import json`, no `pip install`
needed.

### `json.dumps()` — Python → JSON text

```python
import json

person = {"name": "Ada", "age": 30, "active": True}
json_text = json.dumps(person)
print(json_text)   # '{"name": "Ada", "age": 30, "active": true}'
print(type(json_text))   # <class 'str'> -- it's just a string
```

Notice `True` became `true` (lowercase) — JSON syntax, not Python syntax.

For readable output, add `indent`:

```python
print(json.dumps(person, indent=2))
```

### `json.loads()` — JSON text → Python

```python
json_text = '{"name": "Ada", "age": 30, "active": true}'
person = json.loads(json_text)
print(person)          # {'name': 'Ada', 'age': 30, 'active': True}
print(type(person))    # <class 'dict'>
print(person["name"])  # "Ada"
```

`loads` = "load string." This is the reverse of `dumps` = "dump string."

### Reading and writing JSON files

```python
import json

person = {"name": "Ada", "age": 30}

with open("day-42/output.json", "w") as file:
    json.dump(person, file, indent=2)   # note: dump, not dumps -- writes directly to a file

with open("day-42/output.json", "r") as file:
    loaded = json.load(file)             # note: load, not loads -- reads directly from a file
print(loaded)
```

`dump`/`load` (no "s") work directly with an open file, combining
[Day 18](../day-18/README.md)'s `with` pattern with JSON conversion in one
step — you don't need to manually `.read()` the text and then `json.loads()`
it yourself.

### Nested JSON

Real API responses (Day 41) nest objects and arrays inside each other. Access
them exactly like any nested dict/list (Day 13, Day 11):

```python
data = {
    "user": {"name": "Ada", "roles": ["admin", "editor"]},
    "active": True,
}
print(data["user"]["name"])       # "Ada"
print(data["user"]["roles"][0])   # "admin"
```

## Worked example

See [`examples/json_basics.py`](examples/json_basics.py). Run it with:

```bash
python day-42/examples/json_basics.py
```

## Exercises

1. **`exercise_1_dumps_loads.py`** — convert a dict to a JSON string with
   `json.dumps()`, then parse it back with `json.loads()`, and confirm the
   round trip gives back an equal dict.
2. **`exercise_2_pretty_print.py`** — print a nested dict as indented JSON
   using `json.dumps(..., indent=2)`.
3. **`exercise_3_write_read_file.py`** — write a dict to
   `day-42/exercises_output.json` with `json.dump()`, then read it back with
   `json.load()` and print it.
4. **`exercise_4_nested_access.py`** — given a nested JSON-like structure
   (a dict of a list of dicts), extract and print a specific deeply nested
   value.

## Common Gotchas

- **Confusing `dumps`/`loads` (strings) with `dump`/`load` (files).** The
  "s" versions work with in-memory strings; the plain versions work directly
  with an open file object — mixing them up is a very common mistake
  (`json.dump(data)` with no file argument raises `TypeError`).
- **JSON keys are always strings.** `json.dumps({1: "a"})` produces
  `'{"1": "a"}'` — the integer key `1` becomes the string `"1"` in JSON, since
  JSON object keys must be strings; round-tripping back with `json.loads()`
  won't restore the original `int` key.
- **`True`/`None` vs `true`/`null`.** Inside Python code you write
  `True`/`False`/`None`; inside a raw JSON string (or a `.json` file) it's
  `true`/`false`/`null` — mixing the two up in a string you're trying to
  parse causes a `json.JSONDecodeError`.
- **Trying to `json.dumps()` a non-JSON-serializable object.** Only the types
  in the table above convert cleanly — dumping something like a custom class
  instance (Day 21) without special handling raises `TypeError: Object of
  type X is not JSON serializable`.
