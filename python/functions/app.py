"""
    Greet: the name of the function
    Documentation: to learn functions
"""


def greet():
    print("Hi there")
    print("Welcome onboard")


greet()


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Maxwell")
print(message)
file = open("content.txt", "w")
file.write(message)
