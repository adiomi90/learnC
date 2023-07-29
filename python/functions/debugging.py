def multiply(*number):
    total = 1
    for num in number:
        total *= num
        return total


print("Start")
print(multiply(2, 3, 5, 8))
