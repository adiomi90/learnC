items = [
    ("particles", 1),
    ("tikils", 2),
    ("sickIn", 3)
]

result = list(filter(lambda item: item[1] > 2, items))
print(result)
