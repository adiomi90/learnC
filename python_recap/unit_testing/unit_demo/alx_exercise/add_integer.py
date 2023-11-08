def add_integer(a, b=98):
    if not (isinstance(a, (int,float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    
    return int(a) + int(b)




print(add_integer(2,"same"))