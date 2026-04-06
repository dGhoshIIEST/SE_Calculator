import unittest

from exceptions import InvalidMatrixError, MatrixDimensionError
from matrix import (
    add_matrix,
    evaluate_matrix_expression,
    multiply_matrix,
    parse_matrix,
    subtract_matrix,
    transpose_matrix,
)
from calculator import Calculator


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_parse_matrix(self):
        self.assertEqual(parse_matrix("[[1,2],[3,4]]"), [[1, 2], [3, 4]])

    def test_matrix_add(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        self.assertEqual(add_matrix(a, b), [[6, 8], [10, 12]])

    def test_matrix_subtract(self):
        a = [[5, 6], [7, 8]]
        b = [[1, 2], [3, 4]]
        self.assertEqual(subtract_matrix(a, b), [[4, 4], [4, 4]])

    def test_matrix_multiply(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        self.assertEqual(multiply_matrix(a, b), [[19, 22], [43, 50]])

    def test_matrix_transpose(self):
        a = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(transpose_matrix(a), [[1, 4], [2, 5], [3, 6]])

    def test_evaluate_matrix_add(self):
        expr = "[[1,2],[3,4]] + [[5,6],[7,8]]"
        self.assertEqual(self.calc.evaluate(expr, mode=6), [[6, 8], [10, 12]])

    def test_evaluate_matrix_multiply(self):
        expr = "[[1,2],[3,4]] * [[5,6],[7,8]]"
        self.assertEqual(self.calc.evaluate(expr, mode=6), [[19, 22], [43, 50]])

    def test_evaluate_matrix_transpose(self):
        expr = "transpose([[1,2,3],[4,5,6]])"
        self.assertEqual(evaluate_matrix_expression(expr), [[1, 4], [2, 5], [3, 6]])

    def test_invalid_matrix_shape(self):
        with self.assertRaises(InvalidMatrixError):
            parse_matrix("[[1,2],[3]]")

    def test_invalid_matrix_element(self):
        with self.assertRaises(InvalidMatrixError):
            parse_matrix("[[1,2],[3,'x']]")

    def test_dimension_mismatch_add(self):
        with self.assertRaises(MatrixDimensionError):
            evaluate_matrix_expression("[[1,2],[3,4]] + [[1,2,3],[4,5,6]]")

    def test_dimension_mismatch_multiply(self):
        with self.assertRaises(MatrixDimensionError):
            evaluate_matrix_expression("[[1,2,3]] * [[1,2],[3,4]]")

    def test_empty_expression(self):
        with self.assertRaises(InvalidMatrixError):
            evaluate_matrix_expression("")


if __name__ == "__main__":
    unittest.main()
