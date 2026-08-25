# Try this one yourself, interactively, in a terminal:
#   python day-49/examples/pdb_demo.py
#
# Uncomment the breakpoint() line below first. When you run it, execution
# will pause right there and drop you into the (Pdb) prompt. Try:
#   p total       -- print the current value of `total`
#   p item        -- print the current value of `item`
#   n             -- run the next line
#   c             -- continue running to the end (or the next breakpoint)
#   q             -- quit the debugger


def calculate_total(items):
    total = 0
    for item in items:
        # breakpoint()
        total += item["price"] * item["quantity"]
    return total


order = [
    {"price": 9.99, "quantity": 2},
    {"price": 4.5, "quantity": 3},
]

print(calculate_total(order))
