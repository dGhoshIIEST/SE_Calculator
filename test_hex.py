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
        # ----- NORMAL CASES -----
        # Case 1: Basic single-digit addition without carry
        self.assertEqual(self.hex_calc.add("H'A'", "H'5'"), "H'F'")
        
        # Case 2: Multi-digit addition without carry
        self.assertEqual(self.hex_calc.add("H'1A'", "H'2'"), "H'1C'")
        
        # Case 3: Multi-digit addition with carry propagation
        self.assertEqual(self.hex_calc.add("H'ABC'", "H'123'"), "H'BDF'")
        
        # Case 4: Simple two-digit hex addition
        self.assertEqual(self.hex_calc.add("H'12'", "H'34'"), "H'46'")
        
        # Case 5: Addition of larger numbers
        self.assertEqual(self.hex_calc.add("H'ABCD'", "H'1234'"), "H'BE01'")
        
        # ----- BOUNDARY CONDITIONS -----
        # Boundary 1: Addition with carry (single digit overflow)
        self.assertEqual(self.hex_calc.add("H'7'", "H'9'"), "H'10'")
        
        # Boundary 2: Overflow to next digit group (all F's case)
        self.assertEqual(self.hex_calc.add("H'FF'", "H'1'"), "H'100'")
        
        # Boundary 3: Addition with zero (identity element)
        self.assertEqual(self.hex_calc.add("H'0'", "H'AB'"), "H'AB'")
        
        # Boundary 4: Addition with leading zeros (normalization)
        self.assertEqual(self.hex_calc.add("H'00A'", "H'005'"), "H'F'")
        
        # Boundary 5: Addition with negative numbers (negative result)
        self.assertEqual(self.hex_calc.add("H'5'", "H'-3'"), "H'2'")
        
        # Boundary 6: Addition resulting in negative number
        self.assertEqual(self.hex_calc.add("H'1'", "H'-2'"), "H'-1'")
        
        # ----- INVALID INPUT HANDLING -----
        # Invalid Case 1: Invalid hex digit (G is not valid in hexadecimal)
        with self.assertRaises(ValueError):
            self.hex_calc.add("H'G1'", "H'2'")
        
        # Invalid Case 2: Invalid hex digit in second operand (Z is not valid)
        with self.assertRaises(ValueError):
            self.hex_calc.add("H'A'", "H'Z5'")
        
        # Invalid Case 3: Missing hex format prefix in first operand
        with self.assertRaises(ValueError):
            self.hex_calc.add("A5", "H'B'")
        
        # Invalid Case 4: Missing hex format prefix in second operand
        with self.assertRaises(ValueError):
            self.hex_calc.add("H'A'", "B5")
        
        # Invalid Case 5: Invalid format with incorrect brackets
        with self.assertRaises(ValueError):
            self.hex_calc.add("H[A5]", "H'B'")
    # ---------------------------------
    # PRATYUSH 3 TESTS
    # ---------------------------------
    
    def test_subtract(self):
        self.assertEqual(
            self.hex_calc.subtract("H'F'", "H'5'"),
            "H'A'"
        )

    def test_subtract_with_borrow(self):
        self.assertEqual(
            self.hex_calc.subtract("H'10'", "H'1'"),
            "H'F'"
        )

    def test_subtract_negative_result(self):
        self.assertEqual(
            self.hex_calc.subtract("H'2'", "H'5'"),
            "H'-3'"
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
    # COMMON VALIDATION TEST 
    # ---------------------------------
    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            self.hex_calc.hex_to_decimal("123")


if __name__ == "__main__":
    unittest.main()