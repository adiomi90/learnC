try:
    age = int(input("Age: "))
    print(age)
except ValueError as ex:
    print(ex)
    print(type(ex))
    print("You didn't enter a valid value")
else:
    print("No exception were thrown")
print("Execption continues")