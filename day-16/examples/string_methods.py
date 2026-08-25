text = "Hello World"
print(text.upper())
print(text.lower())
print(text.title())
print("hello".capitalize())

padded = "   hello   "
print(padded.strip())
print(padded.lstrip())
print(padded.rstrip())

sentence = "Learn Python in 60 Days"
print(sentence.find("Python"))
print("Python" in sentence)
print(sentence.startswith("Learn"))
print(sentence.endswith("Days"))

csv_line = "Ada,30,London"
parts = csv_line.split(",")
print(parts)

words = ["Learn", "Python", "fast"]
print(" ".join(words))

print("I like cats".replace("cats", "dogs"))
