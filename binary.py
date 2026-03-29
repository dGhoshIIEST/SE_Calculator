from exceptions import invalidbinaryerror


def check_binary(b):
    b = b.strip()
    if not b:
        raise invalidbinaryerror("empty binary string")
    for ch in b:
        if ch not in ('0', '1'):
            raise invalidbinaryerror(f"invalid digit: '{ch}'")


def binary_to_decimal(b):
    b = b.strip()
    check_binary(b)
    return str(int(b, 2))


def decimal_to_binary(d):
    num = int(d.strip())
    if num < 0:
        return '-' + bin(abs(num))[2:]
    return bin(num)[2:]


def binary_add(a, b):
    a, b = a.strip(), b.strip()
    check_binary(a)
    check_binary(b)
    res = int(a, 2) + int(b, 2)
    return bin(res)[2:]


def binary_subtract(a, b):
    a, b = a.strip(), b.strip()
    check_binary(a)
    check_binary(b)
    res = int(a, 2) - int(b, 2)
    if res < 0:
        return '-' + bin(abs(res))[2:]
    return bin(res)[2:]


def binary_multiply(a, b):
    a, b = a.strip(), b.strip()
    check_binary(a)
    check_binary(b)
    res = int(a, 2) * int(b, 2)
    return bin(res)[2:]


def ones_complement(b):
    b = b.strip()
    check_binary(b)
    return ''.join('1' if bit == '0' else '0' for bit in b)


def twos_complement(b):
    b = b.strip()
    check_binary(b)
    ones = ones_complement(b)
    res = int(ones, 2) + 1
    width = len(b)
    binary_res = bin(res)[2:]
    if len(binary_res) > width:
        binary_res = binary_res[-width:]
    else:
        binary_res = binary_res.zfill(width)
    return binary_res
