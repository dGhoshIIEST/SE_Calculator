import unittest
from matrix import  multiply_matrix
from matrix import add_matrix, transpose_matrix, subtract_matrix

class TestMatrix(unittest.TestCase):
    
    # Normal cases
    
    
    def test_matrix_multiply(self):
        self.assertEqual(
            multiply_matrix("[[1,2],[3,4]]", "[[5,6],[7,8]]"),
            "[[19, 22], [43, 50]]"
        )
    
    
    
    # Edge cases
    
    
    def test_1x1_matrix_multiply(self):
        self.assertEqual(
            multiply_matrix("[[5]]", "[[3]]"),
            "[[15]]"
        )
    
   
    
    
    
    def test_non_square_matrix_multiply(self):
        self.assertEqual(
            multiply_matrix("[[1,2,3],[4,5,6]]", "[[7,8],[9,10],[11,12]]"),
            "[[58, 64], [139, 154]]"
        )
    
   
    
    # Error cases
    
    
    def test_multiply_incompatible_dimensions(self):
        with self.assertRaises(ValueError):
            multiply_matrix("[[1,2],[3,4]]", "[[5,6,7],[8,9,10],[11,12,13]]")
    
    def test_multiply_incompatible_dimensions_columns(self):
        with self.assertRaises(ValueError):
            multiply_matrix("[[1,2,3],[4,5,6]]", "[[7,8,9],[10,11,12]]")
    
   
    
    
    
    

# Optional: this allows running the script directly
    def test_matrix_add(self):
        self.assertEqual(
            add_matrix("[[1,2],[3,4]]", "[[5,6],[7,8]]"),
            "[[6, 8], [10, 12]]"
        )
    
    def test_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[1,2,3],[4,5,6]]"),
            "[[1, 4], [2, 5], [3, 6]]"
        )
    
    def test_matrix_subtract(self):
        self.assertEqual(
            subtract_matrix("[[5,6],[7,8]]", "[[1,2],[3,4]]"),
            "[[4, 4], [4, 4]]"
        )
    
    # Edge cases
    def test_1x1_matrix_add(self):
        self.assertEqual(
            add_matrix("[[5]]", "[[3]]"),
            "[[8]]"
        )
    
    def test_1x1_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[5]]"),
            "[[5]]"
        )
    
    def test_1x1_matrix_subtract(self):
        self.assertEqual(
            subtract_matrix("[[5]]", "[[3]]"),
            "[[2]]"
        )
    
    def test_non_square_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[1,2],[3,4],[5,6]]"),
            "[[1, 3, 5], [2, 4, 6]]"
        )
    
    # Error cases
    def test_add_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            add_matrix("[[1,2],[3,4]]", "[[5,6,7],[8,9,10]]")
    
    def test_add_dimension_mismatch_rows(self):
        with self.assertRaises(ValueError):
            add_matrix("[[1,2],[3,4]]", "[[5,6]]")
     
    def test_malformed_matrix_string(self):
        with self.assertRaises(ValueError):
            add_matrix("[[1,2],[3,4", "[[5,6],[7,8]]")
    
    def test_malformed_matrix_string_brackets(self):
        with self.assertRaises(ValueError):
            add_matrix("[1,2],[3,4]]", "[[5,6],[7,8]]")
    
    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            add_matrix("[]", "[[5,6],[7,8]]")
    
    def test_empty_row_matrix(self):
        with self.assertRaises(ValueError):
            add_matrix("[[]]", "[[5,6],[7,8]]")
    
    def test_non_rectangular_matrix(self):
        with self.assertRaises(ValueError):
            add_matrix("[[1,2,3],[4,5]]", "[[6,7,8],[9,10,11]]")
    
    def test_non_numeric_matrix(self):
        with self.assertRaises(ValueError):
            add_matrix("[[1,2],[3,'a']]", "[[4,5],[6,7]]")
    
    def test_transpose_empty_matrix(self):
        with self.assertRaises(ValueError):
            transpose_matrix("[]")
    
    def test_transpose_empty_row_matrix(self):
        with self.assertRaises(ValueError):
            transpose_matrix("[[]]")
    
    def test_subtract_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            subtract_matrix("[[1,2],[3,4]]", "[[5,6,7],[8,9,10]]")

if __name__ == '__main__':
    unittest.main()

def print_matrix_operations():
    """Print outputs of matrix operations for demonstration"""
    print("=== Matrix Operations Demo ===")
    
    # Test matrices
    matrix_a = "[[1,2],[3,4]]"
    matrix_b = "[[5,6],[7,8]]"
    
    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")
    print()
    
    
    # Multiplication
    try:
        result = multiply_matrix(matrix_a, matrix_b)
        print(f"Multiplication (A * B): {result}")
    except Exception as e:
        print(f"Multiplication Error: {e}")
    
    
    # Addition
    try:
        result = add_matrix(matrix_a, matrix_b)
        print(f"Addition (A + B): {result}")
    except Exception as e:
        print(f"Addition Error: {e}")
    
    # Subtraction
    try:
        result = subtract_matrix(matrix_a, matrix_b)
        print(f"Subtraction (A - B): {result}")
    except Exception as e:
        print(f"Subtraction Error: {e}")
    
    # Transpose
    try:
        result = transpose_matrix(matrix_a)
        print(f"Transpose of A: {result}")
    except Exception as e:
        print(f"Transpose Error: {e}")
    
    print("\n=== End Demo ===")
