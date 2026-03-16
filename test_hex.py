# test_hex.py

import unittest
from hex import HexCalculator


class TestHexCalculator(unittest.TestCase):

    def setUp(self):
        self.hex_calc = HexCalculator()

    # ---------------------------------
    # SRAVANTI 1 TESTS
    # ---------------------------------
    def test_hex_to_decimal(self):
        self.assertEqual(
            self.hex_calc.hex_to_decimal("H'1A5'"),
            "D'421'"
        )

    # ---------------------------------
    # SAICHAITANYA 2 TESTS
    # ---------------------------------
    def test_decimal_to_hex(self):
        self.assertEqual(
            self.hex_calc.decimal_to_hex("D'243'"),
            "H'F3'"
        )

    # ---------------------------------
    # JOYDIP 3 TESTS
    # ---------------------------------
    def test_add(self):
        self.assertEqual(
            self.hex_calc.add("H'A'", "H'5'"),
            "H'F'"
        )
    # ---------------------------------
    # PRATYUSH 3 TESTS
    # ---------------------------------
    
    def test_subtract(self):
        self.assertEqual(
            self.hex_calc.subtract("H'F'", "H'5'"),
            "H'A'"
        )

    # ---------------------------------
    # SNEHA 4 TESTS
    # ---------------------------------
    def test_fifteen_complement(self):
        self.assertEqual(
            self.hex_calc.fifteen_complement("H'A'"),
            "H'5'"
        )

    def test_sixteen_complement(self):
        self.assertEqual(
            self.hex_calc.sixteen_complement("H'A'"),
            "H'6'"
        )

    # ---------------------------------
    # COMMON VALIDATION TEST --- Already Done
    # ---------------------------------
    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            self.hex_calc.hex_to_decimal("123")


if __name__ == "__main__":
    unittest.main()