import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    # base test cases
    def setUp(self):
        self.calc = Calculator()

    # ---------------------------------
    # PREVIOUS BASIC DECIMAL TESTS
    # (kept as-is for backward compatibility)
    # ---------------------------------
    def test_add_decimal(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub_decimal(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)

    def test_multiply_decimal(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide_decimal_positive(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

    def test_divide_decimal_negative(self):
        self.assertEqual(self.calc.divide(4, -2), -2)

    def test_divide_fail(self):  # this should still pass
        self.assertNotEqual(self.calc.divide(4, -2), 2)

    def test_divide_by_zero_decimal(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    # ---------------------------------
    # MODE SETTING TESTS
    # ---------------------------------
    def test_set_mode_string(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.get_mode(), "hex")

    def test_set_mode_number(self):
        self.calc.set_mode(4)
        self.assertEqual(self.calc.get_mode(), "hex")

    def test_invalid_mode_string(self):
        with self.assertRaises(ValueError):
            self.calc.set_mode("abc")

    def test_invalid_mode_number(self):
        with self.assertRaises(ValueError):
            self.calc.set_mode(99)

    # ---------------------------------
    # DIRECT HEX MODE TESTS
    # ---------------------------------
    def test_hex_add_direct(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.add("H'2'", "H'3'"), "H'5'")

    def test_hex_subtract_direct(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.subtract("H'2'", "H'3'"), "H'-1'")

    def test_hex_multiply_direct(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.multiply("H'2'", "H'3'"), "H'6'")

    def test_hex_divide_direct(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.divide("H'4'", "H'2'"), "H'2'")

    def test_hex_divide_by_zero(self):
        self.calc.set_mode("hex")
        with self.assertRaises(ValueError):
            self.calc.divide("H'5'", "H'0'")

    # ---------------------------------
    # EVALUATE() TESTS
    # ---------------------------------
    def test_evaluate_add(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("add", "H'A'", "H'5'"), "H'F'")

    def test_evaluate_subtract(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("subtract", "H'F'", "H'5'"), "H'A'")

    def test_evaluate_multiply(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("multiply", "H'3'", "H'4'"), "H'C'")

    def test_evaluate_divide(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("divide", "H'1A'", "H'3'"), "H'8'")

    def test_evaluate_hex_to_decimal(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("hex_to_decimal", "H'1A'"), "D'26'")

    def test_evaluate_decimal_to_hex(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("decimal_to_hex", "D'26'"), "H'1A'")

    def test_evaluate_fifteen_complement(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("fifteen_complement", "H'A'"), "H'5'")

    def test_evaluate_sixteen_complement(self):
        self.calc.set_mode("hex")
        self.assertEqual(self.calc.evaluate("sixteen_complement", "H'A'"), "H'6'")

    def test_evaluate_invalid_operation(self):
        self.calc.set_mode("hex")
        with self.assertRaises(ValueError):
            self.calc.evaluate("modulus", "H'A'", "H'2'")


# Optional: this allows running the script directly
if __name__ == '__main__':
    unittest.main()