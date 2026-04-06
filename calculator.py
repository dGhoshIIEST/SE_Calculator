import ast
from typing import Union

from matrix import evaluate_matrix_expression, format_matrix


class Calculator:
    # mode: 0 -> arithmetic, 6 -> matrix
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

    def _safe_eval_arithmetic(self, expression: str) -> Union[int, float]:
        node = ast.parse(expression, mode="eval")

        def go(n):
            if isinstance(n, ast.Expression):
                return go(n.body)
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                return n.value
            if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.UAdd, ast.USub)):
                v = go(n.operand)
                return v if isinstance(n.op, ast.UAdd) else -v
            if isinstance(n, ast.BinOp):
                l = go(n.left)
                r = go(n.right)
                if isinstance(n.op, ast.Add):
                    return l + r
                if isinstance(n.op, ast.Sub):
                    return l - r
                if isinstance(n.op, ast.Mult):
                    return l * r
                if isinstance(n.op, ast.Div):
                    if r == 0:
                        raise ValueError("Division by zero")
                    return l / r
            raise ValueError("Unsupported arithmetic expression")

        return go(node)

    def evaluate(self, expression: str, mode=0):
        if mode in (6, "matrix", "Matrix"):
            return evaluate_matrix_expression(expression)
        return self._safe_eval_arithmetic(expression)


if __name__ == "__main__":
    c = Calculator()
    while True:
        try:
            mode = input("Enter mode (0 for arithmetic, 6 for matrix, q to quit): ").strip()
            if mode.lower() == "q":
                break
            expr = input("Enter expression: ").strip()
            m = 6 if mode == "6" else 0
            ans = c.evaluate(expr, mode=m)
            if m == 6:
                print(format_matrix(ans))
            else:
                print(ans)
        except Exception as e:
            print(f"Error: {e}")
