# Day 37: Modules & packages

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- What `import` actually does
- The standard library, and importing from it (`import x`, `from x import y`)
- Writing and importing your own module
- Packages, `__init__.py`, and the `if __name__ == "__main__":` idiom

## Explanation

### What `import` does

You've already used `import` a few times this module (`from functools import
reduce`, `from functools import wraps`) without a full explanation. A
**module** is just a `.py` file. `import some_module` runs that file once,
and gives you access to everything defined in it (functions, classes,
variables) through the name `some_module`.

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)            # 3.14159...
```

`math` here is the **standard library** — modules that ship with Python
itself, ready to use with no installation (unlike third-party packages
installed with `pip`, Day 2). Other standard library modules you'll use soon:
`re` ([Day 39](../day-39/README.md)), `datetime`, `json`
([Days 42-43](../day-42/README.md)).

### Two import styles

```python
import math
print(math.sqrt(16))       # must prefix with "math."

from math import sqrt
print(sqrt(16))              # imported directly, no prefix

from math import sqrt, pi   # import multiple names at once
```

`import module_name` keeps things namespaced (clearer where a name came
from); `from module_name import specific_thing` is more concise when you use
that thing often. Both are correct Python — pick based on readability for
the specific case.

### Writing your own module

Any `.py` file can be imported by another, as long as Python can find it
(normally: it's in the same folder, or a folder on Python's search path).
Say you have `math_helpers.py`:

```python
# math_helpers.py
def square(n):
    return n * n

def cube(n):
    return n * n * n
```

Another file in the same folder can import it by filename (no `.py`):

```python
# main.py
from math_helpers import square, cube

print(square(4))   # 16
print(cube(3))       # 27
```

### `if __name__ == "__main__":`

Every module has a special variable `__name__`. When a file is run directly
(`python main.py`), Python sets `__name__` to `"__main__"` in that file. When
a file is *imported* by another file instead, `__name__` is set to the
module's own name.

This lets a file work both as a standalone script **and** as an importable
module, without its "run this when executed directly" code firing just from
being imported:

```python
# math_helpers.py
def square(n):
    return n * n

if __name__ == "__main__":
    print(square(5))   # only runs if you execute this file directly
```

```bash
python math_helpers.py   # prints 25 -- __name__ is "__main__" here
```

```python
from math_helpers import square   # importing it does NOT print 25
```

You'll see this idiom constantly in real Python code — it's the standard way
to make a file dual-purpose.

### Packages

A **package** is a folder of modules, usually containing an `__init__.py`
file (which can be empty) that marks it as importable as a package:

```
my_package/
├── __init__.py
├── shapes.py
└── colors.py
```

```python
from my_package import shapes
from my_package.colors import RED
```

This course doesn't build a multi-file package today — you'll see one in
practice on [Day 40](../day-40/README.md)'s CLI project, which is organized
as a small package.

## Worked example

See [`examples/main.py`](examples/main.py), which imports from
[`examples/math_helpers.py`](examples/math_helpers.py) — two files in the
same folder, showing both import styles and the `__name__` idiom. Run it
with:

```bash
python day-37/examples/main.py
```

## Exercises

1. **`exercise_1_stdlib_import.py`** — `import math` and print `math.pi` and
   `math.sqrt(64)`.
2. **`exercise_2_from_import.py`** — `from math import floor, ceil` and print
   the result of each on `4.7`.
3. **`exercise_3_own_module.py`** and **`exercise_3_helpers.py`** — write a
   small `exercise_3_helpers.py` module with a function `is_palindrome(text)`,
   then import and use it from `exercise_3_own_module.py`.
4. **`exercise_4_main_guard.py`** — write a file with a function and an
   `if __name__ == "__main__":` block that only prints something when the
   file is run directly.

## Common Gotchas

- **`ModuleNotFoundError` for a file that "should" be importable.** Python
  looks for modules relative to where you *run* Python from, not necessarily
  where the importing file lives — this is exactly why every command in this
  course is run from the repository root.
- **Naming your own file the same as a standard library module.** A file
  named `math.py` in your project shadows the real `math` module for any
  import in that same folder — avoid reusing standard library names.
- **Forgetting the `.py` when explaining, but including it when importing.**
  `import math_helpers.py` is wrong — imports use the module name without
  the extension: `import math_helpers`.
- **Putting real logic outside any `if __name__ == "__main__":` guard when a
  file is meant to be both a script and an importable module.** Otherwise
  that code runs immediately just from being imported, which is rarely what
  you want for a reusable module.
