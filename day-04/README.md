# Day 4: Operators

**Module:** 1 — Fundamentals

## What you'll learn

- Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- Shorthand assignment operators (`+=`, `-=`, ...)
- Operator precedence

## Explanation

### Arithmetic operators

```python
7 + 3   # 10  addition
7 - 3   # 4   subtraction
7 * 3   # 21  multiplication
7 / 3   # 2.333...  division — always returns a float
7 // 3  # 2   floor division — divides and rounds down to the nearest whole number
7 % 3   # 1   modulo — the remainder after division
7 ** 3  # 343 exponent — 7 to the power of 3
```

`/` (true division) always gives a `float`, even when the numbers divide evenly
(`6 / 3` is `2.0`, not `2`). `//` (floor division) gives you a whole number.

### Comparison operators

These compare two values and always give back a `bool` (`True`/`False`):

```python
5 == 5   # True   equal to
5 != 3   # True   not equal to
5 > 3    # True   greater than
5 < 3    # False  less than
5 >= 5   # True   greater than or equal to
5 <= 3   # False  less than or equal to
```

### Logical operators

These combine or invert boolean values:

```python
True and False   # False — both sides must be True
True or False    # True  — at least one side must be True
not True         # False — flips the value
```

A common use is combining comparisons:

```python
age = 25
is_adult_but_not_senior = age >= 18 and age < 65
```

### Shorthand assignment operators

A compact way to update a variable based on its current value:

```python
x = 10
x += 5   # same as x = x + 5  -> 15
x -= 3   # same as x = x - 3  -> 12
x *= 2   # same as x = x * 2  -> 24
x /= 4   # same as x = x / 4  -> 6.0
```

### Operator precedence

Just like in math, `**` and `*`/`/` are evaluated before `+`/`-`. Use parentheses
`( )` whenever you're not 100% sure of the order, or just to make intent clear:

```python
2 + 3 * 4    # 14, not 20 — multiplication happens first
(2 + 3) * 4  # 20 — parentheses force addition first
```

## Worked example

See [`examples/operators.py`](examples/operators.py). Run it with:

```bash
python day-04/examples/operators.py
```

## Exercises

1. **`exercise_1_arithmetic.py`** — given two numbers, print the result of all six
   arithmetic operators applied to them.
2. **`exercise_2_comparisons.py`** — given two numbers, print the result of all six
   comparison operators applied to them.
3. **`exercise_3_logical.py`** — given an age, print whether the person is a
   "working-age adult" (18 <= age < 65) using `and`.
4. **`exercise_4_shorthand.py`** — start with a variable at `100`, apply `-=`, `*=`,
   and `//=` in sequence, printing the value after each step.

## Common Gotchas

- **`/` vs `//`.** `/` always gives a float; `//` gives a whole number (rounded
  toward negative infinity, not just truncated — `-7 // 2` is `-4`, not `-3`).
- **Chained comparisons look right but can surprise you.** `1 < 2 < 3` does work in
  Python (`True`) and means `1 < 2 and 2 < 3` — but don't rely on this reading
  intuitively coming from other languages.
- **`=` vs `==` again.** Using `=` inside a comparison, like `if x = 5:`, is a
  syntax error in Python — good, because that's a classic bug in other languages.
- **`and`/`or` short-circuit.** In `a() and b()`, if `a()` is falsy, `b()` never
  runs at all. This matters once you write functions with side effects.
