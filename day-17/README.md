# Day 17: File handling I (open / read / write)

**Module:** 2 — Data Structures & Files

## What you'll learn

- Opening a file with `open()` and file modes (`"r"`, `"w"`, `"a"`)
- Reading a whole file, line by line, or as a list of lines
- Writing and appending text
- Why you must `close()` a file (and the problem that creates)

## Explanation

### File paths in this lesson

Every command below assumes you're running from the **repository root** (same as
every other day so far). This day includes a sample data file at
[`day-17/sample.txt`](sample.txt) that the examples and exercises read from —
scripts reference it as the path `"day-17/sample.txt"`.

### Opening a file

`open(path, mode)` returns a **file object** you can read from or write to:

```python
file = open("day-17/sample.txt", "r")   # "r" = read (this is also the default mode)
```

Common modes:

| Mode | Meaning |
|---|---|
| `"r"` | Read (file must already exist) |
| `"w"` | Write — **creates the file if missing, and erases it if it already exists** |
| `"a"` | Append — creates the file if missing, adds to the end if it exists |

### Reading

```python
file = open("day-17/sample.txt", "r")
contents = file.read()      # the whole file as one string
file.close()
print(contents)
```

Other ways to read:

```python
file = open("day-17/sample.txt", "r")
first_line = file.readline()   # just the next line, including its newline character
file.close()

file = open("day-17/sample.txt", "r")
lines = file.readlines()        # a list of every line, each still ending in "\n"
file.close()

file = open("day-17/sample.txt", "r")
for line in file:               # a file object is directly loop-able, line by line
    print(line.strip())          # .strip() removes the trailing "\n" (Day 16)
file.close()
```

### Writing

```python
file = open("day-17/examples_output.txt", "w")
file.write("First line\n")     # write() does NOT add a newline for you -- add "\n" yourself
file.write("Second line\n")
file.close()
```

`"w"` mode **erases the file's previous contents** the moment you open it, even
if you never call `write()`. Use `"a"` (append) if you want to add to an existing
file without losing what's there:

```python
file = open("day-17/examples_output.txt", "a")
file.write("Third line, appended\n")
file.close()
```

### Why `close()` matters

Until you `close()` a file, your writes might not actually be saved to disk yet
(they can sit in a memory buffer), and the file stays "locked" by your program.
Forgetting to close files is a common source of bugs — data that looks written
but isn't, or files other programs can't open because yours still has them held.
[Day 18](../day-18/README.md) introduces a much safer pattern that closes files
for you automatically, and is what you should actually use in real code from
tomorrow onward. Today, close manually so you understand what's happening
underneath.

## Worked example

See [`examples/file_basics.py`](examples/file_basics.py). Run it with:

```bash
python day-17/examples/file_basics.py
```

## Exercises

1. **`exercise_1_read_all.py`** — open `day-17/sample.txt` and print its entire
   contents.
2. **`exercise_2_read_lines.py`** — open `day-17/sample.txt` and print each line
   with its line number, e.g. `"1: apple"` (strip the newline first).
3. **`exercise_3_write.py`** — write three lines of your choice to
   `day-17/exercises_output.txt` using `"w"` mode, then read it back and print it.
4. **`exercise_4_append.py`** — append one more line to
   `day-17/exercises_output.txt` using `"a"` mode, then read and print the whole
   file to confirm all four lines are present.

## Common Gotchas

- **`"w"` silently erases existing content.** Opening a file you meant to append
  to with `"w"` instead of `"a"` destroys everything that was there — a very easy
  and very costly mistake.
- **Forgetting `close()`.** Especially after writing — your data may not actually
  be on disk, and re-running your script before closing can behave unexpectedly.
- **Reading a file that doesn't exist.** `open("missing.txt", "r")` raises
  `FileNotFoundError` — you'll learn to handle this gracefully with exceptions on
  [Day 28](../day-28/README.md).
- **`readlines()` / looping over a file keeps the trailing `\n`.** Forgetting to
  `.strip()` each line leaves a stray blank line's worth of whitespace in your
  output.
