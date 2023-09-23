def no_c(my_string):
    new_string = [n for n in my_string if n != "c" and n != "C"]
    return "".join(new_string)



print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))