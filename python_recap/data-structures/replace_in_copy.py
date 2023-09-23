def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list)-1:
        return my_list.copy()
    else:
        list = my_list.copy()
        list[idx] = element
        return list
    
mylist = [2,3,4,2]
result = new_in_list(mylist , 2, 44)
print(result)
print(mylist)