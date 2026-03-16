import unittest
from matrix import subtract_matrix

class TestMatrix(unittest.TestCase):
    def test_matrix_subtract(self):
        self.assertEqual(
            subtract_matrix("[[5,6],[7,8]]", "[[1,2],[3,4]]"),
            "[[4, 4], [4, 4]]"
        )

    def test_1x1_matrix_subtract(self):
        self.assertEqual(
            subtract_matrix("[[5]]", "[[3]]"),
            "[[2]]"
        )

    def test_subtract_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            subtract_matrix("[[1,2],[3,4]]", "[[5,6,7],[8,9,10]]")


# Optional: this allows running the script directly
if __name__ == '__main__':
    unittest.main()


def print_matrix_operations():
    """Print outputs of matrix subtraction for demonstration"""
    print("=== Matrix Subtraction Demo ===")
    
    # Test matrices
    matrix_a = "[[1,2],[3,4]]"
    matrix_b = "[[5,6],[7,8]]"
    
    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")
    print()

    # Subtraction
    try:
        result = subtract_matrix(matrix_a, matrix_b)
        print(f"Subtraction (A - B): {result}")
    except Exception as e:
        print(f"Subtraction Error: {e}")
    
    print("\n=== End Demo ===")