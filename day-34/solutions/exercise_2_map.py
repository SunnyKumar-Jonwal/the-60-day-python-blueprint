celsius_temps = [0, 20, 37, 100]

fahrenheit_temps = list(map(lambda c: c * 9 / 5 + 32, celsius_temps))
print(fahrenheit_temps)
