def max_integer(my_list):
    if len(my_list) == 0:
        return None
    
    max_number = 0
    for n in my_list:
        if n > max_number:
            max_number = n
    return max_number

print(max_integer([2,5,3,8,24,98,2,78,34]))

