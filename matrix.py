import ast

class Matrix:

    def parse_matrix(self, mat_str):
        try:
            mat = ast.literal_eval(mat_str)

            if not isinstance(mat, list) or not mat:
                raise ValueError("Invalid matrix")

            row_len = len(mat[0])
            for row in mat:
                if not isinstance(row, list) or len(row) != row_len:
                    raise ValueError("Irregular matrix")

            return mat

        except:
            raise ValueError("Invalid matrix format")


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


    def matrix_subtract(self, A, B):
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
                row.append(A[i][j] - B[i][j])
            result.append(row)

        return str(result)


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


    def matrix_transpose(self, A):
        A = self.parse_matrix(A)

        if not A:
            raise ValueError("Empty matrix")

        rows = len(A)
        cols = len(A[0])

        result = []
        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(A[i][j])
            result.append(row)

        return str(result)