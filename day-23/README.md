# Day 23: Inheritance

**Module:** 3 — OOP

## What you'll learn

- Creating a subclass that inherits from a parent class
- `super()` and calling the parent's `__init__`
- Overriding a parent's method
- Checking types with `isinstance()`

## Explanation

### Why inheritance?

Say you're modeling animals. A `Dog` and a `Cat` share things in common (a
name, an age) but also differ (how they make a sound). **Inheritance** lets a
class reuse another class's attributes and methods, and only add or change
what's different.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):     # Dog inherits from Animal
    def speak(self):     # overriding Animal's speak()
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")
```

`Animal` is the **parent class** (also called a **base class** or
**superclass**). `Dog` and `Cat` are **subclasses** (or **child classes**) —
each `is an` `Animal`, plus its own behavior.

```python
rex = Dog("Rex")
whiskers = Cat("Whiskers")

rex.speak()        # "Rex says Woof!"      -- Dog's own speak()
whiskers.speak()   # "Whiskers says Meow!" -- Cat's own speak()
print(rex.name)    # "Rex" -- inherited from Animal, never redefined in Dog
```

`Dog` never wrote its own `__init__` — it automatically uses `Animal`'s.

### `super()`

If a subclass *does* need its own `__init__`, but still wants the parent's
setup to run too, call `super().__init__(...)`:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # runs Animal's __init__, setting self.name
        self.breed = breed         # then adds Dog's own attribute
```

```python
rex = Dog("Rex", "Labrador")
print(rex.name)    # "Rex"  -- set by Animal's __init__ via super()
print(rex.breed)   # "Labrador" -- set by Dog's own __init__
```

Without `super().__init__(name)`, you'd have to repeat `self.name = name`
yourself in `Dog` — `super()` avoids that duplication and keeps `Animal`'s
setup logic in one place.

### Checking types

```python
print(isinstance(rex, Dog))      # True
print(isinstance(rex, Animal))   # True -- a Dog IS an Animal too
print(isinstance(rex, Cat))      # False
```

`isinstance()` respects the inheritance chain — every `Dog` is also
considered an `Animal`, since that's what inheriting from it means.

## Worked example

See [`examples/inheritance.py`](examples/inheritance.py). Run it with:

```bash
python day-23/examples/inheritance.py
```

## Exercises

1. **`exercise_1_basic_inherit.py`** — define a `Vehicle` class with `make` and
   `model`, then a `Car` subclass that inherits it with no changes; create a
   `Car` and print its `make`/`model`.
2. **`exercise_2_override.py`** — define a `Shape` class with a `describe()`
   method, and two subclasses `Square` and `Circle` that each override
   `describe()` with their own message.
3. **`exercise_3_super.py`** — define an `Employee` class with `name` and
   `salary`, and a `Manager` subclass that adds a `team_size` attribute, using
   `super().__init__()` for the shared part.
4. **`exercise_4_isinstance.py`** — given instances of a parent and two
   subclasses, print the result of several `isinstance()` checks between them.

## Common Gotchas

- **Forgetting `super().__init__()`.** If a subclass defines its own
  `__init__` without calling `super().__init__(...)`, the parent's setup never
  runs, and any attributes it would have set are simply missing.
- **Overriding when you meant to extend.** Redefining a method entirely (as in
  the `Dog`/`Cat` example) replaces the parent's version completely. If you
  want to *add* to the parent's behavior rather than replace it, call
  `super().method_name()` inside your override, then do the extra work.
- **Deep inheritance chains get hard to follow.** A class inheriting from a
  class that inherits from another class (and so on) can make it hard to trace
  where an attribute or method actually comes from — prefer shallow, clear
  hierarchies.
- **Confusing "is-a" with "has-a".** Inheritance models "a `Dog` **is an**
  `Animal`." If the relationship is really "a `Car` **has an** `Engine`,"
  that's composition (storing an `Engine` instance as an attribute), not
  inheritance.
