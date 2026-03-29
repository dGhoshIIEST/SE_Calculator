from exceptions import invalidhexerror


def check_hex(h):
    h = h.strip()
    if not h:
        raise invalidhexerror("empty hex string")
    valid = set('0123456789ABCDEFabcdef')
    for ch in h:
        if ch not in valid:
            raise invalidhexerror(f"invalid character: '{ch}'")


def hex_to_decimal(h):
    h = h.strip()
    check_hex(h)
    return str(int(h, 16))


def decimal_to_hex(d):
    num = int(d.strip())
    if num < 0:
        return '-' + hex(abs(num))[2:].upper()
    return hex(num)[2:].upper()


def hex_add(a, b):
    a, b = a.strip(), b.strip()
    check_hex(a)
    check_hex(b)
    res = int(a, 16) + int(b, 16)
    return hex(res)[2:].upper()


def hex_subtract(a, b):
    a, b = a.strip(), b.strip()
    check_hex(a)
    check_hex(b)
    res = int(a, 16) - int(b, 16)
    if res < 0:
        return '-' + hex(abs(res))[2:].upper()
    return hex(res)[2:].upper()


def hex_multiply(a, b):
    a, b = a.strip(), b.strip()
    check_hex(a)
    check_hex(b)
    res = int(a, 16) * int(b, 16)
    return hex(res)[2:].upper()


def fifteens_complement(h):
    h = h.strip()
    check_hex(h)
    result = []
    for ch in h.upper():
        val = int(ch, 16)
        result.append(hex(15 - val)[2:].upper())
    return ''.join(result)


def sixteens_complement(h):
    h = h.strip()
    check_hex(h)
    fifteens = fifteens_complement(h)
    res = int(fifteens, 16) + 1
    return hex(res)[2:].upper()
