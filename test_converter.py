import unittest
from converter import convert


class TestConverter(unittest.TestCase):

    def test_oct_to_dec_basic(self):
        """Test basic octal to decimal conversion."""
        self.assertEqual(convert('247', 'OCT', 'DEC'), "D'167'")

    def test_dec_to_oct_basic(self):
        """Test basic decimal to octal conversion."""
        self.assertEqual(convert('167', 'DEC', 'OCT'), "O'247'")

    def test_zero_oct_to_dec(self):
        """Test zero from octal to decimal."""
        self.assertEqual(convert('0', 'OCT', 'DEC'), "D'0'")

    def test_zero_dec_to_oct(self):
        """Test zero from decimal to octal."""
        self.assertEqual(convert('0', 'DEC', 'OCT'), "O'0'")

    def test_leading_zeros_oct_to_dec(self):
        """Test octal with leading zeros to decimal."""
        self.assertEqual(convert('007', 'OCT', 'DEC'), "D'7'")

    def test_dec_to_oct_no_leading_zeros(self):
        """Test decimal to octal, no leading zeros in output."""
        self.assertEqual(convert('7', 'DEC', 'OCT'), "O'7'")

    def test_large_number_oct_to_dec(self):
        """Test large octal number to decimal."""
        # 777 octal = 7*64 + 7*8 + 7 = 448 + 56 + 7 = 511
        self.assertEqual(convert('777', 'OCT', 'DEC'), "D'511'")

    def test_large_number_dec_to_oct(self):
        """Test large decimal number to octal."""
        # 511 decimal = 777 octal
        self.assertEqual(convert('511', 'DEC', 'OCT'), "O'777'")

    def test_single_digit_oct_to_dec(self):
        """Test single digit octal to decimal."""
        self.assertEqual(convert('7', 'OCT', 'DEC'), "D'7'")

    def test_single_digit_dec_to_oct(self):
        """Test single digit decimal to octal."""
        self.assertEqual(convert('7', 'DEC', 'OCT'), "O'7'")

    def test_round_trip(self):
        """Test round trip conversion."""
        original = '123'
        octal = convert(original, 'DEC', 'OCT')
        back = convert(octal[2:-1], 'OCT', 'DEC')  # Remove O' and '
        self.assertEqual(back, f"D'{original}'")

    def test_invalid_from_base(self):
        """Test invalid from_base raises ValueError."""
        with self.assertRaises(ValueError):
            convert('123', 'HEX', 'DEC')

    def test_invalid_to_base(self):
        """Test invalid to_base raises ValueError."""
        with self.assertRaises(ValueError):
            convert('123', 'DEC', 'HEX')

    def test_invalid_digits_oct(self):
        """Test invalid digits for octal raises ValueError."""
        with self.assertRaises(ValueError):
            convert('89', 'OCT', 'DEC')

    def test_invalid_digits_dec(self):
        """Test invalid digits for decimal raises ValueError."""
        with self.assertRaises(ValueError):
            convert('12a', 'DEC', 'OCT')

    def test_case_insensitive_bases(self):
        """Test that bases are case insensitive."""
        self.assertEqual(convert('247', 'oct', 'dec'), "D'167'")
        self.assertEqual(convert('167', 'Dec', 'Oct'), "O'247'")

    def test_empty_value(self):
        """Test empty value raises ValueError."""
        with self.assertRaises(ValueError):
            convert('', 'OCT', 'DEC')


if __name__ == '__main__':
    unittest.main()