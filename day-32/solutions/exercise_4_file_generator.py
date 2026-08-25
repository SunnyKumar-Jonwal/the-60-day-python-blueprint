def read_lines(path):
    with open(path) as file:
        for line in file:
            yield line.strip()


for line in read_lines("day-17/sample.txt"):
    print(line)
