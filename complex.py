import re

import cmath

class ComplexCalculator:
    def __init__(self):
        pass

    def add(self, a: complex, b: complex) -> complex:
        return a + b

    def subtract(self, a: complex, b: complex) -> complex:
        return a - b

    def multiply(self, a: complex, b: complex) -> complex:
        return a * b

    def divide(self, a: complex, b: complex) -> complex:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def get_magnitude(self, a: complex) -> float:
        return abs(a)

    def get_phase(self, a: complex) -> float:
        return cmath.phase(a)
    
    def parse_and_calculate(self, expression: str) -> complex:
        # 1. Remove all spaces to make parsing predictable
        expression = expression.replace(" ", "")
        
        # 2. Regex pattern to find: (something) operator (something)
        # The \( and \) match the literal parentheses. 
        # The (.*?) captures the number string inside them.
        # The ([\+\-\*\/]) captures the math operator.
        pattern = r'\((.*?)\)([\+\-\*\/])\((.*?)\)'
        match = re.match(pattern, expression)
        
        if not match:
            raise ValueError("Invalid expression format. Expected format: (a+bj)*(c+dj)")
            
        # 3. Extract the pieces
        num1_str, operator, num2_str = match.groups()
        
        try:
            # Python's built-in complex() is smart enough to turn '3+2j' into a real complex number!
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        except ValueError:
            raise ValueError("Could not parse numbers. Ensure format is like 3+2j")
            
        # 4. Route to the correct math function we built earlier
        if operator == '+':
            return self.add(num1, num2)
        elif operator == '-':
            return self.subtract(num1, num2)
        elif operator == '*':
            return self.multiply(num1, num2)
        elif operator == '/':
            return self.divide(num1, num2)
        else:
            raise ValueError("Unknown operator")