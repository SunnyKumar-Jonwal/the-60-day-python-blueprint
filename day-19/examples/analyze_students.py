with open("day-19/students.csv") as file:
    lines = file.readlines()

students = []
for line in lines[1:]:
    name, score = line.strip().split(",")
    students.append({"name": name, "score": int(score)})

print(students)

scores = [student["score"] for student in students]
average = sum(scores) / len(scores)
top_student = max(students, key=lambda s: s["score"])

print(f"Average score: {average:.1f}")
print(f"Top student: {top_student['name']} ({top_student['score']})")

with open("day-19/summary.txt", "w") as file:
    file.write(f"Average score: {average:.1f}\n")
    file.write(f"Top student: {top_student['name']} ({top_student['score']})\n")
