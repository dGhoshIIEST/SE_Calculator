import unittest
import math
from trigonometric import Trignometry

class TestTrigonometric(unittest.TestCase):
    def setUp(self):
        self.trig = Trignometry()

    # --- Basic Trigonometric Tests ---

    def test_sin(self):
        self.assertAlmostEqual(self.trig.sin_deg(30), 0.5, places=5)
        self.assertAlmostEqual(self.trig.sin_deg(90), 1.0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(self.trig.cos_deg(60), 0.5, places=5)
        self.assertAlmostEqual(self.trig.cos_deg(0), 1.0, places=5)

    def test_tan(self):
        self.assertAlmostEqual(self.trig.tan_deg(45), 1.0, places=5)
        self.assertAlmostEqual(self.trig.tan_deg(0), 0.0, places=5)

    # --- Inverse ---

    def test_asin(self):
        self.assertAlmostEqual(self.trig.asin_deg(0.5), 30.0, places=5)
        with self.assertRaises(ValueError):
            self.trig.asin_deg(2)  # Out of range

    def test_acos(self):
        self.assertAlmostEqual(self.trig.acos_deg(0.5), 60.0, places=5)
        with self.assertRaises(ValueError):
            self.trig.acos_deg(-1.5)  # Out of range

    def test_atan(self):
        self.assertAlmostEqual(self.trig.atan_deg(1), 45.0, places=5)
        self.assertAlmostEqual(self.trig.atan_deg(0), 0.0, places=5)

    # --- Hyperbolic ---

    def test_sinh(self):
        self.assertAlmostEqual(self.trig.sinh_val(0), 0.0, places=5)
        self.assertAlmostEqual(self.trig.sinh_val(1), math.sinh(1), places=5)

    def test_cosh(self):
        self.assertAlmostEqual(self.trig.cosh_val(0), 1.0, places=5)
        self.assertAlmostEqual(self.trig.cosh_val(1), math.cosh(1), places=5)

    def test_tanh(self):
        self.assertAlmostEqual(self.trig.tanh_val(0), 0.0, places=5)
        self.assertAlmostEqual(self.trig.tanh_val(1), math.tanh(1), places=5)

    # --- Error Handling Tests ---

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.trig.sin_deg("not_a_number")
        with self.assertRaises(ValueError):
            self.trig.sinh_val(None)

if __name__ == '__main__':
    unittest.main()