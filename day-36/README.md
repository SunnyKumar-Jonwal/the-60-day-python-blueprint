# Day 36: Decorators II (with arguments)

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- Why a decorator sometimes needs its own arguments, separate from the
  function it wraps
- The three-level nested function pattern this requires
- Building a practical `@repeat(n)` decorator
- Building a practical `@retry(attempts)` decorator

## Explanation

### The problem: decorators that need configuration

Yesterday's decorators (`@shout`, `@announce`) took no arguments of their
own — just `@decorator_name` directly above a function. But what if you want
`@repeat(3)` — repeat the function call 3 times — where `3` is configurable?

`@repeat(3)` isn't calling the decorator on the function directly. It's
calling `repeat(3)` **first**, and whatever *that* returns becomes the actual
decorator applied to the function. This means `repeat` needs an extra layer:

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")
# Hello, Ada!
# Hello, Ada!
# Hello, Ada!
```

Three levels, each wrapping the next:

1. `repeat(times)` — takes the decorator's **own** argument (`3`), and
   returns...
2. `decorator(func)` — takes the function being decorated, and returns...
3. `wrapper(*args, **kwargs)` — the actual replacement that runs each time
   the decorated function is called.

Compare to Day 35's `@shout`, which only needed levels 2 and 3 — the extra
outer level is entirely what makes `@repeat(3)` (with its own argument)
different from `@shout` (with none).

### `_` as a variable name

`for _ in range(times):` uses `_` as the loop variable name — a Python
convention meaning "I need to loop this many times, but I don't actually use
the loop variable's value." Any name would work; `_` just signals "ignored"
to readers.

### A practical example: `@retry`

```python
def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"Attempt {attempt} failed: {error}")
            raise last_error
        return wrapper
    return decorator


@retry(3)
def flaky_function():
    raise ValueError("Something went wrong")


flaky_function()   # tries 3 times, printing each failure, then re-raises
```

This combines decorators with `try`/`except` (Day 28) — a good example of
how the tools from this course compose together in real code.

## Worked example

See [`examples/decorators_with_args.py`](examples/decorators_with_args.py).
Run it with:

```bash
python day-36/examples/decorators_with_args.py
```

## Exercises

1. **`exercise_1_repeat.py`** — build the `@repeat(times)` decorator above and
   apply it to a function that prints a message, with `times=2`.
2. **`exercise_2_repeat_return.py`** — modify `@repeat` so it collects every
   call's return value into a list and returns that list, instead of just the
   last result; apply it to a function returning a fixed value.
3. **`exercise_3_min_delay_style.py`** — build a `@require_positive` decorator
   (no arguments of its own — should NOT use the three-level pattern) that
   raises `ValueError` if any positional argument to the wrapped function is
   negative.
4. **`exercise_4_retry.py`** — build the `@retry(attempts)` decorator above,
   applied to a function that always raises, and observe the printed attempts
   before it re-raises (wrap the call in `try`/`except` so the script doesn't
   crash).

## Common Gotchas

- **Missing a level of nesting.** `@repeat(3)` needs `repeat(times)` to
   return `decorator`, and `decorator(func)` to return `wrapper` — skipping
   one level (e.g. trying to combine `decorator` and `wrapper` into one
   function) breaks the calling convention `@repeat(3)` expects.
- **Forgetting the outer call's parentheses.** `@repeat` (without calling it)
   applies `repeat` itself as the decorator, receiving the function as `times`
   — completely different from `@repeat(3)`, and will fail confusingly.
- **A decorator without its own arguments does NOT need the three-level
   pattern.** `@require_positive` (Exercise 3) only needs two levels
   (`decorator(func)` then `wrapper`), exactly like Day 35 — adding an unused
   third level "just in case" is unnecessary complexity.
- **Not returning the inner function at every level.** Each of `repeat`,
  `decorator` must explicitly `return` the next function down — forgetting a
  `return` anywhere in the chain makes the decorator silently produce `None`
  instead of a usable function.
