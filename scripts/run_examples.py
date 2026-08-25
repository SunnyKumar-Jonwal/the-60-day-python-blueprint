"""Run every day's examples/, solutions/, and milestone project entry-point
script from the repository root, failing (nonzero exit) if any of them
errors unexpectedly.

Used by CI (.github/workflows/lint-and-test.yml) and safe to run locally:

    python scripts/run_examples.py

Handles a few special cases that show up across the 60-day course:

- FastAPI apps that start a blocking uvicorn server (detected by the source
  containing "uvicorn.run(") are run with a short timeout; being killed by
  the timeout counts as success -- that means the server started up fine.
  A nonzero exit *before* the timeout means it crashed on startup.
- Day 49's two traceback-reading demos are SUPPOSED to crash with an
  uncaught exception -- they're listed in EXPECTED_TO_FAIL below.
- A few scripts read from stdin (Day 5's interactive demos, the Day 20/30
  menu-driven projects) or expect real CLI arguments (Day 40's argparse
  project) -- STDIN_INPUT and ARGS_OVERRIDE supply what a learner would
  actually type/pass.

Only files directly inside an examples/, solutions/, or project/ folder are
run (not recursively) -- this deliberately skips importable submodules like
day-58/.../routers/books.py or day-59/project/routers/books.py, which
aren't meant to be executed directly and would fail on their relative
imports if run standalone from the wrong directory.

Exercises are intentionally-incomplete TODO stubs and are not run here --
ruff and pytest still cover them where applicable.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

EXPECTED_TO_FAIL = {
    "day-49/examples/traceback_reading.py",
    "day-49/solutions/exercise_1_read_traceback.py",
}

STDIN_INPUT = {
    "day-05/examples/greet_interactive.py": "Ada\n30\n",
    "day-05/solutions/exercise_4_interactive.py": "Ada\n8\n",
    "day-20/project/contact_book.py": "5\n",
    "day-30/project/bank_simulator.py": "6\n",
}

ARGS_OVERRIDE = {
    "day-40/project/todo.py": ["list"],
}

SERVER_TIMEOUT_SECONDS = 5
DEFAULT_TIMEOUT_SECONDS = 30


def is_server_script(path: Path) -> bool:
    return "uvicorn.run(" in path.read_text(encoding="utf-8")


def run_script(path: Path, rel: str) -> tuple[bool, str]:
    stdin_data = STDIN_INPUT.get(rel)
    extra_args = ARGS_OVERRIDE.get(rel, [])
    server = is_server_script(path)
    timeout = SERVER_TIMEOUT_SECONDS if server else DEFAULT_TIMEOUT_SECONDS

    timed_out = False
    try:
        result = subprocess.run(
            [sys.executable, str(path), *extra_args],
            cwd=REPO_ROOT,
            input=stdin_data,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        result = exc
        timed_out = True

    if server:
        # A server is expected to still be running when the timeout hits --
        # that's success. A nonzero *early* exit means it crashed on startup.
        if timed_out:
            return True, ""
        if result.returncode != 0:
            return False, result.stderr
        return True, ""

    if rel in EXPECTED_TO_FAIL:
        if timed_out:
            return False, "expected to crash quickly, but timed out instead"
        if result.returncode == 0:
            return False, "expected an uncaught exception, but it exited cleanly"
        return True, ""

    if timed_out:
        return False, f"timed out after {timeout}s"
    if result.returncode != 0:
        return False, result.stderr
    return True, ""


def collect_scripts() -> list[Path]:
    scripts: set[Path] = set()
    for folder in ("examples", "solutions", "project"):
        scripts.update(REPO_ROOT.glob(f"day-*/{folder}/*.py"))
    return sorted(scripts)


def main() -> int:
    scripts = collect_scripts()
    failures = []

    for path in scripts:
        rel = path.relative_to(REPO_ROOT).as_posix()
        ok, message = run_script(path, rel)
        print(f"[{'OK' if ok else 'FAIL'}] {rel}")
        if not ok:
            failures.append((rel, message))

    if failures:
        print("\n=== FAILURES ===")
        for rel, message in failures:
            print(f"\n{rel}:\n{message}")
        print(f"\n{len(failures)} of {len(scripts)} scripts failed.")
        return 1

    print(f"\nAll {len(scripts)} scripts OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
