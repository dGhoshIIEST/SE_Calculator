import ast

class SetOperations:
    def parse_set(self, value):
        if isinstance(value, set):
            return value

        if not isinstance(value, str):
            raise ValueError("Set input must be a string or set")

        text = value.strip()
        if text == "{}":
            return set()

        try:
            parsed = ast.literal_eval(text)
        except (SyntaxError, ValueError) as exc:
            raise ValueError("Invalid set input") from exc

        if isinstance(parsed, (set, list, tuple)):
            return set(parsed)

        raise ValueError("Set input must be a set, list, or tuple")

    def union(self, left, right):
        return self.parse_set(left) | self.parse_set(right)

    def intersection(self, left, right):
        return self.parse_set(left) & self.parse_set(right)

    def difference(self, left, right):
        return self.parse_set(left) - self.parse_set(right)

    def symmetric_difference(self, left, right):
        return self.parse_set(left) ^ self.parse_set(right)

    def is_subset(self, left, right):
        return self.parse_set(left).issubset(self.parse_set(right))

    def is_superset(self, left, right):
        return self.parse_set(left).issuperset(self.parse_set(right))

    def evaluate_expression(self, expression):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError("Expression must be a non-empty string")

        text = expression.strip()
        lowered = text.lower()

        operations = [
            (" union ", self.union),
            (" intersection ", self.intersection),
            (" difference ", self.difference),
            (" symdiff ", self.symmetric_difference),
            (" subset ", self.is_subset),
            (" superset ", self.is_superset),
        ]

        for marker, function in operations:
            if marker in lowered:
                idx = lowered.index(marker)
                left = text[:idx].strip()
                right = text[idx + len(marker):].strip()
                if not left or not right:
                    raise ValueError("Invalid set expression")
                return function(left, right)

        raise ValueError("Invalid set expression")
         #the code is checked
