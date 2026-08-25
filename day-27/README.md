# Day 27: Dunder methods II (`__eq__`, operator overloading)

**Module:** 3 — OOP

## What you'll learn

- Why `==` doesn't do what you'd expect by default on custom objects
- `__eq__` to define your own equality
- `__lt__` and friends for ordering comparisons
- `__add__` for making `+` work on your own objects

## Explanation

### The default `==` is identity, not equality

Without any dunder methods, `==` on custom objects checks whether they're the
exact same object in memory — not whether their data matches:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)   # False -- different objects, even though x and y match!
```

### `__eq__` — defining your own equality

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)   # True -- now compares values, not identity
```

`other` is whatever's on the right side of `==` — `__eq__` is called as
`p1.__eq__(p2)` when you write `p1 == p2`.

### Ordering: `__lt__` and friends

To make `<`, `>`, `<=`, `>=` work, define the corresponding dunder methods.
Most commonly you'll define `__lt__` ("less than") and let Python's
`sorted()`/`max()`/`min()` (Day 11) use it:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


products = [Product("Mug", 9.99), Product("Pen", 1.5)]
cheapest = min(products)   # uses __lt__ under the hood
print(cheapest.name)        # "Pen"
```

### Operator overloading: `__add__`

Defining `__add__` makes `+` work on your objects — this is called
**operator overloading**:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)   # Point(4, 6) -- calls p1.__add__(p2)
```

Common dunder methods you can overload this way: `__sub__` (`-`), `__mul__`
(`*`), `__len__` (so `len(obj)` works), and many more — the pattern is always
the same: define the dunder method, and Python's built-in syntax or function
calls it for you.

## Worked example

See [`examples/dunder_operators.py`](examples/dunder_operators.py). Run it
with:

```bash
python day-27/examples/dunder_operators.py
```

## Exercises

1. **`exercise_1_eq.py`** — define a `Fraction` class with `numerator` and
   `denominator`, and an `__eq__` that compares two fractions by cross
   multiplication (`a/b == c/d` when `a*d == c*b`).
2. **`exercise_2_lt.py`** — add `__lt__` to a `Fraction` class (same
   cross-multiplication idea), then use `sorted()` on a list of fractions.
3. **`exercise_3_add.py`** — define a `Vector` class with `x` and `y`, and an
   `__add__` that adds two vectors component-wise.
4. **`exercise_4_len.py`** — define a `Playlist` class wrapping a list of
   songs, and a `__len__` so `len(playlist)` returns the number of songs.

## Common Gotchas

- **Forgetting `__eq__` breaks `in` and set/dict membership too.** Without a
  custom `__eq__`, `some_point in list_of_points` also falls back to identity
  comparison, which usually isn't what you want.
- **Defining `__lt__` but expecting `>` to work automatically.** Python does
  NOT infer `__gt__` from `__lt__` by default — you'd need to define both, or
  swap the comparison order yourself (`b < a` instead of `a > b`). For
  `sorted()`, `min()`, and `max()`, `__lt__` alone is enough.
- **`self` and `other` might not be the same type.** `p1 + "not a point"`
  would try `other.x` on a string and crash with `AttributeError` — real-world
  operator overloading often checks the other type first, but that's beyond
  what this course covers today.
- **Overloading operators in a way that surprises readers.** `+` should mean
  something that actually resembles addition — overloading `+` to do
  something unrelated (like "merge and delete") makes code that reads fine
  but behaves in a confusing way.
