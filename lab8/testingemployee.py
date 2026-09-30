import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    # test template, instant of the class
    def setUp(self):
        self.emp1 = Employee("Peter", "Pan", 90000)

    # test if email format is working properly
    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "ppan@email.com")

    # test full name
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

    # test raise
    def test_apply_raise(self):
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.salary, 94500)
if __name__ =="__main__":
    unittest.main()