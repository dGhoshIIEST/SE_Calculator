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
        #Removing all spaces to make parsing predictable
        expression = expression.replace(" ", "")
        
        #Regex pattern to find: (something) operator (something)
        # The \( and \) match the literal parentheses. 
        # The (.*?) captures the number string inside them.
        # The ([\+\-\*\/]) captures the math operator.
        pattern = r'\((.*?)\)([\+\-\*\/])\((.*?)\)'
        match = re.fullmatch(pattern, expression)
        
        if not match:
            raise ValueError("Invalid expression format. Expected format: (a+bj)*(c+dj)")
            
        #Extracting the pieces
        num1_str, operator, num2_str = match.groups()
        
        try:
           
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        except ValueError:
            raise ValueError("Could not parse numbers. Ensure format is like 3+2j")
            
        # Route to the correct math function we built earlier
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