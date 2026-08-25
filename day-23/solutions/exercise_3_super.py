class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


manager = Manager("Priya", 95000, 6)
print(manager.name)
print(manager.salary)
print(manager.team_size)
