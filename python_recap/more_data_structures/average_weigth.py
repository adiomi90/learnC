def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    mul, addition = 0, 0

    for tupl in my_list:
        mul += tupl[0] * tupl[1]
        addition += tupl[1]

    return (mul / addition)



my_list = []
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
    