# Day 11: Lists

**Module:** 2 — Data Structures & Files

## What you'll learn

- Creating and indexing lists
- Mutating a list: append, insert, remove, pop
- Slicing lists (same rules as string slicing from Day 10)
- Looping over a list
- Common list operations: `len()`, `in`, `sort()`, `sorted()`

## Explanation

### Creating a list

A **list** is an ordered, mutable (changeable) collection of values:

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]   # a list can hold mixed types, though usually shouldn't
empty = []
```

Indexing and slicing work exactly like they did for strings on
[Day 10](../day-10/README.md):

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # "apple"
print(fruits[-1])    # "cherry"
print(fruits[0:2])   # ["apple", "banana"]
```

### Lists are mutable

Unlike strings, you *can* change a list in place:

```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"
print(fruits)   # ["avocado", "banana", "cherry"]
```

### Adding and removing items

```python
fruits = ["apple", "banana"]
fruits.append("cherry")        # add to the end -> ["apple", "banana", "cherry"]
fruits.insert(1, "apricot")    # insert at index 1 -> ["apple", "apricot", "banana", "cherry"]
fruits.remove("banana")        # remove the first matching value
last = fruits.pop()             # removes and returns the last item
first = fruits.pop(0)           # removes and returns the item at index 0
```

`remove(value)` raises `ValueError` if the value isn't found. `pop(index)` raises
`IndexError` if the index is out of range.

### Looping over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)   # enumerate() gives you both the position and the value
```

### Checking membership and length

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print(len(fruits))          # 3
```

### Sorting

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()               # sorts in place, returns None
print(numbers)                # [1, 1, 3, 4, 5]

original = [3, 1, 4, 1, 5]
new_list = sorted(original)   # returns a new sorted list, leaves original unchanged
print(original)                # [3, 1, 4, 1, 5]
print(new_list)                 # [1, 1, 3, 4, 5]
```

## Worked example

See [`examples/lists.py`](examples/lists.py). Run it with:

```bash
python day-11/examples/lists.py
```

## Exercises

1. **`exercise_1_build_list.py`** — build a list of 5 numbers, print it, then
   print its length.
2. **`exercise_2_add_remove.py`** — start with a list of 3 items, `append` one,
   `insert` one at index 0, then `remove` one, printing the list after each step.
3. **`exercise_3_loop_enumerate.py`** — given a list of names, print each one
   prefixed by its position, e.g. `"0: Ada"`, using `enumerate()`.
4. **`exercise_4_sort.py`** — given an unsorted list of numbers, print a sorted
   copy using `sorted()` without changing the original, then print the original
   to prove it's unchanged.

## Common Gotchas

- **Confusing `sort()` and `sorted()`.** `list.sort()` mutates in place and
  returns `None` — `numbers = numbers.sort()` throws away your list and replaces
  it with `None`. `sorted(list)` returns a new list and leaves the original alone.
- **`remove()` removes by value, `pop()` removes by index.** Mixing them up is a
  very common mistake — `fruits.remove(0)` tries to remove the *value* `0`, not
  the item at index `0`.
- **Index out of range.** `fruits[10]` on a 3-item list raises `IndexError`,
  exactly like with strings.
- **Aliasing.** `a = [1, 2, 3]` then `b = a` does **not** copy the list — `b` and
  `a` point to the *same* list, so changing one changes the other. Use
  `b = a.copy()` (or `a[:]`) to get an independent copy.
