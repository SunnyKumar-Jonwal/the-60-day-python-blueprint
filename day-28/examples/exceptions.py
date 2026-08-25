try:
    age_text = "not a number"
    age = int(age_text)
    print(f"Next year you'll be {age + 1}")
except ValueError:
    print("That's not a valid number.")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as error:
    print(f"Index problem: {error}")
except ValueError as error:
    print(f"Value problem: {error}")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Done.")


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    new_balance = withdraw(100, 500)
except ValueError as error:
    print(f"Withdrawal failed: {error}")
