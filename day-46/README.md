# Day 46: Intro to pandas II (filtering & aggregation)

**Module:** 5 — Real-World Libraries

## What you'll learn

- Boolean filtering (selecting rows that match a condition)
- Sorting with `sort_values()`
- Adding computed columns
- `groupby()` for aggregation

## Explanation

This continues directly from [Day 45](../day-45/README.md), using the same
[`sales.csv`](../day-45/sales.csv).

### Boolean filtering

Just like a list comprehension's `if` (Day 15), you can filter a DataFrame
down to only the rows matching a condition:

```python
import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

electronics = sales[sales["category"] == "Electronics"]
print(electronics)

big_orders = sales[sales["quantity"] > 10]
print(big_orders)

both = sales[(sales["category"] == "Electronics") & (sales["quantity"] > 5)]
print(both)
```

`sales["category"] == "Electronics"` produces a `Series` of `True`/`False`
values (one per row); putting that inside `sales[...]` keeps only the rows
where it's `True`. For combining conditions, pandas uses `&` (and) / `|`
(or) instead of Python's `and`/`or` — and each condition needs its own
parentheses, exactly as shown above.

### Sorting

```python
sorted_sales = sales.sort_values("quantity")               # ascending by default
sorted_desc = sales.sort_values("quantity", ascending=False) # descending
print(sorted_desc.head())
```

### Adding a computed column

```python
sales["total"] = sales["quantity"] * sales["price"]
print(sales[["product", "quantity", "price", "total"]].head())
```

Assigning to a column name that doesn't exist yet creates it — computed from
existing columns, vectorized exactly like numpy from Day 44 (pandas columns
are built on numpy arrays underneath).

### `groupby()` — aggregating by category

```python
totals_by_category = sales.groupby("category")["quantity"].sum()
print(totals_by_category)
```

`groupby("category")` splits the DataFrame into one group per unique
category value; `["quantity"].sum()` then sums the `quantity` column
*within each group separately*. This single line replaces what would be a
manual loop-and-dict-accumulate pattern like the one you wrote by hand on
[Day 19](../day-19/README.md).

Other common aggregations work the same way:

```python
sales.groupby("category")["price"].mean()
sales.groupby("category").size()          # count of rows per group
sales.groupby("category")["quantity"].agg(["sum", "mean", "max"])   # multiple at once
```

## Worked example

See [`examples/filter_aggregate.py`](examples/filter_aggregate.py). Run it
with:

```bash
python day-46/examples/filter_aggregate.py
```

## Exercises

All exercises read `day-45/sales.csv` (the same file from Day 45).

1. **`exercise_1_filter.py`** — filter to only rows where `category` is
   `"Accessories"`, and print the result.
2. **`exercise_2_sort.py`** — sort the DataFrame by `price` descending, and
   print the top 5 rows.
3. **`exercise_3_computed_column.py`** — add a `total` column (`quantity *
   price`), and print the rows sorted by `total` descending.
4. **`exercise_4_groupby.py`** — group by `category` and print the total
   `quantity` sold per category, sorted descending.

## Common Gotchas

- **Using `and`/`or` instead of `&`/`|`.** `sales[cond1 and cond2]` raises
  `ValueError: The truth value of a Series is ambiguous` — pandas needs the
  bitwise operators `&`/`|` for combining row-wise conditions, with
  parentheses around each condition.
- **Forgetting parentheses around each condition.** `sales[a == 1 & b == 2]`
  parses incorrectly due to operator precedence — always write
  `sales[(a == 1) & (b == 2)]`.
- **`groupby()` without selecting a column first, then trying `.sum()`
  directly.** `sales.groupby("category").sum()` sums *every* numeric column
  at once, which usually isn't what you want — select the specific column
  first: `sales.groupby("category")["quantity"].sum()`.
- **Forgetting `sort_values()` returns a new DataFrame.** Like
  `sorted()`/`.sort()` on lists (Day 11), `sort_values()` doesn't sort in
  place by default — assign the result to a variable (or pass
  `inplace=True`, which most style guides now discourage in favor of
  reassignment).
