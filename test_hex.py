import unittest
from hex import HexCalculator


class TestHexCalculator(unittest.TestCase):

    def setUp(self):
        self.hex_calc = HexCalculator()

    # ---------------------------------
    # SRAVANTI TEST
    # ---------------------------------
    def test_hex_to_decimal(self):
        self.assertEqual(
            self.hex_calc.hex_to_decimal("H'1A5'"),
            "D'421'"
        )

    # ---------------------------------
    # SAICHAITANYA TEST
    # ---------------------------------
    def test_decimal_to_hex(self):
        self.assertEqual(
            self.hex_calc.decimal_to_hex("D'243'"),
            "H'F3'"
        )

    # ---------------------------------
    # JOYDIP TEST
    # ---------------------------------
    def test_add(self):
        self.assertEqual(
            self.hex_calc.add("H'A'", "H'5'"),
            "H'F'"
        )

    # ---------------------------------
    # PRATYUSH TEST
    # ---------------------------------
    def test_subtract(self):
        self.assertEqual(
            self.hex_calc.subtract("H'F'", "H'5'"),
            "H'A'"
        )

    # ---------------------------------
    # SNEHA TESTS
    # ---------------------------------
    def test_fifteen_complement(self):
        self.assertEqual(self.hex_calc.fifteen_complement("H'A'"), "H'5'")

    def test_sixteen_complement(self):
        self.assertEqual(self.hex_calc.sixteen_complement("H'A'"), "H'6'")

    def test_fifteen_zero(self):
        self.assertEqual(self.hex_calc.fifteen_complement("H'0'"), "H'F'")

    def test_fifteen_all_F(self):
        self.assertEqual(self.hex_calc.fifteen_complement("H'F'"), "H'0'")

    def test_fifteen_multi_digit(self):
        self.assertEqual(self.hex_calc.fifteen_complement("H'1A3'"), "H'E5C'")

    def test_fifteen_all_zero(self):
        self.assertEqual(self.hex_calc.fifteen_complement("H'000'"), "H'FFF'")

    def test_sixteen_zero(self):
        self.assertEqual(self.hex_calc.sixteen_complement("H'0'"), "H'10'")

    def test_sixteen_all_F(self):
        self.assertEqual(self.hex_calc.sixteen_complement("H'F'"), "H'1'")

    def test_sixteen_multi_digit(self):
        self.assertEqual(self.hex_calc.sixteen_complement("H'1A3'"), "H'E5D'")

    def test_sixteen_all_zero(self):
        self.assertEqual(self.hex_calc.sixteen_complement("H'000'"), "H'1000'")

    # ---------------------------------
    # COMMON VALIDATION TEST
    # ---------------------------------
    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            self.hex_calc.hex_to_decimal("123")


if __name__ == "__main__":
    unittest.main()