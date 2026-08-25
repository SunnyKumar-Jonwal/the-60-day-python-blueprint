# Day 12: Tuples

**Module:** 2 — Data Structures & Files

## What you'll learn

- Creating tuples and why they're immutable
- Indexing and slicing (same as lists)
- Tuple unpacking
- When to use a tuple instead of a list

## Explanation

### Creating a tuple

A **tuple** looks like a list but uses parentheses, and — crucially — is
**immutable**: once created, it can't be changed.

```python
point = (3, 4)
colors = ("red", "green", "blue")
single = (5,)   # a one-item tuple needs a trailing comma, otherwise (5) is just the int 5
empty = ()
```

Indexing and slicing work exactly like lists:

```python
point = (3, 4)
print(point[0])   # 3
print(point[-1])  # 4
```

### Immutability

```python
point = (3, 4)
point[0] = 10   # TypeError: 'tuple' object does not support item assignment
```

You can't `append`, `insert`, `remove`, or `pop` on a tuple — those methods don't
exist for it. If you need to "modify" one, you build a new tuple instead.

### Tuple unpacking

You can assign a tuple's items straight into separate variables in one line —
this is called **unpacking**, and it's one of the most useful things about tuples:

```python
point = (3, 4)
x, y = point
print(x, y)   # 3 4

name, age = "Ada", 30   # this itself is unpacking a tuple: ("Ada", 30)
```

This is also how you get multiple values back from a function at once — a
function can `return a, b`, which is really returning a tuple, and the caller
unpacks it:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([3, 1, 4, 1, 5])
print(lowest, highest)   # 1 5
```

### When to use a tuple vs. a list

- Use a **tuple** for a fixed, small group of related values that won't change —
  coordinates `(x, y)`, an RGB color `(255, 0, 0)`, a record you're returning from
  a function.
- Use a **list** when you're building a collection that grows, shrinks, or gets
  reordered.

A practical side effect of immutability: tuples can be used as dictionary keys
(Day 13) or put into sets (Day 14) — lists cannot, because both require their
contents to be unchangeable.

## Worked example

See [`examples/tuples.py`](examples/tuples.py). Run it with:

```bash
python day-12/examples/tuples.py
```

## Exercises

1. **`exercise_1_create.py`** — create a tuple of 3 favorite colors and print it.
2. **`exercise_2_unpack.py`** — given a tuple representing `(name, age, city)`,
   unpack it into three variables and print a sentence using all three.
3. **`exercise_3_immutable.py`** — attempt to modify an item in a tuple, catch
   what happens by reading the error, and instead build a *new* tuple with that
   one value changed.
4. **`exercise_4_return_tuple.py`** — write a function that returns two values (a
   sum and a product) as a tuple, then unpack the result when calling it.

## Common Gotchas

- **Forgetting the trailing comma for a one-item tuple.** `(5)` is just the
  integer `5` in parentheses — you need `(5,)` to make it an actual tuple.
- **Trying to mutate a tuple.** Any attempt to `.append()`, assign to an index,
  or otherwise change a tuple raises an error — that's the whole point of using
  one.
- **Unpacking with the wrong number of variables.** `x, y = (1, 2, 3)` raises
  `ValueError: too many values to unpack` — the count on the left must match the
  count on the right.
- **Thinking parentheses always make a tuple.** `(1 + 2)` is just `3` — the
  parentheses here are just grouping, not tuple syntax. It's the comma(s) that
  make it a tuple, not the parentheses.
