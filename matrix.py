import ast
from typing import List, Sequence, Tuple, Union

from exceptions import InvalidMatrixError, MatrixDimensionError

Number = Union[int, float]
Matrix = List[List[Number]]


def _is_number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def parse_matrix(text: str) -> Matrix:
    """Parse a row-major matrix string like [[1,2],[3,4]]."""
    try:
        obj = ast.literal_eval(text.strip())
    except Exception as exc:
        raise InvalidMatrixError("Invalid matrix format") from exc

    if not isinstance(obj, list) or not obj:
        raise InvalidMatrixError("Matrix must be a non-empty list of rows")

    if not all(isinstance(row, list) for row in obj):
        raise InvalidMatrixError("Matrix rows must be lists")

    col_count = len(obj[0])
    if col_count == 0:
        raise InvalidMatrixError("Matrix rows cannot be empty")

    out: Matrix = []
    for row in obj:
        if len(row) != col_count:
            raise InvalidMatrixError("All rows must have the same length")
        new_row: List[Number] = []
        for val in row:
            if not _is_number(val):
                raise InvalidMatrixError("Matrix elements must be numeric")
            new_row.append(val)
        out.append(new_row)
    return out


def matrix_shape(m: Matrix) -> Tuple[int, int]:
    return len(m), len(m[0])


def add_matrix(a: Matrix, b: Matrix) -> Matrix:
    if matrix_shape(a) != matrix_shape(b):
        raise MatrixDimensionError("Matrix addition requires equal dimensions")
    r, c = matrix_shape(a)
    return [[a[i][j] + b[i][j] for j in range(c)] for i in range(r)]


def subtract_matrix(a: Matrix, b: Matrix) -> Matrix:
    if matrix_shape(a) != matrix_shape(b):
        raise MatrixDimensionError("Matrix subtraction requires equal dimensions")
    r, c = matrix_shape(a)
    return [[a[i][j] - b[i][j] for j in range(c)] for i in range(r)]


def multiply_matrix(a: Matrix, b: Matrix) -> Matrix:
    ra, ca = matrix_shape(a)
    rb, cb = matrix_shape(b)
    if ca != rb:
        raise MatrixDimensionError(
            "Matrix multiplication requires columns of first matrix to equal rows of second matrix"
        )
    out: Matrix = []
    for i in range(ra):
        row: List[Number] = []
        for j in range(cb):
            s = 0
            for k in range(ca):
                s += a[i][k] * b[k][j]
            row.append(s)
        out.append(row)
    return out


def transpose_matrix(a: Matrix) -> Matrix:
    r, c = matrix_shape(a)
    return [[a[i][j] for i in range(r)] for j in range(c)]


def _find_top_level_operator(expr: str, ops: Sequence[str]) -> Tuple[int, str]:
    depth = 0
    for i, ch in enumerate(expr):
        if ch in "[({":
            depth += 1
        elif ch in "])}":
            depth -= 1
        elif depth == 0 and ch in ops:
            return i, ch
    return -1, ""


def _normalize(expr: str) -> str:
    return " ".join(expr.strip().split())


def evaluate_matrix_expression(expression: str) -> Matrix:
    expr = _normalize(expression)
    if not expr:
        raise InvalidMatrixError("Empty matrix expression")

    low = expr.lower()
    if low.startswith("transpose(") and expr.endswith(")"):
        inside = expr[len("transpose(") : -1]
        return transpose_matrix(parse_matrix(inside))

    if low.startswith("t(") and expr.endswith(")"):
        inside = expr[2:-1]
        return transpose_matrix(parse_matrix(inside))

    idx, op = _find_top_level_operator(expr, "+-*")
    if idx == -1:
        return parse_matrix(expr)

    left = expr[:idx].strip()
    right = expr[idx + 1 :].strip()
    if not left or not right:
        raise InvalidMatrixError("Invalid matrix expression")

    a = parse_matrix(left)
    b = parse_matrix(right)

    if op == "+":
        return add_matrix(a, b)
    if op == "-":
        return subtract_matrix(a, b)
    return multiply_matrix(a, b)


def format_matrix(m: Matrix) -> str:
    return str(m)
