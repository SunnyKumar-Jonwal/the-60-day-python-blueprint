items = ["a", "b", "c"]
iterator = iter(items)

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)
