import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(4, -2), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_evaluate_arithmetic_string(self):
        self.assertEqual(self.calc.evaluate("2 + 3 * 4"), 14)


if __name__ == "__main__":
    unittest.main()
