def weight_average(my_list):
    if not my_list:
        return 0
    add , mul  = 0, 0
    
    for tup in my_list:
        add += tup[1]
        mul += tup[0] + tup[1]

    return (mul / add)


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))