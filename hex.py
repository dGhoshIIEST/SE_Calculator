class HexOperations:
    def validate_hex(self, hex_str: str) -> str:
        """Validates and extracts the hex part of the string."""
        if not hex_str.startswith("H'"):
            raise ValueError("Invalid HEX format. Must start with H'")
        hex_val = hex_str[2:]
        if not hex_val:
            raise ValueError("Empty HEX value")
        try:
            int(hex_val, 16)
        except ValueError:
            raise ValueError("Invalid HEX characters")
        return hex_val
    def validate_dec(self, dec_str: str) -> str:
        """Validates and extracts the decimal part of the string."""
        if not dec_str.startswith("D'"):
            raise ValueError("Invalid Decimal format. Must start with D'")
        dec_val = dec_str[2:]
        if not dec_val:
            raise ValueError("Empty Decimal value")
        try:
            int(dec_val)
        except ValueError:
            raise ValueError("Invalid Decimal characters")
        return dec_val
    def hex(self, dec_str: str) -> str:
        """Hexadecimal <-> Decimal conversions e.g. hex(D'243) returns H'F3"""
        val = self.validate_dec(dec_str)
        num = int(val)
        return f"H'{hex(num)[2:].upper()}"
    def dec(self, hex_str: str) -> str:
        """Hexadecimal <-> Decimal conversions e.g. dec(H'1A5) is D'421"""
        val = self.validate_hex(hex_str)
        num = int(val, 16)
        return f"D'{num}"
    def add(self, hex1: str, hex2: str) -> str:
        """Arithmetic operations in HEX base (Addition)"""
        val1 = int(self.validate_hex(hex1), 16)
        val2 = int(self.validate_hex(hex2), 16)
        return f"H'{hex(val1 + val2)[2:].upper()}"
    def subtract(self, hex1: str, hex2: str) -> str:
        """Arithmetic operations in HEX base (Subtraction)"""
        val1 = int(self.validate_hex(hex1), 16)
        val2 = int(self.validate_hex(hex2), 16)
        res = val1 - val2
        if res < 0:
            return f"-H'{hex(abs(res))[2:].upper()}"
        return f"H'{hex(res)[2:].upper()}"
    def multiply(self, hex1: str, hex2: str) -> str:
        """Arithmetic operations in HEX base (Multiplication)"""
        val1 = int(self.validate_hex(hex1), 16)
        val2 = int(self.validate_hex(hex2), 16)
        return f"H'{hex(val1 * val2)[2:].upper()}"
    def divide(self, hex1: str, hex2: str) -> str:
        """Arithmetic operations in HEX base (Division)"""
        val1 = int(self.validate_hex(hex1), 16)
        val2 = int(self.validate_hex(hex2), 16)
        if val2 == 0:
            raise ValueError("Division by zero")
        return f"H'{hex(val1 // val2)[2:].upper()}"
    def complement_15s(self, hex_str: str) -> str:
        """Complements (15's)"""
        val = self.validate_hex(hex_str)
        comp = "".join(hex(15 - int(c, 16))[2:].upper() for c in val)
        return f"H'{comp}"
    def complement_16s(self, hex_str: str) -> str:
        """Complements (16's)"""
        _15s = self.complement_15s(hex_str)
        val = int(_15s[2:], 16) + 1
        # Pad with leading zeros based on original length, or standard hex length
        # Standard approach: 15's complement + 1
        comp_16 = hex(val)[2:].upper()
        # Ensure it maintains at least the length of the input (handle overflow if needed, but standard 16's comp just adds 1)
        expected_len = len(hex_str) - 2
        comp_16 = comp_16.zfill(expected_len)
        # If length exceeded (e.g., FFFF + 1 = 10000), we just take the last expected_len digits for proper 2s/16s comp behaviour
        if len(comp_16) > expected_len:
            comp_16 = comp_16[-expected_len:]
        return f"H'{comp_16}"