""" numbers = [1, 2, 3]
print(*numbers)

values = list(range(10))
valu = [*range(10)]
print(valu)
 """

first = {"x": 1}
second = {"x": 10, "y": 2}
third = {**first, **second, "z": 1}
print(third)

part = [1, 2, 3]
par2 = [1, 3, 4]
part2 = part + par2
print(part2)
