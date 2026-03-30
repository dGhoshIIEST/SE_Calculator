import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    # base test cases
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(4, -2), -2)

    def test_divide_fail(self):
        self.assertNotEqual(self.calc.divide(4, -2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    # set operation test cases
    def test_set_union(self):
        self.assertEqual(self.calc.set_union("{1,2}", "{2,3}"), {1, 2, 3})

    def test_set_intersection(self):
        self.assertEqual(self.calc.set_intersection("{1,2,3}", "{2,4}"), {2})

    def test_set_difference(self):
        self.assertEqual(self.calc.set_difference("{1,2,3}", "{2}"), {1, 3})

    def test_set_symmetric_difference(self):
        self.assertEqual(self.calc.set_symmetric_difference("{1,2,3}", "{2,4}"), {1, 3, 4})

    def test_set_subset(self):
        self.assertTrue(self.calc.set_is_subset("{1,2}", "{1,2,3}"))

    def test_set_superset(self):
        self.assertTrue(self.calc.set_is_superset("{1,2,3}", "{1,2}"))

    def test_set_empty_set_boundary(self):
        self.assertEqual(self.calc.set_union("{}", "{1,2}"), {1, 2})

    def test_set_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calc.set_union("{1,2}", "not_a_set")

    def test_set_expression_union(self):
        self.assertEqual(self.calc.evaluate("{1,2} union {2,3}"), {1, 2, 3})

    def test_set_expression_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("{1,2} merge {2,3}")


if __name__ == '__main__':
    unittest.main()
