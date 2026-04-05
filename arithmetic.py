# arithmetic.py

import math

def format_result(x):
    return str(int(x)) if x == int(x) else str(x)

def add(a, b):
    return format_result(float(a) + float(b))

def sub(a, b):
    return format_result(float(a) - float(b))

def mul(a, b):
    return format_result(float(a) * float(b))

def div(a, b):
    a, b = float(a), float(b)
    if b == 0:
        raise ValueError("Division by zero")
    return format_result(a / b)

def modulo(a, b):
    a, b = float(a), float(b)
    if b == 0:
        raise ValueError("Modulo by zero")
    return format_result(a % b)

def power(a, b):
    return format_result(float(a) ** float(b))

def factorial(n):
    n = float(n)
    if n < 0:
        raise ValueError("Negative factorial")
    return format_result(math.factorial(int(n)))

def sqrt(x):
    return format_result(math.sqrt(float(x)))

def cbrt(x):
    return format_result(float(x) ** (1/3))

def log(x):
    return format_result(math.log10(float(x)))

def floor(x):
    return format_result(math.floor(float(x)))

def ceil(x):
    return format_result(math.ceil(float(x)))

