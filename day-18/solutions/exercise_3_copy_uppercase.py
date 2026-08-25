with open("day-17/sample.txt") as infile:
    with open("day-18/exercises_uppercase.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())

with open("day-18/exercises_uppercase.txt") as file:
    print(file.read())
