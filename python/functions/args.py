def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(2, 4, 2, 55, 3))
