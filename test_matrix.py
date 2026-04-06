def test_add():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_add('[[1,2],[3,4]]', '[[5,6],[7,8]]') == '[[6, 8], [10, 12]]'

def test_multiply():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_multiply('[[1,2],[3,4]]', '[[5,6],[7,8]]') == '[[19, 22], [43, 50]]'

def test_transpose():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_transpose('[[1,2],[3,4]]') == '[[1, 3], [2, 4]]'

def test_subtract():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_subtract('[[5,6],[7,8]]', '[[1,2],[3,4]]') == '[[4, 4], [4, 4]]'

def test_add_dimension_mismatch():
    from matrix import Matrix
    m = Matrix()
    try:
        m.matrix_add('[[1,2]]', '[[1,2],[3,4]]')
        assert False
    except ValueError:
        assert True
def test_empty_matrix():
    from matrix import Matrix
    m = Matrix()
    try:
        m.matrix_add('[]', '[]')
        assert False
    except ValueError:
        assert True

def test_invalid_format():
    from matrix import Matrix
    m = Matrix()
    try:
        m.matrix_add('abc', '[[1,2]]')
        assert False
    except ValueError:
        assert True

def test_irregular_matrix():
    from matrix import Matrix
    m = Matrix()
    try:
        m.matrix_add('[[1,2],[3]]', '[[1,2],[3,4]]')
        assert False
    except ValueError:
        assert True

def test_multiply_dimension_mismatch():
    from matrix import Matrix
    m = Matrix()
    try:
        m.matrix_multiply('[[1,2]]', '[[1,2]]')
        assert False
    except ValueError:
        assert True

def test_single_element():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_add('[[5]]', '[[3]]') == '[[8]]'

def test_negative_values():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_add('[[-1,-2],[-3,-4]]', '[[1,2],[3,4]]') == '[[0, 0], [0, 0]]'

def test_transpose_rectangular():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_transpose('[[1,2,3],[4,5,6]]') == '[[1, 4], [2, 5], [3, 6]]'

def test_large_matrix():
    from matrix import Matrix
    m = Matrix()
    A = '[[1,1],[1,1]]'
    B = '[[1,1],[1,1]]'
    assert m.matrix_add(A, B) == '[[2, 2], [2, 2]]'