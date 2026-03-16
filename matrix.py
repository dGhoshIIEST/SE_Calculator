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
        result.append(row)
    
    return _matrix_to_string(result)

