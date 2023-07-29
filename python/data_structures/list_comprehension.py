items = [
    ("Product1", 10),
    ("Product", 9),
    ("Product", 12),
    ("Product", 80),
    ("Product", 19),
    ("Product", 50),
]
# list comprehension
# use an if statement to filter the list
prices = [item[1] for item in items if item[1] > 10]
print(prices)
