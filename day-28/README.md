# Day 28: Exceptions (try / except / finally)

**Module:** 3 — OOP

## What you'll learn

- What an exception is (you've been seeing them crash programs since Day 3)
- Catching errors with `try`/`except`
- Catching specific exception types
- `finally` for cleanup code that always runs
- Raising your own exceptions with `raise`

## Explanation

### You've met exceptions all course long

Every crash you've seen so far — `ValueError` from `int("abc")`,
`IndexError` from an out-of-range list index, `KeyError` from a missing dict
key, `FileNotFoundError` from opening a missing file — is Python raising an
**exception**. Until today, you had no way to respond to one except letting
the program crash. `try`/`except` changes that.

### `try` / `except`

```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year you'll be {age + 1}")
except ValueError:
    print("That's not a valid number.")
```

Python runs the `try` block. If a `ValueError` happens anywhere inside it,
Python jumps straight to the matching `except` block instead of crashing, and
execution continues normally after it.

### Catching specific exception types

You can catch different exception types differently, and access the actual
exception object with `as`:

```python
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as error:
    print(f"Index problem: {error}")
except ValueError as error:
    print(f"Value problem: {error}")
```

Catching the specific exception type you expect (`ValueError`, `IndexError`,
`KeyError`, `FileNotFoundError`, ...) is much better practice than a bare
`except:` — a bare `except` also silently catches things you didn't expect
(including typos in your own code), which hides real bugs instead of handling
them.

### `else` and `finally`

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print(f"Result: {result}")   # runs only if the try block succeeded, no exception
finally:
    print("Done.")                # always runs, whether or not an exception happened
```

`finally` is commonly used for cleanup that must happen either way — though
for files specifically, `with` (Day 18) already handles this for you
automatically, which is why `with` is preferred over manual
`try`/`finally` + `close()`.

### Raising your own exceptions

`raise` lets you trigger an exception yourself, when your code detects a
problem it can't sensibly continue past:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    new_balance = withdraw(100, 500)
except ValueError as error:
    print(f"Withdrawal failed: {error}")
```

## Worked example

See [`examples/exceptions.py`](examples/exceptions.py). Run it with:

```bash
python day-28/examples/exceptions.py
```

## Exercises

1. **`exercise_1_catch_value_error.py`** — write a function `safe_int(text)`
   that returns `int(text)`, or `None` if it's not a valid number (catch
   `ValueError`); test it with a valid and an invalid string.
2. **`exercise_2_catch_multiple.py`** — write a function that indexes into a
   list with a given index, catching both `IndexError` and `TypeError`
   (e.g. if the index isn't an int), printing a specific message for each.
3. **`exercise_3_finally.py`** — write a `try`/`except`/`finally` block around
   a division that might raise `ZeroDivisionError`, printing `"Cleaning
   up..."` in `finally` regardless of the outcome.
4. **`exercise_4_raise.py`** — write a function `set_age(age)` that raises
   `ValueError` if `age < 0`, and call it inside a `try`/`except` with both a
   valid and an invalid value.

## Common Gotchas

- **Bare `except:` hides bugs.** `except:` (no type) catches *everything*,
  including exceptions you never intended to handle — always catch a specific
  exception type, or at minimum `except Exception:`.
- **Catching too broadly, too early.** Wrapping your entire program in one
  giant `try`/`except` makes it hard to know what actually failed — keep
  `try` blocks focused on the specific operation that might raise.
- **Forgetting exceptions stop execution at the point they're raised.** Code
  after the line that raised, still inside the same `try` block, never runs —
  execution jumps straight to `except`.
- **Using exceptions for normal control flow.** `try`/`except` is for
  handling genuinely exceptional situations (bad input, missing files) — a
  routine check like "is this list empty?" is clearer as a plain `if`
  (Day 6), not a `try` around code that would raise on empty input.
