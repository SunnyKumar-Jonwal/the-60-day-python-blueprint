numerator = 10
denominator = 0

try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Cleaning up...")
