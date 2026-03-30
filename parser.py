"""
parser.py
Input Parser Module — Octal Calculator Project

Parses strings like "O'247" or "D'123" into their components.
Format: <prefix>'<value>  where prefix is O (octal) or D (decimal).
"""

import re
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Maps a single-letter prefix to its canonical base-mode name.
PREFIX_TO_MODE: dict[str, str] = {
    "O": "OCT",
    "D": "DEC",
}

# Regex pattern that a value must fully match for each base mode.
VALID_DIGIT_PATTERN: dict[str, str] = {
    "OCT": r"^[0-7]+$",   # octal: digits 0-7 only
    "DEC": r"^[0-9]+$",   # decimal: digits 0-9
}

# Separator between prefix and value.
SEPARATOR = "'"

# Blank result template — returned (with an error filled in) on failure.
_BLANK: dict[str, Optional[str]] = {
    "base_mode": None,
    "value": None,
    "error": None,
}


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _failure(error: str, base_mode: Optional[str] = None) -> dict:
    """Return a failed-parse result with the given error message."""
    return {**_BLANK, "base_mode": base_mode, "error": error}


def _success(base_mode: str, value: str) -> dict:
    """Return a successful parse result."""
    return {"base_mode": base_mode, "value": value, "error": None}


def _digit_error(base_mode: str, value_part: str) -> str:
    """Build a human-readable digit-validation error message."""
    allowed = "0-7" if base_mode == "OCT" else "0-9"
    label   = "Octal" if base_mode == "OCT" else "Decimal"
    return (
        f"Invalid {base_mode.lower()} value '{value_part}'. "
        f"{label} accepts only digits {allowed}."
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def parse_input(input_str: str) -> dict:
    """Parse a prefixed numeric string and return its components.

    Accepts inputs of the form ``<prefix>'<value>`` where:
      - ``prefix`` is ``O`` (octal) or ``D`` (decimal), case-insensitive.
      - ``value`` is a non-empty string of digits valid for that base.

    Args:
        input_str: Raw input string, e.g. ``"O'247"`` or ``"D'123"``.

    Returns:
        A dict with three keys:

        - ``base_mode`` (str | None): ``'OCT'`` or ``'DEC'``, or None on error.
        - ``value``     (str | None): Extracted digit string, or None on error.
        - ``error``     (str | None): Error message, or None on success.

    Examples:
        >>> parse_input("O'247")
        {'base_mode': 'OCT', 'value': '247', 'error': None}

        >>> parse_input("D'123")
        {'base_mode': 'DEC', 'value': '123', 'error': None}

        >>> parse_input("O'89")
        {'base_mode': 'OCT', 'value': None, 'error': "Invalid octal value '89'. Octal accepts only digits 0-7."}

        >>> parse_input("X'10")
        {'base_mode': None, 'value': None, 'error': "Unknown prefix 'X'. Supported: O (octal), D (decimal)."}
    """

    # 1. Reject non-string input early.
    if not isinstance(input_str, str):
        return _failure("Input must be a string.")

    input_str = input_str.strip()

    # 2. Reject blank / whitespace-only input.
    if not input_str:
        return _failure("Input string is empty.")

    # 3. The separator must be present to split prefix from value.
    if SEPARATOR not in input_str:
        return _failure(
            f"Missing separator '{SEPARATOR}' in '{input_str}'. "
            f"Expected format: <prefix>{SEPARATOR}<value>  e.g. O'247 or D'123."
        )

    # Split on the first apostrophe only; anything after belongs to the value.
    prefix_raw, _, value_part = input_str.partition(SEPARATOR)

    # 4. Normalise and look up the prefix.
    prefix = prefix_raw.upper()
    if prefix not in PREFIX_TO_MODE:
        known = ", ".join(f"{k} ({v.lower()})" for k, v in PREFIX_TO_MODE.items())
        return _failure(f"Unknown prefix '{prefix_raw}'. Supported: {known}.")

    base_mode = PREFIX_TO_MODE[prefix]

    # 5. A value must follow the separator.
    if not value_part:
        return _failure(
            f"No value found after prefix '{prefix}{SEPARATOR}'.",
            base_mode=base_mode,
        )

    # 6. Every character in the value must be a valid digit for the base.
    if not re.fullmatch(VALID_DIGIT_PATTERN[base_mode], value_part):
        return _failure(_digit_error(base_mode, value_part), base_mode=base_mode)

    # All checks passed.
    return _success(base_mode, value_part)
