file = open("day-17/exercises_output.txt", "a")
file.write("Line four, appended\n")
file.close()

file = open("day-17/exercises_output.txt")
print(file.read())
file.close()
