# Day 1: What Python is & why it's popular

**Module:** 1 — Fundamentals

## What you'll learn

- What a programming language is, in plain terms
- What makes Python different from many other languages
- What kinds of things Python is used for
- How to run your very first line of Python

## Explanation

A computer only understands very simple, low-level instructions. A **programming
language** is a way for humans to write instructions in a form that's readable to
people, which then gets translated into something the computer can execute.

**Python** is one such language. It was designed to read almost like plain English,
which is why it's often recommended as a first language. A few things that make it
popular:

- **Readable syntax.** Python uses indentation (spaces) to show which code belongs
  together, instead of curly braces `{ }` like many other languages. This forces code
  to stay visually organized.
- **General purpose.** The same language is used for websites (Instagram, Spotify's
  backend), data analysis, automating boring tasks, scientific computing, and AI —
  you're not locked into one niche.
- **Huge ecosystem.** Anything you want to do, there's very likely a free library
  already written for it. Later in this course you'll use libraries like `requests`
  (talking to websites) and `pandas` (analyzing data).
- **Interpreted, not compiled.** You run Python source code directly — there's no
  separate "build" step before you can see it work. You write a line, you run it, you
  see the result. That fast feedback loop is a big part of why it's a good first
  language.

### Your first program

Every programming tutorial starts here for a reason — it's the smallest possible
"it works":

```python
print("Hello, world!")
```

`print(...)` is a **function** — a reusable command — that displays whatever is
inside the parentheses on the screen. You'll learn far more about functions on
[Day 8](../day-08/README.md), but you don't need to understand how `print` is *built*
to start using it.

### Running a Python file

Python code lives in plain text files ending in `.py`. To run one, open a terminal
in the folder containing the file and type:

```bash
python hello.py
```

(On some systems, especially macOS/Linux, the command is `python3` instead of
`python` — more on that on [Day 2](../day-02/README.md).)

## Worked example

See [`examples/hello.py`](examples/hello.py). Run it with:

```bash
python day-01/examples/hello.py
```

You should see three lines of greeting text printed to your terminal.

## Exercises

Open the files in [`exercises/`](exercises/) — each has `TODO` comments marking what
to fill in. Check your work against [`solutions/`](solutions/) afterward.

1. **`exercise_1_hello.py`** — print a greeting with your own name in it.
2. **`exercise_2_lines.py`** — print three separate lines using three separate
   `print(...)` calls.
3. **`exercise_3_favorites.py`** — print your favorite food, hobby, and place, one
   per line.
4. **`exercise_4_math.py`** — print the result of `7 + 5` and the result of `7 * 5`
   using `print(...)` directly around the expressions.

## Common Gotchas

- **Forgetting quotes.** `print(Hello)` is not the same as `print("Hello")` — without
  quotes, Python thinks `Hello` is the name of a variable (something you'll meet on
  [Day 3](../day-03/README.md)) and will error with `NameError`.
- **Mismatched quotes.** `print("Hello')` (mixing `"` and `'`) is a syntax error.
  Use the same quote character to open and close a string.
- **Forgetting parentheses.** In Python 3, `print "Hello"` (no parentheses) is a
  syntax error — that was valid in the much older Python 2, which you don't need to
  worry about.
- **Case sensitivity.** `Print("Hello")` (capital P) fails — Python is case-sensitive,
  so it's `print`, not `Print` or `PRINT`.
