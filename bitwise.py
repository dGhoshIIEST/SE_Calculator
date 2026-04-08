def check_int(val, name="value"):
    try:
        return int(val)
    except (ValueError, TypeError):
        raise TypeError(f"{name} must be an integer, got: '{val}'")


def bitwise_and(a, b):
    return str(check_int(a) & check_int(b))


def bitwise_or(a, b):
    return str(check_int(a) | check_int(b))


def bitwise_xor(a, b):
    return str(check_int(a) ^ check_int(b))


def bitwise_not(a):
    return str(~check_int(a))


def left_shift(a, n):
    val = check_int(a)
    shift = check_int(n, "shift amount")
    if shift < 0:
        raise ValueError("shift cant be negative")
    return str(val << shift)


def right_shift(a, n):
    val = check_int(a)
    shift = check_int(n, "shift amount")
    if shift < 0:
        raise ValueError("shift cant be negative")
    return str(val >> shift)


def bit_count(a):
    val = check_int(a)
    return str(bin(val).count('1'))


def bit_mask(a, mask):
    return str(check_int(a) & check_int(mask))


def left_rotate(a, n, bit_width):
    val = check_int(a)
    rot = check_int(n, "rotation")
    width = check_int(bit_width, "bit width")
    if width <= 0:
        raise ValueError("bit width must be positive")
    rot = rot % width
    mask = (1 << width) - 1
    val = val & mask
    res = ((val << rot) | (val >> (width - rot))) & mask
    return bin(res)


def right_rotate(a, n, bit_width):
    val = check_int(a)
    rot = check_int(n, "rotation")
    width = check_int(bit_width, "bit width")
    if width <= 0:
        raise ValueError("bit width must be positive")
    rot = rot % width
    mask = (1 << width) - 1
    val = val & mask
    res = ((val >> rot) | (val << (width - rot))) & mask
    return bin(res)
