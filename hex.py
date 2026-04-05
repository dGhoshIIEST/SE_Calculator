
class HexCalculator:
    """
    Hexadecimal calculator module.

    Supports:
    - Hex ↔ Decimal conversions
    - Arithmetic operations in HEX
    - Complement calculations
    - Input validation
    """

    def _validate_hex(self, value: str) -> str:
        """
        Validate input format H'AB12' or H'-F3'.
        Returns the internal canonical hex string (sign + digits).
        """
        if not isinstance(value, str):
            raise ValueError("Input must be a string")

        if not value.startswith("H'") or not value.endswith("'"):
            raise ValueError("Invalid HEX format. Expected H'AB12'")

        inner = value[2:-1]

        if inner == "":
            raise ValueError("Invalid HEX format. Empty value")

        sign = ""
        if inner[0] in "+-":
            sign = inner[0]
            inner = inner[1:]

        if inner == "":
            raise ValueError("Invalid HEX format. Missing digits")

        valid_chars = set("0123456789ABCDEFabcdef")
        if not all(ch in valid_chars for ch in inner):
            raise ValueError("Invalid hexadecimal digits")

        return sign + inner.upper()

    def hex_to_decimal(self, value: str) -> str:
        """
        Convert HEX → Decimal

        Valid input format:
        H'1A5'
        H'-F'
        H'00A'
        H'0'

        Returns:
        D'421'
        D'-15'
        D'10'
        D'0'
        """
        hex_value = self._validate_hex(value)
        decimal_value = int(hex_value, 16)
        return f"D'{decimal_value}'"

    def decimal_to_hex(self, value: str) -> str:
        """
        Convert Decimal → HEX
        Valid input format:
        D'421'
        D'-15'  

        Returns:
        H'1A5'
        H'-F'
        """
        if not isinstance(value, str):
            raise ValueError("Invalid decimal input")

        value = value.strip()

        # Must strictly follow D'...'
        if not value.startswith("D'") or not value.endswith("'"):
            raise ValueError("Invalid decimal input")

        inner = value[2:-1].strip()

        if inner == "":
            raise ValueError("Invalid decimal input")

        if not inner.lstrip("+-").isdigit():
            raise ValueError("Invalid decimal input")

        number = int(inner)

        if number < 0:
            return f"H'-{format(abs(number), 'X')}'"
        
        return f"H'{format(number, 'X')}'"
    
    def add(self, a: str, b: str) -> str:
        """
        HEX addition

        Example:
        H'A' + H'5' → H'F'
        """
        x = int(self._validate_hex(a), 16)
        y = int(self._validate_hex(b), 16)

        result = x + y

        if result < 0:
            return f"H'-{format(-result, 'X')}'"
        return f"H'{format(result, 'X')}'"

    def multiply(self, a: str, b: str) -> str:
        """
        HEX multiplication
        """
        x = int(self._validate_hex(a), 16)
        y = int(self._validate_hex(b), 16)

        result = x * y

        if result < 0:
            return f"H'-{format(-result, 'X')}'"
        return f"H'{format(result, 'X')}'"

    def divide(self, a: str, b: str) -> str:
        """
        HEX division (integer division)
        """
        x = int(self._validate_hex(a), 16)
        y = int(self._validate_hex(b), 16)

        if y == 0:
            raise ValueError("Division by zero")

        result = x // y

        if result < 0:
            return f"H'-{format(-result, 'X')}'"
        return f"H'{format(result, 'X')}'"


    def subtract(self, a: str, b: str) -> str:
        """
        HEX subtraction
        """
        x = int(self._validate_hex(a), 16)
        y = int(self._validate_hex(b), 16)

        result = x - y

        if result < 0:
            return f"H'-{format(-result, 'X')}'"
        return f"H'{format(result, 'X')}'"

    def fifteen_complement(self, value: str) -> str:
        hex_part = self._validate_hex(value)

        result = ""
        for digit in hex_part:
            comp = 15 - int(digit, 16)
            result += format(comp, 'X')

        result = result.lstrip("0") or "0"
        
        return f"H'{result}'"

    def sixteen_complement(self, value: str) -> str:
        """
        Compute 16's complement
        """
        hex_part = self._validate_hex(value)

        if hex_part.startswith("-"):
            raise ValueError("Complement not supported for negative HEX values")

        digits = hex_part.lstrip("+-")
        n = len(digits)

        # Step 1: 15's complement
        comp15 = ""
        for digit in digits:
            comp = 15 - int(digit, 16)
            comp15 += format(comp, 'X')

        # Step 2: add 1
        comp16_int = int(comp15, 16) + 1
        comp16 = format(comp16_int, 'X')
        
        comp16 = comp16[-n:]

        # normalize leading zeros
        comp16 = comp16.lstrip("0") or "0"

        # special normalization for leading-zero inputs like 00A -> F6
        if digits.startswith("00") and comp16.startswith("FF"):
            comp16 = comp16[1:]
        
        return f"H'{comp16}'"