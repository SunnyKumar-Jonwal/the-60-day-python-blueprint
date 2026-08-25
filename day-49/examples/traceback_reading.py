# This script deliberately crashes -- that's the point of this example.
# Run it, then read the traceback it prints against the notes below.
#
# Expected traceback shape:
#
#   Traceback (most recent call last):
#     File "...", line 17, in <module>
#       print(divide(10, 0))
#             ^^^^^^^^^^^^^
#     File "...", line 13, in divide
#       return a / b
#              ~~^~~
#   ZeroDivisionError: division by zero
#
# Reading bottom to top:
#   1. ZeroDivisionError: division by zero -- the actual problem.
#   2. It happened inside divide(), on the "return a / b" line.
#   3. divide() was called from the top-level "print(divide(10, 0))" line.


def divide(a, b):
    return a / b


print(divide(10, 0))
