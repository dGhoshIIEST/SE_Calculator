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



def multiply_matrix(a: str, b: str) -> str:
    """Multiply two matrices"""
def add_matrix(a: str, b: str) -> str:
    """Add two matrices"""
    calc = Calculator()
    matrix_a = _parse_matrix(a)
    matrix_b = _parse_matrix(b)
    
    # Check dimensions: columns(A) must equal rows(B)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    
    if cols_a != rows_b:
        raise ValueError("Incompatible matrix dimensions")
    
    rows_a = len(matrix_a)
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            sum_val = 0
            for k in range(cols_a):
                sum_val = calc.add(sum_val, calc.multiply(matrix_a[i][k], matrix_b[k][j]))
            row.append(sum_val)
    # Check dimensions
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have identical dimensions")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(calc.add(matrix_a[i][j], matrix_b[i][j]))
        result.append(row)
    
    return _matrix_to_string(result)

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
