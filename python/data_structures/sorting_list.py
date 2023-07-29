numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)


names = [
    ("particles", 20),
    ("sister", 35),
    ("dange", 22),
    ("larger", 45)
]


def sort_item(item):
    return item[1]


names.sort(key=sort_item, reverse=True)
print(names)
