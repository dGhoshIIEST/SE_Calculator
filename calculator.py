from octal import *
from octal_conversion import *
from validate_octal import *
from arithmetic import *

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def oct_to_dec(self, o):
        return octal_to_decimal(o)

    def dec_to_oct(self, d):
        return decimal_to_octal(d)

    def add_oct(self, a, b):
        return add_octal(a, b)

    def sub_oct(self, a, b):
        return subtract_octal(a, b)

    def mul_oct(self, a, b):
        return multiply_octal(a, b)

    def div_oct(self, a, b):
        return divide_octal(a, b)

    def seven_comp(self, o):
        return sevensComplement(o)

    def eight_comp(self, o):
        return eightsComplement(o)