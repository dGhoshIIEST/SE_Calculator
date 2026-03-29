import unittest
from hex import (
    hex_to_decimal, decimal_to_hex, hex_add,
    hex_subtract, hex_multiply, fifteens_complement, sixteens_complement
)
from exceptions import invalidhexerror


class testhex(unittest.TestCase):

    def test_hex_to_decimal(self):
        self.assertEqual(hex_to_decimal('1A5'), '421')

    def test_hex_to_decimal_zero(self):
        self.assertEqual(hex_to_decimal('0'), '0')

    def test_hex_to_decimal_single(self):
        self.assertEqual(hex_to_decimal('F'), '15')

    def test_hex_to_decimal_lowercase(self):
        self.assertEqual(hex_to_decimal('ff'), '255')

    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex('243'), 'F3')

    def test_decimal_to_hex_zero(self):
        self.assertEqual(decimal_to_hex('0'), '0')

    def test_decimal_to_hex_255(self):
        self.assertEqual(decimal_to_hex('255'), 'FF')

    def test_hex_add(self):
        self.assertEqual(hex_add('1A', '0F'), '29')

    def test_hex_add_with_carry(self):
        self.assertEqual(hex_add('FF', '1'), '100')

    def test_hex_subtract(self):
        self.assertEqual(hex_subtract('1A', '0F'), 'B')

    def test_hex_multiply(self):
        self.assertEqual(hex_multiply('A', '2'), '14')

    def test_fifteens_complement(self):
        self.assertEqual(fifteens_complement('1A5'), 'E5A')

    def test_fifteens_complement_all_f(self):
        self.assertEqual(fifteens_complement('FFF'), '000')

    def test_sixteens_complement(self):
        self.assertEqual(sixteens_complement('1A5'), 'E5B')

    def test_invalid_hex_char(self):
        with self.assertRaises(invalidhexerror):
            hex_to_decimal('1G5')

    def test_invalid_hex_special(self):
        with self.assertRaises(invalidhexerror):
            hex_to_decimal('12#')

    def test_invalid_hex_empty(self):
        with self.assertRaises(invalidhexerror):
            hex_to_decimal('')


if __name__ == "__main__":
    unittest.main()
