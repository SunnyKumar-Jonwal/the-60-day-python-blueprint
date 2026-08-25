# Day 60: Capstone (part 2) — finish + interview prep

**Module:** 6 — Web APIs & Capstone

## Finishing the capstone

Yesterday you built the [Library API](../day-59/project/) end to end. Today
isn't a new project — it's finishing that one properly, the way real work
actually ends: verify it, polish it, and (optionally) extend it.

### 1. Verify everything, one more time

```bash
python day-59/project/main.py
# in another terminal:
curl http://127.0.0.1:8000/books
curl http://127.0.0.1:8000/books/stats
```

```bash
pytest day-59/project/test_books.py -v
ruff check day-59/project/
```

If anything fails, this is exactly the debugging process from
[Day 49](../day-49/README.md): read the traceback from the bottom up, form a
hypothesis, and test it.

### 2. Read the whole project in order

Rather than jumping between files, read [`day-59/project/`](../day-59/project/)
top to bottom in this order — it's designed to be read this way:
`models.py` (domain) → `repository.py` (persistence) →
`routers/books.py` (API) → `main.py` (wiring) → `test_books.py` (proof it
works). Notice how each layer only knows about the one below it — the API
layer never writes SQL, and the persistence layer never imports FastAPI.
That separation is the single biggest thing worth taking away from this
capstone into your own future projects.

### 3. Pick a stretch goal

[`day-59/project/README.md`](../day-59/project/README.md) lists four stretch
goals (pagination, a `return` action, author stats, a `Member` resource).
Pick at least one and implement it, including a test for it — this is the
best evidence, at the end of 60 days, that you can extend a real codebase
you didn't write from scratch, safely.

### 4. Interview prep

[`interview-question-bank.md`](../interview-question-bank.md) (repo root)
has 25-30 common Python interview questions with explained answers, spanning
the entire course — mutable vs. immutable types, list vs. generator,
decorators, OOP concepts, and more. Work through it as a final review.

## You're done

Sixty days ago this course assumed zero programming experience. You've
since built a contact book, a bank account simulator, a CLI task manager, a
data analysis pipeline with real tests, and a full CRUD API with a database
— each one working, verified, and yours. That's the actual skill: not
having read about Python, but having built things with it that ran
correctly. Keep building.
