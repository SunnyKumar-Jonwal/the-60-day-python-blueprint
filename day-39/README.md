# Day 39: Regex

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- What a regular expression is, and when it beats plain string methods
- `re.search()`, `re.match()`, `re.findall()`, `re.sub()`
- Core pattern syntax: character classes, quantifiers, groups
- Raw strings and why regex patterns should almost always use them

## Explanation

### Why regex, when you already have string methods?

Day 16's `.find()`, `.startswith()`, `.replace()` handle exact, literal text.
A **regular expression** (regex) describes a *pattern* of text instead — "a
digit followed by three letters," "anything that looks like an email
address." Python's `re` module (standard library, `import re`) implements
this.

```python
import re

text = "My phone number is 555-1234"
match = re.search(r"\d{3}-\d{4}", text)
print(match.group())   # "555-1234"
```

### Raw strings

Regex patterns use `\` heavily (`\d`, `\w`, `\s`, ...), and Python strings
also treat `\` as an escape character (Day 10) — without care, `"\d"` isn't
even a valid escape sequence to Python. A **raw string**, prefixed `r"..."`,
tells Python "don't process backslashes as escapes, pass them through
literally." Always write regex patterns as raw strings:

```python
re.search(r"\d{3}", text)    # correct -- \d reaches re.search literally
re.search("\d{3}", text)     # works by luck for \d, but is bad practice and
                                # breaks outright for other sequences like \b
```

### Core pattern syntax

| Pattern | Matches |
|---|---|
| `\d` | any digit (0-9) |
| `\w` | any "word" character (letters, digits, underscore) |
| `\s` | any whitespace (space, tab, newline) |
| `.` | any single character (except newline) |
| `^` | start of the string |
| `$` | end of the string |
| `*` | 0 or more of the previous item |
| `+` | 1 or more of the previous item |
| `?` | 0 or 1 of the previous item |
| `{n}` | exactly `n` of the previous item |
| `{n,m}` | between `n` and `m` of the previous item |
| `[abc]` | any one of `a`, `b`, or `c` |
| `(...)` | a group — captures that part of the match separately |

### `re.search()` vs `re.match()`

```python
re.match(r"\d+", "abc123")    # None -- match() only checks the START of the string
re.search(r"\d+", "abc123")   # matches "123" -- search() looks anywhere in the string
```

`re.search()` is what you want almost all the time; `re.match()` is a common
source of confusion for exactly this reason.

### `re.findall()` — every match

```python
text = "Call 555-1234 or 555-5678"
numbers = re.findall(r"\d{3}-\d{4}", text)
print(numbers)   # ["555-1234", "555-5678"]
```

### `re.sub()` — find and replace by pattern

```python
text = "Contact: 555-1234"
masked = re.sub(r"\d{3}-\d{4}", "[REDACTED]", text)
print(masked)   # "Contact: [REDACTED]"
```

### Groups — capturing parts of a match

```python
match = re.search(r"(\d{3})-(\d{4})", "555-1234")
print(match.group())    # "555-1234" -- the whole match
print(match.group(1))   # "555"       -- the first parenthesized group
print(match.group(2))   # "1234"      -- the second parenthesized group
```

## Worked example

See [`examples/regex_basics.py`](examples/regex_basics.py). Run it with:

```bash
python day-39/examples/regex_basics.py
```

## Exercises

1. **`exercise_1_search.py`** — use `re.search()` to find a 5-digit ZIP code
   in a sentence, and print the match.
2. **`exercise_2_findall.py`** — use `re.findall()` to extract every email
   address (simplified pattern: `word characters, @, word characters, ., word
   characters`) from a block of text with several emails in it.
3. **`exercise_3_sub.py`** — use `re.sub()` to replace every sequence of
   multiple spaces in a string with a single space.
4. **`exercise_4_groups.py`** — use `re.search()` with groups to split a date
   string like `"2024-08-25"` into year, month, and day, printing each.

## Common Gotchas

- **Forgetting the raw string prefix.** `"\d"` and `r"\d"` often behave the
  same by coincidence, but relying on that is fragile — always use `r"..."`
  for regex patterns as a habit, no exceptions.
- **`re.match()` when you meant `re.search()`.** `match()` silently returns
  `None` for anything not at the very start of the string — a very common
  source of "why doesn't my regex match" confusion.
- **Forgetting `re.search()`/`re.match()` return `None` on no match.**
  Calling `.group()` on `None` raises `AttributeError: 'NoneType' object has
  no attribute 'group'` — always check `if match:` before using the result.
- **Reaching for regex when a plain string method would do.** Checking
  whether text starts with a fixed prefix is `text.startswith(...)`
  (Day 16), not a regex — regex earns its complexity for actual *patterns*,
  not exact literal text.
