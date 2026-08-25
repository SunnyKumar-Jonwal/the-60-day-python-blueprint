# Python Interview Question Bank

30 common Python interview questions, spanning the whole 60-day course, with
explained answers — not just the answer, but the *why*. Use this as a final
review, or dip into a section that matches whatever module you just
finished.

## Fundamentals

### 1. What's the difference between a list and a tuple?

Both are ordered collections. A list (`[1, 2, 3]`) is **mutable** — you can
append, remove, or reassign items. A tuple (`(1, 2, 3)`) is **immutable** —
once created, it can't be changed. Use a tuple for a fixed group of values
(like coordinates), and a list for a collection that grows, shrinks, or
gets reordered. See [Day 11](day-11/README.md) and [Day 12](day-12/README.md).

### 2. What does "mutable" vs "immutable" mean, and which built-in types are which?

A **mutable** object can be changed in place after creation; an
**immutable** one cannot — "changing" it means creating a new object.
Immutable: `int`, `float`, `str`, `bool`, `tuple`. Mutable: `list`, `dict`,
`set`. This matters for function defaults (see Q7), for dict/set keys (only
immutable types can be keys, because a key's hash must never change while
it's in use), and for reasoning about whether two variables referring to
"the same" value can affect each other.

### 3. What's the difference between `==` and `is`?

`==` checks whether two values are **equal**; `is` checks whether two names
refer to the **exact same object in memory** (identity). `a == b` can be
`True` while `a is b` is `False` (two separate lists with the same
contents, for example). `is` is mainly used to check against `None`
(`if x is None:`), never for general value comparison.

### 4. What is a "truthy" or "falsy" value in Python?

In a boolean context (`if`, `while`, `and`/`or`), Python treats some values
as automatically `False` even though they aren't literally the `bool`
`False`: `0`, `0.0`, `""`, `None`, and empty collections (`[]`, `{}`, `()`,
`set()`). Everything else is truthy. See [Day 6](day-06/README.md).

### 5. What's the difference between `*args` and `**kwargs`?

`*args` collects any number of extra **positional** arguments into a
tuple; `**kwargs` collects any number of extra **keyword** arguments into a
dict. Both let a function accept a flexible, unknown-in-advance number of
arguments — most commonly seen in decorators (see Q20), where the wrapper
needs to pass through whatever arguments the wrapped function was actually
called with. See [Day 35](day-35/README.md).

## Data structures & files

### 6. When would you use a set instead of a list?

When you need **uniqueness** (a set automatically drops duplicates) or fast
**membership testing** (`x in some_set` is much faster than `x in
some_list` for large collections), and you don't care about order. Sets
also support mathematical operations like union (`|`), intersection (`&`),
and difference (`-`). See [Day 14](day-14/README.md).

### 7. What happens if you use a mutable default argument in a function?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The default list is created **once**, when the function is defined — not
fresh on every call. Every call that doesn't pass its own `items` shares and
mutates that *same* list, so results accumulate unexpectedly across calls.
The fix: default to `None`, and create a new list inside the function body
if it wasn't provided.

### 8. How do you safely access a dictionary key that might not exist?

`some_dict.get(key)` returns `None` (or a default you specify:
`.get(key, default)`) instead of raising `KeyError` the way `some_dict[key]`
would. Alternatively, check first with `if key in some_dict:`. See
[Day 13](day-13/README.md).

## Object-oriented programming

### 9. What's the difference between a class and an instance?

A **class** is the blueprint (`class Dog:`); an **instance** (or object) is
one specific thing built from that blueprint (`rex = Dog("Rex")`). Many
instances can be created from one class, each with its own independent
attribute values. See [Day 21](day-21/README.md).

### 10. What's the purpose of `self`?

`self` refers to the specific instance a method is being called on. It's
always the first parameter of an instance method, and Python passes it
automatically (`rex.bark()` is really `Dog.bark(rex)` underneath) — you
never supply it yourself when calling. Inside a method, `self.name` reads
or writes *this instance's* `name`, not some shared value.

### 11. What is inheritance, and what problem does it solve?

Inheritance lets a class (the subclass) reuse another class's (the parent's)
attributes and methods, adding or overriding only what's different — it
avoids duplicating shared logic across related classes. `class Dog(Animal):`
means every `Dog` "is an" `Animal` too. See [Day 23](day-23/README.md).

### 12. What is polymorphism, in your own words?

Different classes exposing the same method name, so code that calls that
method works with any of them without needing to know which specific class
it's dealing with. In Python this doesn't require inheritance at all (duck
typing) — if an object has a `.speak()` method, code that calls `.speak()`
works, regardless of the object's actual class. See [Day 24](day-24/README.md).

### 13. What's the difference between `__str__` and `__repr__`?

`__str__` is for a human-readable representation, used by `print()` and
`str()`. `__repr__` is for an unambiguous, developer-facing representation,
used by `repr()` and whenever an object appears inside another structure
being printed (like a list of objects). If only `__repr__` is defined,
`print()` falls back to it. See [Day 26](day-26/README.md).

### 14. What is encapsulation, and how does Python implement it without true "private" members?

Encapsulation means controlling access to an object's internal data. Python
doesn't enforce privacy at the language level — instead it uses naming
conventions (`_protected`, `__private` with name-mangling) that other
programmers are expected to respect, plus `@property` to add validation or
computed logic to attribute access without changing how callers use the
class. See [Day 25](day-25/README.md).

### 15. What's the difference between an instance method, a `@classmethod`, and a `@staticmethod`?

An instance method takes `self` and operates on one specific object. A
`@classmethod` takes `cls` (the class itself) instead — commonly used for
alternative constructors. A `@staticmethod` takes neither — it's a plain
function that's grouped inside the class because it's conceptually related,
but doesn't need any instance or class data. See [Day 22](day-22/README.md).

### 16. Why create a custom exception class instead of just raising `ValueError`?

A custom exception (`class InsufficientFundsError(Exception):`) gives a
specific, unambiguous name to a specific failure — if you catch
`ValueError`, you can't tell which of several possible causes actually
triggered it. A custom exception can also carry extra structured data
(via its own `__init__`), and a small hierarchy of related custom
exceptions can share a common base class so callers can catch them broadly
or specifically as needed. See [Day 29](day-29/README.md).

## Functional features

### 17. What is a generator, and how is it different from a function that returns a list?

A function that returns a list builds and holds the **entire** result in
memory before returning it. A **generator** function (one containing
`yield`) produces values **lazily**, one at a time, pausing between each —
it never holds more than the current value in memory. This matters a lot
for large or infinite sequences. See [Day 32](day-32/README.md).

### 18. What does the `yield` keyword do?

`yield` pauses a function's execution and hands back a value, without
losing the function's local state — the next time the generator is asked
for a value (via `next()` or a `for` loop), execution resumes right after
that `yield`. A function containing `yield` becomes a generator function;
calling it doesn't run the body immediately, it creates a generator object.

### 19. What is a closure?

A function defined inside another function that "remembers" variables from
its enclosing scope, even after the outer function has finished running.
`make_multiplier(2)` returning an inner function that still has access to
`factor = 2` on every later call is a closure. `nonlocal` is needed if the
inner function needs to *reassign* (not just read) an outer variable. See
[Day 33](day-33/README.md).

### 20. What is a decorator, and how would you write a simple one?

A decorator is a function that takes a function and returns a (usually
wrapped) function, letting you add behavior to a function without modifying
its source. `@my_decorator` above `def f():` is shorthand for `f =
my_decorator(f)`.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

See [Day 35](day-35/README.md).

### 21. What's the difference between a list comprehension and a generator expression?

They look almost identical (`[x for x in y]` vs `(x for x in y)`), but a
list comprehension builds the entire list immediately and holds it in
memory; a generator expression produces values lazily, like a generator
function, without building anything until values are actually requested.
See [Day 15](day-15/README.md) and [Day 32](day-32/README.md).

## Real-world libraries & testing

### 22. What's the purpose of `assert` in a test, versus using it as a general runtime check?

In a **test**, `assert condition` is how pytest recognizes a pass/fail —
if `condition` is falsy, `AssertionError` is raised and pytest reports that
test as failed. In general application code, `assert` is not a substitute
for real error handling: it can be globally disabled (`python -O`), so it
should never guard something the program depends on for correctness — use
`raise` and real exceptions for that instead. See [Day 47](day-47/README.md).

### 23. Why use the `logging` module instead of `print()` in a real application?

`logging` supports **severity levels** (DEBUG/INFO/WARNING/ERROR/CRITICAL)
that can be filtered without deleting code, structured **formatting**
(timestamps, source), and routing output to files or elsewhere — none of
which plain `print()` gives you. Turning off noisy debug output across an
entire codebase is a one-line change with `logging`, versus hunting down
and deleting/commenting every relevant `print()`. See [Day 48](day-48/README.md).

### 24. What is the purpose of a pytest fixture?

A fixture provides reusable setup (data, objects, connections) that
multiple test functions can share, without repeating the setup code in
every test. A test function receives a fixture's value automatically by
naming it as a parameter — pytest matches them by name. See
[Day 47](day-47/README.md).

## Web APIs & databases

### 25. What's the conventional difference between `POST` and `PUT` in a REST API?

`POST` conventionally means "create a new resource" (e.g. `POST /books`
adds a new book). `PUT` conventionally means "replace an existing resource
entirely" at a known URL (e.g. `PUT /books/5` replaces book 5's data). Using
`POST` for updates works technically but breaks the convention other
developers (and tools) expect. See [Day 56](day-56/README.md).

### 26. Why are parameterized queries important when working with SQL?

Building a SQL query by directly inserting a variable into a string (with
an f-string or `+`) opens the door to **SQL injection** — a malicious input
value can alter the SQL that actually runs, including deleting data or
bypassing checks. A parameterized query (`cursor.execute("... WHERE id =
?", (value,))`) makes the database treat the value purely as data, never as
part of the SQL command itself. This isn't a style preference — it's a real
security requirement. See [Day 54](day-54/README.md).

### 27. What does FastAPI do with a function's type hints?

FastAPI reads a route function's parameter type hints to automatically
**validate and convert** incoming request data (path params, query params,
request bodies via Pydantic models), and to **generate interactive API
documentation** — the same type hints you write for your own clarity double
as the mechanism that powers request validation and the `/docs` page. See
[Day 51](day-51/README.md) and [Day 52](day-52/README.md).

### 28. What's the difference between using `TestClient` and starting a live server to test an API?

`TestClient` (built on `httpx`) calls a FastAPI app directly, in-process —
no network, no port, no actual server process. It's faster and more
reliable for automated tests than starting `uvicorn` and sending real HTTP
requests, and it's what the tests throughout this course's capstone use.
Starting a live server is still useful for manual, exploratory testing
(`curl`, a browser, `/docs`). See [Day 57](day-57/README.md).

## General

### 29. What is the GIL (Global Interpreter Lock), at a conceptual level?

The GIL is a lock in CPython (the standard Python implementation) that
allows only **one thread** to execute Python bytecode at a time, even on a
multi-core machine. This means Python threads don't give you true parallel
execution of Python code (though they're still useful for I/O-bound work,
where a thread spends most of its time waiting, not computing). For
CPU-bound parallelism, Python code typically uses multiple **processes**
instead of threads. This course doesn't cover concurrency in depth — this
is a conceptual awareness question, not something you've built with here.

### 30. Is Python compiled or interpreted?

Python source is compiled to an intermediate **bytecode** (`.pyc` files),
which is then executed by the Python interpreter (a virtual machine) — so
it's not purely interpreted line-by-line the way some simpler scripting
languages historically were, but it's also not compiled all the way to
native machine code ahead of time the way C or Rust are. In practice,
Python is usually just called an interpreted language because that
bytecode compilation is automatic and invisible — you never see or manage a
separate build step, which is exactly the fast "write it, run it" loop
[Day 1](day-01/README.md) described.
