import unittest
from matrix import add_matrix

class TestMatrix(unittest.TestCase):
    
    # Normal cases
    def test_matrix_add(self):
        self.assertEqual(
            add_matrix("[[1,2],[3,4]]", "[[5,6],[7,8]]"),
            "[[6, 8], [10, 12]]"
        )
    
    # Edge cases
    def test_1x1_matrix_add(self):
        self.assertEqual(
            add_matrix("[[5]]", "[[3]]"),
            "[[8]]"
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
    
    # Addition
    try:
        result = add_matrix(matrix_a, matrix_b)
        print(f"Addition (A + B): {result}")
    except Exception as e:
        print(f"Addition Error: {e}")
    
    print("\n=== End Demo ===")
