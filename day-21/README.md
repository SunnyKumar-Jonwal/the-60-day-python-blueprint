# Day 21: Classes & objects

**Module:** 3 — OOP

## What you'll learn

- What a class is, and what an object (instance) is
- Defining a class with `__init__` and `self`
- Instance attributes and methods
- Creating multiple independent objects from one class

## Explanation

### Why classes?

You've been grouping related data in dicts since [Day 13](../day-13/README.md):

```python
dog = {"name": "Rex", "breed": "Labrador", "age": 3}
```

That works, but there's no way to attach *behavior* to it — no built-in way to
say "here's how a dog barks." A **class** is a blueprint that bundles data
(**attributes**) and behavior (**methods**) together. An **object** (or
**instance**) is one specific thing built from that blueprint.

### Defining a class

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
```

- `class Dog:` starts the definition — class names conventionally use
  `CapitalizedWords` (unlike variables and functions, which use `snake_case`).
- `__init__` is a special method (you'll meet more "dunder" methods on
  [Day 26](../day-26/README.md)) that runs automatically when you create a new
  object — it's where you set up the object's initial attributes.
- `self` refers to *this particular object*. It's always the first parameter of
  every regular method, and Python passes it automatically — you never supply it
  yourself when calling the method.
- `self.name = name` stores `name` as an **attribute** on this object, so it can
  be accessed later (`some_dog.name`) and used by other methods (`bark` reads
  `self.name`).

### Creating objects

```python
rex = Dog("Rex", "Labrador", 3)
buddy = Dog("Buddy", "Poodle", 5)

print(rex.name)     # "Rex"
print(buddy.name)   # "Buddy" -- a completely independent object
rex.bark()            # "Rex says Woof!"
buddy.bark()          # "Buddy says Woof!"
```

Each object has its **own** copy of the attributes set in `__init__`. Changing
`rex.age` doesn't affect `buddy.age` at all — they're separate objects built
from the same blueprint.

### Methods take `self`, then whatever else they need

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age}.")

    def rename(self, new_name):
        self.name = new_name
```

Calling `rex.have_birthday()` is really Python calling `Dog.have_birthday(rex)`
under the hood — `self` *is* `rex` inside that call. You never write that `Dog.`
form yourself; `rex.have_birthday()` is the normal way.

## Worked example

See [`examples/classes.py`](examples/classes.py). Run it with:

```bash
python day-21/examples/classes.py
```

## Exercises

1. **`exercise_1_basic_class.py`** — define a `Book` class with `title`,
   `author`, and `pages` attributes, create one instance, and print its
   attributes.
2. **`exercise_2_method.py`** — add a method `summary()` to a `Book` class that
   returns a string like `"'Dune' by Frank Herbert (412 pages)"`.
3. **`exercise_3_multiple_instances.py`** — create three `Book` instances and
   print each one's `summary()`.
4. **`exercise_4_mutating_method.py`** — define a `Counter` class with a
   `count` attribute starting at 0, and an `increment()` method that adds 1 to
   it. Create one, call `increment()` three times, and print the final count.

## Common Gotchas

- **Forgetting `self`.** Every method needs `self` as its first parameter, and
  every access to an attribute inside the class needs the `self.` prefix —
  `def bark(): print(name)` fails because `name` on its own isn't defined; it's
  `self.name`.
- **Forgetting to call `__init__`'s parameters `self.x = x`.** Just writing
  `x` as a parameter without assigning `self.x = x` means the value is lost once
  `__init__` finishes — it never becomes a lasting attribute of the object.
- **Confusing the class with an instance.** `Dog` is the blueprint; `rex = Dog(...)`
  is one instance built from it. `Dog.bark()` (calling on the class itself,
  without an instance) fails — methods need an actual instance to operate on.
- **Naming clash between parameter and attribute.** `def __init__(self, name):
  name = name` does nothing useful — the parameter `name` and a plain local
  variable `name` are not the same as `self.name`.
