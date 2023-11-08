import unittest
from math import pi
from circle1 import circle_area


class CircleAreaTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2), pi * (2**2))
        self.assertAlmostEqual(circle_area(4.4), pi * (4.4**2))
    
    def test_type(self):
        self.assertRaises(TypeError,circle_area, "Particles")
        self.assertRaises(TypeError,circle_area, True)
        self.assertRaises(TypeError, circle_area, 2j + 5)

    def test_value(self):
        self.assertRaises(ValueError,circle_area, -2)

