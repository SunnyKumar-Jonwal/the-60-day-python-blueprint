with open("day-19/students.csv") as file:
    lines = file.readlines()

students = []
for line in lines[1:]:
    name, score = line.strip().split(",")
    students.append({"name": name, "score": int(score)})

passing = [student["name"] for student in students if student["score"] >= 80]
print(passing)
