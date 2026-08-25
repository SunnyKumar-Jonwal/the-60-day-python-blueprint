# Day 9: Intro to type hints

**Module:** 1 — Fundamentals

## What you'll learn

- What type hints are and why people use them
- Annotating variables and function parameters
- Annotating function return types
- What type hints *don't* do (they're not enforced at runtime)

## Explanation

### What are type hints?

A **type hint** is an optional annotation that documents what type a variable or
function parameter is expected to hold:

```python
age: int = 30
name: str = "Ada"
price: float = 19.99
is_active: bool = True
```

This is exactly the same as writing `age = 30` — Python doesn't check or enforce
the hint at runtime. It's purely documentation, but extremely valuable
documentation: your editor can use it to catch mistakes before you even run the
code, and it tells other readers (including future you) what a function expects
without them having to read its whole body.

### Annotating functions

This is where type hints earn their keep — a function signature with hints tells
you everything about how to call it, at a glance:

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` and `b: int` say both parameters should be `int`.
- `-> int` says the function returns an `int`.

Compare to the same function without hints — `def add(a, b):` — where you'd have
to read the body (or trust the name) to guess what types are expected.

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

Default values combine with hints normally — the hint comes right after the
parameter name, and the default comes after that.

### Type hints are not enforced

Python will *not* stop you from calling `add("2", "3")` even though both parameters
are hinted as `int` — you'd get `"23"` back (string concatenation), not a crash, and
not a warning. Hints are a contract you and your tools agree to honor, not a wall
Python builds for you. Tools like `mypy` (not covered in this course) can check
your code against its hints and flag violations before you run it — that's the
real payoff, but it's an extra step, not something Python does automatically.

### More types are coming

You've only met `int`, `float`, `str`, `bool` so far. Once you learn lists, tuples,
dicts, and sets starting Day 11, you'll be able to hint those too (e.g.
`list[int]`, `dict[str, int]`) — for now, stick to the basic types.

## Worked example

See [`examples/type_hints.py`](examples/type_hints.py). Run it with:

```bash
python day-09/examples/type_hints.py
```

## Exercises

1. **`exercise_1_annotate_vars.py`** — add type hints to three given variable
   assignments.
2. **`exercise_2_hinted_function.py`** — write a hinted function
   `multiply(a: int, b: int) -> int` and call it.
3. **`exercise_3_default_hinted.py`** — write a hinted function
   `power(base: float, exponent: int = 2) -> float` and call it twice.
4. **`exercise_4_mismatch.py`** — deliberately call a hinted function with the
   "wrong" type and print the (surprising, still-working) result, to see for
   yourself that hints aren't enforced.

## Common Gotchas

- **Thinking hints prevent bugs by themselves.** They don't, unless you also run a
  type checker like `mypy`, which this course doesn't cover — treat them as
  documentation for now.
- **Forgetting the `->` for return types.** `def add(a: int, b: int) int:` (no
  arrow) is a syntax error — it must be `-> int:`.
- **Over-hinting too early.** Don't stress about hinting every single line, e.g.
  loop counters — hints earn the most value on function signatures, which is where
  this course focuses them.
- **Hinting with a value that doesn't match.** `age: int = "30"` is legal Python
  (it runs) but is misleading and defeats the point — keep the hint honest.
