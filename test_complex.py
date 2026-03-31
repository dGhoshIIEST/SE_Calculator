# test_complex.py
import unittest
from complex import (
    parse_complex_string, add_complex, subtract_complex, 
    multiply_complex, divide_complex, compute_magnitude, 
    compute_phase, evaluate_complex_expression
)
import math
class TestComplexArithmetic(unittest.TestCase):

    # --- Parser Tests ---
    def test_parse_complex_string_valid(self):
        c1, op, c2 = parse_complex_string('(3 + 2j) * (5+ 3j)')
        self.assertEqual(c1, '3+2j')
        self.assertEqual(op, '*')
        self.assertEqual(c2, '5+3j')

    def test_parse_complex_string_invalid(self):
        # Boundary Condition: Missing brackets should raise a ValueError
        with self.assertRaises(ValueError):
            parse_complex_string('3+2j * 5+3j')

    # --- Member 2 Tests ---
    def test_add_complex(self):
        # Test normal addition and negative addition
        self.assertEqual(add_complex((3, 2), (5, 3)), (8, 5))
        self.assertEqual(add_complex((0, 0), (5, 3)), (5, 3))
        self.assertEqual(add_complex((1, 0), (0, 1)), (1, 1))
        self.assertEqual(add_complex((2, -3), (-1, 4)), (1, 1))

        # Boundary cases
        self.assertEqual(add_complex((0, 0), (0, 0)), (0, 0))
        self.assertEqual(add_complex((999999, 0), (0, 999999)), (999999, 999999))
        self.assertEqual(add_complex((-1, -1), (-1, -1)), (-2, -2))

        # Invalid input handling
        with self.assertRaises(TypeError):
            add_complex((1,), (2, 3))  # Too few elements
        with self.assertRaises(TypeError):
            add_complex((1, 2, 3), (2, 3))  # Too many elements
        with self.assertRaises(TypeError):
            add_complex((1, 'a'), (2, 3))  # Non-numeric
        with self.assertRaises(TypeError):
            add_complex('not a tuple', (2, 3))

    def test_subtract_complex(self):
        # Test normal subtraction
        self.assertEqual(subtract_complex((5, 3), (3, 2)), (2, 1))
        self.assertEqual(subtract_complex((0, 0), (5, 3)), (-5, -3))
        self.assertEqual(subtract_complex((1, 0), (0, 1)), (1, -1))
        self.assertEqual(subtract_complex((2, -3), (-1, 4)), (3, -7))

        # Boundary cases
        self.assertEqual(subtract_complex((0, 0), (0, 0)), (0, 0))
        self.assertEqual(subtract_complex((999999, 0), (0, 999999)), (999999, -999999))
        self.assertEqual(subtract_complex((-1, -1), (-1, -1)), (0, 0))

        # Invalid input handling
        with self.assertRaises(TypeError):
            subtract_complex((1,), (2, 3))  # Too few elements
        with self.assertRaises(TypeError):
            subtract_complex((1, 2, 3), (2, 3))  # Too many elements
        with self.assertRaises(TypeError):
            subtract_complex((1, 'a'), (2, 3))  # Non-numeric
        with self.assertRaises(TypeError):
            subtract_complex('not a tuple', (2, 3))


    # --- Member 3 Tests ---

    def test_multiply_complex(self):
        # Normal cases
        self.assertEqual(multiply_complex((3, 2), (5, 3)), (9, 19))  # (3+2j)*(5+3j) = (3*5-2*3, 3*3+2*5) = (15-6, 9+10) = (9, 19)
        self.assertEqual(multiply_complex((0, 0), (5, 3)), (0, 0))   # Zero times anything
        self.assertEqual(multiply_complex((1, 0), (0, 1)), (0, 1))   # (1+0j)*(0+1j) = (0, 1)
        self.assertEqual(multiply_complex((2, -3), (-1, 4)), (10, 11)) # (2-3j)*(-1+4j) = (2*-1-(-3)*4, 2*4+(-3)*-1) = (-2+12, 8+3) = (10, 11)

        # Boundary cases
        self.assertEqual(multiply_complex((0, 0), (0, 0)), (0, 0))   # Both zero
        self.assertEqual(multiply_complex((999999, 0), (0, 999999)), (0, 999999*999999))
        self.assertEqual(multiply_complex((-1, -1), (-1, -1)), (0, 2))

        # Invalid input handling
        with self.assertRaises(TypeError):
            multiply_complex((1,), (2, 3))  # Too few elements
        with self.assertRaises(TypeError):
            multiply_complex((1, 2, 3), (2, 3))  # Too many elements
        with self.assertRaises(TypeError):
            multiply_complex((1, 'a'), (2, 3))  # Non-numeric
        with self.assertRaises(TypeError):
            multiply_complex('not a tuple', (2, 3))


    def test_divide_complex(self):
        # Normal cases
        self.assertEqual(divide_complex((3, 2), (5, 3)), (0.6176470588235294, 0.029411764705882353))
        self.assertEqual(divide_complex((0, 0), (5, 3)), (0.0, 0.0))
        self.assertEqual(divide_complex((1, 0), (1, 0)), (1.0, 0.0))
        self.assertEqual(divide_complex((2, -3), (-1, 4)), (-0.8235294117647058, -0.29411764705882354))

        # Boundary cases
        self.assertEqual(divide_complex((0, 0), (0, 1)), (0.0, 0.0))
        self.assertEqual(divide_complex((999999, 0), (0, 999999)), (0.0, -1.0))
        self.assertEqual(divide_complex((-1, -1), (-1, -1)), (1.0, 0.0))

        # Invalid input handling
        with self.assertRaises(TypeError):
            divide_complex((1,), (2, 3))  # Too few elements
        with self.assertRaises(TypeError):
            divide_complex((1, 2, 3), (2, 3))  # Too many elements
        with self.assertRaises(TypeError):
            divide_complex((1, 'a'), (2, 3))  # Non-numeric
        with self.assertRaises(TypeError):
            divide_complex('not a tuple', (2, 3))


    def test_divide_complex_by_zero(self):
        # Test division by zero exception handling
        with self.assertRaises(ValueError):
            divide_complex((1, 2), (0, 0))

    # --- Member 4 Tests ---
    def test_compute_magnitude(self):
    # Test magnitude calculations
        self.assertAlmostEqual(compute_magnitude('3+4j'), 5.0)
        self.assertAlmostEqual(compute_magnitude('1+0j'), 1.0)
        self.assertAlmostEqual(compute_magnitude('0+2j'), 2.0)


    def test_compute_phase(self):
        # Test phase calculations (check against known angles)
        self.assertAlmostEqual(compute_phase('1+0j'), 0.0)
        self.assertAlmostEqual(compute_phase('0+1j'), math.pi/2)
        self.assertAlmostEqual(compute_phase('-1+0j'), math.pi)


    # --- Member 5 Tests (Integration) ---
    def test_evaluate_complex_expression(self):
        # Test the full pipeline from raw string to final output
        pass

if __name__ == "__main__":
    unittest.main()