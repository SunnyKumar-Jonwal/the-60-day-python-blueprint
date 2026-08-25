# TODO: build a @retry(attempts) decorator (three levels) that calls the
# wrapped function, catching ValueError, printing "Attempt N failed: {error}"
# each time, and re-raising the last error if every attempt fails

# TODO: apply @retry(3) to a function always_fails() that raises ValueError("nope")
# TODO: call always_fails() inside try/except so the script doesn't crash,
# printing a final "Gave up." message in the except block
