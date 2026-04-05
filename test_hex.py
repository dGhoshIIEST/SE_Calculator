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
 FeatureB_8_Sneha
        self.assertEqual(
            self.hex_calc.add("H'A'", "H'5'"),
            "H'F'"
        )

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
            
    def test_multiply(self):
        # ----- NORMAL CASES -----
        # Case 1: Basic single-digit multiplication without carry
        self.assertEqual(self.hex_calc.multiply("H'3'", "H'4'"), "H'C'")
        
        # Case 2: Multi-digit multiplication without carry
        self.assertEqual(self.hex_calc.multiply("H'2'", "H'10'"), "H'20'")
        
        # Case 3: Multi-digit multiplication with carry propagation
        self.assertEqual(self.hex_calc.multiply("H'1A'", "H'2'"), "H'34'")
        
        # Case 4: Simple two-digit hex multiplication
        self.assertEqual(self.hex_calc.multiply("H'5'", "H'6'"), "H'1E'")
        
        # Case 5: Multiplication of larger numbers
        self.assertEqual(self.hex_calc.multiply("H'AB'", "H'CD'"), "H'88EF'")
        
        # ----- BOUNDARY CONDITIONS -----
        # Boundary 1: Multiplication with zero (annihilator element)
        self.assertEqual(self.hex_calc.multiply("H'A'", "H'0'"), "H'0'")
        
        # Boundary 2: Multiplication with one (identity element)
        self.assertEqual(self.hex_calc.multiply("H'A'", "H'1'"), "H'A'")
        
        # Boundary 3: Multiplication resulting in zero
        self.assertEqual(self.hex_calc.multiply("H'A'", "H'-0'"), "H'0'")
        
        # Boundary 4: Multiplication with negative numbers (negative result)
        self.assertEqual(self.hex_calc.multiply("H'-3'", "H'4'"), "H'-C'")
        
        # Boundary 5: Multiplication resulting in negative number
        self.assertEqual(self.hex_calc.multiply("H'-2'", "H'-3'"), "H'6'")
        
        # ----- INVALID INPUT HANDLING -----
        # Invalid Case 1: Invalid hex digit (G is not valid in hexadecimal)
        with self.assertRaises(ValueError):
            self.hex_calc.multiply("H'G1'", "H'2'")
        
        # Invalid Case 2: Invalid hex digit in second operand (Z is not valid)
        with self.assertRaises(ValueError):
            self.hex_calc.multiply("H'A'", "H'Z5'")
        
        # Invalid Case 3: Missing hex format prefix in first operand
        with self.assertRaises(ValueError):
            self.hex_calc.multiply("A5", "H'B'")
        
        # Invalid Case 4: Missing hex format prefix in second operand
        with self.assertRaises(ValueError):
            self.hex_calc.multiply("H'A'", "B5")
        
        # Invalid Case 5: Invalid format with incorrect brackets
        with self.assertRaises(ValueError):
            self.hex_calc.multiply("H[A5]", "H'B'")
            
    def test_divide(self):
        
        # ----- NORMAL CASES -----
        # Case 1: Basic single-digit division without remainder
        self.assertEqual(self.hex_calc.divide("H'C'", "H'4'"), "H'3'")
        
        # Case 2: Multi-digit division without remainder
        self.assertEqual(self.hex_calc.divide("H'20'", "H'2'"), "H'10'")
        
        # Case 3: Multi-digit division with remainder (integer division)
        self.assertEqual(self.hex_calc.divide("H'1A'", "H'3'"), "H'8'")
        
        # Case 4: Simple two-digit hex division
        self.assertEqual(self.hex_calc.divide("H'1E'", "H'6'"), "H'5'")
        
        # Case 5: Division of larger numbers
        self.assertEqual(self.hex_calc.divide("H'88EF'", "H'AB'"), "H'CD'")
        
        # ----- BOUNDARY CONDITIONS -----
        # Boundary 1: Division by one (identity element)
        self.assertEqual(self.hex_calc.divide("H'A'", "H'1'"), "H'A'")
        
        # Boundary 2: Division resulting in zero
        self.assertEqual(self.hex_calc.divide("H'1'", "H'2'"), "H'0'")
        
        # Boundary 3: Division with negative numbers (negative result)
        self.assertEqual(self.hex_calc.divide("H'-C'", "H'4'"), "H'-3'")
        
        # Boundary 4: Division resulting in negative number
        self.assertEqual(self.hex_calc.divide("H'-6'", "H'-2'"), "H'3'")
        
        # ----- INVALID INPUT HANDLING -----
        # Invalid Case 1: Division by zero
        with self.assertRaises(ValueError):
            self.hex_calc.divide("H'A'", "H'0'")
            
        # Invalid Case 2: Invalid hex digit (G is not valid in hexadecimal)
        with self.assertRaises(ValueError):
            self.hex_calc.divide("H'G1'", "H'2'")
            
        # Invalid Case 3: Invalid hex digit in second operand (Z is not valid)
        with self.assertRaises(ValueError):
            self.hex_calc.divide("H'A'", "H'Z5'")
            
        # Invalid Case 4: Missing hex format prefix in first operand
        with self.assertRaises(ValueError):
            self.hex_calc.divide("A5", "H'B'")
        
        # Invalid Case 5: Missing hex format prefix in second operand
        with self.assertRaises(ValueError):
            self.hex_calc.divide("H'A'", "B5")
 FeatureB_8

    # ---------------------------------
    # PRATYUSH TEST
    # ---------------------------------
 FeatureB_8_Sneha
    def test_subtract(self):
        self.assertEqual(
            self.hex_calc.subtract("H'F'", "H'5'"),
            "H'A'"
        )

    
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
 FeatureB_8

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
 FeatureB_8_Sneha
    # COMMON VALIDATION TEST

    # COMMON VALIDATION TEST 
 FeatureB_8
    # ---------------------------------
    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            self.hex_calc.hex_to_decimal("123")


if __name__ == "__main__":
    unittest.main()