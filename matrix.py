def parse_matrix(mat_str):
    import ast
    return ast.literal_eval(mat_str)

def add_matrix(a, b): pass

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
def transpose_matrix(a): pass
