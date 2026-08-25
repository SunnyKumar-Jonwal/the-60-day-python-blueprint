# Day 29: Custom exceptions

**Module:** 3 — OOP

## What you'll learn

- Defining your own exception classes
- Why custom exceptions are more useful than reusing `ValueError` everywhere
- Adding data to a custom exception
- Building a small hierarchy of related custom exceptions

## Explanation

### Why define your own exception?

Yesterday you raised built-in exceptions like `ValueError`. That's fine for
simple cases, but as a program grows, generic exceptions become ambiguous —
if you catch `ValueError`, you can't tell *which* of the ten places in your
code that might raise a `ValueError` actually caused it. A **custom
exception** gives a specific, meaningful name to a specific problem in your
program.

### Defining a custom exception

A custom exception is just a class that inherits from `Exception` (or one of
its built-in subclasses, like `ValueError`) — combining what you learned about
inheritance on [Day 23](../day-23/README.md) with yesterday's exceptions:

```python
class InsufficientFundsError(Exception):
    pass
```

That's a complete, usable exception. Raise and catch it exactly like a
built-in one:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money in the account")
    return balance - amount


try:
    withdraw(100, 500)
except InsufficientFundsError as error:
    print(f"Withdrawal failed: {error}")
```

### Catching specifically vs. catching broadly

Because `InsufficientFundsError` inherits from `Exception`, you *could* catch
it with a bare `except Exception:` — but catching it by its specific name
lets you handle it differently from, say, a `FileNotFoundError` that might
also happen in the same `try` block. This is the entire point of defining it.

### Adding data to a custom exception

A custom exception is a normal class — give it its own `__init__` (Day 21) to
carry extra structured information, not just a message string:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount_requested):
        self.balance = balance
        self.amount_requested = amount_requested
        message = f"Cannot withdraw {amount_requested}: balance is only {balance}"
        super().__init__(message)   # sets up the standard str(error) message too


try:
    raise InsufficientFundsError(balance=100, amount_requested=500)
except InsufficientFundsError as error:
    print(error)                    # uses the message passed to super().__init__()
    print(error.amount_requested)   # 500 -- your own extra data, still accessible
```

### A small hierarchy of custom exceptions

Just like any classes, custom exceptions can form an inheritance hierarchy —
useful when several specific errors should all also be catchable together
under one umbrella:

```python
class BankError(Exception):
    """Base class for every error this bank account module can raise."""


class InsufficientFundsError(BankError):
    pass


class InvalidAmountError(BankError):
    pass


try:
    raise InvalidAmountError("Amount must be positive")
except BankError as error:   # catches InsufficientFundsError OR InvalidAmountError
    print(f"Bank error: {error}")
```

## Worked example

See [`examples/custom_exceptions.py`](examples/custom_exceptions.py). Run it
with:

```bash
python day-29/examples/custom_exceptions.py
```

## Exercises

1. **`exercise_1_basic_custom.py`** — define `NegativeAgeError(Exception)`,
   raise it from a function that rejects negative ages, and catch it.
2. **`exercise_2_with_data.py`** — define `OutOfStockError(Exception)` that
   stores `item_name` and `requested_quantity` via `__init__`, raise it, and
   print both pieces of data from the caught exception.
3. **`exercise_3_hierarchy.py`** — define a base `ValidationError(Exception)`
   and two subclasses `TooShortError` and `TooLongError`; raise one of them
   and catch it via the base `ValidationError`.
4. **`exercise_4_reraise_scenario.py`** — write a `validate_password(password)`
   function that raises `TooShortError` if under 8 characters or
   `TooLongError` if over 64, and test it with both a valid and an invalid
   password.

## Common Gotchas

- **Inheriting from `object` instead of `Exception`.** `class MyError: pass`
  (no parent, or the wrong parent) isn't a valid exception — `raise MyError()`
  fails with `TypeError: exceptions must derive from BaseException`. Always
  inherit from `Exception` (directly or indirectly).
- **Forgetting `super().__init__(message)`.** If you override `__init__` on a
  custom exception and don't call `super().__init__(...)`, `str(error)` and
  `print(error)` may not show a useful message.
- **Making the hierarchy too deep or too shallow.** One base exception with
  a handful of direct subclasses (as in the example above) covers most needs
  — don't build multiple inheritance levels of custom exceptions without a
  concrete reason to catch them at different levels.
- **Using custom exceptions for things that aren't really errors.** If
  something is an expected, normal outcome (like "search found nothing"),
  returning `None` or an empty list is usually clearer than raising and
  catching an exception for it.
