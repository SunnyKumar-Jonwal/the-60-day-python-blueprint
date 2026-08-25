# Day 22: Instance vs class attributes/methods

**Module:** 3 — OOP

## What you'll learn

- Class attributes (shared by every instance) vs instance attributes (unique
  per instance)
- `@classmethod` and `@staticmethod`
- When to reach for each

## Explanation

### Class attributes

An attribute defined directly in the class body (not inside `__init__`,
without `self.`) is a **class attribute** — it's shared by every instance of
the class, unless a specific instance overrides it:

```python
class Dog:
    species = "Canis familiaris"   # class attribute -- same for every Dog

    def __init__(self, name):
        self.name = name             # instance attribute -- unique per Dog
```

```python
rex = Dog("Rex")
buddy = Dog("Buddy")

print(rex.species)     # "Canis familiaris"
print(buddy.species)   # "Canis familiaris" -- same value, shared from the class
print(rex.name)        # "Rex"
print(buddy.name)       # "Buddy" -- different, each instance's own
```

Class attributes are useful for constants or defaults shared across every
instance — a species name, a tax rate, a maximum allowed value.

**Careful:** assigning to `rex.species = "..."` creates a *new instance
attribute* on `rex` alone, shadowing the class attribute — it does not change
it for `buddy` or for the class. To actually change the shared value for every
instance, assign to `Dog.species = "..."` instead.

### `@classmethod`

A **class method** receives the class itself (conventionally named `cls`)
instead of an instance (`self`). It's marked with the `@classmethod`
**decorator** — a `@`-prefixed line right above the method that changes how
Python treats it. (You'll learn how decorators work in general on
[Day 35](../day-35/README.md); for now, just know `@classmethod` and
`@staticmethod` are decorators you apply to methods that don't need a specific
instance.)

Class methods are commonly used as **alternative constructors**:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year):
        age = current_year - birth_year
        return cls(name, age)   # cls(...) here means Dog(...)


rex = Dog.from_birth_year("Rex", 2021, 2024)
print(rex.age)   # 3
```

### `@staticmethod`

A **static method** takes neither `self` nor `cls` — it's just a regular
function that happens to live inside the class because it's conceptually
related to it:

```python
class Dog:
    @staticmethod
    def is_valid_age(age):
        return age >= 0


print(Dog.is_valid_age(3))    # True -- called on the class, no instance needed
print(Dog.is_valid_age(-1))   # False
```

### Choosing between them

| | First parameter | Called via | Use for |
|---|---|---|---|
| Instance method | `self` | `instance.method()` | Behavior that reads/changes this object's data |
| `@classmethod` | `cls` | `Class.method()` or `instance.method()` | Alternative constructors, things about the class as a whole |
| `@staticmethod` | *(none)* | `Class.method()` or `instance.method()` | A helper that's related but doesn't need `self` or `cls` at all |

## Worked example

See [`examples/attributes_methods.py`](examples/attributes_methods.py). Run it
with:

```bash
python day-22/examples/attributes_methods.py
```

## Exercises

1. **`exercise_1_class_attribute.py`** — define a `Circle` class with a class
   attribute `pi = 3.14159` and an instance attribute `radius`; add a method
   `area()` using both.
2. **`exercise_2_shared_state.py`** — define an `Employee` class with a class
   attribute `company = "Acme Corp"`, create two instances, and print both
   instances' `company` to show they share the same value.
3. **`exercise_3_classmethod.py`** — add a `@classmethod` `from_string(cls,
   data)` to a `Person` class that parses `"name,age"` and returns a new
   instance.
4. **`exercise_4_staticmethod.py`** — add a `@staticmethod` `is_valid_score(score)`
   to a `Grade` class that returns whether a score is between 0 and 100.

## Common Gotchas

- **Accidentally shadowing a class attribute.** `instance.attr = value`
  *always* creates or updates an instance attribute, even if a class attribute
  of the same name exists — it never modifies the shared class attribute.
- **Mutable class attributes.** `class Dog: tricks = []` shares the **same
  list** across every instance — appending to `some_dog.tricks` affects every
  other dog too. Mutable defaults belong in `__init__` as instance attributes,
  not as class attributes.
- **Forgetting `cls` in a classmethod.** Just like `self` in instance methods,
  `cls` must be the first parameter of a `@classmethod` — Python supplies it
  automatically, you don't pass it yourself.
- **Overusing `@staticmethod`.** If a method never needs `self` and doesn't
  logically belong to the class's identity, it might just be better as a plain
  function outside the class altogether.
