try:
    with open("") as file:
        age = int(input(""))
        xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown")
