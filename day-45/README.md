# Day 45: Intro to pandas I (reading CSV, exploring data)

**Module:** 5 — Real-World Libraries

## What you'll learn

- What pandas is for, and how a `DataFrame` relates to what you already know
- Reading a CSV with `read_csv()`
- Exploring a `DataFrame`: `head()`, `info()`, `describe()`
- Selecting columns and rows

## Explanation

### What pandas is

You've parsed CSV files by hand since [Day 19](../day-19/README.md), one
line at a time with `.split(",")`. **pandas** is a third-party library
(`pip install pandas`, already in this repo's `requirements.txt`) built on
top of numpy ([Day 44](../day-44/README.md)) that does this — and everything
after it — properly: reading, exploring, filtering, and aggregating tabular
data, without you writing that manual parsing loop again.

Convention: `import pandas as pd`.

### The `DataFrame`

A **`DataFrame`** is pandas's core structure — a table, with labeled rows and
columns, conceptually similar to a spreadsheet or a list of dicts you've been
building since Day 19, but with far more built-in tooling.

### Reading a CSV

```python
import pandas as pd

sales = pd.read_csv("day-45/sales.csv")
print(sales)
```

`read_csv()` reads the file, treats the first row as column headers by
default, and infers each column's type (numbers stay numbers, text stays
text) automatically — this alone replaces all of Day 19's manual
`split(",")` and `int(...)` conversions.

### Exploring a `DataFrame`

```python
sales = pd.read_csv("day-45/sales.csv")

print(sales.head())      # first 5 rows -- a quick look without printing everything
print(sales.head(3))      # first 3 rows
print(sales.shape)         # (rows, columns) -- like numpy's .shape
print(sales.columns)       # the column names
sales.info()                 # column names, types, non-null counts -- a structural overview
print(sales.describe())    # count, mean, std, min, max, quartiles for numeric columns
```

`info()` prints directly rather than returning something to `print()`
yourself — that's the one exception among these.

### Selecting columns

```python
print(sales["product"])          # one column, as a "Series" (pandas's 1D structure)
print(sales[["product", "price"]])  # multiple columns, as a DataFrame -- note the double [[ ]]
```

### Selecting rows

```python
print(sales.iloc[0])       # the first row, by position (like list indexing)
print(sales.iloc[0:3])      # the first three rows, by position
print(sales.loc[0])          # the row labeled 0 (usually the same as iloc[0] with default indexing)
```

`iloc` = "integer location" (position-based, like a list); `loc` = "label
location" (based on the actual index labels, which happen to be `0, 1, 2,
...` by default but don't have to be).

## Worked example

See [`examples/pandas_basics.py`](examples/pandas_basics.py), which explores
[`sales.csv`](sales.csv). Run it with:

```bash
python day-45/examples/pandas_basics.py
```

## Exercises

All exercises read [`day-45/sales.csv`](sales.csv).

1. **`exercise_1_read_explore.py`** — read the CSV, print `.head(3)`,
   `.shape`, and `.columns`.
2. **`exercise_2_describe.py`** — print `.describe()` for the numeric
   columns.
3. **`exercise_3_select_columns.py`** — print just the `product` and
   `quantity` columns together.
4. **`exercise_4_select_rows.py`** — print the first 5 rows using `.iloc`.

## Common Gotchas

- **Single `[ ]` vs. double `[[ ]]` for column selection.** `sales["price"]`
  gives a `Series` (one column); `sales[["price"]]` (double brackets) gives a
  one-column `DataFrame` — they look almost identical when printed but behave
  differently for later operations.
- **Forgetting the file path is relative to the repo root.** Consistent with
  every day using files in this course, `"day-45/sales.csv"` assumes you're
  running from the repository root.
- **Confusing `.loc` and `.iloc`.** `.iloc` always means position (0, 1, 2,
  ...), `.loc` means the actual index label — with the default numeric index
  they often look the same, but they stop matching the moment you filter,
  sort, or set a custom index (Day 46).
- **Calling `.describe()` and expecting text columns included.** By default,
  `.describe()` only summarizes numeric columns — text columns like
  `product` are silently skipped unless you ask for them explicitly.
