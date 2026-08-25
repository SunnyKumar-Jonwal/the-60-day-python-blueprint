def countdown(start):
    current = start
    while current >= 1:
        yield current
        current -= 1


for number in countdown(5):
    print(number)
