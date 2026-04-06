def parse_matrix(mat_str):
    import ast
    return ast.literal_eval(mat_str)

def matrix_add(self, A, B):
    A = self.parse_matrix(A)
    B = self.parse_matrix(B)

    if not A or not B:
        raise ValueError("Empty matrix")

    rows = len(A)
    cols = len(A[0])

    if rows != len(B) or cols != len(B[0]):
        raise ValueError("Matrix dimensions must match")

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return str(result)

def subtract_matrix(a, b): pass
def multiply_matrix(a, b): pass

def matrix_multiply(self, A, B):
    A = self.parse_matrix(A)
    B = self.parse_matrix(B)

    if not A or not B:
        raise ValueError("Empty matrix")

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Invalid dimensions for multiplication")

    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            val = 0
            for k in range(cols_A):
                val += A[i][k] * B[k][j]
            row.append(val)
        result.append(row)

    return str(result)

def transpose_matrix(a): pass
