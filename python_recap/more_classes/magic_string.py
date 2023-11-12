def magic_string(list=None):
    if list is None:
        list = []
    list.append("Best School")
    return ",".join(list)

accumulate_list = []
for n in range(11):
    print(magic_string(accumulate_list))
