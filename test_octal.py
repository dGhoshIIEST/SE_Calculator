import unittest
from octal import (
    octal_to_decimal, decimal_to_octal, octal_add,
    octal_subtract, octal_multiply, sevens_complement, eights_complement
)
from exceptions import invalidoctalerror


class testoctal(unittest.TestCase):

    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal('247'), '167')

    def test_octal_to_decimal_zero(self):
        self.assertEqual(octal_to_decimal('0'), '0')

    def test_octal_to_decimal_seven(self):
        self.assertEqual(octal_to_decimal('7'), '7')

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal('167'), '247')

    def test_decimal_to_octal_zero(self):
        self.assertEqual(decimal_to_octal('0'), '0')

    def test_decimal_to_octal_eight(self):
        self.assertEqual(decimal_to_octal('8'), '10')

    def test_octal_add(self):
        self.assertEqual(octal_add('12', '15'), '27')

    def test_octal_add_with_carry(self):
        self.assertEqual(octal_add('77', '1'), '100')

    def test_octal_subtract(self):
        self.assertEqual(octal_subtract('27', '15'), '12')

    def test_octal_multiply(self):
        self.assertEqual(octal_multiply('3', '4'), '14')

    def test_sevens_complement(self):
        self.assertEqual(sevens_complement('247'), '530')

    def test_sevens_complement_zero(self):
        self.assertEqual(sevens_complement('000'), '777')

    def test_eights_complement(self):
        self.assertEqual(eights_complement('247'), '531')

    def test_invalid_octal_digit_8(self):
        with self.assertRaises(invalidoctalerror):
            octal_to_decimal('128')

    def test_invalid_octal_digit_9(self):
        with self.assertRaises(invalidoctalerror):
            octal_to_decimal('19')

    def test_invalid_octal_letters(self):
        with self.assertRaises(invalidoctalerror):
            octal_to_decimal('12A')

    def test_invalid_octal_empty(self):
        with self.assertRaises(invalidoctalerror):
            octal_to_decimal('')


if __name__ == "__main__":
    unittest.main()
