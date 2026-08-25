# Day 26: Dunder methods I (`__init__`, `__str__`, `__repr__`)

**Module:** 3 — OOP

## What you'll learn

- What "dunder" methods are and why they exist
- `__init__` properly explained (you've used it since Day 21)
- `__str__` for human-readable output
- `__repr__` for unambiguous, developer-facing output
- The difference between the two, and when each is used

## Explanation

### What's a "dunder" method?

**Dunder** is short for "double underscore" — methods like `__init__`,
`__str__`, and `__eq__` (tomorrow) are surrounded by double underscores on
both sides. These are **special methods** that Python calls automatically in
response to built-in operations: creating an object, printing it, comparing
it with `==`, and many more. You don't call them directly (`obj.__str__()`) —
you trigger them by using the built-in operation they're wired to
(`str(obj)`, `print(obj)`).

### `__init__` — you already know this one

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__init__` runs automatically right after Python creates a new object, and is
where you set up its initial attributes. You've used this since
[Day 21](../day-21/README.md) — it's the first dunder method in this course,
just not named as one yet.

### `__str__` — human-readable output

Without any dunder methods, printing an object gives an unhelpful default:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p)   # <__main__.Point object at 0x000001A2B3C4D5E6> -- not useful
```

Defining `__str__` fixes this — it's called automatically by `print()` and
`str()`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p = Point(3, 4)
print(p)        # Point(3, 4)
print(str(p))   # Point(3, 4) -- same thing
```

### `__repr__` — unambiguous, developer-facing output

`__repr__` serves a different purpose: an unambiguous representation meant for
**developers debugging**, ideally one that looks like valid Python code that
could recreate the object. It's what you see when you inspect a value
directly in an interactive session, or when an object shows up inside a list
being printed:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


p = Point(3, 4)
print(repr(p))        # Point(x=3, y=4)
print([p, p])          # [Point(x=3, y=4), Point(x=3, y=4)] -- lists use repr() for their items
```

### `__str__` vs `__repr__`

- If a class only defines `__repr__` and not `__str__`, `print()` falls back
  to using `__repr__` — so defining just `__repr__` is a reasonable minimum.
- If both are defined, `print()`/`str()` use `__str__`, while `repr()` and
  things like printing a list of objects use `__repr__`.
- Convention: `__str__` should read naturally for end users; `__repr__`
  should be precise enough for debugging, ideally showing the values that
  built the object.

## Worked example

See [`examples/dunder_str_repr.py`](examples/dunder_str_repr.py). Run it with:

```bash
python day-26/examples/dunder_str_repr.py
```

## Exercises

1. **`exercise_1_str.py`** — define a `Product` class with `name` and `price`,
   and a `__str__` that returns `"{name}: ${price}"`; print an instance.
2. **`exercise_2_repr.py`** — add a `__repr__` to `Product` that returns
   `"Product(name='{name}', price={price})"`; print `repr(instance)`.
3. **`exercise_3_list_of_objects.py`** — create a list of three `Product`
   instances and print the list directly, observing that `__repr__` is what
   shows for each item.
4. **`exercise_4_default_fallback.py`** — define a class with only `__repr__`
   defined (no `__str__`), then `print()` an instance and observe it falls
   back to `__repr__`.

## Common Gotchas

- **Forgetting `__str__`/`__repr__` must `return` a string.** Returning
  anything else (or nothing, meaning `None`) raises `TypeError: __str__
  returned non-string` — these dunder methods have a strict contract.
- **Confusing when each is used.** `print(obj)` and `f"{obj}"` use `__str__`
  (falling back to `__repr__` if it's missing); printing a *list containing*
  objects always uses each item's `__repr__`, never `__str__`.
- **Calling `obj.__str__()` directly.** It works, but it's not idiomatic —
  use `str(obj)` or just `print(obj)`, and let Python call the dunder method
  for you.
- **Leaving both undefined.** The default `__repr__` (`<__main__.ClassName
  object at 0x...>`) is nearly useless for debugging — defining at least
  `__repr__` on your classes is a habit worth building early.
