def make_power_function(exponent):
    def power(base):
        return base**exponent

    return power


square = make_power_function(2)
cube = make_power_function(3)
print(square(4))
print(cube(2))
