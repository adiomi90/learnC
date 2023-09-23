def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
    

result = replace_in_list([2, 3, 4, 3, 5, 3], 2, 399)
print(result)   