import unittest
from calculator import Calculator

class TestBitwise(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_bitwise_and(self):
        self.assertEqual(self.calc.calculate("12 & 10"), 8)

    def test_bitwise_or(self):
        self.assertEqual(self.calc.calculate("12 | 10"), 14)

    def test_bitwise_xor(self):
        self.assertEqual(self.calc.calculate("12 ^ 10"), 6)

    def test_bitwise_lshift(self):
        self.assertEqual(self.calc.calculate("3 << 2"), 12)

    def test_bitwise_rshift(self):
        self.assertEqual(self.calc.calculate("3 >> 1"), 1)

    def test_bitwise_rshift_2(self):
        self.assertEqual(self.calc.calculate("3 >> 2"), 0)

    def test_bitwise_not(self):
        self.assertEqual(self.calc.calculate("~0"), -1)

    def test_mixed_expression(self):
        self.assertEqual(self.calc.calculate("2 + (1 << 3)"), 10)

    def test_bitwise_not_2(self):
        self.assertNotEqual(self.calc.calculate("~0"), 0)

    def test_bit_masking(self):
        self.assertEqual(self.calc.calculate("mask(15, 8)"), 8)

    def test_bit_counting(self):
        self.assertEqual(self.calc.calculate("count_bits(7)"), 3)
        self.assertEqual(self.calc.calculate("count_bits(255)"), 8)

    def test_bit_rotation_left(self):
        self.assertEqual(self.calc.calculate("rotate_left(1, 2)"), 4)
        self.assertEqual(self.calc.calculate("rotate_left(128, 1, 8)"), 1)

    def test_bit_rotation_right(self):
        self.assertEqual(self.calc.calculate("rotate_right(4, 2)"), 1)
        self.assertEqual(self.calc.calculate("rotate_right(1, 1, 8)"), 128)

    def test_mixed_expression_2(self):
        self.assertEqual(self.calc.calculate("count_bits((2 + 2) << 1)"), 1)

    def test_negative_shift_error(self):
        result = self.calc.calculate("8 >> -1")
        self.assertTrue("Error" in str(result))

if __name__ == "__main__":
    unittest.main()