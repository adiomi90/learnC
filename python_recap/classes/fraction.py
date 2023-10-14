from typing import Any


class Fraction:
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int, "Integers only please"
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self, other):
        new_num = self.num * other.denom + self.denom * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __sub__(self, other):
        new_num = self.num * other.denom - self.denom * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __div__(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return Fraction(new_num, new_denom)
    
    def __truediv__(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return Fraction(new_num, new_denom)

    def inverse(self):
        return Fraction(self.denom, self.num)
    
    def __eq__(self, other):
        return self.num * other.denom == self.denom * other.num
    
    