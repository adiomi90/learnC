class Employee:
    """An employee class"""

    raise_amt = 10

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self._first, self._last)
    
    @property
    def fullname(self):
        return "{} {}".format(self._first, self._last)
    
    def apply_raise(self):
        self._pay = int(self._pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmet

emp_1 = Employee("Max", "Ink", 50000)
emp_2 = Employee("Ink", "Baby", 3000)


emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"


new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.fullname)








""" Employee.set_raise_amt(20)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt) """



