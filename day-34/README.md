# Day 34: Lambdas & functional tools

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- `lambda` — small, anonymous, one-expression functions
- `map()` and `filter()`
- `functools.reduce()`
- When a `lambda` helps, and when a regular `def` is clearer

## Explanation

### `lambda` — anonymous functions

A `lambda` is a function written inline, with no name, limited to a single
expression (no statements, no multiple lines):

```python
square = lambda n: n * n
print(square(5))   # 25
```

This is exactly equivalent to:

```python
def square(n):
    return n * n
```

`lambda`s are almost never assigned to a variable like that in real code
(just write a regular `def` if you're naming it) — their real use is being
passed directly as an argument to another function, right where they're
needed, without the ceremony of a separate `def`.

You've actually already used this pattern — `key=lambda s: s["score"]` on
[Day 19](../day-19/README.md) and `__lt__` comparisons on
[Day 27](../day-27/README.md) both used a `lambda` to tell `sorted()`/`min()`/
`max()` what to compare by.

### `map()` — transform every item

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda n: n * n, numbers))
print(squared)   # [1, 4, 9, 16]
```

`map(function, iterable)` applies `function` to every item and returns a
**lazy** iterator (like a generator, Day 32) — wrap it in `list(...)` to see
all the results at once. This is the same result you'd get from
`[n * n for n in numbers]` — a list comprehension is usually considered more
readable in Python, but you'll see `map()` in other people's code, so it's
worth recognizing.

### `filter()` — keep only matching items

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)   # [2, 4, 6]
```

Same idea as `map()`, but the function returns `True`/`False`, and only items
where it's `True` are kept. Again, `[n for n in numbers if n % 2 == 0]`
(Day 15) does the same thing and is generally preferred in Python.

### `functools.reduce()` — combine into one value

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda acc, n: acc + n, numbers)
print(total)   # 10
```

`reduce(function, iterable)` repeatedly applies `function` to an accumulator
and the next item, collapsing the whole iterable into a single value. This
particular example is better written as `sum(numbers)` — `reduce` earns its
keep for combining logic that doesn't already have a built-in
(`sum`/`max`/`min`/`any`/`all`), like building a running product or merging
dicts.

`from functools import reduce` is this course's first real use of `import` —
[Day 37](../day-37/README.md) explains what's actually happening when you
write that line; for now, just know `functools` is part of Python's standard
library, and `reduce` isn't a built-in the way `map`/`filter` are, so it must
be imported before use.

### When to reach for each

In modern, idiomatic Python, comprehensions (Day 15) are usually preferred
over `map()`/`filter()` for simple cases — they read left-to-right and don't
need a `lambda`. Reach for `map()`/`filter()`/`reduce()` when working with
code that's already written in that style, or when passing an existing named
function (not a `lambda`) makes the intent especially clear:

```python
words = ["hello", "world"]
print(list(map(str.upper, words)))   # ["HELLO", "WORLD"] -- no lambda needed at all
```

## Worked example

See [`examples/functional_tools.py`](examples/functional_tools.py). Run it
with:

```bash
python day-34/examples/functional_tools.py
```

## Exercises

1. **`exercise_1_lambda_basics.py`** — write a `lambda` that returns whether a
   number is negative, and test it on a few values.
2. **`exercise_2_map.py`** — given a list of temperatures in Celsius, use
   `map()` with a `lambda` to convert them all to Fahrenheit.
3. **`exercise_3_filter.py`** — given a list of words, use `filter()` with a
   `lambda` to keep only the ones starting with a vowel.
4. **`exercise_4_reduce.py`** — given a list of numbers, use
   `functools.reduce()` to compute their product (running multiplication).

## Common Gotchas

- **Writing a multi-line `lambda`.** It's not possible — `lambda` bodies are
  a single expression only. If the logic needs more than one line, write a
  regular `def` instead.
- **Assigning a `lambda` to a variable just to call it later.** `square =
  lambda n: n * n` works, but a normal `def square(n): return n * n` is
  clearer and gives you a proper name for error messages and debugging —
  save `lambda` for inline use.
- **Forgetting `map()`/`filter()` return lazy iterators, not lists.**
  `map(...)` printed directly shows something like `<map object at 0x...>` —
  wrap it in `list(...)` to see the actual values, same idea as generators
  from Day 32.
- **Forgetting to import `reduce`.** Unlike `map`/`filter` (built-ins),
  `reduce` must be imported: `from functools import reduce`, or calling it
  raises `NameError`.
