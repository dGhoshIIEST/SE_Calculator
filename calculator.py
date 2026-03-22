from set import SetOperations


class Calculator:
    def __init__(self):
        self.set_ops = SetOperations()

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

    def set_union(self, left, right):
        return self.set_ops.union(left, right)

    def set_intersection(self, left, right):
        return self.set_ops.intersection(left, right)

    def set_difference(self, left, right):
        return self.set_ops.difference(left, right)

    def set_symmetric_difference(self, left, right):
        return self.set_ops.symmetric_difference(left, right)

    def set_is_subset(self, left, right):
        return self.set_ops.is_subset(left, right)

    def set_is_superset(self, left, right):
        return self.set_ops.is_superset(left, right)

    def evaluate(self, expression, mode="set"):
        if mode != "set":
            raise ValueError("Only set mode is supported in this repository state")
        return self.set_ops.evaluate_expression(expression)
