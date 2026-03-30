import ast
import bitwise

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

    def calculate(self, expression: str):
        try:
            node = ast.parse(expression, mode='eval').body
            return self._evaluate_node(node)
        except Exception as e:
            return f"Error: {str(e)}"

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)
            op_type = type(node.op)
            if op_type == ast.Add:
                return self.add(left, right)
            elif op_type == ast.Sub:
                return self.subtract(left, right)
            elif op_type == ast.Mult:
                return self.multiply(left, right)
            elif op_type == ast.Div:
                return self.divide(left, right)
            elif op_type == ast.BitAnd:
                return bitwise.perform_and(left, right)
            elif op_type == ast.BitOr:
                return bitwise.perform_or(left, right)
            elif op_type == ast.BitXor:
                return bitwise.perform_xor(left, right)
            elif op_type == ast.LShift:
                return bitwise.perform_left_shift(left, right)
            elif op_type == ast.RShift:
                return bitwise.perform_right_shift(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = self._evaluate_node(node.operand)
            op_type = type(node.op)
            if op_type == ast.Invert:
                return bitwise.perform_not(operand)
            elif op_type == ast.USub:
                return -operand
        elif isinstance(node, ast.Call):
            func_name = node.func.id
            args = [self._evaluate_node(arg) for arg in node.args]
            if func_name == "mask":
                return bitwise.perform_bit_masking(args[0], args[1])
            elif func_name == "count_bits":
                return bitwise.perform_bit_counting(args[0])
            elif func_name == "rotate_left":
                size = args[2] if len(args) > 2 else 32
                return bitwise.perform_bit_rotation_left(args[0], args[1], size)
            elif func_name == "rotate_right":
                size = args[2] if len(args) > 2 else 32
                return bitwise.perform_bit_rotation_right(args[0], args[1], size)
        raise ValueError("Unsupported Operation")