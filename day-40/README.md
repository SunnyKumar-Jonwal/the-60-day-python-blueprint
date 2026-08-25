# Day 40: Milestone — CLI Task Manager (mini-project)

**Module:** 4 — Functional Features & Tooling

## What you're building

A command-line **task manager** you run with real arguments and flags —
`todo.py add "Buy milk"`, `todo.py list`, `todo.py done 0`, `todo.py search
"report"` — instead of an interactive menu like Days 20 and 30. Tasks persist
to a text file between runs.

Full instructions, code, and a stretch goal live in [`project/`](project/) —
start there.

## What this exercises

- **`argparse`** — real command-line arguments and subcommands, introduced
  and explained in the project README (this is the first time this course
  uses it).
- **Generators** ([Day 32](../day-32/README.md)) — `load_tasks()` yields
  tasks one at a time instead of building a list eagerly.
- **Regex** ([Day 39](../day-39/README.md)) — the `search` subcommand
  filters tasks by a regex pattern, not just an exact substring.
- **File handling** ([Days 17](../day-17/README.md)-[18](../day-18/README.md))
  — tasks persist to `tasks.txt` with `with`.

## Run it

```bash
python day-40/project/todo.py add "Buy milk"
python day-40/project/todo.py list
python day-40/project/todo.py done 0
python day-40/project/todo.py search "milk"
```

See [`project/README.md`](project/README.md) for the full write-up, every
command and flag, and the stretch goal.
