python -m unittest
import unittest

class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 75), 25)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(100, -75), 25)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(-10, -10), 10)

if __name__ == "__main__":
    unittest.main()

