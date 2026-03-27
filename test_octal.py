import unittest
from octal import *

class TestOctal(unittest.TestCase):

    def testComplement(self):
        self.assertEqual(sevensComplement("O'123"), "O'654")
        self.assertEqual(sevensComplement("O'123"), "O'655")
        self.assertEqual(eightsComplement("O'0"), "O'0") 
        self.assertEqual(eightsComplement("O'456"), "O'322")
        self.assertEqual(eightsComplement("O'000"), "O'000")
        self.assertEqual(sevensComplement("O'001"), "O'776")
        self.assertEqual(eightsComplement("O'777"), "O'001")
        self.assertEqual(sevensComplement("O'10"), "O'60")
    

if __name__ == "__main__":
    unittest.main()