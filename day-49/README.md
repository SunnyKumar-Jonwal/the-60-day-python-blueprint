# Day 49: Debugging techniques

**Module:** 5 — Real-World Libraries

## What you'll learn

- Reading a traceback properly, from the bottom up
- Effective `print()` debugging
- `pdb` — Python's built-in interactive debugger, via `breakpoint()`
- A systematic approach to narrowing down a bug

## Explanation

### Reading a traceback

You've seen tracebacks crash programs since Day 3. Here's one, read
properly:

```
Traceback (most recent call last):
  File "script.py", line 9, in <module>
    print(divide(10, 0))
          ^^^^^^^^^^^^^
  File "script.py", line 5, in divide
    return a / b
           ~~^~~
ZeroDivisionError: division by zero
```

Read **bottom to top**:

1. The **last line** is the actual error: `ZeroDivisionError: division by
   zero` — this is almost always the first thing worth reading.
2. Working upward, each `File "...", line N, in <function>` block shows one
   step of the **call stack** — which function called which, in order. The
   *bottom* frame (closest to the error) is where it actually happened; the
   frames above it show how execution got there.
3. In this example: `divide()` (line 5) is where the division happened, and
   it was called from line 9's top-level `print(divide(10, 0))`.

For a longer traceback with many frames, the bottom frame is still where to
start — work upward only if you need to understand *how* the program got
into that state.

### `print()` debugging

The simplest, often fastest technique: print the values you're unsure about,
right before the line that's misbehaving.

```python
def calculate_total(items):
    total = 0
    for item in items:
        print(f"DEBUG: item = {item}, running total = {total}")   # temporary
        total += item["price"] * item["quantity"]
    return total
```

This works well for small, quick investigations — the downside is
remembering to remove the debug prints afterward (or using
[Day 48](../day-48/README.md)'s `logging.debug(...)` instead, which you can
just leave in and turn off).

### `pdb` and `breakpoint()`

For anything more involved than a couple of prints, Python's built-in
debugger lets you **pause execution and inspect the program interactively**:

```python
def calculate_total(items):
    total = 0
    for item in items:
        breakpoint()   # execution pauses here when this line runs
        total += item["price"] * item["quantity"]
    return total
```

When execution hits `breakpoint()`, you get an interactive prompt (`(Pdb)`)
right there in the terminal. Useful commands:

| Command | Does |
|---|---|
| `p variable_name` | print a variable's current value |
| `n` | run the next line (step over) |
| `s` | step into a function call |
| `c` | continue running until the next breakpoint (or the program ends) |
| `l` | show the surrounding source code |
| `q` | quit the debugger |

This course's examples avoid actually calling `breakpoint()` in the scripts
you run non-interactively (it would pause and wait for input) — see
[`examples/pdb_demo.py`](examples/pdb_demo.py) for a commented-out example
you should try running yourself, interactively, in a terminal.

### A systematic approach

When something's broken:

1. **Read the full error message and traceback first.** Don't guess — the
   bottom line usually tells you exactly what went wrong.
2. **Reproduce it reliably.** A bug you can trigger on demand is a bug you
   can actually fix; one you can't reproduce is much harder.
3. **Narrow the location.** Use `print()`/`logging.debug()`/`breakpoint()` to
   find exactly which line and which value is wrong, working inward from
   "somewhere in this function" to "this specific line."
4. **Form a hypothesis, then test it.** "I think `x` is `None` here because
   the earlier `if` should have set it" — check that specific claim, don't
   just poke around randomly.
5. **Fix the cause, not the symptom.** If a value is unexpectedly `None`,
   adding an `if value is not None:` check might silence the crash without
   fixing why it's `None` in the first place.

## Worked example

See [`examples/traceback_reading.py`](examples/traceback_reading.py) (a
script that deliberately crashes, with a walkthrough of its traceback in
comments) and [`examples/pdb_demo.py`](examples/pdb_demo.py) (try this one
yourself interactively). Run the first with:

```bash
python day-49/examples/traceback_reading.py
```

This one is **expected to crash** — that's the point; read the printed
traceback against the comments in the file.

## Exercises

1. **`exercise_1_read_traceback.py`** — run the provided script, read the
   traceback it produces, and write (in a comment at the bottom of the file)
   which line and which variable caused the crash.
2. **`exercise_2_print_debug.py`** — a function has a subtle bug; add
   `print()` statements to narrow down exactly where the wrong value first
   appears, then fix the bug.
3. **`exercise_3_fix_the_bug.py`** — given a small buggy function and a
   description of the expected behavior, find and fix the bug using whichever
   technique you like.
4. **`exercise_4_breakpoint_practice.md`** — a terminal exercise: add a
   `breakpoint()` to a script yourself, run it, and use `p`, `n`, and `c` to
   step through it. Write down what you saw.

## Common Gotchas

- **Reading a traceback top to bottom.** The most useful information — the
  actual exception type and message — is at the very bottom; starting from
  the top usually wastes time.
- **Leaving `breakpoint()` calls in committed code.** They pause execution
  waiting for interactive input — completely broken if hit in an automated
  test or a deployed program. Search for stray `breakpoint()` calls before
  committing.
- **Debugging by randomly changing code until it works.** Without a clear
  hypothesis about *why* something is broken, "fixes" often just move the bug
  somewhere else, or mask it without understanding it.
- **Only checking the "happy path."** Many bugs live in edge cases — empty
  input, zero, negative numbers, the very first or last item — actively
  testing these, not just the typical case, catches bugs before users do.
