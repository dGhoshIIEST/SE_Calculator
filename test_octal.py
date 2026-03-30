import unittest
from octal import *
from arithmetic import *

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
    


if __name__ == "__main__":
    unittest.main()