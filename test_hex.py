import unittest
from hex import HexOperations
class TestHexOperations(unittest.TestCase):
    def setUp(self):
        self.hex_ops = HexOperations()
    def test_hex_conversion(self):
        # Hexadecimal <-> Decimal conversions e.g. "hex(D'243)" returns "H'F3", "dec(H'1A5)" is "D'421"
        self.assertEqual(self.hex_ops.hex("D'243"), "H'F3")
    def test_dec_conversion(self):
        self.assertEqual(self.hex_ops.dec("H'1A5"), "D'421")
    def test_add(self):
        self.assertEqual(self.hex_ops.add("H'A", "H'5"), "H'F")
        self.assertEqual(self.hex_ops.add("H'AB12", "H'1"), "H'AB13")
    def test_subtract(self):
        self.assertEqual(self.hex_ops.subtract("H'10", "H'A"), "H'6")
        self.assertEqual(self.hex_ops.subtract("H'A", "H'10"), "-H'6")
    def test_multiply(self):
        self.assertEqual(self.hex_ops.multiply("H'2", "H'8"), "H'10")
    def test_divide(self):
        self.assertEqual(self.hex_ops.divide("H'10", "H'2"), "H'8")
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.hex_ops.divide("H'10", "H'0")
    def test_complement_15s(self):
        self.assertEqual(self.hex_ops.complement_15s("H'A5"), "H'5A")
        self.assertEqual(self.hex_ops.complement_15s("H'F3"), "H'0C")
    def test_complement_16s(self):
        self.assertEqual(self.hex_ops.complement_16s("H'A5"), "H'5B")
        self.assertEqual(self.hex_ops.complement_16s("H'00"), "H'00") # 15s is FF -> +1 is 100 -> truncated to 00
    def test_invalid_input(self):
        # Invalid prefix
        with self.assertRaises(ValueError):
            self.hex_ops.validate_hex("1A")
        # Invalid chars
        with self.assertRaises(ValueError):
            self.hex_ops.validate_hex("H'1G")
        # Decimal invalid
        with self.assertRaises(ValueError):
            self.hex_ops.validate_dec("D'ABC")
if __name__ == '__main__':
    unittest.main()