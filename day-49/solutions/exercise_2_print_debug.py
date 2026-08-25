def find_max(numbers):
    max_value = numbers[0]  # fixed: start from the first item, not 0
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


print(find_max([-5, -2, -10]))
