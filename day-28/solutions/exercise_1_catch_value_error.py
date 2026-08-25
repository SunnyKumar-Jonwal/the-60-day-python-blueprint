def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


print(safe_int("42"))
print(safe_int("not a number"))
