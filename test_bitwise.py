import unittest
from bitwise import (
    bitwise_and, bitwise_or, bitwise_xor, bitwise_not,
    left_shift, right_shift, bit_count, bit_mask,
    left_rotate, right_rotate
)


class testbitwise(unittest.TestCase):

    def test_bitwise_and(self):
        self.assertEqual(bitwise_and('5', '3'), '1')

    def test_bitwise_and_zero(self):
        self.assertEqual(bitwise_and('5', '0'), '0')

    def test_bitwise_and_same(self):
        self.assertEqual(bitwise_and('7', '7'), '7')

    def test_bitwise_or(self):
        self.assertEqual(bitwise_or('5', '3'), '7')

    def test_bitwise_or_zero(self):
        self.assertEqual(bitwise_or('5', '0'), '5')

    def test_bitwise_xor(self):
        self.assertEqual(bitwise_xor('5', '3'), '6')

    def test_bitwise_xor_same(self):
        self.assertEqual(bitwise_xor('5', '5'), '0')

    def test_bitwise_not(self):
        self.assertEqual(bitwise_not('5'), '-6')

    def test_bitwise_not_zero(self):
        self.assertEqual(bitwise_not('0'), '-1')

    def test_left_shift(self):
        self.assertEqual(left_shift('3', '2'), '12')

    def test_left_shift_zero(self):
        self.assertEqual(left_shift('5', '0'), '5')

    def test_left_shift_negative_amount(self):
        with self.assertRaises(ValueError):
            left_shift('5', '-1')

    def test_right_shift(self):
        self.assertEqual(right_shift('16', '2'), '4')

    def test_right_shift_zero(self):
        self.assertEqual(right_shift('5', '0'), '5')

    def test_right_shift_negative_amount(self):
        with self.assertRaises(ValueError):
            right_shift('5', '-1')

    def test_bit_count(self):
        self.assertEqual(bit_count('7'), '3')

    def test_bit_count_zero(self):
        self.assertEqual(bit_count('0'), '0')

    def test_bit_count_power_of_two(self):
        self.assertEqual(bit_count('8'), '1')

    def test_bit_mask(self):
        self.assertEqual(bit_mask('255', '15'), '15')

    def test_left_rotate(self):
        res = left_rotate(str(0b1100), '1', '4')
        self.assertEqual(res, '0b1001')

    def test_right_rotate(self):
        res = right_rotate(str(0b1100), '1', '4')
        self.assertEqual(res, '0b110')

    def test_non_integer_and(self):
        with self.assertRaises(TypeError):
            bitwise_and('abc', '3')

    def test_non_integer_not(self):
        with self.assertRaises(TypeError):
            bitwise_not('3.5')


if __name__ == "__main__":
    unittest.main()
