import unittest
from octal import *
from arithmetic import *
from octal_conversion import *
from validate_octal import *
class TestOctal(unittest.TestCase):

    def testComplement(self):
        self.assertEqual(sevensComplement("O'123"), "O'654")
        self.assertEqual(eightsComplement("O'123"), "O'655")
        self.assertEqual(eightsComplement("O'0"), "O'0") 
        self.assertEqual(eightsComplement("O'456"), "O'322")
        self.assertEqual(eightsComplement("O'000"), "O'000")
        self.assertEqual(sevensComplement("O'001"), "O'776")
        self.assertEqual(eightsComplement("O'777"), "O'001")
        self.assertEqual(sevensComplement("O'10"), "O'67")

    def test_add_octal(self):
        self.assertEqual(add_octal("O'10", "O'7"), "O'17")
        self.assertEqual(add_octal("O'1", "O'1"), "O'2")

    def test_subtract_octal(self):
        self.assertEqual(subtract_octal("O'10", "O'7"), "O'1")

    def test_subtract_negative(self):
        with self.assertRaises(ValueError):
            subtract_octal("O'7", "O'10")

    def test_multiply_octal(self):
        self.assertEqual(multiply_octal("O'2", "O'3"), "O'6")

    def test_divide_octal(self):
        self.assertEqual(divide_octal("O'10", "O'2"), "O'4")

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_octal("O'10", "O'0")

    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal("O'10"), "D'8")
        self.assertEqual(octal_to_decimal("O'17"), "D'15")
        self.assertEqual(octal_to_decimal("O'247"), "D'167")

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal("D'8"), "O'10")
        self.assertEqual(decimal_to_octal("D'15"), "O'17")
        self.assertEqual(decimal_to_octal("D'167"), "O'247")

        self.assertEqual(validate_octal("O'123"), "123")

        with self.assertRaises(ValueError):
            validate_octal("123")   # wrong format

    def test_validate_octal(self):
        self.assertEqual(validate_octal("O'123"), "123")

        with self.assertRaises(ValueError):
            validate_octal("123")   # wrong format

        with self.assertRaises(ValueError):
            validate_octal("O'89")  # invalid digit

        with self.assertRaises(ValueError):
            validate_octal("O'")    # empty input
if __name__ == "__main__":
    unittest.main()