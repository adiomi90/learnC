def say_my_name(first_name, last_name=""):
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    return f"My name is {first_name} {last_name}" 

print(say_my_name("John", "Smith"))
print(say_my_name("Walter", "White"))
print(say_my_name("Bob"))
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)