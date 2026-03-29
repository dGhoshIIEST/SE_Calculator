#Prashant Dubey
#Aritmetic operations in Octal Base
def add_octal(a, b):
    d1 = int(validate_octal(a), 8)
    d2 = int(validate_octal(b), 8)
    return f"O'{oct(d1 + d2)[2:]}"


def subtract_octal(a, b):
    d1 = int(validate_octal(a), 8)
    d2 = int(validate_octal(b), 8)
    result = d1 - d2

    if result < 0:
        raise ValueError("Negative result not supported")

    return f"O'{oct(result)[2:]}"


def multiply_octal(a, b):
    d1 = int(validate_octal(a), 8)
    d2 = int(validate_octal(b), 8)
    return f"O'{oct(d1 * d2)[2:]}"


def divide_octal(a, b):
    d1 = int(validate_octal(a), 8)
    d2 = int(validate_octal(b), 8)

    if d2 == 0:
        raise ValueError("Division by zero")

    return f"O'{oct(d1 // d2)[2:]}"
