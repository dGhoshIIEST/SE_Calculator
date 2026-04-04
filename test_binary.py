import unittest
from binary import (
    binary_to_decimal, decimal_to_binary, binary_add,
    binary_subtract, binary_multiply, ones_complement, twos_complement
)
from exceptions import invalidbinaryerror


class testbinary(unittest.TestCase):

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1010'), '10')

    def test_binary_to_decimal_zero(self):
        self.assertEqual(binary_to_decimal('0'), '0')

    def test_binary_to_decimal_one(self):
        self.assertEqual(binary_to_decimal('1'), '1')

    def test_binary_to_decimal_large(self):
        self.assertEqual(binary_to_decimal('11111111'), '255')

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary('10'), '1010')

    def test_decimal_to_binary_zero(self):
        self.assertEqual(decimal_to_binary('0'), '0')

    def test_decimal_to_binary_one(self):
        self.assertEqual(decimal_to_binary('1'), '1')

    def test_binary_add(self):
        self.assertEqual(binary_add('011', '010'), '101')

    def test_binary_add_with_carry(self):
        self.assertEqual(binary_add('111', '001'), '1000')

    def test_binary_subtract(self):
        self.assertEqual(binary_subtract('110', '010'), '100')

    def test_binary_multiply(self):
        self.assertEqual(binary_multiply('101', '11'), '1111')

    def test_ones_complement(self):
        self.assertEqual(ones_complement('1010'), '0101')

    def test_ones_complement_all_zeros(self):
        self.assertEqual(ones_complement('0000'), '1111')

    def test_ones_complement_all_ones(self):
        self.assertEqual(ones_complement('1111'), '0000')

    def test_twos_complement(self):
        self.assertEqual(twos_complement('1010'), '0110')

    def test_twos_complement_one(self):
        self.assertEqual(twos_complement('0001'), '1111')

    def test_invalid_binary(self):
        with self.assertRaises(invalidbinaryerror):
            binary_to_decimal('1021')

    def test_invalid_binary_letters(self):
        with self.assertRaises(invalidbinaryerror):
            binary_to_decimal('10a1')

    def test_invalid_binary_empty(self):
        with self.assertRaises(invalidbinaryerror):
            binary_to_decimal('')


if __name__ == "__main__":
    unittest.main()
