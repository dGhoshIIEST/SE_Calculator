def validate_octal(octal_str):
    if not isinstance(octal_str, str):
        raise ValueError("Input must be a string")

    if not octal_str.startswith("O'"):
        raise ValueError("Invalid format. Must start with O'")

    digits = octal_str[2:]

    if not digits:
        raise ValueError("No digits provided")

    for d in digits:
        if d not in "01234567":
            raise ValueError("Invalid octal digit")

    return digits