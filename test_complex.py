import unittest
import cmath
from complex import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):
    
    def setUp(self):
        # This runs before every single test
        self.calc = ComplexCalculator()

    def test_add(self):
        # Normal case: (3+2j) + (5+3j) = (8+5j)
        self.assertEqual(self.calc.add(complex(3, 2), complex(5, 3)), complex(8, 5))

    def test_subtract(self):
        # Normal case: (3+2j) - (5+3j) = (-2-1j)
        self.assertEqual(self.calc.subtract(complex(3, 2), complex(5, 3)), complex(-2, -1))

    def test_multiply(self):
        # Normal case: matches the specific example in your lab manual!
        self.assertEqual(self.calc.multiply(complex(1, 2), complex(3, 4)), complex(-5, 10))

    def test_divide(self):
        # Normal case
        self.assertEqual(self.calc.divide(complex(10, 5), complex(2, 1)), complex(5, 0))

    def test_divide_by_zero(self):
        # Invalid input handling (Boundary condition)
        with self.assertRaises(ValueError):
            self.calc.divide(complex(5, 5), complex(0, 0))

    def test_magnitude(self):
        # The magnitude of a 3-4-5 right triangle
        self.assertEqual(self.calc.get_magnitude(complex(3, 4)), 5.0)

    def test_phase(self):
        # Phase of an imaginary number pointing straight up (90 degrees or pi/2)
        # We use assertAlmostEqual for floats to avoid tiny rounding errors
        self.assertAlmostEqual(self.calc.get_phase(complex(0, 1)), cmath.pi / 2)
    
    def test_parse_and_calculate_multiply(self):
        # Testing the exact string format from the lab manual
        # (3+2j) * (5+3j) = (15 + 9j + 10j - 6) = (9+19j)
        result = self.calc.parse_and_calculate('(3+2j)*(5+3j)')
        self.assertEqual(result, complex(9, 19))

    def test_parse_invalid_format(self):
        # Testing our error handling for bad inputs
        with self.assertRaises(ValueError):
            self.calc.parse_and_calculate('3+2j * 5+3j') # Missing parentheses

if __name__ == '__main__':
    unittest.main()