# complex.py
import cmath
from calculator import Calculator
import re


def _complex_str_to_tuple(c_str):
    try:
        c = complex(c_str)
    except ValueError as exc:
        raise ValueError(f"Invalid complex number: {c_str}") from exc
    return (float(c.real), float(c.imag))

def _format_complex(c):
    """
    Helper function to format a Python complex object back into a 
    clean 'a+bj' string without parentheses to match lab requirements.
    """
    res = str(c).replace(' ', '')
    if res.startswith('(') and res.endswith(')'):
        res = res[1:-1]
    return res

def parse_complex_string(expression):
    """
    Parses an input string like '(3+2j) * (5+3j)'.
    Extracts the two complex numbers and the mathematical operator.
    """
    # Regex to capture everything inside the parentheses and the operator between them
    pattern = r'\s*\(([^)]+)\)\s*([+\-*/])\s*\(([^)]+)\)\s*'
    match = re.match(pattern, expression)
    
    if not match:
        raise ValueError("Invalid complex expression format. Expected: '(a+bj) op (c+dj)'")
    
    c1_str, operator, c2_str = match.groups()
    
    # Remove any internal spaces (e.g., '3 + 2j' becomes '3+2j')
    return c1_str.replace(' ', ''), operator, c2_str.replace(' ', '')

def add_complex(c1, c2):
    """
    Member 2: Handles the addition of two complex numbers[cite: 120].
    """

    if not isinstance(c1, tuple) or not isinstance(c2, tuple):
        raise TypeError("Inputs must be tuples")
    if len(c1) != 2 or len(c2) != 2:
        raise TypeError("Tuples must have exactly 2 elements")
    if not (isinstance(c1[0], (int, float)) and isinstance(c1[1], (int, float)) and 
            isinstance(c2[0], (int, float)) and isinstance(c2[1], (int, float))):
        raise TypeError("Tuple elements must be numeric")

    calc = Calculator()
    a, b = c1
    c, d = c2

    real_part = calc.add(a, c)
    imag_part = calc.add(b, d)

    return (real_part, imag_part)

def subtract_complex(c1, c2):
    """
    Member 2: Handles the subtraction of c2 from c1[cite: 120].
    """
    if not isinstance(c1, tuple) or not isinstance(c2, tuple):
        raise TypeError("Inputs must be tuples")
    if len(c1) != 2 or len(c2) != 2:
        raise TypeError("Tuples must have exactly 2 elements")
    if not (isinstance(c1[0], (int, float)) and isinstance(c1[1], (int, float)) and 
            isinstance(c2[0], (int, float)) and isinstance(c2[1], (int, float))):
        raise TypeError("Tuple elements must be numeric")

    calc = Calculator()
    a, b = c1
    c, d = c2

    real_part = calc.subtract(a, c)
    imag_part = calc.subtract(b, d)

    return (real_part, imag_part)

def multiply_complex(c1, c2):
    """
    Member 3: Handles the multiplication of two complex numbers[cite: 120].
    """
    if not isinstance(c1, tuple) or not isinstance(c2, tuple):
        raise TypeError("Inputs must be tuples")
    if len(c1) != 2 or len(c2) != 2:
        raise TypeError("Tuples must have exactly 2 elements")
    if not (isinstance(c1[0], (int, float)) and isinstance(c1[1], (int, float)) and 
            isinstance(c2[0], (int, float)) and isinstance(c2[1], (int, float))):
        raise TypeError("Tuple elements must be numeric")

    calc = Calculator()
    a, b = c1
    c, d = c2
    
    real_part = calc.subtract(calc.multiply(a, c), calc.multiply(b, d))
    imag_part = calc.add(calc.multiply(a, d), calc.multiply(b, c))
    
    return (real_part, imag_part)

def divide_complex(c1, c2):
    """
    Member 3: Handles the division of c1 by c2[cite: 120].
    Must include error handling for division by zero.
    """
    if not isinstance(c1, tuple) or not isinstance(c2, tuple):
        raise TypeError("Inputs must be tuples")
    if len(c1) != 2 or len(c2) != 2:
        raise TypeError("Tuples must have exactly 2 elements")
    if not (isinstance(c1[0], (int, float)) and isinstance(c1[1], (int, float)) and 
            isinstance(c2[0], (int, float)) and isinstance(c2[1], (int, float))):
        raise TypeError("Tuple elements must be numeric")

    calc = Calculator()
    a, b = c1
    c, d = c2
    
    denominator = calc.add(calc.multiply(c, c), calc.multiply(d, d))
    if denominator == 0:
        raise ValueError("Division by zero in complex division")
        
    real_num = calc.add(calc.multiply(a, c), calc.multiply(b, d))
    real_part = calc.divide(real_num, denominator)
    
    imag_num = calc.subtract(calc.multiply(b, c), calc.multiply(a, d))
    imag_part = calc.divide(imag_num, denominator)
    
    return (real_part, imag_part)

def compute_magnitude(c):
    """
    Member 4: Calculates the magnitude of a single complex number[cite: 122].
    """
    z = complex(c.replace(" ", ""))  
    return abs(z)

def compute_phase(c):
    """
    Member 4: Calculates the phase (angle) of a single complex number[cite: 122].
    """
    z = complex(c.replace(" ", "")) 
    return cmath.phase(z)

def evaluate_complex_expression(expression):
    """
    Evaluates a full complex expression string like:
    '(1+2j) * (3+4j)'
    """

    c1_str, op, c2_str = parse_complex_string(expression)
    c1 = _complex_str_to_tuple(c1_str)
    c2 = _complex_str_to_tuple(c2_str)

    if op == '+':
        return add_complex(c1, c2)

    elif op == '-':
        return subtract_complex(c1, c2)

    elif op == '*':
        return multiply_complex(c1, c2)

    elif op == '/':
        return divide_complex(c1, c2)

    else:
        raise ValueError("Unsupported operation")
    
