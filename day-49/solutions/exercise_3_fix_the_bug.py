def get_last_n_items(items, n):
    return items[-n:]  # fixed: no upper bound needed, that -1 was dropping the last item


print(get_last_n_items([1, 2, 3, 4, 5], 3))
