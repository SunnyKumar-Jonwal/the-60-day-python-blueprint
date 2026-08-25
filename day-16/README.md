# Day 16: String methods in depth

**Module:** 2 — Data Structures & Files

## What you'll learn

- Case methods: `upper()`, `lower()`, `title()`, `capitalize()`
- Trimming whitespace: `strip()`, `lstrip()`, `rstrip()`
- Searching: `find()`, `in`, `startswith()`, `endswith()`
- Splitting and joining: `split()`, `join()`
- Replacing: `replace()`

## Explanation

Strings have many built-in methods. You call them with `.method_name(...)` on a
string value. None of them modify the original string in place (remember, strings
are immutable from [Day 10](../day-10/README.md)) — they all **return a new
string**.

### Case conversion

```python
text = "Hello World"
print(text.upper())        # "HELLO WORLD"
print(text.lower())        # "hello world"
print(text.title())        # "Hello World"  -- capitalizes each word
print("hello".capitalize())# "Hello"        -- capitalizes just the first letter
```

### Trimming whitespace

Very useful when cleaning up user input (e.g. from `input()`, Day 5) or lines
read from a file (Day 17):

```python
text = "   hello   "
print(text.strip())    # "hello"    -- removes leading and trailing whitespace
print(text.lstrip())   # "hello   " -- left only
print(text.rstrip())   # "   hello" -- right only
```

### Searching

```python
text = "Learn Python in 60 Days"
print(text.find("Python"))       # 6 -- index where it starts, or -1 if not found
print("Python" in text)           # True -- usually clearer than checking find() != -1
print(text.startswith("Learn"))   # True
print(text.endswith("Days"))      # True
```

### Splitting and joining

```python
csv_line = "Ada,30,London"
parts = csv_line.split(",")
print(parts)   # ["Ada", "30", "London"]

words = ["Learn", "Python", "fast"]
sentence = " ".join(words)
print(sentence)   # "Learn Python fast"
```

`split()` with no argument splits on any whitespace and collapses repeats:

```python
"  a   b  c ".split()   # ["a", "b", "c"]
```

`join()` is called *on the separator*, with the list as the argument — this trips
up almost everyone the first time. Think of it as: `"glue".join(pieces)`.

### Replacing

```python
text = "I like cats"
print(text.replace("cats", "dogs"))   # "I like dogs"
```

## Worked example

See [`examples/string_methods.py`](examples/string_methods.py). Run it with:

```bash
python day-16/examples/string_methods.py
```

## Exercises

1. **`exercise_1_case.py`** — given a messy-cased string, print an uppercase,
   lowercase, and title-case version.
2. **`exercise_2_clean_input.py`** — given a string with extra whitespace around
   it, print the cleaned (stripped) version.
3. **`exercise_3_split_join.py`** — given a comma-separated string of names,
   split it into a list, then join it back together with `" | "` as the
   separator.
4. **`exercise_4_search_replace.py`** — given a sentence, check whether it
   contains a specific word (with `in`), then print a version with that word
   replaced by another.

## Common Gotchas

- **String methods don't mutate.** `text.strip()` doesn't change `text` — you
  must assign the result: `text = text.strip()`.
- **`join()` is called on the separator, not the list.** `words.join(" ")` is
  backwards and raises `AttributeError` (lists don't have `.join()`) — it's
  `" ".join(words)`.
- **`split()` vs `split(",")`.** With no argument, `split()` handles any amount
  of whitespace intelligently; `split(",")` splits on exactly that character and
  won't collapse repeated commas — `"a,,b".split(",")` gives `["a", "", "b"]`.
- **`find()` returns `-1`, not `None`, when nothing is found.** `if text.find("x"):`
  is a bug — `-1` is truthy! Compare explicitly: `if text.find("x") != -1:`, or
  better, just use `if "x" in text:`.
