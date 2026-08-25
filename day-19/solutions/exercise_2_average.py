with open("day-19/students.csv") as file:
    lines = file.readlines()

scores = [int(line.strip().split(",")[1]) for line in lines[1:]]
average = sum(scores) / len(scores)

print(f"{average:.1f}")
