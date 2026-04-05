import unittest
from calculator import Calculator

class TestArithmetic(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.evaluate("2+3"), 5)

    def test_precedence(self):
        self.assertEqual(self.calc.evaluate("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.calc.evaluate("(2+3)*4"), 20)

    def test_power(self):
        self.assertEqual(self.calc.evaluate("3**2"), 9)

    def test_modulo(self):
        self.assertEqual(self.calc.evaluate("10%3"), 1)

    def test_sqrt(self):
        self.assertEqual(self.calc.evaluate("sqrt(16)"), 4)

    def test_cbrt(self):
        self.assertAlmostEqual(self.calc.evaluate("cbrt(27)"), 3)

    def test_factorial(self):
        self.assertEqual(self.calc.evaluate("5!"), 120)

    def test_log(self):
        self.assertAlmostEqual(self.calc.evaluate("log(100)"), 2)

    def test_floor(self):
        self.assertEqual(self.calc.evaluate("floor(2.7)"), 2)

    def test_ceil(self):
        self.assertEqual(self.calc.evaluate("ceil(2.2)"), 3)

    def test_nested(self):
        self.assertEqual(self.calc.evaluate("2*(3+4)"), 14)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("5/0")


if __name__ == "__main__":
    unittest.main()
