# Day 43: `datetime`

**Module:** 5 — Real-World Libraries

## What you'll learn

- `datetime.now()` and building specific dates/times
- Formatting dates as text with `strftime`
- Parsing text into dates with `strptime`
- Date arithmetic with `timedelta`

## Explanation

### The `datetime` module

`datetime` is part of the standard library — `import datetime`, or more
commonly, import the specific class you need directly:

```python
from datetime import datetime

now = datetime.now()
print(now)   # 2024-08-25 14:30:05.123456 (whatever the actual moment is)
```

`datetime` (the module) contains a class also called `datetime` — a bit
confusing at first, but `from datetime import datetime` is the standard way
people write it.

### Building a specific date/time

```python
from datetime import datetime

birthday = datetime(2024, 8, 25)               # year, month, day
meeting = datetime(2024, 8, 25, 14, 30)         # + hour, minute
print(birthday.year, birthday.month, birthday.day)   # 2024 8 25
```

### Formatting: `strftime` (datetime → string)

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))          # "2024-08-25"
print(now.strftime("%B %d, %Y"))          # "August 25, 2024"
print(now.strftime("%H:%M:%S"))            # "14:30:05"
```

Common format codes: `%Y` (4-digit year), `%m` (month number), `%d` (day),
`%B` (full month name), `%H`/`%M`/`%S` (hour/minute/second).

### Parsing: `strptime` (string → datetime)

```python
from datetime import datetime

text = "2024-08-25"
parsed = datetime.strptime(text, "%Y-%m-%d")
print(parsed)          # 2024-08-25 00:00:00
print(parsed.year)     # 2024
```

The format string passed to `strptime` must match the input text's layout
exactly — a mismatch raises `ValueError`.

### Date arithmetic: `timedelta`

```python
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
two_hours_ago = today - timedelta(hours=2)

difference = tomorrow - today
print(difference)           # 1 day, 0:00:00
print(difference.days)      # 1
```

Subtracting two `datetime` objects gives you a `timedelta` representing the
gap between them — useful for "how many days until this date" style
calculations.

### Comparing dates

Since `datetime` objects support the usual comparison operators (Day 4),
comparing two of them works directly:

```python
from datetime import datetime

deadline = datetime(2024, 12, 31)
today = datetime.now()
print(today < deadline)   # True, until the year rolls over
```

## Worked example

See [`examples/datetime_basics.py`](examples/datetime_basics.py). Run it
with:

```bash
python day-43/examples/datetime_basics.py
```

## Exercises

1. **`exercise_1_now_format.py`** — get the current date/time and print it
   formatted as `"YYYY-MM-DD"`.
2. **`exercise_2_parse.py`** — parse the string `"2024-12-25"` into a
   `datetime`, and print its `.year`, `.month`, `.day` separately.
3. **`exercise_3_timedelta.py`** — given a specific date, compute and print
   the date 30 days later using `timedelta`.
4. **`exercise_4_days_until.py`** — given a target date in the future,
   compute and print how many days remain until it, from today.

## Common Gotchas

- **Format code mismatches in `strptime`.** `strptime("2024-08-25", "%m/%d/%Y")`
  raises `ValueError: time data '2024-08-25' does not match format
  '%m/%d/%Y'` — the format string must describe the *actual* layout of the
  input text.
- **Confusing `strftime` and `strptime`.** "**f**time" formats a datetime
  into a string; "**p**time" parses a string into a datetime — the mnemonic
  is `strftime` = "string **f**rom time," `strptime` = "string **p**arse
  time."
- **Adding a plain number of days instead of a `timedelta`.** `today + 5`
  raises `TypeError` — date arithmetic requires `timedelta(days=5)`, not a
  bare integer.
- **Time zones.** `datetime.now()` gives your local naive time with no time
  zone attached — comparing naive datetimes across different time zones (or
  mixing naive and timezone-aware datetimes) gives wrong or error-raising
  results. This course keeps things simple with naive local time throughout.
