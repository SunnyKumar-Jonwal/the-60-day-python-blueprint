# Day 38: pip & virtual environments in depth

**Module:** 4 — Functional Features & Tooling

## What you'll learn

- A deeper look at `pip` beyond `install -r requirements.txt`
- Pinning, upgrading, and uninstalling specific versions
- Inspecting what's installed
- Why every project gets its own virtual environment, revisited with more
  context now that you understand imports (Day 37)

## Explanation

### Why this matters more now

[Day 2](../day-02/README.md) introduced `venv` and basic `pip install` before
you knew what a package or module actually was. Now that Day 37 has explained
`import`, it's worth returning to `pip`/`venv` with the fuller picture: a
virtual environment is really just an isolated *place Python looks for
importable packages* — `pip install` puts things there, and `import` finds
them there.

### Version pinning

```bash
pip install requests==2.31.0   # install an exact version
pip install "requests>=2.28,<3.0"   # a version range
pip install requests             # latest available version
```

Pinning an exact version (`==`) in `requirements.txt` guarantees everyone
installing your project gets identical package versions — important for
reproducibility. This repo's own [`requirements.txt`](../../requirements.txt)
uses unpinned entries (`ruff`, `pytest`) for a learning repo where always
having the latest tool is fine; production projects almost always pin exact
versions.

### Inspecting what's installed

```bash
pip list                    # every package in the current environment
pip show requests           # details about one specific package: version, location, dependencies
pip freeze                  # every package + exact version, in requirements.txt format
```

### Upgrading and uninstalling

```bash
pip install --upgrade requests   # upgrade to the latest version
pip uninstall requests            # remove a package
```

### Keeping `requirements.txt` in sync

A common workflow:

```bash
pip install some-new-package
pip freeze > requirements.txt   # capture the exact current environment
```

Anyone else on the project then runs `pip install -r requirements.txt` and
gets exactly what you have. This is why `requirements.txt` is committed to
version control, while `venv/` itself (Day 2's `.gitignore` entry) never is
— the environment is regenerable from the file; the file is the source of
truth.

### One venv per project

Each project should have its **own** virtual environment, never one shared
venv reused across unrelated projects. Two projects might need conflicting
versions of the same package — a shared environment eventually breaks one of
them. Since a venv is cheap to create (`python -m venv venv`) and easy to
regenerate from `requirements.txt`, there's no downside to keeping them
separate.

## Worked example

This is a terminal-based lesson, like Day 2 — there's no `.py` script to run
today. See [`examples/commands.md`](examples/commands.md) for a
walk-through of every command above with example output.

## Exercises

Terminal exercises, done in a **scratch venv** so you don't disturb this
repo's own environment. Write down what happened for each and compare with
[`solutions/`](solutions/).

1. **`exercise_1_pin_version.md`** — in a scratch venv, install an exact
   older version of a small package (e.g. `pip install requests==2.25.0`),
   then confirm the version with `pip show requests`.
2. **`exercise_2_upgrade.md`** — upgrade that same package to the latest
   version, and confirm the version changed.
3. **`exercise_3_freeze_diff.md`** — run `pip freeze` before and after
   installing a new package, and compare the two outputs.
4. **`exercise_4_uninstall.md`** — uninstall the package, then confirm with
   `pip list` that it's gone.

## Common Gotchas

- **Editing `requirements.txt` by hand and forgetting to actually `pip
  install`.** Adding a line to the file doesn't install anything — you still
  need `pip install -r requirements.txt` (or install the one new package and
  `pip freeze`) to make the environment match the file.
- **Installing globally by accident.** If your terminal prompt doesn't show
  `(venv)`, every `pip install` goes to your system Python instead of the
  project's isolated environment — the exact Day 2 gotcha, still the most
  common `pip` mistake at any experience level.
- **Unpinned dependencies causing "works on my machine."** If
  `requirements.txt` just says `requests` with no version, two people
  installing it a month apart can get different versions with different
  behavior — pin versions for anything beyond a learning project.
- **Confusing `pip uninstall` with deleting the venv folder.** `pip
  uninstall package` removes just that package; deleting the whole `venv/`
  folder removes everything, requiring a full `pip install -r
  requirements.txt` to rebuild it.
