from exceptions import InvalidInputError, InvalidFormatError, InvalidFractionError


def parse_fraction(s):
    if not isinstance(s, str):
        raise InvalidInputError()

    s = s.strip()

    if '/' not in s:
        raise InvalidFormatError()

    parts = s.split('/')

    if len(parts) != 2:
        raise InvalidFormatError()

    try:
        num = int(parts[0])
        den = int(parts[1])
    except:
        raise InvalidInputError()

    return Fraction(num, den)
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise InvalidFractionError()

        # normalize sign
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise InvalidInputError()

        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise InvalidInputError()

        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise InvalidInputError()

        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise InvalidInputError()

        if other.numerator == 0:
            raise InvalidFractionError()

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


