class Person:
    def __init__(self, name, notes, ssn):
        self.name = name
        self._notes = notes
        self.__ssn = ssn

    def show_all(self):
        print(self.name)
        print(self._notes)
        print(self.__ssn)


person = Person("Ada", "VIP client", "000-00-0000")
person.show_all()
