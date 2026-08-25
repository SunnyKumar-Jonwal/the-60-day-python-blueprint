class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


rex = Dog()
whiskers = Cat()

print(isinstance(rex, Dog))
print(isinstance(rex, Animal))
print(isinstance(rex, Cat))
print(isinstance(whiskers, Animal))
