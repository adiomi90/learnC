import unittest
from circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #test area when radius >= 0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * (2.1 **2))
    

    def test_value(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, 2 + 5j)
        self.assertRaises(TypeError, circle_area, "hello")
        self.assertRaises(TypeError, circle_area, True)


