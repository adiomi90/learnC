""" letters = ["a", "b", "c", "d", "r", "e", "k", "t"]

for letter in letters:
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

letters.sort()
print(letters)
 """

hello = [
    ("particles", 1),
    ("tikils", 2),
    ("same", 7),
    ("part", 78),
    ("life", 31)
]


hello.sort(key=lambda item: item[1])
print(hello)
