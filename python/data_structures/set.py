""" numbers = [1, 2, 2, 4, 5, 3]
uniques = set(numbers)
print(uniques)

second = {1, 4}
second.add(5)
second.remove(4)
len(second) """


first_set = {1, 2, 3, 4}
second_set = {1, 3, 5, 7}

print("union", first_set | second_set)
print("intersection ", first_set & second_set)
print("difference", first_set - second_set)
print("difference", second_set - first_set)
print("symetric difference", first_set ^ second_set)
