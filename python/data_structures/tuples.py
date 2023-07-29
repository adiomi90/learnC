# read only list is a tuple

point = (12, 34) + (19, 15)
print(point)

point = (1, 2) * 10
print(point)

point = tuple("Hello world")
print(point)

x, y, *z = (10, 12, 29, 25, 25, 15)
print(x)
print(y)
print(z)

if 10 in point:
    print("exist")
