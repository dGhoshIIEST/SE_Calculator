import math


def power(a, b):
    x = float(a)
    y = float(b)
    res = x ** y
    if res == int(res):
        return str(int(res))
    return str(res)


def modulo(a, b):
    x = float(a)
    y = float(b)
    if y == 0:
        raise ValueError("modulo by zero")
    res = x % y
    if res == int(res):
        return str(int(res))
    return str(res)


def floor_div(a, b):
    x = float(a)
    y = float(b)
    if y == 0:
        raise ValueError("floor division by zero")
    res = x // y
    return str(int(res))


def sqrt(a):
    x = float(a)
    if x < 0:
        raise ValueError("cant take sqrt of negative number")
    res = math.sqrt(x)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def cbrt(a):
    x = float(a)
    if x >= 0:
        res = x ** (1 / 3)
    else:
        res = -((-x) ** (1 / 3))
    res = round(res, 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def log(a):
    x = float(a)
    if x <= 0:
        raise ValueError("log of non-positive number")
    res = math.log10(x)
    res = round(res, 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def ln(a):
    x = float(a)
    if x <= 0:
        raise ValueError("ln of non-positive number")
    res = math.log(x)
    res = round(res, 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def exp(a):
    x = float(a)
    res = math.exp(x)
    res = round(res, 10)
    return str(res)


def ceil(a):
    x = float(a)
    return str(math.ceil(x))


def floor(a):
    x = float(a)
    return str(math.floor(x))


def factorial(n):
    x = int(n)
    if x < 0:
        raise ValueError("factorial of negative number")
    return str(math.factorial(x))


def permutation(n, r):
    n1 = int(n)
    r1 = int(r)
    if n1 < 0 or r1 < 0:
        raise ValueError("need non-negative integers")
    if n1 < r1:
        raise ValueError("n must be >= r")
    res = math.factorial(n1) // math.factorial(n1 - r1)
    return str(res)


def combination(n, r):
    n1 = int(n)
    r1 = int(r)
    if n1 < 0 or r1 < 0:
        raise ValueError("need non-negative integers")
    if n1 < r1:
        raise ValueError("n must be >= r")
    res = math.comb(n1, r1)
    return str(res)
