""" items = [
    ("first_product", 90),
    ("second_product", 80),
    ("third product", 45)
]

prices = []
for product, item in items:
    prices.append(item)

print(prices) """

items = [
    ("product1", 19),
    ("product2", 11),
    ("product3", 27)
]


x = list(map(lambda item: item[1], items))
print(x)
