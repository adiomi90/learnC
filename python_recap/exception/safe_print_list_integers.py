"""
def safe_print_list_integers(my_list=None, x=0):
 if not my_list:
        my_list = []
    
    count = 0
    i = 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
        except(IndexError, ValueError) as e:
            print(e)
            break
    print("")
    return count
    
"""
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)

  

my_list = [1, 2, 3, 4, 5]


nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))


























































""" 
count = 0
    try:
        for value in my_list[:x]:
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
    except IndexError:
        pass  # Handle the case when x is bigger than the length of my_list

    print("")  # Print a newline after all integers are printed
    return count

 """