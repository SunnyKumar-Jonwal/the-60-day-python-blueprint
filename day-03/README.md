# Day 3: Variables & data types

**Module:** 1 — Fundamentals

## What you'll learn

- What a variable is and how to create one
- Python's core built-in data types: `int`, `float`, `str`, `bool`
- Naming rules and conventions for variables
- How to check a value's type with `type()`

## Explanation

### Variables

A **variable** is a name that refers to a value stored in memory. You create one
with `=` (the **assignment operator**):

```python
age = 30
name = "Ada"
```

Unlike some languages, you don't have to declare a variable's type up front —
Python figures it out from the value you assign. This is called **dynamic typing**.

You can reassign a variable at any time, including to a value of a different type:

```python
score = 10
score = "ten"  # legal, but usually a sign of confusing code — avoid mixing types like this
```

### Naming rules

- Must start with a letter or underscore, not a digit: `age`, `_temp` are valid;
  `2fast` is not.
- Can contain letters, digits, and underscores after that.
- Case-sensitive: `Age` and `age` are different variables.
- By convention, Python variables use `snake_case`: `first_name`, not `firstName` or
  `FirstName`.
- Avoid Python's reserved keywords (`if`, `for`, `class`, ...) as variable names.

### Core data types

| Type | Example | Meaning |
|---|---|---|
| `int` | `42`, `-7` | Whole number |
| `float` | `3.14`, `-0.5` | Decimal number |
| `str` | `"hello"` | Text ("string") |
| `bool` | `True`, `False` | Truth value |

```python
age = 30          # int
price = 19.99      # float
name = "Ada"       # str
is_student = False # bool
```

### Checking a type

`type(...)` tells you what type a value currently is:

```python
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
```

### Converting between types

You'll often need to convert one type to another — for example, `input()` (Day 5)
always gives you a string, even if the user typed a number.

```python
str(42)      # "42"
int("42")    # 42
float("3.14")# 3.14
int(3.9)     # 3  (int() truncates, it doesn't round)
```

## Worked example

See [`examples/variables.py`](examples/variables.py). Run it with:

```bash
python day-03/examples/variables.py
```

## Exercises

1. **`exercise_1_basic_vars.py`** — create variables for your name (str), age (int),
   and height in meters (float), and print each one.
2. **`exercise_2_type_check.py`** — print the `type()` of four given values.
3. **`exercise_3_conversion.py`** — convert a string `"25"` to an int and add `5` to
   it, printing the result.
4. **`exercise_4_reassign.py`** — create a variable, print it and its type, reassign
   it to a value of a different type, then print it and its type again.

## Common Gotchas

- **Confusing `=` with `==`.** `=` assigns a value; `==` (Day 4) compares two values.
  `x = 5` sets `x` to `5`. `x == 5` asks "is `x` equal to `5`?" and gives back a
  `bool`.
- **`int("3.14")` fails.** You can't convert a string containing a decimal point
  straight to `int` — convert to `float` first, then `int` if you want to truncate:
  `int(float("3.14"))`.
- **Naming collisions with built-ins.** Naming a variable `str = "hi"` or
  `list = [1, 2]` shadows Python's built-in `str`/`list`, breaking them for the rest
  of that file. Avoid reusing built-in names as variable names.
- **`True`/`False` must be capitalized.** `true` and `false` (lowercase) are not
  valid booleans in Python — they'd be treated as undefined variable names.
