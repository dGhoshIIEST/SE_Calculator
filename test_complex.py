import unittest
from complex import (
    add_complex, subtract_complex, multiply_complex,
    divide_complex, magnitude, phase
)
from exceptions import invalidcomplexerror


class testcomplex(unittest.TestCase):

    def test_complex_add(self):
        self.assertEqual(add_complex('1+2j', '3+4j'), '4+6j')

    def test_complex_add_negative_imag(self):
        self.assertEqual(add_complex('3+2j', '1-4j'), '4-2j')

    def test_complex_add_real_only(self):
        self.assertEqual(add_complex('5', '3'), '8')

    def test_complex_sub(self):
        self.assertEqual(subtract_complex('5+3j', '2+1j'), '3+2j')

    def test_complex_sub_zero(self):
        self.assertEqual(subtract_complex('3+2j', '3+2j'), '0')

    def test_complex_mul(self):
        self.assertEqual(multiply_complex('1+2j', '3+4j'), '-5+10j')

    def test_complex_mul_real(self):
        self.assertEqual(multiply_complex('2', '3+1j'), '6+2j')

    def test_complex_mul_by_zero(self):
        self.assertEqual(multiply_complex('3+2j', '0'), '0')

    def test_complex_div(self):
        res = divide_complex('4+2j', '1+1j')
        self.assertEqual(res, '3-1j')

    def test_complex_div_by_zero(self):
        with self.assertRaises(ValueError):
            divide_complex('3+2j', '0')

    def test_magnitude(self):
        self.assertEqual(magnitude('3+4j'), '5.0')

    def test_magnitude_real(self):
        self.assertEqual(magnitude('5'), '5.0')

    def test_magnitude_imaginary(self):
        self.assertEqual(magnitude('3j'), '3.0')

    def test_phase(self):
        self.assertEqual(phase('1+1j'), '45.0')

    def test_phase_real_positive(self):
        self.assertEqual(phase('5'), '0.0')

    def test_invalid_complex(self):
        with self.assertRaises(invalidcomplexerror):
            add_complex('abc', '1+2j')


if __name__ == "__main__":
    unittest.main()
