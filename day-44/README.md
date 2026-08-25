# Day 44: Intro to numpy

**Module:** 5 — Real-World Libraries

## What you'll learn

- What numpy is for, and why it exists alongside plain lists
- Creating arrays with `np.array()`
- Vectorized arithmetic (operating on a whole array at once)
- Indexing, slicing, and shape
- Aggregate functions: `sum`, `mean`, `min`, `max`

## Explanation

### Why numpy?

You've done numeric work with plain lists since Day 11. Lists are flexible,
but slow for heavy numeric work and clumsy for math — you can't write
`my_list * 2` and expect it to double every number (Day 4's `*` on a list
*repeats* it instead). **numpy** ("numeric Python") provides the `ndarray`
type: a fixed-type, fast array built for exactly this kind of work, and is
the foundation that pandas ([Day 45](../day-45/README.md)) is built on top
of.

`numpy` is a third-party package — `pip install numpy` (already added to
this repo's root `requirements.txt`). The near-universal convention is to
import it as `np`:

```python
import numpy as np
```

### Creating arrays

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print(numbers)          # [1 2 3 4 5]
print(type(numbers))    # <class 'numpy.ndarray'>

matrix = np.array([[1, 2, 3], [4, 5, 6]])   # a 2D array, from a list of lists
print(matrix)
```

### Vectorized arithmetic

This is the headline feature — operations apply to every element at once,
with no explicit loop:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 2)          # [ 2  4  6  8 10]
print(numbers + 10)          # [11 12 13 14 15]
print(numbers**2)             # [ 1  4  9 16 25]

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)                  # [11 22 33] -- element-wise addition
```

Compare to the list comprehension you'd need without numpy:
`[n * 2 for n in numbers]` — numpy does this faster and with less code, which
matters once arrays have thousands or millions of elements.

### Indexing, slicing, shape

Indexing and slicing work like lists (Day 11):

```python
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])       # 10
print(numbers[-1])      # 50
print(numbers[1:3])     # [20 30]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)     # (2, 3) -- 2 rows, 3 columns
print(matrix[0, 1])     # 2 -- row 0, column 1
```

### Aggregate functions

```python
numbers = np.array([4, 8, 15, 16, 23, 42])
print(numbers.sum())     # 108
print(numbers.mean())    # 18.0
print(numbers.min())     # 4
print(numbers.max())     # 42
```

These also exist as `np.sum(numbers)`, `np.mean(numbers)`, etc. — both forms
are common; calling them as methods on the array (`numbers.mean()`) is
usually a little more concise.

## Worked example

See [`examples/numpy_basics.py`](examples/numpy_basics.py). Run it with:

```bash
python day-44/examples/numpy_basics.py
```

## Exercises

1. **`exercise_1_create_array.py`** — create a numpy array from a list of 5
   numbers and print it along with its `type()`.
2. **`exercise_2_vectorized_math.py`** — given an array of prices, use
   vectorized arithmetic to apply a 10% discount to all of them at once.
3. **`exercise_3_slicing.py`** — given an array of 10 numbers, print the
   first three, the last three, and every other one.
4. **`exercise_4_aggregates.py`** — given an array of test scores, print the
   sum, mean, min, and max.

## Common Gotchas

- **Expecting `list * 2` and `array * 2` to do the same thing.** On a plain
  list, `*` repeats it (Day 4); on a numpy array, `*` multiplies every
  element — this is one of the most common points of confusion coming from
  plain Python.
- **Mixed types silently upcasting.** `np.array([1, 2, 3.5])` becomes an
  array of floats, not a mix — numpy arrays hold one consistent type,
  unlike Python lists.
- **Shape mismatches in element-wise operations.** Adding two arrays of
  different lengths raises a `ValueError` about broadcasting — unlike lists,
  numpy won't silently truncate or pad.
- **Forgetting `import numpy as np`.** The `np` alias is such a strong
  convention that almost all numpy code (and every numpy tutorial) assumes
  it — using a different alias makes your code harder for others to read.
