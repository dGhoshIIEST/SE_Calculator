import unittest
from matrix import transpose_matrix

class TestMatrix(unittest.TestCase):
    
    # Normal cases
    def test_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[1,2,3],[4,5,6]]"),
            "[[1, 4], [2, 5], [3, 6]]"
        )
    
    # Edge cases
    def test_1x1_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[5]]"),
            "[[5]]"
        )
    
    def test_non_square_matrix_transpose(self):
        self.assertEqual(
            transpose_matrix("[[1,2],[3,4],[5,6]]"),
            "[[1, 3, 5], [2, 4, 6]]"
        )
    
    # Error cases
    def test_transpose_empty_matrix(self):
        with self.assertRaises(ValueError):
            transpose_matrix("[]")
    
    def test_transpose_empty_row_matrix(self):
        with self.assertRaises(ValueError):
            transpose_matrix("[[]]")

# Optional: this allows running the script directly
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
    
    
    # Transpose
    try:
        result = transpose_matrix(matrix_a)
        print(f"Transpose of A: {result}")
    except Exception as e:
        print(f"Transpose Error: {e}")
    
    print("\n=== End Demo ===")