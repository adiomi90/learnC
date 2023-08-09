class Employee:
    def greet(self):
        print("Hello Employee")

class Person:
    def greet(self):
        print("Hello Person")

class Manager(Employee, Person):
    pass

manager = Manager()
print(manager.greet())



