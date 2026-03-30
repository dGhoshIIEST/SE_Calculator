def perform_and(a, b):
    return int(a) & int(b)

def perform_or(a, b):
    return int(a) | int(b)

def perform_xor(a, b):
    return int(a) ^ int(b)

def perform_not(a):
    return ~int(a)

def perform_left_shift(a, b):
    shift_count = int(b)
    if shift_count < 0:
        raise ValueError("Negative shift count")
    return int(a) << int(b)

def perform_right_shift(a, b):
    shift_count = int(b)
    if shift_count < 0:
        raise ValueError("Negative shift count")
    return int(a) >> shift_count

def perform_bit_masking(val, mask):
    return int(val) & int(mask)

def perform_bit_counting(a):
    val = int(a)
    if val < 0:
        return bin(val & 0xFFFFFFFF).count('1')
    return bin(val).count('1')

def perform_bit_rotation_left(val, shift, bit_size=32):
    v = int(val)
    s = int(shift) % bit_size
    mask = (1 << bit_size) - 1
    return ((v << s) & mask) | ((v >> (bit_size - s)) & mask)

def perform_bit_rotation_right(val, shift, bit_size=32):
    v = int(val)
    s = int(shift) % bit_size
    mask = (1 << bit_size) - 1
    return ((v >> s) & mask) | ((v << (bit_size - s)) & mask)