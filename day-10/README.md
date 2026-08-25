# Day 10: String basics

**Module:** 1 — Fundamentals

## What you'll learn

- Creating strings and escape characters
- Concatenation and repetition
- Indexing and slicing
- `len()`

## Explanation

### Creating strings

Strings can use single or double quotes — pick one and be consistent; the only
time it matters is when your text itself contains a quote character:

```python
a = "hello"
b = 'hello'
c = "it's a nice day"      # use double quotes when the text has a '
d = 'she said "hi"'        # use single quotes when the text has a "
```

For text spanning multiple lines, use triple quotes:

```python
message = """Line one
Line two"""
```

### Escape characters

A backslash `\` starts an **escape sequence** — a way to include characters that
would otherwise be hard to type or would end the string early:

```python
print("Line one\nLine two")   # \n = newline
print("Tab\tstop")            # \t = tab
print("She said \"hi\"")       # \" = a literal double quote inside a double-quoted string
print("C:\\Users")             # \\ = a literal backslash
```

### Concatenation and repetition

```python
first = "Py"
second = "thon"
print(first + second)   # "Python"
print("ab" * 3)          # "ababab"
```

(You already met f-strings on [Day 5](../day-05/README.md), which is usually the
better way to combine strings with variables — plain `+` concatenation is best for
combining literal string fragments.)

### Indexing

Each character in a string has a position, starting at `0`. Negative indices count
from the end:

```python
word = "Python"
print(word[0])    # "P"  -- first character
print(word[5])    # "n"  -- last character
print(word[-1])   # "n"  -- also the last character
print(word[-6])   # "P"  -- also the first character
```

### Slicing

`word[start:stop]` gives you a substring from `start` up to (but not including)
`stop`:

```python
word = "Python"
print(word[0:2])   # "Py"
print(word[2:])    # "thon"  -- omit stop to go to the end
print(word[:2])    # "Py"    -- omit start to go from the beginning
print(word[-3:])   # "hon"   -- last three characters
```

Strings are **immutable** — you can't change a character in place
(`word[0] = "J"` raises a `TypeError`). To "change" a string, you build a new one.

Slicing also accepts a third number, the **step** — `word[start:stop:step]` —
same idea as `range()`'s step from [Day 7](../day-07/README.md). A step of `-1`
walks backwards, which gives a quick way to reverse a string:

```python
word = "Python"
print(word[::-1])   # "nohtyP" -- no start/stop given, step -1 walks the whole string backwards
```

### `len()`

`len(...)` gives you the number of characters in a string:

```python
print(len("Python"))   # 6
```

## Worked example

See [`examples/strings.py`](examples/strings.py). Run it with:

```bash
python day-10/examples/strings.py
```

## Exercises

1. **`exercise_1_escapes.py`** — print a sentence containing a tab, a newline, and
   an escaped double quote.
2. **`exercise_2_slicing.py`** — given the string `"Learn Python in 60 Days"`,
   print just `"Python"` using slicing.
3. **`exercise_3_reverse.py`** — given a word, print it reversed using slicing
   with a negative step (`word[::-1]`).
4. **`exercise_4_initials.py`** — given a full name, print the first letter of
   each of the first and last name using indexing (assume exactly one space
   between them).

## Common Gotchas

- **Off-by-one errors in slicing.** `word[0:2]` gives 2 characters (`0` and `1`),
  not 3 — the `stop` index is exclusive, same as `range()` from Day 7.
- **Trying to modify a string in place.** `word[0] = "J"` raises `TypeError:
  'str' object does not support item assignment` — strings are immutable.
- **Index out of range.** `word[10]` on a 6-character string raises
  `IndexError` — always make sure your index is less than `len(word)`.
- **Confusing `str(x)` with an f-string.** `str(42)` converts a value to a string;
  an f-string like `f"{42}"` embeds a value inside a larger string — different
  tools for different jobs, though both end up producing a `str`.
