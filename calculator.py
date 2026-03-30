import re
from trigonometry_module.trigonometric import Trigonometric

class Calculator:
    
    def __init__(self):
        self.trig = Trigonometric()

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

    def evaluate(self, expr):
        expr = expr.replace(" ", "")

        functions = [
            ("asin", self.trig.asin),
            ("acos", self.trig.acos),
            ("atan", self.trig.atan),
            ("sinh", self.trig.sinh),
            ("cosh", self.trig.cosh),
            ("tanh", self.trig.tanh),
            ("sin", self.trig.sin),
            ("cos", self.trig.cos),
            ("tan", self.trig.tan),
        ]

        for name, func in functions:
            expr = re.sub(rf'{name}\((.*?)\)', lambda m: str(func(m.group(1))) if m.group(1) != "" else (_ for _ in ()).throw(ValueError("Empty input")), expr)

        try:
            return eval(expr)
        except ZeroDivisionError:
                raise ValueError("Division by zero")
        except Exception:
                raise ValueError("Invalid expression")