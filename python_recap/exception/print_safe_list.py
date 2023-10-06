def safe_print_list(my_list=None, x=0):
    if not my_list:
        my_list = []
    count = 0
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            i += 1
            count += 1
        except (ValueError, IndexError):
            break
    print("")
    return count


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))


""" 
if not my_list:
      my_list = []
   
   count = 0
   i = 0

   while i < x:
      try:
         print(my_list[i], end="")
         count += 1
         i += 1
      except IndexError:
         break
   print("")
   return count """
