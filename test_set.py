import itertools
import unittest
from set import SetCalculator, SetFormatter, SetParser
from set import InvalidSetFormat, UnsupportedOperation

class TestSetOperations(unittest.TestCase):

    def setUp(self):
        self.parser = SetParser()
        self.calc = SetCalculator()

        self.A = self.parser.parse("{1,2,3}")
        self.B = self.parser.parse("{3,4}")

    @staticmethod
    def _powerset(values):
        """Generate all subsets for exhaustive binary-operation test cases."""
        values = list(values)
        for size in range(len(values) + 1):
            for combo in itertools.combinations(values, size):
                yield set(combo)

    # ---------------------------
    # Parser Tests
    # ---------------------------
    def test_parse_valid(self):
        result = self.parser.parse("{1, 2, 3}")
        self.assertEqual(result, {1, 2, 3})

    def test_parse_empty(self):
        result = self.parser.parse("{}")
        self.assertEqual(result, set())

    def test_parse_invalid(self):
        with self.assertRaises(InvalidSetFormat):
            self.parser.parse("{1,,2}")

    def test_parse_valid_edge_cases(self):
        valid_inputs = {
            "{  -10,0, 5 }": {-10, 0, 5},
            "{-1, -1, 2}": {-1, 2},
            " {  } ": set(),
            "{42}": {42},
        }

        for raw, expected in valid_inputs.items():
            with self.subTest(raw=raw):
                self.assertEqual(self.parser.parse(raw), expected)

    def test_parse_invalid_cases(self):
        invalid_inputs = [
            "",
            "1,2,3",
            "{1,,2}",
            "{a,b}",
            "{1, 2,}",
            "{{1,2}}",
            "{1 2}",
            "[1,2]",
            "{+1,2}",
        ]

        for raw in invalid_inputs:
            with self.subTest(raw=raw):
                with self.assertRaises(InvalidSetFormat):
                    self.parser.parse(raw)

    # ---------------------------
    # Operation Tests
    # ---------------------------
    def test_union(self):
        self.assertEqual(
            self.calc.compute("union", self.A, self.B),
            "{1, 2, 3, 4}"
        )

    def test_intersection(self):
        self.assertEqual(
            self.calc.compute("intersection", self.A, self.B),
            "{3}"
        )

    def test_difference(self):
        self.assertEqual(
            self.calc.compute("difference", self.A, self.B),
            "{1, 2}"
        )

    def test_symmetric_difference(self):
        self.assertEqual(
            self.calc.compute("symmetric_difference", self.A, self.B),
            "{1, 2, 4}"
        )

    def test_subset(self):
        self.assertTrue(
            self.calc.compute("subset", {1, 2}, {1, 2, 3})
        )

    def test_superset(self):
        self.assertTrue(
            self.calc.compute("superset", {1, 2, 3}, {1, 2})
        )

    def test_operation_exhaustive_small_universe(self):
        universe = {-1, 0, 1, 2}

        operation_to_expected = {
            "union": lambda a, b: SetFormatter.format(a.union(b)),
            "intersection": lambda a, b: SetFormatter.format(a.intersection(b)),
            "difference": lambda a, b: SetFormatter.format(a.difference(b)),
            "symmetric_difference": lambda a, b: SetFormatter.format(a.symmetric_difference(b)),
            "subset": lambda a, b: a.issubset(b),
            "superset": lambda a, b: a.issuperset(b),
        }

        all_sets = list(self._powerset(universe))
        for operation, expected_fn in operation_to_expected.items():
            for left in all_sets:
                for right in all_sets:
                    with self.subTest(operation=operation, left=left, right=right):
                        self.assertEqual(
                            self.calc.compute(operation, left, right),
                            expected_fn(left, right),
                        )

    def test_operation_case_insensitive(self):
        self.assertEqual(
            self.calc.compute("UnIoN", {1, 2}, {2, 3}),
            "{1, 2, 3}",
        )

    def test_subset_and_superset_negative_cases(self):
        self.assertFalse(self.calc.compute("subset", {1, 4}, {1, 2, 3}))
        self.assertFalse(self.calc.compute("superset", {1, 2}, {1, 2, 3}))

    def test_difference_directionality(self):
        self.assertEqual(self.calc.compute("difference", {1, 2, 3}, {3}), "{1, 2}")
        self.assertEqual(self.calc.compute("difference", {3}, {1, 2, 3}), "{}")

    def test_invalid_operation(self):
        with self.assertRaises(UnsupportedOperation):
            self.calc.compute("invalid", self.A, self.B)


if __name__ == "__main__":
    unittest.main()
