# tempCodeRunnerFile.py
import sys
sys.path.insert(1, r'python_recap\unit_testing\unit_demo\alx_exercise')
from find_max import max_integer
import unittest


class TestMaxInteger(unittest.TestCase):
    def test_order_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        unordered = [3, 2, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begin(self):
        max_at_begining = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begining), 4)
    
    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        ints_and_float = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_float), 15.5)

    def test_strings(self):
        string = "Particles"
        self.assertEqual(max_integer(string), "t")

    def test_list_of_strings(self):
        string_list = ["Particles", "is", "same", "as", "ink"]
        self.assertEqual(max_integer(string_list), "same")

    
    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()