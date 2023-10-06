try:
    with open("exception_demo.py") as file:
        print("File is opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid number")
except FileNotFoundError:
    print("File not found")
else:
    print("Exception continued")
