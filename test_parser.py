import unittest
from expression_parser import ExpressionParser

class TestExpressionParser(unittest.TestCase):
    def setUp(self):
        self.parser = ExpressionParser()

    # --- Normal Cases ---
    def test_basic_arithmetic(self):
        self.assertEqual(self.parser.evaluate("2 + 3"), 5)
        self.assertEqual(self.parser.evaluate("10 - 4"), 6)
        self.assertEqual(self.parser.evaluate("3 * 4"), 12)
        self.assertEqual(self.parser.evaluate("8 / 2"), 4.0)

    def test_trigonometric_functions(self):
        # The parser returns strings for trig replacements, but evaluate() ultimately returns a float
        self.assertAlmostEqual(float(self.parser.evaluate("sin(30)")), 0.5, places=5)
        self.assertAlmostEqual(float(self.parser.evaluate("cos(60)")), 0.5, places=5)

    def test_combined_expression(self):
        # Tests the core requirement: combining arithmetic and trigonometry
        # 3 + 2 * 0.5 = 4.0
        self.assertAlmostEqual(self.parser.evaluate("3 + 2 * sin(30)"), 4.0, places=5)
        
        # 10 - 4 * 0.5 = 8.0
        self.assertAlmostEqual(self.parser.evaluate("10 - 4 * cos(60)"), 8.0, places=5)

    # --- Boundary Conditions & Edge Cases ---
    def test_whitespace_handling(self):
        # Parser should ignore all chaotic spacing
        self.assertEqual(self.parser.evaluate("  2   +  3  "), 5)
        self.assertAlmostEqual(self.parser.evaluate(" 3 + 2 * sin ( 30 ) "), 4.0, places=5)

    def test_negative_numbers(self):
        self.assertEqual(self.parser.evaluate("-5 + 3"), -2)
        self.assertAlmostEqual(float(self.parser.evaluate("sin(-30)")), -0.5, places=5)

    # --- Invalid Input Handling ---
    def test_division_by_zero(self):
        # The parser should correctly bubble up the ValueError from calculator.py
        with self.assertRaises(ValueError):
            self.parser.evaluate("5 / 0")

    def test_invalid_syntax(self):
        # Passing letters that aren't mapped functions
        with self.assertRaises(Exception):
            self.parser.evaluate("3 + random_word")

if __name__ == '__main__':
    unittest.main()