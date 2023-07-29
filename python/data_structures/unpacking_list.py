number = [1, 2, 3]
first, second, third = number
print(first)
print(second)
print(third)
# list unpacking

numbers = [1, 2, 4, 3, 5, 3, 5]
first, second, *third = numbers
print(first)
print(second)
print(third)
