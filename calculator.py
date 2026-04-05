from expression_parser import evaluate_expression

class Calculator:
    # mode can be 1: Fraction, 2: Bin, 3: Oct, 4: Hex, 5: Set, 6: Matrix, default  = 0
    mode = 0
    
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
        try:
            return evaluate_expression(expr)
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
