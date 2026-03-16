import ast
from calculator import Calculator

def _parse_matrix(matrix_str):
    """Parse matrix string to list of lists"""
    try:
        matrix = ast.literal_eval(matrix_str)

        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Invalid matrix format")

        if not matrix:
            raise ValueError("Empty matrix")

        row_length = len(matrix[0])

        for row in matrix:
            if len(row) != row_length:
                raise ValueError("Matrix is not rectangular")

            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Matrix contains non-numeric values")

        return matrix

    except (SyntaxError, ValueError):
        raise ValueError("Invalid matrix string format")


def _matrix_to_string(matrix):
    """Convert matrix list to string"""
    return str(matrix)


def subtract_matrix(a: str, b: str) -> str:
    """Subtract matrix B from matrix A"""

    calc = Calculator()

    matrix_a = _parse_matrix(a)
    matrix_b = _parse_matrix(b)

    # Check dimensions
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have identical dimensions")

    result = []

    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(calc.subtract(matrix_a[i][j], matrix_b[i][j]))
        result.append(row)

    return _matrix_to_string(result)