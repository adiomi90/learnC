def divisible_by_2(my_list):
    divisible = []
    for n in my_list:
        if n % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible

my_list = [2, 4, 4, 3, 8, 18, 34]
new_list = divisible_by_2(my_list)

i = 0
while(i < len(my_list)):
    print("{:d} {:s} divisble by 2".format(my_list[i], "is" if new_list[i] else "is not"))
    i+=1