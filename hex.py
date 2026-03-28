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
        Validate input format H'AB12'
        Returns the internal hex string.
        """
        if not isinstance(value, str):
            raise ValueError("Input must be a string")

        if not value.startswith("H'") or not value.endswith("'"):
            raise ValueError("Invalid HEX format. Expected H'AB12'")

        hex_part = value[2:-1]

        try:
            int(hex_part, 16)
        except ValueError:
            raise ValueError("Invalid hexadecimal digits")

        return hex_part

    # -------------------------------
    # Sravanti will edit this part
    # -------------------------------
    def hex_to_decimal(self, value: str) -> str:
        """
        Convert HEX → Decimal

        Example:
        H'1A5' → D'421'
        """
        raise NotImplementedError("hex_to_decimal not implemented yet")

    # -------------------------------
    # Saichaitanya will edit this part
    # -------------------------------
    def decimal_to_hex(self, value: str) -> str:
        """
        Convert Decimal → HEX

        Example:
        D'243' → H'F3'
        """
        raise NotImplementedError("decimal_to_hex not implemented yet")

    # -------------------------------
    # Joydip will edit this part
    # -------------------------------
    def add(self, a: str, b: str) -> str:
        """
        HEX addition

        Example:
        H'A' + H'5' → H'F'
        """
        raise NotImplementedError("add not implemented yet")
    # -------------------------------
    # Pratyush will edit this part
    # -------------------------------
    
    def subtract(self, a: str, b: str) -> str:
        """
        HEX subtraction
        """
        raise NotImplementedError("subtract not implemented yet")

    # -------------------------------
    # Sneha will edit this part
    # -------------------------------
    class HexCalculator:

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