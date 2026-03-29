import unittest
from fraction import add_fraction, sub_fraction, mul_fraction, div_fraction
from exceptions import zerodenominatorerror, invalidfractionerror


class testfraction(unittest.TestCase):

    def test_fraction_add(self):
        self.assertEqual(add_fraction('1/2', '1/4'), '3/4')

    def test_fraction_add_same_denom(self):
        self.assertEqual(add_fraction('1/5', '2/5'), '3/5')

    def test_fraction_add_simplify(self):
        self.assertEqual(add_fraction('1/4', '1/4'), '1/2')

    def test_fraction_add_whole_result(self):
        self.assertEqual(add_fraction('1/2', '1/2'), '1')

    def test_fraction_add_negative(self):
        self.assertEqual(add_fraction('-1/2', '1/4'), '-1/4')

    def test_fraction_add_zero(self):
        self.assertEqual(add_fraction('0/5', '3/7'), '3/7')

    def test_fraction_sub(self):
        self.assertEqual(sub_fraction('3/4', '1/4'), '1/2')

    def test_fraction_sub_negative_result(self):
        self.assertEqual(sub_fraction('1/4', '3/4'), '-1/2')

    def test_fraction_sub_same(self):
        self.assertEqual(sub_fraction('3/5', '3/5'), '0')

    def test_fraction_mul(self):
        self.assertEqual(mul_fraction('2/3', '3/4'), '1/2')

    def test_fraction_mul_by_zero(self):
        self.assertEqual(mul_fraction('2/3', '0/5'), '0')

    def test_fraction_mul_whole_number(self):
        self.assertEqual(mul_fraction('1/2', '2'), '1')

    def test_fraction_div(self):
        self.assertEqual(div_fraction('1/2', '1/4'), '2')

    def test_fraction_div_result_fraction(self):
        self.assertEqual(div_fraction('1/3', '2/3'), '1/2')

    def test_fraction_div_by_zero(self):
        with self.assertRaises(zerodenominatorerror):
            div_fraction('1/2', '0/3')

    def test_fraction_zero_denominator(self):
        with self.assertRaises(zerodenominatorerror):
            add_fraction('1/0', '1/2')

    def test_fraction_invalid_format(self):
        with self.assertRaises(invalidfractionerror):
            add_fraction('abc', '1/2')

    def test_fraction_invalid_format_multiple_slashes(self):
        with self.assertRaises(invalidfractionerror):
            add_fraction('1/2/3', '1/2')


if __name__ == "__main__":
    unittest.main()
