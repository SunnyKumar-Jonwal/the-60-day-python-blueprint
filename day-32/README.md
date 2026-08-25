# Day 32: Generators & `yield`

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- Generator functions and `yield`
- How a generator automatically implements Day 31's iterator protocol
- Generator expressions (like a comprehension, but lazy)
- Why generators save memory over building a full list

## Explanation

### The problem with yesterday's iterator class

`CountUp` from [Day 31](../day-31/README.md) worked, but took nine lines to
express "count from 1 to a limit." A **generator function** does the same
thing in far less code, using `yield` instead of `return`:

```python
def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1


for number in count_up(3):
    print(number)   # 1, 2, 3
```

### How `yield` works

Calling `count_up(3)` doesn't run the function body at all yet — it returns a
**generator object**, which automatically satisfies the full iterator
protocol from Day 31 (`__iter__` and `__next__`) for you, with zero
boilerplate.

Each time `next()` is called on it (which `for` does automatically), the
function runs **until it hits a `yield`**, hands back that value, and then
**pauses exactly where it left off** — remembering all its local variables —
until `next()` is called again:

```python
gen = count_up(3)
print(next(gen))   # 1 -- runs to the first yield, pauses
print(next(gen))   # 2 -- resumes right after that yield, runs to the next one
print(next(gen))   # 3
print(next(gen))   # raises StopIteration -- the function reached its end
```

This "pause and resume, remembering where you were" behavior is exactly what
made `CountUp`'s manual `self.current` tracking necessary — a generator gets
that for free just by using local variables normally.

### Generator expressions

You already know comprehensions from [Day 15](../day-15/README.md):

```python
squares_list = [n * n for n in range(1000000)]   # builds ALL million values right now
```

A **generator expression** looks almost identical, but with `( )` instead of
`[ ]`, and produces values **lazily** — one at a time, only when asked:

```python
squares_gen = (n * n for n in range(1000000))   # builds nothing yet
print(next(squares_gen))   # 0 -- computed only now
print(next(squares_gen))   # 1 -- computed only now
```

### Why this matters: memory

```python
def read_large_file_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line.strip()
```

This never loads the whole file into memory at once — it hands back one
processed line at a time, which matters enormously once "the whole file"
means gigabytes. A list comprehension building `[line.strip() for line in
file]` would need to hold every line in memory simultaneously; a generator
never does.

## Worked example

See [`examples/generators.py`](examples/generators.py). Run it with:

```bash
python day-32/examples/generators.py
```

## Exercises

1. **`exercise_1_basic_generator.py`** — write a generator function
   `countdown(start)` that yields from `start` down to `1`.
2. **`exercise_2_generator_expression.py`** — build a generator expression for
   the squares of numbers 1 through 5, and print each value using a `for`
   loop (not `list(...)`, to actually exercise laziness).
3. **`exercise_3_infinite_with_limit.py`** — write a generator function
   `even_numbers()` that yields even numbers forever (`while True:`), then
   use it with `next()` four times to get the first four even numbers without
   ever finishing the loop.
4. **`exercise_4_file_generator.py`** — write a generator function
   `read_lines(path)` that yields stripped lines one at a time from
   `"day-17/sample.txt"` (reusing Day 17's sample file), and print each one.

## Common Gotchas

- **Confusing `yield` with `return`.** `return` ends a function and gives back
  one value; `yield` pauses it and can hand back many values over multiple
  calls. A function with any `yield` in it becomes a generator function —
  calling it never runs the body immediately, it just creates the generator.
- **Trying to loop over a generator twice.** Once exhausted (like an
  iterator, Day 31), a generator is spent — calling the generator function
  again creates a fresh one.
- **Using `list(generator)` when you didn't need to.** Converting a generator
  to a list defeats its whole memory advantage — only do this when you
  actually need every value held in memory at once (e.g. to sort it).
- **Writing an infinite generator without a way to stop consuming it.**
  `for x in even_numbers():` around the Exercise 3 generator would run
  forever — infinite generators need to be consumed carefully (`next()` a
  fixed number of times, or a `break` inside the loop).
