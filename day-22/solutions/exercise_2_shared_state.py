class Employee:
    company = "Acme Corp"

    def __init__(self, name):
        self.name = name


alice = Employee("Alice")
bob = Employee("Bob")

print(alice.company)
print(bob.company)
