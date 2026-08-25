# Day 2: Setup — installing Python, venv, pip

**Module:** 1 — Fundamentals

## What you'll learn

- How to check whether Python is installed, and which version
- What a virtual environment is and why every project should have one
- How to create, activate, and use one with `venv`
- How to install packages with `pip`

## Explanation

### Checking your Python installation

Open a terminal and run:

```bash
python3 --version   # macOS/Linux
python --version    # Windows
```

You should see something like `Python 3.11.4`. This course targets **Python 3.11+**.
If nothing prints, or you see a much older version (Python 2.x), install a current
version from [python.org/downloads](https://www.python.org/downloads/) first.

From here on, this course writes `python` in commands. If your system only responds
to `python3`, mentally substitute it every time.

### Why virtual environments?

Every Python project can depend on external packages (Day 41 introduces `requests`,
Day 45 introduces `pandas`, and so on). Different projects on your machine might need
*different versions* of the same package. If you installed everything globally,
projects would eventually conflict with each other.

A **virtual environment** (venv) is an isolated, self-contained copy of Python plus
its own private package folder, scoped to one project. Installing something inside
a venv doesn't touch any other project or your system's Python at all.

### Creating and activating a venv

From your project folder:

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# Windows (cmd.exe)
python -m venv venv
venv\Scripts\activate.bat
```

`python -m venv venv` says "run the `venv` module, and create the environment in a
folder named `venv`." You'll know it's activated because your terminal prompt gets
a `(venv)` prefix. From that point on, `python` and `pip` inside that terminal refer
to the venv's private copies — not your system-wide Python.

To leave it: run `deactivate`.

### Installing packages with pip

`pip` is Python's package installer — it downloads and installs libraries from
[PyPI](https://pypi.org), the Python Package Index.

```bash
pip install ruff          # install a single package
pip install -r requirements.txt   # install everything listed in a file
pip list                  # see what's installed in the current environment
pip freeze > requirements.txt     # write installed packages + versions to a file
```

This repo already has a [`requirements.txt`](../../requirements.txt) at the root —
that's the standard way to share "here's what you need to install" with anyone
running the project.

## Worked example

[`examples/check_setup.py`](examples/check_setup.py) is a plain script (no imports
needed yet) that just confirms your environment can run Python files correctly —
run it after activating your venv:

```bash
python day-02/examples/check_setup.py
```

Also try, directly in your terminal (not in a `.py` file):

```bash
python --version
pip list
```

## Exercises

These are done in your terminal, not by writing more Python — that's the point of
today's lesson. Write down what happened for each (a text file, a note, whatever
works for you), then compare with [`solutions/`](solutions/) for the expected result.

1. **`exercise_1_version.md`** — run the version-check command and record the output.
2. **`exercise_2_create_venv.md`** — create a venv named `practice_venv` in a scratch
   folder and activate it.
3. **`exercise_3_install.md`** — with `practice_venv` activated, install `requests`
   and then run `pip list` to confirm it's there.
4. **`exercise_4_freeze.md`** — run `pip freeze` inside `practice_venv` and save the
   output to a file called `frozen.txt`.

## Common Gotchas

- **Forgetting to activate the venv.** If your prompt doesn't show `(venv)`, `pip
  install` is installing globally, not into your project's isolated environment.
- **Committing the `venv/` folder to git.** It's large, machine-specific, and
  regenerable from `requirements.txt` — this repo's [`.gitignore`](../../.gitignore)
  already excludes it. Never commit it.
- **`python` vs `python3`.** On macOS/Linux, `python` may not exist or may point to
  an old Python 2 — use `python3` there. On Windows, the official installer sets up
  `python`.
- **PowerShell blocking the activate script.** If `Activate.ps1` refuses to run with
  a script-execution error, you may need to adjust your execution policy — this is a
  Windows security feature, not a bug in your setup.
