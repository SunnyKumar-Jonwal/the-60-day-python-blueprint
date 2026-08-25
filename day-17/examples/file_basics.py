file = open("day-17/sample.txt")
contents = file.read()
file.close()
print(contents)

file = open("day-17/sample.txt")
first_line = file.readline()
file.close()
print(repr(first_line))

file = open("day-17/sample.txt")
lines = file.readlines()
file.close()
print(lines)

file = open("day-17/sample.txt")
for line in file:
    print(line.strip())
file.close()

file = open("day-17/examples_output.txt", "w")
file.write("First line\n")
file.write("Second line\n")
file.close()

file = open("day-17/examples_output.txt", "a")
file.write("Third line, appended\n")
file.close()

file = open("day-17/examples_output.txt")
print(file.read())
file.close()
