import math
from exceptions import undefinedoperationerror


def sin(x):
    angle = float(x)
    res = round(math.sin(math.radians(angle)), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)


def cos(x):
    angle = float(x)
    res = round(math.cos(math.radians(angle)), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)


def tan(x):
    angle = float(x)
    cos_val = math.cos(math.radians(angle))
    if abs(cos_val) < 1e-10:
        raise undefinedoperationerror(f"tan({x}) is undefined")
    res = round(math.tan(math.radians(angle)), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)


def asin(x):
    val = float(x)
    if val < -1 or val > 1:
        raise ValueError(f"asin({x}) out of range")
    res = round(math.degrees(math.asin(val)), 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def acos(x):
    val = float(x)
    if val < -1 or val > 1:
        raise ValueError(f"acos({x}) out of range")
    res = round(math.degrees(math.acos(val)), 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def atan(x):
    val = float(x)
    res = round(math.degrees(math.atan(val)), 10)
    if res == int(res):
        return str(int(res)) + ".0"
    return str(res)


def sinh(x):
    val = float(x)
    res = round(math.sinh(val), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)


def cosh(x):
    val = float(x)
    res = round(math.cosh(val), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)


def tanh(x):
    val = float(x)
    res = round(math.tanh(val), 10)
    if res == int(res):
        return str(int(res)) + ".0" if int(res) != res else str(res)
    return str(res)
