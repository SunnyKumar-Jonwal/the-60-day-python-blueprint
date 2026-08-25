# Day 47: Intro to pytest

**Module:** 5 — Real-World Libraries

## What you'll learn

- Why automated tests matter, beyond "does it look right when I run it"
- Writing test functions and `assert`
- Test discovery: naming conventions pytest relies on
- Testing that an exception is raised
- Fixtures, briefly

## Explanation

### Why automated tests?

Every day so far, you've verified code by running it and reading the output.
That works, but doesn't scale — as a project grows, you can't manually
re-check every behavior every time you change something. A **test** is code
that checks other code automatically, so you (or anyone else) can re-run the
whole suite in seconds and immediately know if something broke.

**pytest** (`pip install pytest`, already in this repo's root
`requirements.txt`) is the most widely used Python testing tool.

### Writing a test

A test is just a function whose name starts with `test_`, containing
`assert` statements:

```python
# somewhere_test file
def add(a, b):
    return a + b


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2
```

`assert condition` does nothing if `condition` is `True`; if it's `False`, it
raises `AssertionError` — and pytest reports that as a failed test, showing
you exactly what was expected vs. what actually happened.

### Test discovery

pytest finds tests automatically, based on naming conventions:

- Files: named `test_*.py` or `*_test.py` (this repo's
  [`pyproject.toml`](../../pyproject.toml) configures `test_*.py`).
- Functions: named `test_*`.

Running `pytest` from the repository root finds and runs every matching test
across the whole project — no manual registration needed.

```bash
pytest day-47/solutions/test_calculator.py    # run one file
pytest day-47/                                  # run everything under a folder
pytest -v                                        # verbose: show each test's name and result
```

### Testing that an exception is raised

Use `pytest.raises(...)` as a context manager (Day 18's `with`, applied to
something other than a file) to assert that code raises a specific
exception:

```python
import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)
```

If the code inside the `with` block does **not** raise `ValueError`, this
test fails — `pytest.raises` is checking that the exception genuinely
happens, not just tolerating it if it does.

### Fixtures, briefly

A **fixture** provides reusable setup for multiple tests — for example, some
starting data every test in a file needs:

```python
import pytest


@pytest.fixture
def sample_numbers():
    return [4, 8, 15, 16, 23, 42]


def test_sum(sample_numbers):
    assert sum(sample_numbers) == 108


def test_length(sample_numbers):
    assert len(sample_numbers) == 6
```

Any test function that takes `sample_numbers` as a parameter automatically
gets the fixture's return value — pytest matches them by name. This course
uses fixtures sparingly; simple tests with their own inline setup are often
clearer for small projects.

## Worked example

See [`examples/test_calculator.py`](examples/test_calculator.py). Run it
with:

```bash
pytest day-47/examples/test_calculator.py -v
```

## Exercises

Each exercise file already contains the function(s) to test — write the
`test_*` functions. Filenames start with `test_` so pytest's default
discovery picks them up, same as real test files.

1. **`test_1_is_even.py`** — test an `is_even(n)` function with both an even
   and an odd input.
2. **`test_2_strings.py`** — test a `reverse_string(text)` function with a
   few different strings, including an empty string.
3. **`test_3_exceptions.py`** — test that a `withdraw(balance, amount)`
   function raises `ValueError` when `amount > balance`.
4. **`test_4_fixture.py`** — write a `@pytest.fixture` providing a sample
   list, and two tests that both use it (one checking `sum`, one checking
   `max`).

Run any of them with `pytest day-47/solutions/test_N_name.py -v` once solved,
or run the whole folder at once with `pytest day-47/solutions/ -v`.

## Common Gotchas

- **Forgetting the `test_` prefix.** A function named `check_add()` instead
  of `test_add()` is silently never run by pytest — no error, it just never
  gets discovered.
- **Using `print()` to "check" a result instead of `assert`.** A test with
  no `assert` always "passes," whether or not the code is actually correct —
  `assert` is what makes it a real test.
- **One `assert` doing too much at once.** `assert add(2,3) == 5 and
  add(-1,-1) == -2` fails without telling you *which* part failed — prefer
  separate, focused test functions (as in the example above) or separate
  `assert` lines.
- **Forgetting `pytest.raises` needs the risky call *inside* the `with`
  block.** `divide(10, 0)` called before or after the `with pytest.raises
  (ValueError):` line either crashes the test file outright, or the
  assertion checks nothing at all.
