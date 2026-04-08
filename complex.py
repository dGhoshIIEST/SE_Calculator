import cmath
import math
from exceptions import invalidcomplexerror


def parse_complex(s):
    s = s.strip().strip('(').strip(')')
    try:
        return complex(s.replace(' ', ''))
    except ValueError:
        raise invalidcomplexerror(f"cant parse: '{s}'")


def format_complex(c):
    real = round(c.real, 10)
    imag = round(c.imag, 10)

    if imag == 0:
        if real == int(real):
            return str(int(real))
        return str(real)

    if real == 0:
        if imag == int(imag):
            return f"{int(imag)}j"
        return f"{imag}j"

    real_str = str(int(real)) if real == int(real) else str(real)
    imag_val = int(imag) if imag == int(imag) else imag

    if imag_val >= 0:
        return f"{real_str}+{imag_val}j"
    else:
        return f"{real_str}{imag_val}j"


def add_complex(a, b):
    c1 = parse_complex(a)
    c2 = parse_complex(b)
    return format_complex(c1 + c2)


def subtract_complex(a, b):
    c1 = parse_complex(a)
    c2 = parse_complex(b)
    return format_complex(c1 - c2)


def multiply_complex(a, b):
    c1 = parse_complex(a)
    c2 = parse_complex(b)
    return format_complex(c1 * c2)


def divide_complex(a, b):
    c1 = parse_complex(a)
    c2 = parse_complex(b)
    if c2 == 0:
        raise ValueError("cant divide by zero")
    return format_complex(c1 / c2)


def magnitude(a):
    c = parse_complex(a)
    res = round(abs(c), 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def phase(a):
    c = parse_complex(a)
    res = round(math.degrees(cmath.phase(c)), 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)
