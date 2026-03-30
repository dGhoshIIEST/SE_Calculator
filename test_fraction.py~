import unittest
from fraction import parse_fraction, Fraction
from exceptions import InvalidInputError, InvalidFormatError, InvalidFractionError
from test_calculator import TestCalculator

class TestFractionParsing(unittest.TestCase):
    def test_invalid_type(self):
        f = Fraction(1, 2)
        with self.assertRaises(InvalidInputError):
            f + 5

    def test_valid_parse(self):
        self.assertEqual(str(parse_fraction("1/2")), "1/2")
        self.assertEqual(str(parse_fraction(" 2/4 ")), "1/2")  # simplification

    def test_invalid_input_type(self):
        with self.assertRaises(InvalidInputError):
            parse_fraction(123)

    def test_invalid_format(self):
        with self.assertRaises(InvalidFormatError):
            parse_fraction("123")

        with self.assertRaises(InvalidFormatError):
            parse_fraction("1//2")

        with self.assertRaises(InvalidFormatError):
            parse_fraction("1/2/3")

    def test_invalid_numbers(self):
        with self.assertRaises(InvalidInputError):
            parse_fraction("a/b")

    def test_zero_denominator(self):
        with self.assertRaises(InvalidFractionError):
            parse_fraction("5/0")


class TestFractionArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(str(parse_fraction("1/2") + parse_fraction("1/2")), "1/1")
        self.assertEqual(str(parse_fraction("1/3") + parse_fraction("1/6")), "1/2")

    def test_subtraction(self):
        self.assertEqual(str(parse_fraction("3/4") - parse_fraction("1/4")), "1/2")
        self.assertEqual(str(parse_fraction("1/2") - parse_fraction("1/2")), "0/1")

    def test_multiplication(self):
        self.assertEqual(str(parse_fraction("2/3") * parse_fraction("3/4")), "1/2")

    def test_division(self):
        self.assertEqual(str(parse_fraction("1/2") / parse_fraction("3/4")), "2/3")

    def test_divide_by_zero_fraction(self):
        with self.assertRaises(InvalidFractionError):
            parse_fraction("1/2") / parse_fraction("0/5")


class TestEdgeCases(unittest.TestCase):

    def test_negative_handling(self):
        self.assertEqual(str(parse_fraction("1/-2")), "-1/2")
        self.assertEqual(str(parse_fraction("-1/-2")), "1/2")
        self.assertEqual(str(parse_fraction("-1/2")), "-1/2")

    def test_zero_numerator(self):
        self.assertEqual(str(parse_fraction("0/5")), "0/1")

    def test_simplification(self):
        self.assertEqual(str(parse_fraction("10/20")), "1/2")
        self.assertEqual(str(parse_fraction("100/400")), "1/4")


if __name__ == "__main__":
    unittest.main()
