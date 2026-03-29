import math
from exceptions import zerodenominatorerror, invalidfractionerror


def parse_frac(s):
    s = s.strip()
    if '/' in s:
        parts = s.split('/')
        if len(parts) != 2:
            raise invalidfractionerror(f"bad fraction: '{s}'")
        try:
            num = int(parts[0].strip())
            den = int(parts[1].strip())
        except ValueError:
            raise invalidfractionerror(f"bad fraction: '{s}'")
    else:
        try:
            num = int(s)
            den = 1
        except ValueError:
            raise invalidfractionerror(f"bad fraction: '{s}'")
    if den == 0:
        raise zerodenominatorerror("denominator is zero")
    return num, den


def simplify(num, den):
    if num == 0:
        return 0, 1
    if den < 0:
        num, den = -num, -den
    g = math.gcd(abs(num), abs(den))
    return num // g, den // g


def format_frac(num, den):
    num, den = simplify(num, den)
    if den == 1:
        return str(num)
    return f"{num}/{den}"


def add_fraction(a, b):
    n1, d1 = parse_frac(a)
    n2, d2 = parse_frac(b)
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    return format_frac(num, den)


def sub_fraction(a, b):
    n1, d1 = parse_frac(a)
    n2, d2 = parse_frac(b)
    num = n1 * d2 - n2 * d1
    den = d1 * d2
    return format_frac(num, den)


def mul_fraction(a, b):
    n1, d1 = parse_frac(a)
    n2, d2 = parse_frac(b)
    num = n1 * n2
    den = d1 * d2
    return format_frac(num, den)


def div_fraction(a, b):
    n1, d1 = parse_frac(a)
    n2, d2 = parse_frac(b)
    if n2 == 0:
        raise zerodenominatorerror("cant divide by zero fraction")
    num = n1 * d2
    den = d1 * n2
    return format_frac(num, den)
