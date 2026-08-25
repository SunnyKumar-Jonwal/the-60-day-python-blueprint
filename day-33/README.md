# Day 33: Closures

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- Nested functions (a function defined inside another function)
- What a closure is and how it "remembers" its enclosing scope
- `nonlocal`
- A practical use: functions that build other, customized functions

## Explanation

### Nested functions

You can define a function inside another function. The inner function can
see variables from the outer function's scope:

```python
def outer():
    message = "Hello from outer"

    def inner():
        print(message)   # inner() can read outer()'s local variable

    inner()


outer()   # "Hello from outer"
```

### Closures: returning the inner function

The interesting part happens when the outer function **returns** the inner
function instead of calling it directly. The inner function keeps access to
the outer function's variables *even after the outer function has already
finished running*:

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet


hello_greeter = make_greeter("Hello")
hey_greeter = make_greeter("Hey")

print(hello_greeter("Ada"))   # "Hello, Ada!"
print(hey_greeter("Ada"))     # "Hey, Ada!"
```

`make_greeter("Hello")` runs, returns `greet`, and finishes — normally
`greeting` would then be gone. But `greet` is a **closure**: it "closes over"
`greeting` and keeps its own private reference to that specific value, alive
for as long as `hello_greeter` exists. Each call to `make_greeter(...)`
creates a fresh, independent `greeting` — that's why `hello_greeter` and
`hey_greeter` behave differently even though they were built from the same
function.

### `nonlocal`

By default, assigning to a variable inside a nested function creates a *new*
local variable there — it doesn't modify the outer one. `nonlocal` tells
Python "this name refers to the enclosing function's variable, not a new
local one":

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
```

Without `nonlocal count`, `count += 1` inside `increment` would raise
`UnboundLocalError` — Python would see the assignment and treat `count` as a
new local variable, which can't be incremented before it has a value.

### Why this matters

Closures are how you build a function that's customized with some
configuration, without needing a full class (Day 21) just to hold one or two
values. [Day 35](../day-35/README.md)'s decorators are themselves built using
exactly this pattern — a function that returns another function which closes
over the original one.

## Worked example

See [`examples/closures.py`](examples/closures.py). Run it with:

```bash
python day-33/examples/closures.py
```

## Exercises

1. **`exercise_1_basic_closure.py`** — write `make_multiplier(factor)` that
   returns a function multiplying its argument by `factor`; create a
   `double` and a `triple` from it and test both.
2. **`exercise_2_counter.py`** — write `make_counter()` (as above) using
   `nonlocal`, create two independent counters, and show they count
   separately.
3. **`exercise_3_accumulator.py`** — write `make_accumulator()` returning a
   function `add(n)` that keeps a running total across calls, using
   `nonlocal`.
4. **`exercise_4_power_function.py`** — write `make_power_function(exponent)`
   that returns a function computing `base ** exponent`; build a `square`
   function (exponent 2) and a `cube` function (exponent 3) from it.

## Common Gotchas

- **Forgetting `nonlocal` when mutating an outer variable.** `count += 1`
  inside a nested function without `nonlocal count` raises
  `UnboundLocalError: local variable 'count' referenced before assignment` —
  Python decides at compile time that any assigned-to name is local, unless
  told otherwise.
- **Thinking closures share state across different calls to the outer
  function.** `make_counter()` called twice creates two completely
  independent `count` variables — they don't affect each other.
- **`nonlocal` vs `global`.** `nonlocal` refers to the nearest *enclosing
  function's* scope; `global` refers to the module-level scope. They are not
  interchangeable, and `nonlocal` only works inside a nested function.
- **Overusing closures where a class would be clearer.** If you need several
  related pieces of state and several operations on them, a class (Day 21) is
  usually more readable than a tangle of nested functions and `nonlocal`.
