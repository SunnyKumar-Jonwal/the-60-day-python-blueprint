class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age}.")


rex = Dog("Rex", "Labrador", 3)
buddy = Dog("Buddy", "Poodle", 5)

print(rex.name)
print(buddy.name)
rex.bark()
buddy.bark()

rex.have_birthday()
print(buddy.age)
