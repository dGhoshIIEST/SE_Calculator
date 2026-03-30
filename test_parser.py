"""
test_parser.py
Unit Tests — Input Parser Module, Octal Calculator Project

Run with:
    python -m pytest test_parser.py -v
"""

import pytest
from parser import parse_input


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def _ok(base_mode: str, value: str) -> dict:
    """Expected result for a successful parse."""
    return {"base_mode": base_mode, "value": value, "error": None}


def _err(base_mode, value, fragment: str) -> dict:
    """
    Expected shape for a failed parse.
    fragment: a word that must appear (case-insensitive) in the error message.
    """
    return {"base_mode": base_mode, "value": value, "_fragment": fragment}


def assert_result(result: dict, expected: dict) -> None:
    """
    Assert a parse_input() result against an expected dict.
    When expected has '_fragment', checks substring match on the error field
    instead of exact equality, so tests stay decoupled from exact wording.
    """
    assert isinstance(result, dict), "Result must be a dict"
    assert set(result.keys()) == {"base_mode", "value", "error"}, (
        f"Unexpected keys: {result.keys()}"
    )

    if "_fragment" in expected:
        assert result["base_mode"] == expected["base_mode"]
        assert result["value"]     == expected["value"]
        assert result["error"] is not None, "Expected an error but got None"
        assert expected["_fragment"].lower() in result["error"].lower(), (
            f"Error '{result['error']}' does not contain '{expected['_fragment']}'"
        )
    else:
        assert result == expected, f"\nExpected : {expected}\nActual   : {result}"


# ---------------------------------------------------------------------------
# 1. Valid octal inputs
# ---------------------------------------------------------------------------

class TestOctalValid:
    """Correctly formed octal strings should parse without error."""

    def test_typical_octal(self):
        assert_result(parse_input("O'247"), _ok("OCT", "247"))

    def test_single_digit_zero(self):
        assert_result(parse_input("O'0"), _ok("OCT", "0"))

    def test_single_digit_seven(self):
        # 7 is the highest valid octal digit
        assert_result(parse_input("O'7"), _ok("OCT", "7"))

    def test_leading_zeros_preserved(self):
        # Leading zeros are kept as-is (value is a string, not an integer)
        assert_result(parse_input("O'007"), _ok("OCT", "007"))

    def test_long_octal_value(self):
        assert_result(parse_input("O'77777777"), _ok("OCT", "77777777"))

    def test_lowercase_prefix_accepted(self):
        # Prefix matching is case-insensitive
        assert_result(parse_input("o'247"), _ok("OCT", "247"))

    def test_surrounding_whitespace_stripped(self):
        assert_result(parse_input("  O'247  "), _ok("OCT", "247"))


# ---------------------------------------------------------------------------
# 2. Valid decimal inputs
# ---------------------------------------------------------------------------

class TestDecimalValid:
    """Correctly formed decimal strings should parse without error."""

    def test_typical_decimal(self):
        assert_result(parse_input("D'123"), _ok("DEC", "123"))

    def test_single_digit_zero(self):
        assert_result(parse_input("D'0"), _ok("DEC", "0"))

    def test_large_value(self):
        assert_result(parse_input("D'9999999999"), _ok("DEC", "9999999999"))

    def test_lowercase_prefix_accepted(self):
        assert_result(parse_input("d'456"), _ok("DEC", "456"))

    def test_leading_zeros_preserved(self):
        assert_result(parse_input("D'00123"), _ok("DEC", "00123"))

    def test_surrounding_whitespace_stripped(self):
        assert_result(parse_input("  D'789  "), _ok("DEC", "789"))

    def test_digits_8_and_9_valid_in_decimal(self):
        # 8 and 9 are legal in decimal but NOT in octal
        assert_result(parse_input("D'89"), _ok("DEC", "89"))


# ---------------------------------------------------------------------------
# 3. Illegal digits for the stated base
# ---------------------------------------------------------------------------

class TestInvalidDigits:
    """Values containing digits that are out-of-range for the base."""

    def test_octal_digit_8(self):
        assert_result(parse_input("O'128"), _err("OCT", None, "octal"))

    def test_octal_digit_9(self):
        assert_result(parse_input("O'9"), _err("OCT", None, "octal"))

    def test_octal_digits_8_and_9(self):
        assert_result(parse_input("O'89"), _err("OCT", None, "octal"))

    def test_octal_alpha_character(self):
        assert_result(parse_input("O'2A4"), _err("OCT", None, "octal"))

    def test_octal_hex_digit(self):
        assert_result(parse_input("O'1F3"), _err("OCT", None, "octal"))

    def test_decimal_alpha_character(self):
        assert_result(parse_input("D'12A"), _err("DEC", None, "decimal"))

    def test_decimal_decimal_point(self):
        # Floats are not valid — only integer strings are accepted
        assert_result(parse_input("D'12.5"), _err("DEC", None, "decimal"))


# ---------------------------------------------------------------------------
# 4. Unknown or unsupported prefix
# ---------------------------------------------------------------------------

class TestUnknownPrefix:
    """Any prefix other than O or D must produce a prefix error."""

    def test_hex_prefix(self):
        assert_result(parse_input("H'1F"), _err(None, None, "prefix"))

    def test_binary_prefix(self):
        assert_result(parse_input("B'1010"), _err(None, None, "prefix"))

    def test_arbitrary_letter(self):
        assert_result(parse_input("X'10"), _err(None, None, "prefix"))

    def test_numeric_prefix(self):
        assert_result(parse_input("8'123"), _err(None, None, "prefix"))

    def test_empty_prefix(self):
        assert_result(parse_input("'123"), _err(None, None, "prefix"))

    def test_multi_char_prefix(self):
        # "OC" is not a recognised single-letter prefix
        assert_result(parse_input("OC'247"), _err(None, None, "prefix"))


# ---------------------------------------------------------------------------
# 5. Structural / format errors
# ---------------------------------------------------------------------------

class TestMalformedInput:
    """Input that is structurally broken (wrong format)."""

    def test_missing_separator_octal(self):
        assert_result(parse_input("O247"), _err(None, None, "separator"))

    def test_missing_separator_decimal(self):
        assert_result(parse_input("D123"), _err(None, None, "separator"))

    def test_empty_value_after_octal_prefix(self):
        assert_result(parse_input("O'"), _err("OCT", None, "value"))

    def test_empty_value_after_decimal_prefix(self):
        assert_result(parse_input("D'"), _err("DEC", None, "value"))

    def test_empty_string(self):
        assert_result(parse_input(""), _err(None, None, "empty"))

    def test_whitespace_only(self):
        assert_result(parse_input("   "), _err(None, None, "empty"))

    def test_space_inside_value(self):
        # Spaces in the value part are not valid digits
        assert parse_input("O' 247")["error"] is not None

    def test_extra_apostrophe_in_value(self):
        # Second apostrophe becomes part of the value string → invalid digits
        assert parse_input("O'24'7")["error"] is not None

    def test_only_separator(self):
        assert parse_input("'")["error"] is not None


# ---------------------------------------------------------------------------
# 6. Non-string input types
# ---------------------------------------------------------------------------

class TestTypeSafety:
    """parse_input must not crash on non-string arguments."""

    def test_integer(self):
        assert parse_input(247)["error"] is not None       # type: ignore[arg-type]

    def test_none(self):
        assert parse_input(None)["error"] is not None      # type: ignore[arg-type]

    def test_list(self):
        assert parse_input(["O'247"])["error"] is not None # type: ignore[arg-type]

    def test_float(self):
        assert parse_input(2.47)["error"] is not None      # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# 7. Return-value contract (parametrized)
# ---------------------------------------------------------------------------

class TestReturnContract:
    """parse_input must always honour the dict contract, success or failure."""

    VALID_INPUTS   = ["O'247", "D'123", "o'007", "D'89"]
    INVALID_INPUTS = ["O'89", "X'10", "", "D'", "O'", "D123", "D'12A"]

    @pytest.mark.parametrize("s", VALID_INPUTS + INVALID_INPUTS)
    def test_always_returns_three_keys(self, s: str):
        result = parse_input(s)
        assert isinstance(result, dict)
        assert set(result.keys()) == {"base_mode", "value", "error"}

    @pytest.mark.parametrize("s", VALID_INPUTS)
    def test_success_has_null_error(self, s: str):
        assert parse_input(s)["error"] is None

    @pytest.mark.parametrize("s", INVALID_INPUTS)
    def test_failure_has_non_empty_error_string(self, s: str):
        error = parse_input(s)["error"]
        assert isinstance(error, str) and len(error) > 0
