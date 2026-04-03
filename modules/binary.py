# -- Pritam 038 -------------------------------------------------------

import re
import sys

from exceptions.binary_exceptions import InvalidBinaryInputError, NegativeBinaryResultError


def _strip(b: str) -> str:
    """Strip B' prefix and whitespace."""
    b = b.strip().upper()
    if b.startswith("B'"):
        b = b[2:]
    return b


def _validate(b: str) -> None:
    if not b or not all(c in '01' for c in b):
        raise InvalidBinaryInputError(b)


def binary_to_decimal(b: str) -> str:
    """
    Convert binary string to decimal.
    e.g. binary_to_decimal("B'1010") -> "D'10"
    """
    raw = _strip(b)
    _validate(raw)
    return f"D'{int(raw, 2)}"


def decimal_to_binary(d: str) -> str:
    """
    Convert decimal string to binary.
    e.g. decimal_to_binary("D'10") -> "B'1010"
    """
    d = d.strip().upper()
    if d.startswith("D'"):
        d = d[2:]
    n = int(d)
    if n < 0:
        raise ValueError("Negative decimal not supported in basic mode")
    return f"B'{bin(n)[2:]}"

  

# ── Saiyam 037: Arithmetic ──────────────────────────────────────────────────────

def binary_add(a: str, b: str) -> str:
    """
    Add two binary numbers.
    e.g. binary_add("B'011", "B'010") -> "B'101"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da + db}")


def binary_subtract(a: str, b: str) -> str:
    """
    Subtract two binary numbers.
    e.g. binary_subtract("B'101", "B'010") -> "B'011"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if da < db:
        raise NegativeBinaryResultError()
    bit_len = max(len(_strip(a)), len(_strip(b)))
    result = bin(da - db)[2:].zfill(bit_len)
    return f"B'{result}"


def binary_multiply(a: str, b: str) -> str:
    """
    Multiply two binary numbers.
    e.g. binary_multiply("B'011", "B'010") -> "B'110"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da * db}")


def binary_divide(a: str, b: str) -> str:
    """
    Integer divide two binary numbers.
    e.g. binary_divide("B'110", "B'010") -> "B'11"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if db == 0:
        raise ValueError("Binary division by zero")
    return decimal_to_binary(f"D'{da // db}")



#-----------suhani 034: complement-------------------------------


def ones_complement(b: str) -> str:
    """
    Flip all bits.
    e.g. ones_complement("B'1010") -> "B'0101"
    """
    raw = _strip(b)
    _validate(raw)
    return "B'" + ''.join('1' if bit == '0' else '0' for bit in raw)


def twos_complement(b: str) -> str:
    """
    Add 1 to the one's complement.
    e.g. twos_complement("B'0111") -> "B'1001"
    """
    raw = _strip(b)
    _validate(raw)
    ones = ones_complement(f"B'{raw}")[2:]
    val = int(ones, 2) + 1                         # no modulo
    result = bin(val)[2:].zfill(len(ones))         # zfill won't truncate carry
    return f"B'{result}"


# ── Mode 2 Inherited Class ──────────────────────────────────────────────────────
from calculator import Calculator

class Binary(Calculator):
    def __init__(self):
        super().__init__()
        self.mode = 2

    def _normalize_binary(self, value: str) -> str:
        token = str(value).strip().upper()
        if token.startswith("B'"):
            return token
        if token and all(ch in "01" for ch in token):
            return f"B'{token}"
        return token

    def add(self, a, b):
        if self.mode == 2 and isinstance(a, str) and isinstance(b, str):
            left = self._normalize_binary(a)
            right = self._normalize_binary(b)
            return binary_add(left, right)
        return super().add(a, b)

    def subtract(self, a, b):
        if self.mode == 2 and isinstance(a, str) and isinstance(b, str):
            left = self._normalize_binary(a)
            right = self._normalize_binary(b)
            return binary_subtract(left, right)
        return super().subtract(a, b)

    def multiply(self, a, b):
        if self.mode == 2 and isinstance(a, str) and isinstance(b, str):
            left = self._normalize_binary(a)
            right = self._normalize_binary(b)
            return binary_multiply(left, right)
        return super().multiply(a, b)

    def divide(self, a, b):
        if self.mode == 2 and isinstance(a, str) and isinstance(b, str):
            left = self._normalize_binary(a)
            right = self._normalize_binary(b)
            return binary_divide(left, right)
        return super().divide(a, b)

    def evaluate(self, expression: str):
        if self.mode == 2:
            parts = str(expression).split()
            if len(parts) == 3:
                left, op, right = parts
                left = self._normalize_binary(left)
                right = self._normalize_binary(right)
                
                if op == "+": return binary_add(left, right)
                if op == "-": return binary_subtract(left, right)
                if op == "*": return binary_multiply(left, right)
                if op == "/": return binary_divide(left, right)
            raise ValueError("Expression must be in format: <bin> <op> <bin>")
            
        return Calculator.evaluate(self.mode)
