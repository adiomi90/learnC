from math import pi


def circle_area(radius):
    if isinstance(radius, bool):
        raise TypeError("must be an integer")
    if not isinstance(radius, (int, float)):
        raise TypeError("must be an integer or float")
    if radius < 0:
        raise ValueError("radius can not be zero")
    return pi * (radius ** 2)

""" 
message = "Area of a circle with radius {radius} is {Area}"
radii = [2, 7.2, 3 + 5j, -8, True,"particles"]

for radius in radii:
    area = circle_area(radius)
    print(message.format(radius=radius, Area=area)) """