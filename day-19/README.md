# Day 19: Combining data structures & files

**Module:** 2 — Data Structures & Files

## What you'll learn

- Turning file lines into structured data (lists of dicts)
- Aggregating data you've loaded (totals, averages, filtering)
- Writing computed results back out to a file
- How this pattern is the backbone of tomorrow's mini-project

## Explanation

Today doesn't introduce new syntax — it's a practice day that combines
everything from this module so far: lists (Day 11), dicts (Day 13),
comprehensions (Day 15), string methods (Day 16), and file handling (Days
17-18).

### The pattern: file → structured data → answer → file

A huge amount of real-world scripting follows this exact shape:

1. **Read** raw text from a file.
2. **Parse** each line into something structured (usually a dict, or a list of
   dicts for multiple records).
3. **Compute** something from that structured data.
4. **Write** the result somewhere — a file, the screen, or (starting Day 41)
   over the network.

### Parsing a simple CSV by hand

This course hasn't covered the `csv` module (or `pandas`, coming Day 45) yet —
those exist and are the *right* tool for real work, but for now, plain string
methods are enough to parse a simple comma-separated file:

```python
with open("day-19/students.csv", "r") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")     # ["name", "score"]
students = []
for line in lines[1:]:                    # skip the header row
    name, score = line.strip().split(",")
    students.append({"name": name, "score": int(score)})

print(students)
# [{"name": "Ada", "score": 92}, {"name": "Grace", "score": 85}, ...]
```

### Aggregating

```python
scores = [student["score"] for student in students]
average = sum(scores) / len(scores)
top_student = max(students, key=lambda s: s["score"])
```

(`key=lambda s: s["score"]` tells `max()` to compare by score rather than by the
whole dict — you'll properly meet `lambda` on [Day 34](../day-34/README.md);
for now, just copy this pattern when you need it.)

### Writing the result

```python
with open("day-19/summary.txt", "w") as file:
    file.write(f"Average score: {average:.1f}\n")
    file.write(f"Top student: {top_student['name']} ({top_student['score']})\n")
```

## Worked example

See [`examples/analyze_students.py`](examples/analyze_students.py), which reads
[`students.csv`](students.csv) and writes a summary. Run it with:

```bash
python day-19/examples/analyze_students.py
```

## Exercises

All exercises read from [`day-19/students.csv`](students.csv).

1. **`exercise_1_parse.py`** — parse the CSV into a list of dicts and print it.
2. **`exercise_2_average.py`** — compute and print the average score.
3. **`exercise_3_filter_passing.py`** — build and print a list of names of
   students who scored 80 or above, using a list comprehension.
4. **`exercise_4_write_report.py`** — write a report to
   `day-19/exercises_report.txt` listing each student and whether they passed
   (score >= 80) or failed.

## Common Gotchas

- **Forgetting to skip the header row.** `lines[1:]` skips index 0 (the header);
  forgetting the slice tries to `int()` the word `"score"` and crashes with
  `ValueError`.
- **Not stripping the newline before splitting.** `"Ada,92\n".split(",")` gives
  `["Ada", "92\n"]` — the trailing `\n` sneaks into the last field. Always
  `.strip()` the whole line first.
- **Forgetting to convert numeric fields.** Everything read from a file is a
  `str` — `score` needs `int(score)` before you can do math with it, exactly
  like `input()` on Day 5.
- **Building the file path relative to the wrong location.** Consistent with
  every day in this module, paths like `"day-19/students.csv"` assume you're
  running from the repository root.
