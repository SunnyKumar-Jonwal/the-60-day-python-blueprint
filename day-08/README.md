# Day 8: Functions

**Module:** 1 — Fundamentals

## What you'll learn

- Defining and calling functions with `def`
- Parameters, arguments, and `return`
- Default parameter values
- Keyword arguments
- Variable scope (local vs global)

## Explanation

### Defining and calling a function

A **function** is a named, reusable block of code. Define one with `def`, and run
it by calling its name followed by parentheses:

```python
def greet():
    print("Hello!")

greet()   # calling it — prints "Hello!"
```

Without calling it (`greet` with no parentheses), nothing happens — you've just
described the function, not run it.

### Parameters and arguments

A function can accept inputs, called **parameters** in the definition and
**arguments** when you actually call it:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")   # "Ada" is the argument passed to the `name` parameter
```

### `return`

`return` sends a value back to whoever called the function, and immediately exits
the function. Without `return`, a function's result is `None`:

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7
```

```python
def add_no_return(a, b):
    a + b   # computed, but never sent back anywhere

result = add_no_return(3, 4)
print(result)   # None
```

### Default parameter values

Give a parameter a default so callers can omit it:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ada")             # "Hello, Ada!"
greet("Ada", "Hi")        # "Hi, Ada!"
greet("Ada", greeting="Hey")  # "Hey, Ada!" -- keyword argument, explicit and clear
```

Calling with `greeting="Hey"` (naming the parameter) is a **keyword argument** —
useful once a function has several parameters, since it makes each call
self-documenting regardless of order.

### Scope

A variable created *inside* a function is **local** — it only exists while that
function runs, and can't be accessed from outside it:

```python
def f():
    x = 10   # local to f
    print(x)

f()
print(x)   # NameError: x is not defined out here
```

A variable defined outside any function is **global**, and can be *read* from
inside a function — but to reassign it from inside, you need the `global` keyword
(rarely a good idea; prefer passing values in and returning them out instead).

## Worked example

See [`examples/functions.py`](examples/functions.py). Run it with:

```bash
python day-08/examples/functions.py
```

## Exercises

1. **`exercise_1_square.py`** — write a function `square(n)` that returns `n * n`,
   and print the result of calling it with `5`.
2. **`exercise_2_greet_default.py`** — write a function `greet(name, greeting="Hello")`
   and call it twice: once with only `name`, once overriding `greeting`.
3. **`exercise_3_is_even.py`** — write a function `is_even(n)` that returns `True`
   or `False`, and print the result for `4` and `7`.
4. **`exercise_4_max_of_three.py`** — write a function `max_of_three(a, b, c)` that
   returns the largest of the three, without using the built-in `max()`.

## Common Gotchas

- **Forgetting `return`.** A function that only `print`s but never `return`s gives
  back `None` if you try to use its result — `x = greet("Ada")` sets `x` to `None`,
  not to anything useful.
- **Mutable default arguments.** `def f(items=[]):` reuses the *same* list across
  every call that doesn't pass its own — a classic Python trap you'll fully
  appreciate once you reach lists on Day 11. For now, just know: prefer `None` as a
  default and create the value inside the function body if needed.
- **Confusing parameters with arguments.** Parameters are the names in the `def`
  line; arguments are the actual values you pass when calling.
- **Trying to use a local variable outside its function.** If it was created
  inside a function and never `return`ed, it doesn't exist outside — this is
  scope, not a bug.
