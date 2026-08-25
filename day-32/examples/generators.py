def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1


for number in count_up(3):
    print(number)

gen = count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))

squares_gen = (n * n for n in range(5))
for square in squares_gen:
    print(square)


def read_large_file_lines(path):
    with open(path) as file:
        for line in file:
            yield line.strip()


for line in read_large_file_lines("day-17/sample.txt"):
    print(line)
