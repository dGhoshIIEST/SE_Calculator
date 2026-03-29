import unittest
import trigonometric as trig
from exceptions import undefinedoperationerror


class testtrigonometric(unittest.TestCase):

    def test_sin_0(self):
        self.assertEqual(trig.sin('0'), '0.0')

    def test_sin_30(self):
        self.assertEqual(trig.sin('30'), '0.5')

    def test_sin_90(self):
        self.assertEqual(trig.sin('90'), '1.0')

    def test_sin_180(self):
        res = float(trig.sin('180'))
        self.assertAlmostEqual(res, 0.0, places=5)

    def test_cos_0(self):
        self.assertEqual(trig.cos('0'), '1.0')

    def test_cos_60(self):
        res = float(trig.cos('60'))
        self.assertAlmostEqual(res, 0.5, places=5)

    def test_cos_90(self):
        res = float(trig.cos('90'))
        self.assertAlmostEqual(res, 0.0, places=5)

    def test_tan_0(self):
        self.assertEqual(trig.tan('0'), '0.0')

    def test_tan_45(self):
        res = float(trig.tan('45'))
        self.assertAlmostEqual(res, 1.0, places=5)

    def test_tan_90_undefined(self):
        with self.assertRaises(undefinedoperationerror):
            trig.tan('90')

    def test_asin_half(self):
        self.assertEqual(trig.asin('0.5'), '30.0')

    def test_acos_half(self):
        res = float(trig.acos('0.5'))
        self.assertAlmostEqual(res, 60.0, places=5)

    def test_atan_one(self):
        self.assertEqual(trig.atan('1'), '45.0')

    def test_asin_out_of_range(self):
        with self.assertRaises(ValueError):
            trig.asin('2')

    def test_acos_out_of_range(self):
        with self.assertRaises(ValueError):
            trig.acos('-2')

    def test_sinh_0(self):
        self.assertEqual(trig.sinh('0'), '0.0')

    def test_cosh_0(self):
        self.assertEqual(trig.cosh('0'), '1.0')

    def test_tanh_0(self):
        self.assertEqual(trig.tanh('0'), '0.0')

    def test_sinh_1(self):
        res = float(trig.sinh('1'))
        self.assertAlmostEqual(res, 1.1752011936, places=5)

    def test_cosh_1(self):
        res = float(trig.cosh('1'))
        self.assertAlmostEqual(res, 1.5430806348, places=5)


if __name__ == "__main__":
    unittest.main()
