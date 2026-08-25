def get_last_n_items(items, n):
    return items[-n:-1]  # bug is on this line


# Expected: get_last_n_items([1, 2, 3, 4, 5], 3) should return [3, 4, 5]
# (the last 3 items), but it doesn't. Find and fix the bug.
print(get_last_n_items([1, 2, 3, 4, 5], 3))
