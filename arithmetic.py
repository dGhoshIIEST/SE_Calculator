from typing import Tuple

def octal_add(op1: str, op2: str) -> str:
    i, j = len(op1) - 1, len(op2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        d1 = int(op1[i]) if i >= 0 else 0
        d2 = int(op2[j]) if j >= 0 else 0

        total = d1 + d2 + carry
        result.append(str(total % 8))
        carry = total // 8

        i -= 1
        j -= 1

    return ''.join(result[::-1])


def octal_multiply(op1: str, op2: str) -> str:
    result = "0"

    op2 = op2[::-1]
    for i, d2 in enumerate(op2):
        carry = 0
        temp = []

        for d1 in op1[::-1]:
            prod = int(d1) * int(d2) + carry
            temp.append(str(prod % 8))
            carry = prod // 8

        if carry:
            temp.append(str(carry))

        temp = ''.join(temp[::-1]) + ('0' * i)
        result = octal_add(result, temp)

    return result.lstrip('0') or "0"


def get_complement(value: str, comp_type: int) -> str:
    if comp_type not in (7, 8):
        raise ValueError("comp_type must be 7 or 8")

    # 7's complement → subtract each digit from 7
    if comp_type == 7:
        return ''.join(str(7 - int(d)) for d in value)

    # 8's complement → 7's complement + 1
    seven_comp = ''.join(str(7 - int(d)) for d in value)
    return octal_add(seven_comp, "1")