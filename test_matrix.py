def test_add():
    from matrix import Matrix
    m = Matrix()
    assert m.matrix_add('[[1,2],[3,4]]', '[[5,6],[7,8]]') == '[[6, 8], [10, 12]]'