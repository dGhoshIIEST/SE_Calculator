from parser import parse_input

VALID_CHARS: dict[str, set[str]] = {
    'OCT': set('01234567'),
    'DEC': set('0123456789'),
}


def validate_input(parsed: dict) -> dict:
    """
    Validates that the parsed input contains only characters
    valid for its declared base.

    Args:
        parsed: dict with keys 'value' (str) and 'base' (str, 'OCT' or 'DEC')

    Returns:
        dict with keys:
            'is_valid' (bool)
            'error'    (str | None) — None if valid, message if not
    """
    # ── 1. Structural checks ──────────────────────────────────────────────────

    if not isinstance(parsed, dict):
        return {'is_valid': False, 'error': "Input must be a dictionary."}

    if 'value' not in parsed or 'base' not in parsed:
        return {
            'is_valid': False,
            'error': "Parsed input must contain 'value' and 'base' keys.",
        }

    value: str = parsed['value']
    base: str  = parsed['base']

    # ── 2. Type checks ────────────────────────────────────────────────────────

    if not isinstance(value, str):
        return {'is_valid': False, 'error': f"'value' must be a string, got {type(value).__name__}."}

    if not isinstance(base, str):
        return {'is_valid': False, 'error': f"'base' must be a string, got {type(base).__name__}."}

    base = base.upper()

    # ── 3. Empty value ────────────────────────────────────────────────────────

    if value.strip() == '':
        return {'is_valid': False, 'error': "Input value must not be empty."}

    # ── 4. Unsupported base ───────────────────────────────────────────────────

    if base not in VALID_CHARS:
        supported = ', '.join(VALID_CHARS.keys())
        return {
            'is_valid': False,
            'error': f"Unsupported base '{base}'. Supported bases: {supported}.",
        }

    # ── 5. Character validation ───────────────────────────────────────────────

    allowed = VALID_CHARS[base]
    bad_chars = [ch for ch in value if ch not in allowed]

    if bad_chars:
        unique_bad = sorted(set(bad_chars))
        return {
            'is_valid': False,
            'error': (
                f"Invalid character(s) {unique_bad} for base {base}. "
                f"Allowed digits: {''.join(sorted(allowed))}."
            ),
        }

    return {'is_valid': True, 'error': None}
