# Day 35: Decorators I

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- What a decorator actually is (finally explained — you've used `@classmethod`,
  `@staticmethod`, and `@property` since Module 3)
- `*args` and `**kwargs`
- Writing your own decorator
- `functools.wraps`

## Explanation

### What a decorator really is

A decorator is a function that takes a function and returns a (usually
modified) function. That's the whole idea. Here's the mechanism without any
`@` syntax at all:

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


def greet():
    return "hello"


greet = shout(greet)   # replace greet with shout's wrapped version
print(greet())          # "HELLO"
```

`@` syntax is just shorthand for that reassignment:

```python
def shout(func):
    def wrapper():
        return func().upper()
    return wrapper


@shout
def greet():
    return "hello"


print(greet())   # "HELLO" -- @shout above greet is exactly "greet = shout(greet)"
```

This is why `@classmethod`, `@staticmethod` (Day 22), and `@property`
(Day 25) made sense to *use* before you knew how they worked — they follow
exactly this pattern, just built into Python or applied by a library.

### `*args` and `**kwargs`

The `wrapper` above only worked for functions that take no arguments. Real
functions take arguments, so a general-purpose decorator needs a way to
accept **any** arguments and pass them straight through:

```python
def my_function(*args, **kwargs):
    print(args)      # a tuple of all positional arguments
    print(kwargs)     # a dict of all keyword arguments


my_function(1, 2, name="Ada")
# (1, 2)
# {'name': 'Ada'}
```

`*args` collects any number of positional arguments into a tuple (Day 12);
`**kwargs` collects any number of keyword arguments into a dict (Day 13). The
names `args`/`kwargs` are convention, not a requirement — the `*`/`**` are
what matter.

### Writing a real decorator

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


add(3, 4)
# Calling add with (3, 4), {}
# add returned 7
```

`func(*args, **kwargs)` inside `wrapper` **unpacks** the collected arguments
back out to call the original function normally — collecting them with
`*`/`**` and unpacking them with `*`/`**` are the same syntax used in two
different directions.

### `functools.wraps`

Without help, a decorated function loses its original name and docstring —
`add.__name__` would show `"wrapper"`, not `"add"`, which makes debugging
confusing. `functools.wraps` fixes this:

```python
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_call
def add(a, b):
    return a + b


print(add.__name__)   # "add" -- without @wraps(func), this would print "wrapper"
```

Always use `@wraps(func)` on the inner wrapper function in any decorator you
write — it's a small addition that avoids a real, common source of confusion.

## Worked example

See [`examples/decorators.py`](examples/decorators.py). Run it with:

```bash
python day-35/examples/decorators.py
```

## Exercises

1. **`exercise_1_args_kwargs.py`** — write a function `describe_call(*args,
   **kwargs)` that prints the args tuple and kwargs dict, and call it with a
   mix of positional and keyword arguments.
2. **`exercise_2_simple_decorator.py`** — write a decorator `shout` that
   uppercases a wrapped function's string return value, and apply it to a
   `greet(name)` function.
3. **`exercise_3_timing_style.py`** — write a decorator `announce` that
   prints `"Starting {func.__name__}"` before calling the function and
   `"Finished {func.__name__}"` after, using `*args`/`**kwargs` so it works on
   any function.
4. **`exercise_4_wraps.py`** — add `@wraps(func)` to Exercise 3's `announce`
   decorator, and print `decorated_function.__name__` before and after adding
   it to show the difference.

## Common Gotchas

- **Forgetting `*args, **kwargs` in the wrapper.** A decorator's inner
  `wrapper()` with no parameters only works on functions that take zero
  arguments — decorate anything else and you get `TypeError: wrapper() takes
  0 positional arguments but N were given`.
- **Forgetting to `return` inside `wrapper`.** If `wrapper` calls
  `func(*args, **kwargs)` but doesn't `return` the result, the decorated
  function always returns `None`, silently dropping the real return value.
- **Forgetting `@wraps(func)`.** Not a functional bug, but it breaks
  `__name__`, `__doc__`, and makes stack traces and debugging tools show
  `wrapper` everywhere instead of the real function names.
- **Confusing decorator *definition* order with *application* order.** With
  multiple decorators stacked on one function, they apply bottom-up (closest
  to the function first) but you read them top-down — this course doesn't
  stack decorators, but it's worth knowing if you see it in other code.
