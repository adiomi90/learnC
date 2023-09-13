import random
number = random.randint(-10000, 10000)

if number < 0:
    mod = number % -10
else:
    mod = number % 10

print(f"last number of {number} is {mod}")


# YOUR CODE HERE
