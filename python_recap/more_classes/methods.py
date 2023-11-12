import datetime
"""class about regular methods, class methods and instance methods"""
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last , pay):
        self._first = first 
        self._last = last
        self._email = first + "-"+ last + "@email.com"
        self._pay = pay
        
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self._first} {self._last}"
    
    def apply_raise(self):
        self._pay = int(self._pay) * float(self.raise_amt)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount     

    @classmethod
    def from_string(cls, string):
        first, last, pay= string.split("-")
        return cls(first, last, pay)       

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-smith-30000"
emp_str_3 = "Jane-Doe-90000"

emp_11 = Employee.from_string(emp_str_1)
emp_22 = Employee.from_string(emp_str_2)
emp_33 = Employee.from_string(emp_str_3)

Employee.set_raise_amount(1.5)
print(emp_11._pay)
emp_11.apply_raise()
print(emp_11._pay)

print(emp_11._email)
print(emp_22._email)



my_date = datetime.date(1990, 5, 11)
print(Employee.is_working(my_date))