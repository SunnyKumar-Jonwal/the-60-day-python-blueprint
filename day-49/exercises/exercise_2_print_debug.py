def find_max(numbers):
    max_value = 0  # bug is hiding somewhere in this function
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


# This call should print -2 (the largest of these three negative numbers),
# but it doesn't. Add print() statements inside find_max() to see what
# max_value is doing at each step, figure out why, then fix the bug.
print(find_max([-5, -2, -10]))
