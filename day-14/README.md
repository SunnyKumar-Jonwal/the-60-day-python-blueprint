# Day 14: Sets

**Module:** 2 — Data Structures & Files

## What you'll learn

- Creating sets and why duplicates disappear
- Adding and removing items
- Set operations: union, intersection, difference
- When a set is the right tool instead of a list

## Explanation

### Creating a set

A **set** is an unordered collection of unique values — no duplicates, no
guaranteed order, and (like dict keys) items must be immutable:

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)   # {1, 2, 3} -- duplicates are automatically dropped

empty = set()     # NOT {} -- that creates an empty dict, not an empty set
```

### Adding and removing

```python
fruits = {"apple", "banana"}
fruits.add("cherry")          # add one item
fruits.remove("banana")       # removes it; raises KeyError if missing
fruits.discard("kiwi")        # removes it if present; does nothing if missing (no error)
```

### Checking membership

Membership checks (`in`) on a set are typically much faster than on a list,
especially for large collections — this is one of the main reasons to reach for a
set:

```python
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)   # True
```

### Set operations

These mirror the math you may remember from Venn diagrams:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union: all items in either -> {1, 2, 3, 4, 5, 6}
print(a & b)   # intersection: items in both -> {3, 4}
print(a - b)   # difference: in a but not b -> {1, 2}
print(a ^ b)   # symmetric difference: in one but not both -> {1, 2, 5, 6}
```

### When to use a set

- To remove duplicates from a collection: `unique = set(some_list)`.
- To do fast membership testing when you don't care about order.
- To compare two collections for overlap, using the operators above.

Sets are unordered, so never rely on the order you get back when printing or
looping over one.

## Worked example

See [`examples/sets.py`](examples/sets.py). Run it with:

```bash
python day-14/examples/sets.py
```

## Exercises

1. **`exercise_1_dedupe.py`** — given a list with duplicate numbers, use a set to
   print only the unique values.
2. **`exercise_2_add_remove.py`** — start with a set of 3 items, `add` one and
   `discard` one (that doesn't exist, to show it doesn't error), printing after
   each step.
3. **`exercise_3_operations.py`** — given two sets of student names (one per
   class), print students in both classes (intersection) and students in only the
   first class (difference).
4. **`exercise_4_membership.py`** — given a set of allowed usernames, check
   whether two given usernames are in it and print the results.

## Common Gotchas

- **`{}` is an empty dict, not an empty set.** Use `set()` for an empty set.
- **Sets have no order.** Don't index a set (`my_set[0]` fails — `TypeError:
  'set' object is not subscriptable`) and don't expect printed order to be
  stable or match insertion order.
- **`remove()` vs `discard()`.** `remove()` raises `KeyError` if the value isn't
  present; `discard()` silently does nothing — pick based on whether a missing
  value should be an error in your program.
- **Putting a list inside a set.** `{[1, 2]}` raises `TypeError: unhashable type:
  'list'` — set items must be immutable, same rule as dict keys.
