from math import  pi
    
def circle_area(r):
    if isinstance(r, bool):
        raise TypeError("must be an integer")
    if not isinstance(r, (int, float)):
        raise TypeError("radius shoud be an integer or float")
    if r < 0:
        raise ValueError("the radius shoud be positive number")
    return pi * (r **2)

"""     radii = [2, 0 , -3, 2 + 5j, True, "radius"]
    message = "Area of circles with r = {radius} is {area}"
    for r in radii:
        A = circle_area(r)
        print(message.format(radius=r,area=A))  """
    #Test function
