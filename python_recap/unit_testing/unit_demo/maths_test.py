import unittest
from maths import add, divide, multiply, substract

class TestMaths(unittest.TestCase):
    
    def test_add(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_div(self):
        result = divide(10, 5)
        self.assertEqual(result, 2)
        #use context manager for testing exceptions
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_mul(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_sub(self):
        self.assertEqual(substract(10, 5), 5)
    
if __name__ ==  "__main__":
    unittest.main()