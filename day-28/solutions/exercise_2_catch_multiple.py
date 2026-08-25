def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        print("Index out of range")
        return None
    except TypeError:
        print("Index must be an int")
        return None


items = ["a", "b", "c"]
get_item(items, 10)
get_item(items, "x")
