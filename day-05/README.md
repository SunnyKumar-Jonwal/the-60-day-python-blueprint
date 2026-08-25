# Day 5: Input & output

**Module:** 1 — Fundamentals

## What you'll learn

- Reading text from the user with `input()`
- `input()` always returns a string — and what that means for your code
- Formatting output with f-strings
- `print()`'s `sep` and `end` keyword arguments

## Explanation

### Getting input from the user

`input(...)` pauses your program, shows an optional prompt, and waits for the user
to type something and press Enter:

```python
name = input("What's your name? ")
print("Hello, " + name)
```

**Whatever the user types comes back as a `str` — always**, even if they type
`"25"`. If you need a number, you must convert it explicitly (Day 3):

```python
age_text = input("How old are you? ")
age = int(age_text)
print(age + 1)
```

If the user types something that isn't a valid number, `int(...)` raises a
`ValueError` and crashes the program — you'll learn to handle that gracefully with
exceptions starting Day 28.

### Formatting output: f-strings

An **f-string** lets you embed variables and expressions directly inside a string,
prefixed with `f`:

```python
name = "Ada"
age = 30
print(f"{name} is {age} years old.")          # Ada is 30 years old.
print(f"Next year, {name} will be {age + 1}.") # Next year, Ada will be 31.
```

Anything inside `{ }` is evaluated as a Python expression. You can also control
number formatting:

```python
price = 19.9
print(f"${price:.2f}")   # $19.90 — 2 decimal places
```

Before f-strings existed, people used `.format()` or `%` — you may see those in
older code, but f-strings are the modern, preferred way.

### `print()`'s `sep` and `end`

`print()` can take multiple values separated by commas — by default it joins them
with a space and ends with a newline. Both are customizable:

```python
print("a", "b", "c")                  # a b c
print("a", "b", "c", sep="-")         # a-b-c
print("Loading", end="...")           # no newline after
print("done")                          # continues on the same line: Loading...done
```

## Worked example

See [`examples/io_basics.py`](examples/io_basics.py) — note it doesn't call
`input()` directly, since example scripts need to run non-interactively to be
verified automatically. It simulates input by assigning to a variable instead;
[`examples/greet_interactive.py`](examples/greet_interactive.py) shows the real
interactive version — try running that one yourself in a terminal.

```bash
python day-05/examples/io_basics.py
```

## Exercises

1. **`exercise_1_fstrings.py`** — given a name and age, print a sentence using an
   f-string.
2. **`exercise_2_price_format.py`** — given a float price, print it formatted to 2
   decimal places with a `$` in front.
3. **`exercise_3_sep_end.py`** — print `"2024"`, `"08"`, `"25"` on one line
   separated by `-` (to look like a date), then print `"Done"` on the next line.
4. **`exercise_4_interactive.py`** — (run this one yourself in a terminal, it's not
   auto-verified) ask the user for their name and favorite number, then print a
   sentence combining both, converting the number to an int first.

## Common Gotchas

- **Forgetting `input()` returns a string.** `input("Age: ") + 1` crashes with a
  `TypeError` — you can't add an `int` to a `str`. Convert first: `int(input("Age: ")) + 1`.
- **Missing the `f` prefix.** `print("{name}")` prints the literal text `{name}`,
  not the variable's value — the `f` before the opening quote is what activates
  the substitution.
- **Extra/missing spaces in f-strings.** `f"{ name }"` includes the spaces from
  inside the braces if `name` itself has them; usually write `f"{name}"` with no
  padding inside the braces.
- **Mixing up `sep` and `end`.** `sep` controls what goes *between* multiple
  arguments to a single `print()` call; `end` controls what's added *after* the
  whole call finishes (default `"\n"`, a newline).
