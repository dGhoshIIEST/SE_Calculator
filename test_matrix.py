import unittest
from matrix import  multiply_matrix

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
    
    
