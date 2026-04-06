def test_add():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_add('[[1,2],[3,4]]', '[[5,6],[7,8]]') == '[[6, 8], [10, 12]]'

def test_multiply():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_multiply('[[1,2],[3,4]]', '[[5,6],[7,8]]') == '[[19, 22], [43, 50]]'