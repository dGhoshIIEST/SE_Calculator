import unittest
import math
from complex import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):

    def setUp(self):
        # This creates a new calculator object before each test runs
        self.calc = ComplexCalculator()

    # --- NORMAL CASES ---
    def test_addition(self):
        # (1+2j) + (2+3j) = 3+5j
        result = self.calc.evaluate("(1+2j)+(2+3j)")
        self.assertEqual(result, "3.0+5.0j")

    def test_subtraction(self):
        # (5+5j) - (2+1j) = 3+4j
        result = self.calc.evaluate("(5+5j)-(2+1j)")
        self.assertEqual(result, "3.0+4.0j")

    def test_multiplication(self):
        # (1+2j) * (3+4j) = -5+10j
        result = self.calc.evaluate("(1+2j)*(3+4j)")
        self.assertEqual(result, "-5.0+10.0j")

    def test_division(self):
        # (10+5j) / (2+0j) = 5+2.5j
        result = self.calc.evaluate("(10+5j)/(2+0j)")
        self.assertEqual(result, "5.0+2.5j")

    def test_magnitude(self):
        # Magnitude of 3+4j is exactly 5.0 (Pythagorean triple: 3^2 + 4^2 = 5^2)
        result = self.calc.evaluate("mag(3+4j)")
        self.assertEqual(result, "5.0")

    def test_phase(self):
        # Phase of 0+1j is exactly pi/2 (90 degrees)
        result = self.calc.evaluate("phase(0+1j)")
        # Since float comparison can be tricky, we round it for testing
        self.assertEqual(round(float(result), 4), round(math.pi / 2, 4))

    # --- BOUNDARY CONDITIONS & INVALID INPUTS ---
    def test_divide_by_zero(self):
        # The system must catch dividing by zero and raise a ValueError
        with self.assertRaises(ValueError) as context:
            self.calc.evaluate("(5+5j)/(0+0j)")
        self.assertTrue("Division by zero" in str(context.exception))

    def test_invalid_string_format(self):
        # Testing what happens if the user types complete garbage
        with self.assertRaises(ValueError):
            self.calc.evaluate("hello_world")

    def test_missing_parentheses(self):
        # The regex strictly expects parentheses. Missing them should fail.
        with self.assertRaises(ValueError):
            self.calc.evaluate("3+2j*5+3j")

    def test_invalid_operator(self):
        # Testing an operator that isn't supported by the regex
        with self.assertRaises(ValueError):
            self.calc.evaluate("(3+2j)^(5+3j)")

if __name__ == "__main__":
    unittest.main()