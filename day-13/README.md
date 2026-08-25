# Day 13: Dictionaries

**Module:** 2 — Data Structures & Files

## What you'll learn

- Creating and accessing dictionaries
- Adding, updating, and removing keys
- Safely checking for a key with `.get()` and `in`
- Looping over keys, values, and items

## Explanation

### Creating a dictionary

A **dictionary** (`dict`) stores `key: value` pairs. Keys must be unique and
immutable (strings, numbers, or tuples — not lists); values can be anything:

```python
person = {
    "name": "Ada",
    "age": 30,
    "city": "London",
}
```

### Accessing values

```python
person = {"name": "Ada", "age": 30}
print(person["name"])   # "Ada"
print(person["email"])  # KeyError: 'email' -- accessing a missing key crashes
```

### Safe access with `.get()`

`.get(key, default)` never raises — it returns `None` (or your chosen default) if
the key doesn't exist:

```python
print(person.get("email"))              # None
print(person.get("email", "unknown"))   # "unknown"
```

### Adding, updating, removing

```python
person = {"name": "Ada", "age": 30}
person["email"] = "ada@example.com"   # adds a new key
person["age"] = 31                     # updates an existing key -- same syntax either way
del person["email"]                    # removes a key (raises KeyError if missing)
age = person.pop("age")                # removes and returns the value
```

### Checking for a key

```python
person = {"name": "Ada", "age": 30}
print("name" in person)      # True -- checks keys, not values
print("Ada" in person)       # False
```

### Looping

```python
person = {"name": "Ada", "age": 30}

for key in person:
    print(key)                 # loops over keys by default

for key, value in person.items():
    print(key, value)          # loops over key-value pairs together

for value in person.values():
    print(value)                # loops over values only
```

## Worked example

See [`examples/dictionaries.py`](examples/dictionaries.py). Run it with:

```bash
python day-13/examples/dictionaries.py
```

## Exercises

1. **`exercise_1_build_dict.py`** — build a dictionary describing a book (title,
   author, year) and print it.
2. **`exercise_2_safe_get.py`** — given a dictionary, use `.get()` to print a
   value that exists and a default for one that doesn't.
3. **`exercise_3_update.py`** — given a dictionary, add a new key, update an
   existing one, and remove another, printing the dictionary after each step.
4. **`exercise_4_loop_items.py`** — given a dictionary of item names to prices,
   print each as `"item: $price"` using `.items()`.

## Common Gotchas

- **`dict["missing_key"]` crashes.** Use `.get()` when a key might not be there,
  or check with `in` first.
- **`in` checks keys, not values.** `"Ada" in person` checks whether `"Ada"` is a
  *key* — to check values, use `"Ada" in person.values()`.
- **Dictionaries preserve insertion order** (since Python 3.7+), but don't rely on
  sorting — if you need sorted output, sort explicitly.
- **Using a mutable type (like a list) as a key.** `{[1, 2]: "value"}` raises
  `TypeError: unhashable type: 'list'` — only immutable types (str, int, float,
  tuple, bool) can be dictionary keys.
