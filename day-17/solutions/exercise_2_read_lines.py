file = open("day-17/sample.txt")
for number, line in enumerate(file, start=1):
    print(f"{number}: {line.strip()}")
file.close()
