# Day 7: Loops (for / while)

**Module:** 1 — Fundamentals

## What you'll learn

- Repeating code with `for` and `range()`
- Repeating code with `while`
- `break` and `continue`
- Avoiding infinite loops

## Explanation

### `for` loops and `range()`

A `for` loop repeats a block of code once per item in a sequence. `range(...)`
generates a sequence of numbers:

```python
for i in range(5):
    print(i)
# prints 0, 1, 2, 3, 4 — range(5) starts at 0 and stops *before* 5
```

`range()` has three forms:

```python
range(5)        # 0, 1, 2, 3, 4          (stop only)
range(2, 5)     # 2, 3, 4                (start, stop)
range(0, 10, 2) # 0, 2, 4, 6, 8          (start, stop, step)
```

You can also loop directly over the characters of a string (you'll loop over lists,
dicts, and more starting Day 11):

```python
for letter in "abc":
    print(letter)
```

### `while` loops

A `while` loop repeats as long as its condition stays `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1   # without this, the loop would run forever
```

Use `while` when you don't know in advance how many times you'll repeat (e.g.
"keep asking until the user enters a valid number") — use `for` when you're
iterating over a known sequence or a known number of times.

### `break` and `continue`

- `break` exits the loop immediately, skipping anything left in it.
- `continue` skips the rest of *this* iteration and moves to the next one.

```python
for i in range(10):
    if i == 5:
        break        # stop the loop entirely once i reaches 5
    print(i)          # prints 0, 1, 2, 3, 4

for i in range(10):
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)          # prints 1, 3, 5, 7, 9
```

### Avoiding infinite loops

A `while` loop whose condition never becomes `False` runs forever. This is a very
common beginner bug:

```python
count = 0
while count < 5:
    print(count)
    # forgot count += 1 -- this never ends!
```

If your program hangs and never finishes, this is the first thing to check.

## Worked example

See [`examples/loops.py`](examples/loops.py). Run it with:

```bash
python day-07/examples/loops.py
```

## Exercises

1. **`exercise_1_countdown.py`** — print numbers from 5 down to 1 using `range()`
   with a negative step, then print `"Liftoff!"`.
2. **`exercise_2_sum.py`** — sum the numbers from 1 to 100 (inclusive) using a
   `for` loop, and print the total.
3. **`exercise_3_while_guess.py`** — starting from `1`, use a `while` loop to count
   up one at a time until you reach a target number, then print how many tries it
   took.
4. **`exercise_4_skip_multiples.py`** — print numbers 1 to 20, skipping any
   multiple of 3, using `continue`.

## Common Gotchas

- **Off-by-one errors with `range()`.** `range(5)` stops *before* 5 (gives you
  0-4), which trips people up when they expect it to include 5.
- **Forgetting to update the loop variable in a `while` loop.** This causes an
  infinite loop — always double check the condition will eventually become False.
- **Modifying a list while looping over it** (once you reach Day 11) causes items
  to be skipped or revisited unexpectedly — not an issue yet today, but worth
  remembering once you get there.
- **`break` only exits the innermost loop.** If you have a loop inside another
  loop, `break` stops the inner one only, not both.
