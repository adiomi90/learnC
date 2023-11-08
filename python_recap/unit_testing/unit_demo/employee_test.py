import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("Set up")
        self.emp_1 = Employee("Max", "Ink", 400)
        self.emp_2 = Employee("Tik", "Part", 700)

    def tearDown(self):
        print("Tear Down")
        pass

    def test_email(self):
        print("test email")
        self.assertEqual(self.emp_1.email, "Max.Ink@email.com")
        self.assertEqual(self.emp_2.email, "Tik.Part@email.com")

        self.emp_1._first = "Sick"
        self.emp_2._first = "Ti"

        self.assertEqual(self.emp_1.email, "Sick.Ink@email.com")
        self.assertEqual(self.emp_2.email, "Ti.Part@email.com")

    def test_apply_raise(self):
        print("test raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1._pay, 4000)
        self.assertEqual(self.emp_2._pay, 7000)

    def test_full_name(self):
        print("test full name")
        self.assertEqual(self.emp_1.fullname,"Max Ink")
        self.assertEqual(self.emp_2.fullname,"Tik Part")
if __name__ == "__main__":
    unittest.main()