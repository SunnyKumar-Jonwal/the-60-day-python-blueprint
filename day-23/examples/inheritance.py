class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


rex = Dog("Rex", "Labrador")
whiskers = Cat("Whiskers")

rex.speak()
whiskers.speak()
print(rex.name)
print(rex.breed)

print(isinstance(rex, Dog))
print(isinstance(rex, Animal))
print(isinstance(rex, Cat))
