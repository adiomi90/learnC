letters = ["a", "a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "-")

print(letters)

# remove
# letters.pop()

letter = [letter for letter in letters if letter != "a"]
print(letter)

# delete removes a range of items
del letter[0:3]

# remove all methos using clear
# letters.clear


letters = ["a", "b", "c"]
letters.count("c")
if "d" in letters:
    print(letters.index("d"))
