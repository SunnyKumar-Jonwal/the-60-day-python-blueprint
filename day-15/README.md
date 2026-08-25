# Day 15: Comprehensions

**Module:** 2 — Data Structures & Files

## What you'll learn

- List comprehensions
- Adding a condition (filtering) to a comprehension
- Dict comprehensions
- Set comprehensions
- When a comprehension is (and isn't) the right choice

## Explanation

### The problem comprehensions solve

You already know how to build a list by looping and appending:

```python
squares = []
for n in range(5):
    squares.append(n * n)
print(squares)   # [0, 1, 4, 9, 16]
```

A **list comprehension** does the same thing in one line:

```python
squares = [n * n for n in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```

Read it as: "for each `n` in `range(5)`, compute `n * n`, and collect the results
into a list."

### Filtering with a condition

Add an `if` at the end to only include some items:

```python
evens = [n for n in range(10) if n % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]
```

This is equivalent to:

```python
evens = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
```

### Dict comprehensions

Same idea, using `{key: value for ...}`:

```python
squares_by_number = {n: n * n for n in range(5)}
print(squares_by_number)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Set comprehensions

Same idea again, using `{...}` without the colon:

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "yo"]}
print(unique_lengths)   # {2, 5, 3} -- order not guaranteed, see Day 14
```

### When to use one (and when not to)

Comprehensions are great for simple "transform and/or filter" operations. Once
the logic gets complicated — multiple conditions, nested loops that are hard to
read, side effects like printing inside the loop — a regular `for` loop is
clearer. Don't force a comprehension where it hurts readability; being *able* to
write something in one line doesn't mean you should.

## Worked example

See [`examples/comprehensions.py`](examples/comprehensions.py). Run it with:

```bash
python day-15/examples/comprehensions.py
```

## Exercises

1. **`exercise_1_squares.py`** — build a list of squares of numbers 1 through 10
   using a list comprehension.
2. **`exercise_2_filter.py`** — given a list of words, build a list containing
   only the words longer than 4 characters.
3. **`exercise_3_dict_comp.py`** — given a list of words, build a dict mapping
   each word to its length.
4. **`exercise_4_set_comp.py`** — given a list of numbers, build a set of only
   the even ones.

## Common Gotchas

- **Nesting comprehensions too deeply.** `[x for row in matrix for x in row]`
  (flattening a nested list) is about the limit of what stays readable — beyond
  that, use a regular loop.
- **Forgetting comprehensions still build the whole collection.** For very large
  ranges, this uses more memory than a lazy approach — you'll meet generator
  expressions (which avoid this) on [Day 32](../day-32/README.md).
- **Using a comprehension purely for side effects.** `[print(x) for x in items]`
  works, but it's confusing — it builds a throwaway list of `None`s just to run
  `print`. Use a plain `for` loop when you're not collecting a result.
- **Set/dict comprehension order.** Since sets and dicts have their own
  iteration-order rules (Days 13-14), don't assume a comprehension's output
  order matches the input order for sets.
