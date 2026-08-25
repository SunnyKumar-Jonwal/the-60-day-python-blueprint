# Day 25: Encapsulation

**Module:** 3 — OOP

## What you'll learn

- Public, "protected" (`_`), and "private" (`__`) naming conventions
- Why Python doesn't truly enforce privacy, and what it does instead
- `@property` for controlled attribute access
- Validating data on write with a property setter

## Explanation

### What encapsulation means

**Encapsulation** is about controlling access to an object's internal data —
hiding details that outside code shouldn't need to touch directly, and
exposing a clean, controlled interface instead. This protects an object from
being put into an invalid state by code elsewhere that pokes directly at its
attributes.

### Naming conventions

Python doesn't have real access control keywords like `private`/`public` from
other languages. Instead, it uses **naming conventions** that programmers are
expected to respect:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance         # public -- anyone can read/write freely
        self._pin = "1234"              # "protected" -- a single leading underscore
        self.__account_number = "42"    # "private" -- double leading underscore
```

- **No underscore** (`balance`): fully public, freely accessible from anywhere.
- **Single leading underscore** (`_pin`): a convention meaning "internal, don't
  touch this from outside the class" — Python doesn't stop you, it's a polite
  signal to other programmers.
- **Double leading underscore** (`__account_number`): triggers **name
  mangling** — Python internally renames it to `_BankAccount__account_number`,
  which makes accidental access from outside (or from a subclass) unlikely,
  though still not truly impossible for someone determined.

Nothing here is a hard security boundary — Python trusts programmers to
respect the convention rather than enforcing it at the language level.

### `@property` — controlled access

A **property** lets you expose a method that's *called like an attribute* (no
parentheses), which is the standard way in Python to add validation or
computed values without changing how callers use your class:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
```

```python
account = BankAccount(100)
print(account.balance)     # 100 -- calls the @property method, no parentheses
account.balance = 150       # calls the @balance.setter method
print(account.balance)     # 150
account.balance = -50       # raises ValueError -- the setter rejects it
```

From the outside, `account.balance` looks exactly like a plain attribute — but
every read goes through your `@property` method, and every write goes through
your validation in the setter. This is the real payoff of encapsulation in
Python: you can start with a plain public attribute, and later add validation
via a property *without breaking any code that already uses
`account.balance`*.

## Worked example

See [`examples/encapsulation.py`](examples/encapsulation.py). Run it with:

```bash
python day-25/examples/encapsulation.py
```

## Exercises

1. **`exercise_1_conventions.py`** — define a `Person` class with a public
   `name`, a `_notes` (protected) attribute, and a `__ssn` (private) attribute;
   print all three from inside a method to show they're all still accessible
   from within the class.
2. **`exercise_2_property_get.py`** — define a `Temperature` class storing
   `_celsius`, with a `@property` `celsius` that returns it, and a computed
   `@property` `fahrenheit` that converts on the fly.
3. **`exercise_3_property_set.py`** — add a setter to `Temperature.celsius`
   that raises `ValueError` if the value is below -273.15 (absolute zero); set
   a valid value and print it (don't actually trigger the error yet — you'll
   learn to catch exceptions safely on [Day 28](../day-28/README.md)).
4. **`exercise_4_validated_account.py`** — define a `BankAccount` class with a
   `balance` property whose setter rejects negative values; set a valid
   balance and print it.

## Common Gotchas

- **Thinking `__name` is truly private.** It's name-mangled, not hidden —
  `account._BankAccount__account_number` still works from outside if someone
  really wants to reach in. Treat it as a strong hint, not a lock.
- **Forgetting `@balance.setter` must use the same method name as the
  `@property`.** `@property def balance(self): ...` paired with
  `@balance.setter def set_balance(self, value): ...` (different name) doesn't
  connect them — the setter's `def` name must match the property's exactly.
- **Setting the underlying attribute directly, bypassing the property.** If
  your property is named `balance` and backed by `self._balance`, code
  outside the class that somehow sets `self._balance` directly skips your
  validation entirely — this is exactly why the leading-underscore convention
  matters, even though Python won't stop it.
- **Adding properties to every single attribute "just in case."** Plain public
  attributes are fine and idiomatic in Python when there's no validation or
  computed logic needed — reach for `@property` when you actually need to
  intercept reads or writes, not by default.
