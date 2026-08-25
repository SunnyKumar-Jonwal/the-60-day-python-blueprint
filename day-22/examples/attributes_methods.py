class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year):
        age = current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_valid_age(age):
        return age >= 0


rex = Dog("Rex", 3)
buddy = Dog("Buddy", 5)

print(rex.species)
print(buddy.species)
print(rex.name)
print(buddy.name)

puppy = Dog.from_birth_year("Puppy", 2021, 2024)
print(puppy.age)

print(Dog.is_valid_age(3))
print(Dog.is_valid_age(-1))
