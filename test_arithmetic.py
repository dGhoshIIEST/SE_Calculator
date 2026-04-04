import unittest
import arithmetic


class testarithmetic(unittest.TestCase):

    def test_power_positive(self):
        self.assertEqual(arithmetic.power('2', '3'), '8')

    def test_power_zero_exponent(self):
        self.assertEqual(arithmetic.power('5', '0'), '1')

    def test_power_one_exponent(self):
        self.assertEqual(arithmetic.power('7', '1'), '7')

    def test_power_fractional(self):
        self.assertEqual(arithmetic.power('4', '0.5'), '2')

    def test_power_negative_exponent(self):
        self.assertEqual(arithmetic.power('2', '-1'), '0.5')

    def test_modulo(self):
        self.assertEqual(arithmetic.modulo('10', '3'), '1')

    def test_modulo_no_remainder(self):
        self.assertEqual(arithmetic.modulo('10', '5'), '0')

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            arithmetic.modulo('5', '0')

    def test_floor_div(self):
        self.assertEqual(arithmetic.floor_div('7', '2'), '3')

    def test_floor_div_exact(self):
        self.assertEqual(arithmetic.floor_div('6', '3'), '2')

    def test_floor_div_by_zero(self):
        with self.assertRaises(ValueError):
            arithmetic.floor_div('5', '0')

    def test_sqrt(self):
        self.assertEqual(arithmetic.sqrt('16'), '4.0')

    def test_sqrt_zero(self):
        self.assertEqual(arithmetic.sqrt('0'), '0.0')

    def test_sqrt_non_perfect(self):
        res = float(arithmetic.sqrt('2'))
        self.assertAlmostEqual(res, 1.4142135623730951, places=5)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            arithmetic.sqrt('-4')

    def test_cbrt(self):
        self.assertEqual(arithmetic.cbrt('27'), '3.0')

    def test_cbrt_zero(self):
        self.assertEqual(arithmetic.cbrt('0'), '0.0')

    def test_log(self):
        self.assertEqual(arithmetic.log('100'), '2.0')

    def test_log_one(self):
        self.assertEqual(arithmetic.log('1'), '0.0')

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            arithmetic.log('0')

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            arithmetic.log('-5')

    def test_ln_one(self):
        self.assertEqual(arithmetic.ln('1'), '0.0')

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            arithmetic.ln('0')

    def test_exp_zero(self):
        self.assertEqual(arithmetic.exp('0'), '1.0')

    def test_exp_one(self):
        res = float(arithmetic.exp('1'))
        self.assertAlmostEqual(res, 2.718281828, places=5)

    def test_ceil(self):
        self.assertEqual(arithmetic.ceil('4.2'), '5')

    def test_ceil_integer(self):
        self.assertEqual(arithmetic.ceil('4.0'), '4')

    def test_floor(self):
        self.assertEqual(arithmetic.floor('4.8'), '4')

    def test_floor_integer(self):
        self.assertEqual(arithmetic.floor('4.0'), '4')

    def test_factorial(self):
        self.assertEqual(arithmetic.factorial('5'), '120')

    def test_factorial_zero(self):
        self.assertEqual(arithmetic.factorial('0'), '1')

    def test_factorial_one(self):
        self.assertEqual(arithmetic.factorial('1'), '1')

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            arithmetic.factorial('-1')

    def test_permutation(self):
        self.assertEqual(arithmetic.permutation('5', '2'), '20')

    def test_permutation_same(self):
        self.assertEqual(arithmetic.permutation('5', '5'), '120')

    def test_permutation_zero_r(self):
        self.assertEqual(arithmetic.permutation('5', '0'), '1')

    def test_permutation_invalid(self):
        with self.assertRaises(ValueError):
            arithmetic.permutation('2', '5')

    def test_combination(self):
        self.assertEqual(arithmetic.combination('5', '2'), '10')

    def test_combination_same(self):
        self.assertEqual(arithmetic.combination('5', '5'), '1')

    def test_combination_zero_r(self):
        self.assertEqual(arithmetic.combination('5', '0'), '1')

    def test_combination_invalid(self):
        with self.assertRaises(ValueError):
            arithmetic.combination('2', '5')


if __name__ == "__main__":
    unittest.main()
