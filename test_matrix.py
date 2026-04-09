import unittest
from matrix import add, subtract, multiply, transpose
from exceptions import invalidmatrixerror, dimensionmismatcherror


class testmatrix(unittest.TestCase):

    def test_matrix_add(self):
        res = add('[[1,2],[3,4]]', '[[5,6],[7,8]]')
        self.assertEqual(res, '[[6,8],[10,12]]')

    def test_matrix_add_single_element(self):
        res = add('[[1]]', '[[2]]')
        self.assertEqual(res, '[[3]]')

    def test_matrix_add_negative(self):
        res = add('[[1,2],[3,4]]', '[[-1,-2],[-3,-4]]')
        self.assertEqual(res, '[[0,0],[0,0]]')

    def test_matrix_add_dimension_mismatch(self):
        with self.assertRaises(dimensionmismatcherror):
            add('[[1,2]]', '[[1,2],[3,4]]')

    def test_matrix_subtract(self):
        res = subtract('[[5,6],[7,8]]', '[[1,2],[3,4]]')
        self.assertEqual(res, '[[4,4],[4,4]]')

    def test_matrix_subtract_to_zero(self):
        res = subtract('[[3,4],[5,6]]', '[[3,4],[5,6]]')
        self.assertEqual(res, '[[0,0],[0,0]]')

    def test_matrix_subtract_dimension_mismatch(self):
        with self.assertRaises(dimensionmismatcherror):
            subtract('[[1,2,3]]', '[[1,2]]')

    def test_matrix_multiply(self):
        res = multiply('[[1,2],[3,4]]', '[[5,6],[7,8]]')
        self.assertEqual(res, '[[19,22],[43,50]]')

    def test_matrix_multiply_identity(self):
        res = multiply('[[1,0],[0,1]]', '[[5,6],[7,8]]')
        self.assertEqual(res, '[[5,6],[7,8]]')

    def test_matrix_multiply_rectangular(self):
        res = multiply('[[1,2,3]]', '[[4],[5],[6]]')
        self.assertEqual(res, '[[32]]')

    def test_matrix_multiply_dimension_mismatch(self):
        with self.assertRaises(dimensionmismatcherror):
            multiply('[[1,2]]', '[[1,2]]')

    def test_matrix_transpose(self):
        res = transpose('[[1,2],[3,4]]')
        self.assertEqual(res, '[[1,3],[2,4]]')

    def test_matrix_transpose_rectangular(self):
        res = transpose('[[1,2,3],[4,5,6]]')
        self.assertEqual(res, '[[1,4],[2,5],[3,6]]')

    def test_matrix_transpose_single_row(self):
        res = transpose('[[1,2,3]]')
        self.assertEqual(res, '[[1],[2],[3]]')

    def test_matrix_transpose_single_col(self):
        res = transpose('[[1],[2],[3]]')
        self.assertEqual(res, '[[1,2,3]]')

    def test_invalid_matrix_format(self):
        with self.assertRaises(invalidmatrixerror):
            add('not_a_matrix', '[[1,2]]')

    def test_invalid_matrix_non_numeric(self):
        with self.assertRaises(invalidmatrixerror):
            add('[["a","b"]]', '[[1,2]]')

    def test_invalid_matrix_inconsistent_rows(self):
        with self.assertRaises(invalidmatrixerror):
            add('[[1,2],[3]]', '[[1,2],[3,4]]')


if __name__ == "__main__":
    unittest.main()
