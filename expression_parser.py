import re
import ast
from trigonometric import Trignometry
from calculator import Calculator

class ExpressionParser:
    def __init__(self):
        self.trig = Trignometry()
        self.calc = Calculator()

    def evaluate(self, expression):
        expression = expression.replace(" ", "")

        pattern = r'(sin|cos|tan|asin|acos|atan|sinh|cosh|tanh)\(([-]?\d+\.?\d*)\)'

        def replace_trig(match):
            func_name = match.group(1)
            value = float(match.group(2))

            trig_methods = {
                'sin': self.trig.sin_deg,
                'cos': self.trig.cos_deg,
                'tan': self.trig.tan_deg,
                'asin': self.trig.asin_deg,
                'acos': self.trig.acos_deg,
                'atan': self.trig.atan_deg,
                'sinh': self.trig.sinh_val,
                'cosh': self.trig.cosh_val,
                'tanh': self.trig.tanh_val
            }

            if func_name in trig_methods:
                result = trig_methods[func_name](value)
                return str(result)
            return match.group(0)

        while re.search(pattern, expression):
            expression = re.sub(pattern, replace_trig, expression)

        operators = {
            ast.Add: self.calc.add,
            ast.Sub: self.calc.subtract,
            ast.Mult: self.calc.multiply,
            ast.Div: self.calc.divide
        }

        def evaluate_ast(node):
            if isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = evaluate_ast(node.left)
                right = evaluate_ast(node.right)
                return operators[type(node.op)](left, right)
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate_ast(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return operand
            raise TypeError(f"Unsupported operation in expression.")

        node = ast.parse(expression, mode='eval').body
        return evaluate_ast(node)

if __name__ == "__main__":
    parser = ExpressionParser()
    print(parser.evaluate("3 + 2 * sin(30)"))