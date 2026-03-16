import ast
from calculator import Calculator

def _parse_matrix(matrix_str):
    """Parse matrix string to list of lists using ast.literal_eval"""
    try:
        matrix = ast.literal_eval(matrix_str)
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Invalid matrix format")
        if not matrix:
            raise ValueError("Empty matrix")
        
        # Check if matrix is rectangular
        row_length = len(matrix[0])
        if row_length == 0:
            raise ValueError("Empty row in matrix")
        
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
    """Convert matrix list of lists to string format"""
    return str(matrix)

def transpose_matrix(a: str) -> str:
    """Transpose a matrix"""
    matrix_a = _parse_matrix(a)
    
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix_a[i][j])
        result.append(row)
    
    return _matrix_to_string(result)