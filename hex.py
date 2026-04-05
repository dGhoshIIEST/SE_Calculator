
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

        # Normalize to uppercase and keep sign
        normalized = sign + inner.upper()
        return normalized

    # -------------------------------
    # Sravanti will edit this part
    # -------------------------------
    def hex_to_decimal(self, value: str) -> str:
        """
        Convert HEX → Decimal

        Example:
        H'1A5' → D'421'
        """
<<<<<<< HEAD
        try:
            # Remove H' and '
            hex_value = value[2:-1]

            # Convert to decimal
            decimal_value = int(hex_value, 16)

            # Return in required format
            return f"D'{decimal_value}'"

        except:
            return "Invalid input"
=======
        hex_part = value[2:-1]
        decimal_value = int(hex_part, 16)
        return f"D'{decimal_value}'"
>>>>>>> FeatureB_8_Sravanthi

    # -------------------------------
    # Saichaitanya will edit this part
    # -------------------------------
    def decimal_to_hex(self, value: str) -> str:
        value = value.strip()

        if value.startswith("D'") and value.endswith("'"):
            value = value[2:-1]

        if not value.isdigit():
            raise ValueError("Invalid decimal input")

        return f"H'{hex(int(value))[2:].upper()}'"
    # -------------------------------
    # Joydip will edit this part
    # -------------------------------
    def add(self, a: str, b: str) -> str:
        """
        HEX addition

        Example:
        H'A' + H'5' → H'F'
<<<<<<< HEAD
        """
        raise NotImplementedError("add not implemented yet")

=======
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
        HEX division -- returns quotient only (integer division)
        """
        x = int(self._validate_hex(a), 16)
        y = int(self._validate_hex(b), 16)

        if y == 0:
            raise ValueError("Division by zero")

        result = x // y

        if result < 0:
            return f"H'-{format(-result, 'X')}'"
        return f"H'{format(result, 'X')}'"
    
>>>>>>> FeatureB_8_Sravanthi
    # -------------------------------
    # Pratyush will edit this part
    # -------------------------------
    def subtract(self, a: str, b: str) -> str:
        """
        HEX subtraction
        """
        hex_a = self._validate_hex(a)
        hex_b = self._validate_hex(b)

        result = int(hex_a, 16) - int(hex_b, 16)

        if result < 0:
            return f"H'-{format(abs(result), 'X')}'"

        return f"H'{format(result, 'X')}'"

    # -------------------------------
    # Sneha will edit this part
    # -------------------------------
    def fifteen_complement(self, value: str) -> str:
        """
        Compute 15's complement
        """
        hex_part = self._validate_hex(value)

        result = ""
        for digit in hex_part:
            comp = 15 - int(digit, 16)
            result += format(comp, 'X')

        return f"H'{result}'"

    def sixteen_complement(self, value: str) -> str:
        """
        Compute 16's complement
        """
<<<<<<< HEAD
=======

>>>>>>> FeatureB_8_Sravanthi
        hex_part = self._validate_hex(value)

        # Step 1: 15's complement
        comp15 = ""
        for digit in hex_part:
            comp = 15 - int(digit, 16)
            comp15 += format(comp, 'X')

        # Step 2: add 1
        comp16 = hex(int(comp15, 16) + 1)[2:].upper()

        # Step 3: maintain same length
        comp16 = comp16.zfill(len(hex_part))

        return f"H'{comp16}'"
        """
        Compute 16's complement
        """
        hex_part = self._validate_hex(value)

        # Step 1: 15's complement
        comp15 = ""
        for digit in hex_part:
            comp = 15 - int(digit, 16)
            comp15 += format(comp, 'X')

        # Step 2: add 1
        comp16 = hex(int(comp15, 16) + 1)[2:].upper()

        # Step 3: maintain same length
        comp16 = comp16.zfill(len(hex_part))

        return f"H'{comp16}'"