file = open("day-17/exercises_output.txt", "w")
file.write("Line one\n")
file.write("Line two\n")
file.write("Line three\n")
file.close()

file = open("day-17/exercises_output.txt")
print(file.read())
file.close()
