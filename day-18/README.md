# Day 18: File handling II (context managers)

**Module:** 2 — Data Structures & Files

## What you'll learn

- The `with` statement and why it's the right way to open files
- How `with` guarantees a file gets closed, even if an error happens
- Reading and writing multiple files in one `with` block
- Working with file paths using `pathlib` basics

## Explanation

### The problem with manual `close()`

Yesterday you wrote code like this:

```python
file = open("day-17/sample.txt", "r")
contents = file.read()
file.close()
```

If something goes wrong *between* `open()` and `close()` — an error is raised
while processing the file — `close()` never runs, and the file stays open. Over a
long-running program, this kind of leak adds up.

### `with` — the fix

The `with` statement wraps file handling in a way that guarantees `close()` runs
automatically when the block ends, **even if an error happens inside it**:

```python
with open("day-17/sample.txt", "r") as file:
    contents = file.read()
    print(contents)
# file is automatically closed here, as soon as the indented block ends
```

This pattern is called a **context manager**. `with open(...) as file:` opens the
file, hands it to you as `file` for the duration of the indented block, and
closes it the moment you leave that block — no matter how you leave it (normal
completion or an error). From here on in this course, **always use `with` to work
with files** — the manual `open()`/`close()` pattern from Day 17 was only to show
you what's happening underneath.

### Writing with `with`

```python
with open("day-18/examples_output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
# automatically closed and saved here
```

### Working with multiple files at once

You can open more than one file in the same `with` statement:

```python
with open("day-17/sample.txt", "r") as infile, open("day-18/examples_output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

### A note on `pathlib`

Python's `pathlib` module offers a more modern way to represent file paths as
objects instead of plain strings — you'll see it more from Day 37 (modules &
packages) onward. For now, plain string paths like `"day-18/sample.txt"` are
perfectly fine and what this course uses throughout Module 2.

## Worked example

See [`examples/context_managers.py`](examples/context_managers.py). Run it with:

```bash
python day-18/examples/context_managers.py
```

## Exercises

1. **`exercise_1_with_read.py`** — use `with` to open `day-17/sample.txt` and
   print its contents (reusing Day 17's sample file).
2. **`exercise_2_with_write.py`** — use `with` to write three lines to
   `day-18/exercises_output.txt`.
3. **`exercise_3_copy_uppercase.py`** — use `with` to read `day-17/sample.txt`
   and write an uppercase version of every line to
   `day-18/exercises_uppercase.txt`.
4. **`exercise_4_count_lines.py`** — use `with` to open `day-17/sample.txt` and
   print how many lines it has.

## Common Gotchas

- **Forgetting `as file`.** `with open("x.txt"):` opens and closes the file but
  gives you no way to reference it inside the block — you almost always want
  `as some_name`.
- **Using the file object outside the `with` block.** Once you leave the
  indented block, the file is closed — trying to `.read()` again afterward raises
  `ValueError: I/O operation on closed file`.
- **Reverting to manual `open()`/`close()` out of habit.** There's no good reason
  to do this in new code from today onward — `with` is strictly safer and no
  more typing overall.
- **Indentation errors inside `with`.** Everything that needs the open file must
  be indented *inside* the `with` block — code after it (at the original
  indentation level) runs after the file is already closed.
