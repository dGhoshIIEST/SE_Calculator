import unittest
from hex import hex_to_decimal

class TestHex(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(hex_to_decimal("H'1A5"), "D'421")

if __name__ == "__main__":
    unittest.main()
