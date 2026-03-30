import unittest
from arithmetic import octal_add, octal_multiply, get_complement


class TestArithmetic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(octal_add("7", "1"), "10")
        self.assertEqual(octal_add("10", "7"), "17")
        self.assertEqual(octal_add("123", "456"), "601")

    def test_multiply(self):
        self.assertEqual(octal_multiply("2", "3"), "6")
        self.assertEqual(octal_multiply("7", "7"), "61")
        self.assertEqual(octal_multiply("10", "10"), "100")

    def test_complement_7(self):
        self.assertEqual(get_complement("123", 7), "654")
        self.assertEqual(get_complement("0", 7), "7")

    def test_complement_8(self):
        self.assertEqual(get_complement("123", 8), "655")
        self.assertEqual(get_complement("0", 8), "10")

    def test_edge_cases(self):
        self.assertEqual(octal_add("0", "0"), "0")
        self.assertEqual(octal_multiply("0", "123"), "0")


if __name__ == "__main__":
    unittest.main()