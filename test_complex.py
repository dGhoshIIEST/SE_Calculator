import unittest
import cmath
from complex import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = ComplexCalculator()

     # 1. NORMAL CASES
    def test_add(self):
        self.assertEqual(self.calc.add(complex(3, 2), complex(5, 3)), complex(8, 5))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(complex(3, 2), complex(5, 3)), complex(-2, -1))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(complex(1, 2), complex(3, 4)), complex(-5, 10))

    def test_divide(self):
        self.assertEqual(self.calc.divide(complex(10, 5), complex(2, 1)), complex(5, 0))

    def test_magnitude(self):
        self.assertEqual(self.calc.get_magnitude(complex(3, 4)), 5.0)

    def test_phase(self):
        self.assertAlmostEqual(self.calc.get_phase(complex(0, 1)), cmath.pi / 2)

    def test_parse_and_calculate_normal(self):
        result = self.calc.parse_and_calculate('(3+2j)*(5+3j)')
        self.assertEqual(result, complex(9, 19))

    # 2. BOUNDARY CONDITIONS
    def test_boundary_zeros(self):
        # Adding zeros
        self.assertEqual(self.calc.add(complex(0, 0), complex(0, 0)), complex(0, 0))
        
    def test_boundary_pure_imaginary(self):
        # (2j) * (3j) = -6
        self.assertEqual(self.calc.multiply(complex(0, 2), complex(0, 3)), complex(-6, 0))

    def test_boundary_negative_parsing(self):
        # Parsing strings with heavily negative components
        result = self.calc.parse_and_calculate('(-3-2j)+(-5-3j)')
        self.assertEqual(result, complex(-8, -5))

    def test_boundary_extra_spaces_parsing(self):
        # Parser should strip all spaces and still work
        result = self.calc.parse_and_calculate(' (  3 + 2j ) * ( 5 + 3j ) ')
        self.assertEqual(result, complex(9, 19))

    # 3. INVALID INPUT HANDLING
    def test_invalid_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(complex(5, 5), complex(0, 0))

    def test_invalid_parse_missing_parentheses(self):
        with self.assertRaises(ValueError):
            self.calc.parse_and_calculate('3+2j * 5+3j') # Missing parentheses around the numbers

    def test_invalid_parse_garbage_characters(self):
        # Testing our re.fullmatch fix!
        with self.assertRaises(ValueError):
            self.calc.parse_and_calculate('(3+2j)*(5+3j)hello')

    def test_invalid_parse_bad_number_format(self):
        # Parentheses are right, but 'a' is not a number
        with self.assertRaises(ValueError):
            self.calc.parse_and_calculate('(a+2j)*(5+3j)')

    def test_invalid_parse_unknown_operator(self):
        # Using '^' instead of a valid math operator
        with self.assertRaises(ValueError):
            self.calc.parse_and_calculate('(3+2j)^(5+3j)')


if __name__ == '__main__':
    unittest.main()