# ------------------ OCTAL MODULE ------------------
# Implemented by: Piyush Wadadare

# ------------------ CONVERSIONS ------------------

def octal_to_decimal(octal_str):
    digits = octal_str[2:]   # remove "O'"
    decimal = int(digits, 8)
    return f"D'{decimal}"


def decimal_to_octal(decimal_str):
    num = int(decimal_str[2:])   # remove "D'"
    return f"O'{oct(num)[2:]}"