def print_reversed_list_integer(mylist=[]):
    if mylist is None:
        return
    for n in reversed(mylist):
        print("{}".format(n))



print_reversed_list_integer([5,4,7,9,14,3])