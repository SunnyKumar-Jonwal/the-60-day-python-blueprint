class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    # TODO: add a @celsius.setter that raises ValueError if value < -273.15,
    # otherwise sets self._celsius = value


# TODO: create a Temperature(25), then set .celsius = 30, then print .celsius
