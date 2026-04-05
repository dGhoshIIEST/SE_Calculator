from hex import HexCalculator


class Calculator:
    # mode can be 1: Fraction, 2: Bin, 3: Oct, 4: Hex, 5: Set, 6: Matrix, default = 0
    mode = 0

    MODE_MAP = {
        "fraction": 1,
        "bin": 2,
        "oct": 3,
        "hex": 4,
        "set": 5,
        "matrix": 6
    }

    REVERSE_MODE_MAP = {v: k for k, v in MODE_MAP.items()}

    def __init__(self):
        self.mode = None
        self.hex_calc = HexCalculator()

    def set_mode(self, mode):
        """
        Set calculator mode.
        Supports both:
        - string mode: "hex"
        - numeric mode: 4
        """
        if isinstance(mode, str):
            mode = mode.lower().strip()
            if mode not in self.MODE_MAP:
                raise ValueError(f"Unsupported mode: {mode}")
            self.mode = mode

        elif isinstance(mode, int):
            if mode not in self.REVERSE_MODE_MAP:
                raise ValueError(f"Unsupported mode number: {mode}")
            self.mode = self.REVERSE_MODE_MAP[mode]

        else:
            raise ValueError("Mode must be either string or integer")

    def get_mode(self):
        return self.mode

    def _ensure_hex_mode(self):
        if self.mode != "hex":
            raise ValueError(f"Current mode is '{self.mode}', not 'hex'")

    # -------------------------------
    # Common arithmetic interface
    # -------------------------------
    def add(self, a, b):
        if self.mode == "hex":
            return self.hex_calc.add(a, b)
        return a + b

    def subtract(self, a, b):
        if self.mode == "hex":
            return self.hex_calc.subtract(a, b)
        return a - b

    def multiply(self, a, b):
        if self.mode == "hex":
            return self.hex_calc.multiply(a, b)
        return a * b

    def divide(self, a, b):
        if self.mode == "hex":
            return self.hex_calc.divide(a, b)

        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    # -------------------------------
    # HEX-specific extra operations
    # -------------------------------
    def hex_to_decimal(self, value):
        self._ensure_hex_mode()
        return self.hex_calc.hex_to_decimal(value)

    def decimal_to_hex(self, value):
        self._ensure_hex_mode()
        return self.hex_calc.decimal_to_hex(value)

    def fifteen_complement(self, value):
        self._ensure_hex_mode()
        return self.hex_calc.fifteen_complement(value)

    def sixteen_complement(self, value):
        self._ensure_hex_mode()
        return self.hex_calc.sixteen_complement(value)

    # -------------------------------
    # Unified evaluator / dispatcher
    # -------------------------------
    def evaluate(self, operation, a, b=None):
        """
        Evaluate an operation based on current mode.

        Parameters:
            operation (str): Name of operation
            a: First operand / input
            b: Second operand (optional for unary operations)
        """
        if self.mode is None:
            raise ValueError("Calculator mode is not set")

        if self.mode == "hex":
            if operation == "add":
                return self.add(a, b)
            elif operation == "subtract":
                return self.subtract(a, b)
            elif operation == "multiply":
                return self.multiply(a, b)
            elif operation == "divide":
                return self.divide(a, b)
            elif operation == "hex_to_decimal":
                return self.hex_to_decimal(a)
            elif operation == "decimal_to_hex":
                return self.decimal_to_hex(a)
            elif operation == "fifteen_complement":
                return self.fifteen_complement(a)
            elif operation == "sixteen_complement":
                return self.sixteen_complement(a)
            else:
                raise ValueError(f"Unsupported HEX operation: {operation}")

        elif self.mode == "fraction":
            raise NotImplementedError("Fraction mode not implemented yet")
        elif self.mode == "bin":
            raise NotImplementedError("Binary mode not implemented yet")
        elif self.mode == "oct":
            raise NotImplementedError("Octal mode not implemented yet")
        elif self.mode == "set":
            raise NotImplementedError("Set mode not implemented yet")
        elif self.mode == "matrix":
            raise NotImplementedError("Matrix mode not implemented yet")

        else:
            raise ValueError("Invalid calculator mode")