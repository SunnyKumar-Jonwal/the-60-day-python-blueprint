# CLI Task Manager — Day 40 mini-project

A command-line task manager driven by real arguments and flags, not an
interactive menu — `todo.py add "Buy milk"`, not "press 1 to add a task."
Tasks persist to a plain text file between runs.

## Setup

Nothing beyond the repo's root setup (see the [root README](../../README.md)) —
this project uses only the Python standard library (`argparse`, `re`).

## A quick `argparse` primer

This project's first new tool is `argparse`, the standard library module for
parsing real command-line arguments — the difference between running
`python todo.py add "Buy milk"` and having the script prompt you with
`input()` afterward.

```python
import argparse

parser = argparse.ArgumentParser(description="A simple command-line task manager")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("text", nargs="+", help="The task description")
```

- `ArgumentParser()` sets up the parser for your whole program.
- `add_subparsers()` lets one program have multiple **subcommands** — `add`,
  `list`, `done`, `search` are each their own subparser here, similar in
  spirit to how `git` has `git add`, `git commit`, `git push`.
- `add_argument("text", nargs="+")` declares a required positional argument
  that can span multiple words (`nargs="+"` collects one-or-more values into
  a list) — so `todo.py add Buy some milk` becomes `["Buy", "some", "milk"]`.
- `add_argument("--pending", action="store_true")` declares an optional flag
  — present means `True`, absent means `False`, with no value needed after
  it.
- `parser.parse_args()` reads `sys.argv` (the actual words typed after
  `python todo.py`) and turns them into an object with one attribute per
  argument — `args.text`, `args.pending`, and so on.

`todo.py` attaches which function handles each subcommand with
`set_defaults(func=cmd_add)`, so `main()` can just call `args.func(args)`
without a long `if`/`elif` chain over `args.command`.

## Run it

From the **repository root**:

```bash
python day-40/project/todo.py add "Buy milk"
python day-40/project/todo.py add "Finish the report"
python day-40/project/todo.py list
python day-40/project/todo.py done 0
python day-40/project/todo.py list --pending
python day-40/project/todo.py list --done
python day-40/project/todo.py search "report"
python day-40/project/todo.py --help
```

Tasks are stored one per line in [`tasks.txt`](tasks.txt) as `done_flag|text`
(e.g. `0|Buy groceries`), and the app ships with two sample tasks already in
there.

## Sample session

```
$ python day-40/project/todo.py list
[ ] 0: Buy groceries
[ ] 1: Write the quarterly report

$ python day-40/project/todo.py add "Call the plumber"
Added: Call the plumber

$ python day-40/project/todo.py done 0
Marked done: Buy groceries

$ python day-40/project/todo.py list
[x] 0: Buy groceries
[ ] 1: Write the quarterly report
[ ] 2: Call the plumber

$ python day-40/project/todo.py list --pending
[ ] 1: Write the quarterly report
[ ] 2: Call the plumber

$ python day-40/project/todo.py search "report"
[ ] 1: Write the quarterly report
```

## How it's built

- `load_tasks(path)` — a **generator function** (Day 32) that `yield`s one
  task dict at a time as it reads `tasks.txt`, instead of building the whole
  list inside itself.
- `save_tasks(path, tasks)` — writes the full task list back out, one line
  per task, with `with` (Day 18).
- `cmd_add`, `cmd_list`, `cmd_done`, `cmd_search` — each takes the parsed
  `args` object and does one job, exactly like Day 20 and Day 30's
  command-handling functions, just triggered by `argparse` instead of a menu
  loop.
- `cmd_search` compiles the user's pattern with `re.compile(..., re.IGNORECASE)`
  (Day 39) and checks it against every task's text with `pattern.search(...)`.

## Stretch goal

Pick one (or more) to extend the project once the core works:

- **A `remove` subcommand**: delete a task by index.
- **Priorities**: add a `--priority high/medium/low` flag to `add`, store it
  alongside the task, and sort `list`'s output by priority.
- **Due dates**: accept a `--due YYYY-MM-DD` flag on `add`, and add a
  `--overdue` flag to `list` that only shows tasks past their due date (you'll
  have the tools for real date parsing after Day 43).
- **Undo**: add an `undo <index>` subcommand that marks a completed task as
  pending again.
