class lockedClass:
    """
    A class with a locked set attribute in the __slots__
    """

    __slots__ = ("first_name", "age")

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age


person = lockedClass("Particles", 33)
print(person.first_name)
print(person.age)

person.last_name = "Doe"
print(person.last_name)
