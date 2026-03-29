import unittest
from set import (
    set_union, set_intersection, set_difference,
    set_symmetric_difference, is_subset, is_superset
)
from exceptions import invalidseterror


class testset(unittest.TestCase):

    def test_set_union(self):
        self.assertEqual(set_union('{1,2}', '{2,3}'), '{1,2,3}')

    def test_set_union_disjoint(self):
        self.assertEqual(set_union('{1,2}', '{3,4}'), '{1,2,3,4}')

    def test_set_union_identical(self):
        self.assertEqual(set_union('{1,2,3}', '{1,2,3}'), '{1,2,3}')

    def test_set_union_empty(self):
        self.assertEqual(set_union('{}', '{1,2}'), '{1,2}')

    def test_set_intersection(self):
        self.assertEqual(set_intersection('{1,2,3}', '{2,3,4}'), '{2,3}')

    def test_set_intersection_disjoint(self):
        self.assertEqual(set_intersection('{1,2}', '{3,4}'), '{}')

    def test_set_intersection_identical(self):
        self.assertEqual(set_intersection('{1,2}', '{1,2}'), '{1,2}')

    def test_set_difference(self):
        self.assertEqual(set_difference('{1,2,3}', '{2,3}'), '{1}')

    def test_set_difference_no_common(self):
        self.assertEqual(set_difference('{1,2}', '{3,4}'), '{1,2}')

    def test_set_difference_all_common(self):
        self.assertEqual(set_difference('{1,2}', '{1,2}'), '{}')

    def test_set_symmetric_difference(self):
        self.assertEqual(set_symmetric_difference('{1,2,3}', '{2,3,4}'), '{1,4}')

    def test_set_symmetric_difference_identical(self):
        self.assertEqual(set_symmetric_difference('{1,2}', '{1,2}'), '{}')

    def test_is_subset_true(self):
        self.assertEqual(is_subset('{1,2}', '{1,2,3}'), 'True')

    def test_is_subset_false(self):
        self.assertEqual(is_subset('{1,4}', '{1,2,3}'), 'False')

    def test_is_subset_equal(self):
        self.assertEqual(is_subset('{1,2}', '{1,2}'), 'True')

    def test_is_subset_empty(self):
        self.assertEqual(is_subset('{}', '{1,2}'), 'True')

    def test_is_superset_true(self):
        self.assertEqual(is_superset('{1,2,3}', '{1,2}'), 'True')

    def test_is_superset_false(self):
        self.assertEqual(is_superset('{1,2}', '{1,2,3}'), 'False')

    def test_invalid_set_no_braces(self):
        with self.assertRaises(invalidseterror):
            set_union('1,2', '{3,4}')

    def test_invalid_set_missing_close(self):
        with self.assertRaises(invalidseterror):
            set_union('{1,2', '{3,4}')


if __name__ == "__main__":
    unittest.main()
