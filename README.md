# Learn Python in 60 Days (From Scratch)

[![Python Practice](https://github.com/SunnyKumar-Jonwal/the-60-day-python-blueprint.git/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/SunnyKumar-Jonwal/learn-python-in-60-days/actions/workflows/lint-and-test.yml)

A self-contained, day-by-day Python curriculum for absolute beginners. Sixty days,
six modules, five mini-projects, and a two-day capstone — each day is a folder with
an explanation, worked examples, exercises, and solutions.

No prior programming experience assumed. Each day only uses concepts introduced on
that day or earlier.

## Roadmap

| Day | Topic | Module | Mini-project? |
|---|---|---|---|
| 01 | What Python is & why it's popular | 1 — Fundamentals | |
| 02 | Setup: installing Python, venv, pip | 1 — Fundamentals | |
| 03 | Variables & data types | 1 — Fundamentals | |
| 04 | Operators | 1 — Fundamentals | |
| 05 | Input & output | 1 — Fundamentals | |
| 06 | Control flow (if / elif / else) | 1 — Fundamentals | |
| 07 | Loops (for / while) | 1 — Fundamentals | |
| 08 | Functions | 1 — Fundamentals | |
| 09 | Intro to type hints | 1 — Fundamentals | |
| 10 | String basics | 1 — Fundamentals | |
| 11 | Lists | 2 — Data Structures & Files | |
| 12 | Tuples | 2 — Data Structures & Files | |
| 13 | Dictionaries | 2 — Data Structures & Files | |
| 14 | Sets | 2 — Data Structures & Files | |
| 15 | Comprehensions | 2 — Data Structures & Files | |
| 16 | String methods in depth | 2 — Data Structures & Files | |
| 17 | File handling I (open/read/write) | 2 — Data Structures & Files | |
| 18 | File handling II (context managers) | 2 — Data Structures & Files | |
| 19 | Combining data structures & files | 2 — Data Structures & Files | |
| 20 | **Mini-project: Contact Book** | 2 — Data Structures & Files | ✅ |
| 21 | Classes & objects | 3 — OOP | |
| 22 | Instance vs class attributes/methods | 3 — OOP | |
| 23 | Inheritance | 3 — OOP | |
| 24 | Polymorphism | 3 — OOP | |
| 25 | Encapsulation | 3 — OOP | |
| 26 | Dunder methods I (`__init__`, `__str__`, `__repr__`) | 3 — OOP | |
| 27 | Dunder methods II (`__eq__`, operator overloading) | 3 — OOP | |
| 28 | Exceptions (try/except/finally) | 3 — OOP | |
| 29 | Custom exceptions | 3 — OOP | |
| 30 | **Mini-project: Bank Account Simulator** | 3 — OOP | ✅ |
| 31 | Iterators & the iterator protocol | 4 — Functional & Tooling | |
| 32 | Generators & `yield` | 4 — Functional & Tooling | |
| 33 | Closures | 4 — Functional & Tooling | |
| 34 | Lambdas & functional tools | 4 — Functional & Tooling | |
| 35 | Decorators I | 4 — Functional & Tooling | |
| 36 | Decorators II (with arguments) | 4 — Functional & Tooling | |
| 37 | Modules & packages | 4 — Functional & Tooling | |
| 38 | pip & virtual environments in depth | 4 — Functional & Tooling | |
| 39 | Regex | 4 — Functional & Tooling | |
| 40 | **Mini-project: CLI Task Manager** | 4 — Functional & Tooling | ✅ |
| 41 | The `requests` library & real APIs | 5 — Real-World Libraries | |
| 42 | JSON handling | 5 — Real-World Libraries | |
| 43 | `datetime` | 5 — Real-World Libraries | |
| 44 | Intro to numpy | 5 — Real-World Libraries | |
| 45 | Intro to pandas I (reading CSV) | 5 — Real-World Libraries | |
| 46 | Intro to pandas II (filtering & aggregation) | 5 — Real-World Libraries | |
| 47 | Intro to pytest | 5 — Real-World Libraries | |
| 48 | Logging | 5 — Real-World Libraries | |
| 49 | Debugging techniques | 5 — Real-World Libraries | |
| 50 | **Mini-project: Weather Data Analysis** | 5 — Real-World Libraries | ✅ |
| 51 | FastAPI basics & first endpoint | 6 — Web APIs & Capstone | |
| 52 | Path/query params, request & response models | 6 — Web APIs & Capstone | |
| 53 | Status codes & error handling | 6 — Web APIs & Capstone | |
| 54 | SQLite basics | 6 — Web APIs & Capstone | |
| 55 | Connecting FastAPI to SQLite | 6 — Web APIs & Capstone | |
| 56 | Building a full REST API (CRUD) | 6 — Web APIs & Capstone | |
| 57 | API testing (pytest + TestClient) | 6 — Web APIs & Capstone | |
| 58 | Review & polish | 6 — Web APIs & Capstone | |
| 59 | **Capstone (part 1): build the Library API** | 6 — Web APIs & Capstone | ✅ |
| 60 | **Capstone (part 2): finish + interview prep** | 6 — Web APIs & Capstone | ✅ |

Also included: [`interview-question-bank.md`](interview-question-bank.md) — 25-30 common
Python interview questions with explained answers, and [`PROGRESS.md`](PROGRESS.md), a
checklist to track your way through all 60 days.

## Prerequisites

- **Python 3.11+** — [download here](https://www.python.org/downloads/). Verify with:
  ```bash
  python3 --version   # macOS/Linux
  python --version    # Windows
  ```
- **A code editor** — [VS Code](https://code.visualstudio.com/) is a solid free choice;
  install its Python extension once you have it open.
- **A terminal** — the one built into your editor is fine.

No prior programming knowledge is required — Day 1 starts from zero.

### Create and activate a virtual environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

Then install the base dependencies:

```bash
pip install -r requirements.txt
```

Later modules add packages (`requests`, `pandas`, `numpy`, `fastapi`, ...) to
`requirements.txt` as they're needed — rerun `pip install -r requirements.txt` after
pulling updates.

## How to use this repo

1. Work through folders in order: `day-01/`, `day-02/`, ... `day-60/`.
2. Each day's `README.md` has the explanation and worked example — read it first.
3. Run the examples yourself: `python day-01/examples/hello.py` (or whatever's inside).
4. Attempt the exercises in `exercises/` (they have `TODO`s, no solutions inline).
5. Check your work against `solutions/` once you've tried.
6. On milestone days (20, 30, 40, 50, 59-60) build the mini-project — these are the
   best evidence of what you've actually learned.

## Status

All 60 days are complete, verified, and covered by CI. This repo was built incrementally,

`.github/workflows/lint-and-test.yml` runs on every push/PR: `ruff check .`, the full
`pytest` suite, and [`scripts/run_examples.py`](scripts/run_examples.py), which actually
executes every day's `examples/`, `solutions/`, and milestone `project/` script (starting
and stopping the FastAPI ones, feeding input to the interactive ones) and fails the build
if any of them error unexpectedly.

## License

[MIT](LICENSE) © SunnyKumar Jonwal
