def element_at(my_list,idx):
    if idx < 0:
        return None
    elif idx > len(my_list) -1:
        return None
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))


element_at([2, 3, 5, 5, 3, 5, 3, 52], 8)
