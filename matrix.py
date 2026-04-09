import json
from exceptions import invalidmatrixerror, dimensionmismatcherror


def parse_matrix(s):
    s = s.strip()
    try:
        mat = json.loads(s)
    except (json.JSONDecodeError, ValueError):
        raise invalidmatrixerror(f"cant parse matrix: '{s}'")

    if not isinstance(mat, list) or not mat:
        raise invalidmatrixerror("matrix must be a non-empty list of lists")

    for row in mat:
        if not isinstance(row, list):
            raise invalidmatrixerror("each row must be a list")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise invalidmatrixerror(f"element must be numeric, got: {elem}")

    row_len = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_len:
            raise invalidmatrixerror(
                f"row 0 has {row_len} cols but row {i} has {len(row)}"
            )

    return mat


def format_matrix(mat):
    rows = []
    for row in mat:
        formatted = []
        for val in row:
            if isinstance(val, float) and val == int(val):
                formatted.append(str(int(val)))
            else:
                formatted.append(str(val))
        rows.append('[' + ','.join(formatted) + ']')
    return '[' + ','.join(rows) + ']'


def get_dims(mat):
    r = len(mat)
    c = len(mat[0]) if r > 0 else 0
    return r, c


def add(a, b):
    m1 = parse_matrix(a)
    m2 = parse_matrix(b)
    r1, c1 = get_dims(m1)
    r2, c2 = get_dims(m2)

    if r1 != r2 or c1 != c2:
        raise dimensionmismatcherror(
            f"cant add ({r1}x{c1}) and ({r2}x{c2})"
        )

    result = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)

    return format_matrix(result)


def subtract(a, b):
    m1 = parse_matrix(a)
    m2 = parse_matrix(b)
    r1, c1 = get_dims(m1)
    r2, c2 = get_dims(m2)

    if r1 != r2 or c1 != c2:
        raise dimensionmismatcherror(
            f"cant subtract ({r1}x{c1}) and ({r2}x{c2})"
        )

    result = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)

    return format_matrix(result)


def multiply(a, b):
    m1 = parse_matrix(a)
    m2 = parse_matrix(b)
    r1, c1 = get_dims(m1)
    r2, c2 = get_dims(m2)

    if c1 != r2:
        raise dimensionmismatcherror(
            f"cant multiply: cols of first ({c1}) != rows of second ({r2})"
        )

    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += m1[i][k] * m2[k][j]
            row.append(total)
        result.append(row)

    return format_matrix(result)


def transpose(a):
    m = parse_matrix(a)
    rows, cols = get_dims(m)

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(m[i][j])
        result.append(row)

    return format_matrix(result)
