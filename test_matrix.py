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