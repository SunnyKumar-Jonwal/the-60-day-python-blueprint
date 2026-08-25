# TODO: build a @require_positive decorator (NO arguments of its own -- two
# levels only: decorator -> wrapper) that raises ValueError if any positional
# argument to the wrapped function is negative, otherwise calls it normally

# TODO: apply @require_positive to a function add(a, b) that returns a + b
# TODO: call add(3, 4) inside try/except and print the result
# TODO: call add(-3, 4) inside try/except and print the caught error message
