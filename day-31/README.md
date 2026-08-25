# Day 31: Iterators & the iterator protocol

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- What actually happens when a `for` loop runs
- `iter()` and `next()`
- `StopIteration`
- Building your own iterator class with `__iter__` and `__next__`

## Explanation

### What a `for` loop is really doing

You've written dozens of `for` loops since [Day 7](../day-07/README.md)
without needing to know what happens underneath. Today, you find out.

```python
numbers = [10, 20, 30]
for n in numbers:
    print(n)
```

Under the hood, Python does roughly this:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)     # get an iterator from the list
while True:
    try:
        n = next(iterator)    # ask for the next value
    except StopIteration:      # no more values -- the signal to stop
        break
    print(n)
```

`for` isn't special magic — it's exactly this pattern, written for you.

### `iter()` and `next()`

- `iter(collection)` returns an **iterator** — an object that remembers where
  it is and knows how to produce the next value.
- `next(iterator)` produces the next value, or raises `StopIteration` once
  there are no more.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))   # 10
print(next(iterator))   # 20
print(next(iterator))   # 30
print(next(iterator))   # raises StopIteration -- nothing left
```

### Iterable vs. iterator

These are two different (related) things:

- An **iterable** is anything you can call `iter()` on — lists, tuples,
  dicts, sets, strings, files (all the things you've looped over since
  Day 7).
- An **iterator** is what `iter()` gives you back — something you can call
  `next()` on, one value at a time.

Every iterator is also iterable (calling `iter()` on it just returns itself),
but not every iterable is an iterator — a list is iterable, but you can't call
`next()` directly on a list itself, only on `iter(the_list)`.

### Building your own iterator

Any class that defines both `__iter__` (returning itself) and `__next__`
(returning the next value, or raising `StopIteration` when done) works with
`for` loops, `list(...)`, and everywhere else Python expects something
iterable:

```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current


for number in CountUp(3):
    print(number)   # 1, 2, 3
```

[Day 32](../day-32/README.md) introduces **generators**, which give you this
same behavior with far less boilerplate — but understanding the protocol
underneath first makes generators much easier to understand tomorrow.

## Worked example

See [`examples/iterators.py`](examples/iterators.py). Run it with:

```bash
python day-31/examples/iterators.py
```

## Exercises

1. **`exercise_1_manual_iter.py`** — given a list, get its iterator with
   `iter()` and call `next()` on it three times, printing each result.
2. **`exercise_2_stop_iteration.py`** — write a loop using `while True`,
   `next()`, and a `try`/`except StopIteration` (Day 28) that manually
   replicates a `for` loop over a short list.
3. **`exercise_3_custom_iterator.py`** — write a `CountDown` class (the
   reverse of `CountUp` above) that counts down from a starting number to 1.
4. **`exercise_4_even_iterator.py`** — write an iterator class `EvenNumbers`
   that yields only even numbers up to a limit when looped over.

## Common Gotchas

- **Calling `next()` on something that isn't an iterator.** `next([1, 2, 3])`
  raises `TypeError: 'list' object is not an iterator` — you need
  `next(iter([1, 2, 3]))`.
- **Forgetting `__iter__` must return `self`.** Without it, your object isn't
  recognized as its own iterator, and `for` loops over it fail.
- **An iterator is exhausted after one full pass.** Once `StopIteration` has
  been raised, calling `next()` again keeps raising it — you need a fresh
  `iter(...)` call to start over, exactly like a spent generator (Day 32).
- **Confusing "iterable" with "has a `for` loop written for it."** Any custom
  class you write for a `for` loop to work on must implement the protocol
  above (or [Day 32](../day-32/README.md)'s simpler `yield` form) — `for` does
  not work on arbitrary objects just because they hold data.
