import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("2 1 -")
        self.assertEqual(1, result)
    def test_multpily(self):
        result = rpn.calculate("3 4 *")
        self.assertEqual(12, result)
    def test_divide(self):
        result = rpn.calculate("9 3 /")
        self.assertEqual(3.0, result)
    def test_exponentiation(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27.0, result)
