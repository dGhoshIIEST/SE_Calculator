import cmath
import re

class ComplexCalculator:
    def evaluate(self, expression: str) -> str:
        """
        Parses and evaluates a complex number expression.
        Example input: '(3+2j)*(5+3j)'
        """
        # Remove all spaces so we don't have to worry about weird spacing
        expr = expression.replace(" ", "")

        # Regex to match the arithmetic format: (a+bj) operator (c+dj)
        # Group 1: First number, Group 2: Operator, Group 3: Second number
        pattern = r'\(([^)]+)\)([\+\-\*\/])\(([^)]+)\)'
        match = re.match(pattern, expr)

        if match:
            c1_str = match.group(1)
            operator = match.group(2)
            c2_str = match.group(3)
            return self._perform_arithmetic(c1_str, operator, c2_str)

        # Regex to handle Magnitude: e.g., 'mag(3+2j)'
        mag_match = re.match(r'mag\(([^)]+)\)', expr)
        if mag_match:
            return self.magnitude(mag_match.group(1))

        # Regex to handle Phase: e.g., 'phase(3+2j)'
        phase_match = re.match(r'phase\(([^)]+)\)', expr)
        if phase_match:
            return self.phase(phase_match.group(1))

        raise ValueError("Invalid complex number expression format.")

    def _perform_arithmetic(self, c1: str, operator: str, c2: str) -> str:
        # Convert strings to actual complex numbers
        try:
            z1 = complex(c1)
            z2 = complex(c2)
        except ValueError:
            raise ValueError("Invalid format. Use a+bj notation.")

        # Perform the actual math
        if operator == '+':
            result = z1 + z2
        elif operator == '-':
            result = z1 - z2
        elif operator == '*':
            result = z1 * z2
        elif operator == '/':
            if z2 == 0:
                raise ValueError("Division by zero")
            result = z1 / z2
        else:
            raise ValueError("Unknown operator")

        return self._format_result(result)

    def magnitude(self, c_str: str) -> str:
        z = complex(c_str)
        # Magnitude is calculated as sqrt(a^2 + b^2)
        return str(abs(z))

    def phase(self, c_str: str) -> str:
        z = complex(c_str)
        # Phase is calculated in radians
        return str(cmath.phase(z))

    def _format_result(self, z: complex) -> str:
        """Formats the output back to a readable a+bj string."""
        # Ensure the imaginary part always has a + or - sign
        sign = '+' if z.imag >= 0 else '-'
        return f"{z.real}{sign}{abs(z.imag)}j"

# # Example Usage (You can delete this part in your final file, it's just to show you how it works):
# if __name__ == "__main__":
#     calc = ComplexCalculator()
#     print(calc.evaluate("(3+2j)*(5+3j)"))  # Output: 9.0+19.0j
#     print(calc.evaluate("(1+2j)+(2+3j)"))  # Output: 3.0+5.0j
#     print(calc.evaluate("mag(3+4j)"))      # Output: 5.0