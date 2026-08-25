# Day 6: Control flow (if / elif / else)

**Module:** 1 — Fundamentals

## What you'll learn

- How to make decisions in code with `if`, `elif`, `else`
- How indentation defines code blocks in Python
- Nesting conditionals
- Truthy and falsy values

## Explanation

### `if`, `elif`, `else`

A conditional runs a block of code only when a condition is `True`:

```python
age = 20

if age >= 18:
    print("You're an adult.")
```

Add `elif` (short for "else if") for additional conditions, and `else` for a
catch-all when none of them matched:

```python
score = 72

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

Conditions are checked top to bottom; the **first** one that's `True` runs, and the
rest are skipped — even if a later one would also be `True`.

### Indentation matters

Python uses indentation (4 spaces is the standard convention) to show which lines
belong to which block — there are no `{ }` braces. Everything indented under an
`if`/`elif`/`else` line belongs to that branch:

```python
if age >= 18:
    print("This line runs only if age >= 18.")
    print("So does this one.")
print("This line always runs — it's not indented under the if.")
```

Mixing tabs and spaces, or inconsistent indentation, causes an `IndentationError`.

### Nesting

Conditionals can contain other conditionals:

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Entry denied: no ID.")
else:
    print("Entry denied: underage.")
```

Often, combining conditions with `and`/`or` (Day 4) reads more cleanly than nesting:

```python
if age >= 18 and has_id:
    print("Entry allowed.")
```

### Truthy and falsy values

`if` doesn't strictly require a `bool` — Python treats some values as automatically
"falsy" when used in a condition: `0`, `0.0`, `""` (empty string), `None`, and empty
collections (you'll meet these starting Day 11) are all falsy. Everything else is
"truthy":

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("No name given.")   # this runs, because "" is falsy
```

## Worked example

See [`examples/grading.py`](examples/grading.py). Run it with:

```bash
python day-06/examples/grading.py
```

## Exercises

1. **`exercise_1_even_odd.py`** — given a number, print `"Even"` or `"Odd"`.
2. **`exercise_2_grade.py`** — given a score, print a letter grade using
   `if`/`elif`/`else` (A: 90+, B: 80+, C: 70+, F: below 70).
3. **`exercise_3_login.py`** — given a username and password, print `"Access
   granted"` only if both match expected values (use `and`), otherwise `"Access
   denied"`.
4. **`exercise_4_falsy.py`** — given a string that might be empty, print
   `"Empty!"` if it's falsy, otherwise print the string itself.

## Common Gotchas

- **Forgetting the colon `:`.** `if age >= 18` (no colon) is a syntax error —
  every `if`/`elif`/`else` line must end with `:`.
- **Inconsistent indentation.** Mixing 2 and 4 spaces (or tabs and spaces) in the
  same block raises `IndentationError`. Pick 4 spaces and stay consistent — most
  editors do this automatically once configured for Python.
- **Using `=` instead of `==` in a condition.** `if age = 18:` is a syntax error in
  Python (good — it prevents a classic bug), you want `if age == 18:`.
- **Unreachable `elif` branches.** If an earlier condition is broader than a later
  one (e.g. `if score >= 70:` before `elif score >= 90:`), the later branch can
  never run — order conditions from most to least specific.
