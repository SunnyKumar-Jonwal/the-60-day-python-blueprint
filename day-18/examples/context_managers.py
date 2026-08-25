with open("day-17/sample.txt") as file:
    contents = file.read()
    print(contents)

with open("day-18/examples_output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

with open("day-18/examples_output.txt") as file:
    print(file.read())

with open("day-17/sample.txt") as infile, open("day-18/examples_output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())

with open("day-18/examples_output.txt") as file:
    print(file.read())
