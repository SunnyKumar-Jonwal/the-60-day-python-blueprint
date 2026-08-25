class Person:
    def __init__(self, name, notes, ssn):
        self.name = name          # public
        self._notes = notes        # protected (convention only)
        self.__ssn = ssn            # private (name-mangled)

    def show_all(self):
        # TODO: print self.name, self._notes, and self.__ssn -- all accessible
        # from inside the class, regardless of naming convention
        pass


# TODO: create a Person and call show_all()
