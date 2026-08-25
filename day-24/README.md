# Day 24: Polymorphism

**Module:** 3 — OOP

## What you'll learn

- What polymorphism means in practice
- Writing code that works with any object sharing a method name
- Duck typing
- How this connects to yesterday's method overriding

## Explanation

### What polymorphism means

**Polymorphism** ("many forms") is the idea that different classes can share
the same method name, and you can call that method the same way regardless of
which specific class the object actually is. You already saw the mechanism for
this on [Day 23](../day-23/README.md) — method overriding — polymorphism is
what that mechanism gives you the power to *do*.

```python
class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Duck:
    def speak(self):
        return "Quack!"
```

None of these inherit from each other — they're unrelated classes that just
happen to each define a `speak()` method. This is enough:

```python
animals = [Dog(), Cat(), Duck()]

for animal in animals:
    print(animal.speak())   # "Woof!", "Meow!", "Quack!"
```

The loop doesn't know or care which specific class each `animal` is — it just
calls `.speak()` and trusts that whatever the object is, it knows how to
respond. This is the payoff: code written once (the loop) works with any
object that implements the expected method, including classes that don't
exist yet.

### Duck typing

Python takes this further than languages that require explicit shared
interfaces: "if it walks like a duck and quacks like a duck, it's a duck." As
long as an object has the method you're calling, Python doesn't check what
class it "officially" is:

```python
class Robot:
    def speak(self):
        return "BEEP BOOP"


animals = [Dog(), Cat(), Duck(), Robot()]
for animal in animals:
    print(animal.speak())   # works for the Robot too -- it has speak(), that's all that matters
```

### Polymorphism with inheritance

The same idea applies when subclasses override a shared parent method — which
is exactly what you built on Day 23:

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())   # 12, then 78.53975 -- same call, different behavior per class
```

`raise NotImplementedError(...)` in the base `Shape.area()` is a common pattern
meaning "every subclass must override this" — you'll cover `raise` and
exceptions properly starting [Day 28](../day-28/README.md).

## Worked example

See [`examples/polymorphism.py`](examples/polymorphism.py). Run it with:

```bash
python day-24/examples/polymorphism.py
```

## Exercises

1. **`exercise_1_unrelated_classes.py`** — define three unrelated classes
   (`Guitar`, `Piano`, `Drum`), each with a `play()` method, then loop over a
   list of one of each and call `play()` on all of them.
2. **`exercise_2_shape_areas.py`** — define a `Shape` base class and two
   subclasses `Triangle` and `Square`, each with their own `area()`; loop over
   a list of both and print each area.
3. **`exercise_3_total_area.py`** — reuse Exercise 2's shapes, and write a
   function `total_area(shapes)` that sums up `.area()` across a list of mixed
   shape objects.
4. **`exercise_4_duck_typing.py`** — define two unrelated classes that both
   have a `describe()` method, put instances of both in one list, and print
   each one's `describe()` in a loop.

## Common Gotchas

- **Thinking polymorphism requires inheritance.** It doesn't — duck typing
  (Exercise 1 and 4) works between completely unrelated classes, as long as
  they share a method name.
- **Calling a method that not every object in the collection actually has.**
  If one item in your list is missing the method you're calling,
  `AttributeError` crashes the loop at that item — consistency of the shared
  method name across all objects is what makes this pattern work.
- **Forgetting to override in a subclass.** If `Shape.area()` raises
  `NotImplementedError` and a subclass never defines its own `area()`, calling
  it on that subclass still raises the error — inheriting a method doesn't
  automatically make it correct for every subclass.
- **Over-engineering with polymorphism where a simple `if`/`elif` would do.**
  For two or three fixed cases that will never grow, a straightforward
  conditional (Day 6) can be clearer than building a class hierarchy just to
  avoid it.
