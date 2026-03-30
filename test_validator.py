"""
test_validator.py

Unit tests for the Validator module.

parse_input() is MOCKED here so that tests run independently
of the Parser module. When the full team integrates, these mocks can be
removed and replaced with real parser calls in integration tests.
"""

import unittest
from unittest.mock import patch

from validator import validate_input


class TestValidateInputOCT(unittest.TestCase):
    """Tests for octal (OCT) base validation."""

    def test_valid_octal(self):
        parsed = {'value': '7045321', 'base': 'OCT'}
        result = validate_input(parsed)
        self.assertTrue(result['is_valid'])
        self.assertIsNone(result['error'])

    def test_valid_octal_single_digit(self):
        result = validate_input({'value': '0', 'base': 'OCT'})
        self.assertTrue(result['is_valid'])

    def test_valid_octal_all_digits(self):
        result = validate_input({'value': '01234567', 'base': 'OCT'})
        self.assertTrue(result['is_valid'])

    def test_invalid_octal_digit_8(self):
        result = validate_input({'value': '7081', 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('8', result['error'])

    def test_invalid_octal_digit_9(self):
        result = validate_input({'value': '9', 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('9', result['error'])

    def test_invalid_octal_letter(self):
        result = validate_input({'value': '75A2', 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('A', result['error'])

    def test_invalid_octal_multiple_bad_chars(self):
        result = validate_input({'value': '89AB', 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        # All bad chars should be mentioned
        for ch in ['8', '9', 'A', 'B']:
            self.assertIn(ch, result['error'])

    def test_octal_base_case_insensitive(self):
        result = validate_input({'value': '754', 'base': 'oct'})
        self.assertTrue(result['is_valid'])


class TestValidateInputDEC(unittest.TestCase):
    """Tests for decimal (DEC) base validation."""

    def test_valid_decimal(self):
        result = validate_input({'value': '9081234567', 'base': 'DEC'})
        self.assertTrue(result['is_valid'])
        self.assertIsNone(result['error'])

    def test_valid_decimal_single_digit(self):
        result = validate_input({'value': '5', 'base': 'DEC'})
        self.assertTrue(result['is_valid'])

    def test_valid_decimal_all_digits(self):
        result = validate_input({'value': '0123456789', 'base': 'DEC'})
        self.assertTrue(result['is_valid'])

    def test_invalid_decimal_letter(self):
        result = validate_input({'value': '12X4', 'base': 'DEC'})
        self.assertFalse(result['is_valid'])
        self.assertIn('X', result['error'])

    def test_invalid_decimal_special_char(self):
        result = validate_input({'value': '12.34', 'base': 'DEC'})
        self.assertFalse(result['is_valid'])
        self.assertIn('.', result['error'])

    def test_decimal_base_case_insensitive(self):
        result = validate_input({'value': '999', 'base': 'dec'})
        self.assertTrue(result['is_valid'])


class TestEdgeCases(unittest.TestCase):
    """Edge-case and structural tests."""

    def test_empty_value(self):
        result = validate_input({'value': '', 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('empty', result['error'].lower())

    def test_whitespace_only_value(self):
        result = validate_input({'value': '   ', 'base': 'DEC'})
        self.assertFalse(result['is_valid'])
        self.assertIn('empty', result['error'].lower())

    def test_missing_value_key(self):
        result = validate_input({'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('value', result['error'])

    def test_missing_base_key(self):
        result = validate_input({'value': '123'})
        self.assertFalse(result['is_valid'])
        self.assertIn('base', result['error'])

    def test_missing_both_keys(self):
        result = validate_input({})
        self.assertFalse(result['is_valid'])

    def test_non_dict_input(self):
        result = validate_input("752")
        self.assertFalse(result['is_valid'])
        self.assertIn('dictionary', result['error'].lower())

    def test_unsupported_base_HEX(self):
        result = validate_input({'value': 'A3F', 'base': 'HEX'})
        self.assertFalse(result['is_valid'])
        self.assertIn('HEX', result['error'])

    def test_unsupported_base_BIN(self):
        result = validate_input({'value': '1010', 'base': 'BIN'})
        self.assertFalse(result['is_valid'])

    def test_value_not_a_string(self):
        result = validate_input({'value': 752, 'base': 'OCT'})
        self.assertFalse(result['is_valid'])
        self.assertIn('string', result['error'].lower())

    def test_base_not_a_string(self):
        result = validate_input({'value': '752', 'base': 8})
        self.assertFalse(result['is_valid'])
        self.assertIn('string', result['error'].lower())

    def test_none_value(self):
        result = validate_input({'value': None, 'base': 'OCT'})
        self.assertFalse(result['is_valid'])

    def test_valid_result_structure(self):
        """Ensure return dict always has exactly the required keys."""
        result = validate_input({'value': '123', 'base': 'DEC'})
        self.assertIn('is_valid', result)
        self.assertIn('error', result)
        self.assertEqual(len(result), 2)


class TestWithMockedParser(unittest.TestCase):
    """
    Simulates the integration point with parse_input().
    parse_input() is mocked — these tests do NOT require parser.py to exist.
    """

    @patch('validator.parse_input', return_value={'value': '754', 'base': 'OCT'})
    def test_pipeline_valid_octal(self, mock_parse):
        from validator import parse_input
        parsed = parse_input("754")          # returns mocked dict
        result = validate_input(parsed)
        self.assertTrue(result['is_valid'])
        mock_parse.assert_called_once_with("754")

    @patch('validator.parse_input', return_value={'value': '89F', 'base': 'OCT'})
    def test_pipeline_invalid_octal(self, mock_parse):
        from validator import parse_input
        parsed = parse_input("89F")
        result = validate_input(parsed)
        self.assertFalse(result['is_valid'])

    @patch('validator.parse_input', return_value={'value': '1234', 'base': 'DEC'})
    def test_pipeline_valid_decimal(self, mock_parse):
        from validator import parse_input
        parsed = parse_input("1234")
        result = validate_input(parsed)
        self.assertTrue(result['is_valid'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
