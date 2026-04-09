from exceptions import invalidoctalerror


def check_octal(o):
    o = o.strip()
    if not o:
        raise invalidoctalerror("empty octal string")
    for ch in o:
        if ch not in '01234567':
            raise invalidoctalerror(f"invalid digit: '{ch}'")


def octal_to_decimal(o):
    o = o.strip()
    check_octal(o)
    return str(int(o, 8))


def decimal_to_octal(d):
    num = int(d.strip())
    if num < 0:
        return '-' + oct(abs(num))[2:]
    return oct(num)[2:]


def octal_add(a, b):
    a, b = a.strip(), b.strip()
    check_octal(a)
    check_octal(b)
    res = int(a, 8) + int(b, 8)
    return oct(res)[2:]


def octal_subtract(a, b):
    a, b = a.strip(), b.strip()
    check_octal(a)
    check_octal(b)
    res = int(a, 8) - int(b, 8)
    if res < 0:
        return '-' + oct(abs(res))[2:]
    return oct(res)[2:]


def octal_multiply(a, b):
    a, b = a.strip(), b.strip()
    check_octal(a)
    check_octal(b)
    res = int(a, 8) * int(b, 8)
    return oct(res)[2:]


def sevens_complement(o):
    o = o.strip()
    check_octal(o)
    return ''.join(str(7 - int(d)) for d in o)


def eights_complement(o):
    o = o.strip()
    check_octal(o)
    sevens = sevens_complement(o)
    res = int(sevens, 8) + 1
    return oct(res)[2:]
