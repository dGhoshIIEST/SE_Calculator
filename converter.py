from typing import Optional
import parser
import validator


def convert(value: str, from_base: str, to_base: str) -> str:
    """
    Convert a numeric value between octal and decimal bases.

    Args:
        value: Numeric string without prefix (e.g., '247')
        from_base: Source base ('OCT' or 'DEC')
        to_base: Target base ('OCT' or 'DEC')

    Returns:
        Converted value with base prefix (e.g., 'D'167' or 'O'247')

    Raises:
        ValueError: If from_base or to_base is invalid, or if value contains invalid digits for from_base
    """
    # Normalize bases to uppercase
    from_base = from_base.upper()
    to_base = to_base.upper()

    # Validate bases
    if from_base not in ('OCT', 'DEC'):
        raise ValueError(f"Invalid from_base '{from_base}'. Must be 'OCT' or 'DEC'")
    if to_base not in ('OCT', 'DEC'):
        raise ValueError(f"Invalid to_base '{to_base}'. Must be 'OCT' or 'DEC'")

    # Convert to decimal first
    try:
        if from_base == 'OCT':
            decimal_value = int(value, 8)
        else:  # from_base == 'DEC'
            decimal_value = int(value, 10)
    except ValueError:
        raise ValueError(f"Invalid digits in value '{value}' for base {from_base}")

    # Convert to target base
    if to_base == 'DEC':
        result = str(decimal_value)
        prefix = 'D'
    else:  # to_base == 'OCT'
        result = oct(decimal_value)[2:]  # Remove '0o' prefix
        prefix = 'O'

    return f"{prefix}'{result}'"