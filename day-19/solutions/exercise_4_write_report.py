with open("day-19/students.csv") as file:
    lines = file.readlines()

students = []
for line in lines[1:]:
    name, score = line.strip().split(",")
    students.append({"name": name, "score": int(score)})

with open("day-19/exercises_report.txt", "w") as file:
    for student in students:
        result = "PASS" if student["score"] >= 80 else "FAIL"
        file.write(f"{student['name']}: {result}\n")

with open("day-19/exercises_report.txt") as file:
    print(file.read())
