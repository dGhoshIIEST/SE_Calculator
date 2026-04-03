
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
        self.assertEqual(self.hex_calc.add("H'A'", "H'5'"), "H'F'")
        self.assertEqual(self.hex_calc.add("H'7'", "H'9'"), "H'10'")
        self.assertEqual(self.hex_calc.add("H'FF'", "H'1'"), "H'100'")
        self.assertEqual(self.hex_calc.add("H'1A'", "H'2'"), "H'1C'")
        self.assertEqual(self.hex_calc.add("H'0'", "H'AB'"), "H'AB'")
        self.assertEqual(self.hex_calc.add("H'5'", "H'-3'"), "H'2'")
        self.assertEqual(self.hex_calc.add("H'00A'", "H'005'"), "H'F'")
        self.assertEqual(self.hex_calc.add("H'ABC'", "H'123'"), "H'BDF'")
        self.assertEqual(self.hex_calc.add("H'1'", "H'-2'"), "H'-1'")
        with self.assertRaises(ValueError):
            self.hex_calc.add("H'G1'", "H'2'")
    # ---------------------------------
    # PRATYUSH 3 TESTS
    # ---------------------------------
    
    def test_subtract_all_cases(self):
        # Basic subtract scenarios
        self.assertEqual(self.hex_calc.subtract("H'F'", "H'5'"), "H'A'")
        self.assertEqual(self.hex_calc.subtract("H'10'", "H'1'"), "H'F'")
        self.assertEqual(self.hex_calc.subtract("H'2'", "H'5'"), "H'-3'")

        # Functional edge cases
        self.assertEqual(self.hex_calc.subtract("H'0'", "H'0'"), "H'0'")
        self.assertEqual(self.hex_calc.subtract("H'1A3F'", "H'1A3F'"), "H'0'")
        self.assertEqual(self.hex_calc.subtract("H'1000'", "H'1'"), "H'FFF'")
        self.assertEqual(self.hex_calc.subtract("H'00A'", "H'0001'"), "H'9'")
        self.assertEqual(self.hex_calc.subtract("H'a'", "H'3'"), "H'7'")
        self.assertEqual(self.hex_calc.subtract("H'ABCDEF'", "H'123456'"), "H'999999'")
        self.assertEqual(self.hex_calc.subtract("H'1'", "H'A'"), "H'-9'")
        self.assertEqual(self.hex_calc.subtract("H'10'", "H'1F'"), "H'-F'")

        # Validation and input-type corner cases
        with self.assertRaises(ValueError):
            self.hex_calc.subtract("H'1G'", "H'1'")

        with self.assertRaises(ValueError):
            self.hex_calc.subtract("H'1'", "1")

        with self.assertRaises(ValueError):
            self.hex_calc.subtract(10, "H'1'")

        with self.assertRaises(ValueError):
            self.hex_calc.subtract("H'1'", None)

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

