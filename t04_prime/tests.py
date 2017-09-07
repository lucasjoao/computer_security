import unittest
from lucas import lucas
from mr import mr
from fermat import fermat
from utils import utils


class Tests(unittest.TestCase):
    # utils ###################################################################
    def test_odd(self):
        self.assertTrue(utils.make_number(100, 1000) % 2 != 0)

    # mr ######################################################################
    def test_right_decomposite(self):
        png = mr(10, 100, 10000)
        self.assertEqual(png.decomposite(12), (2, 3))

    def test_wrong_decomposite(self):
        png = mr(10, 100, 10000)
        self.assertNotEqual(png.decomposite(186), (2, 5))

    def test_true_primality_mr(self):
        png = mr(10, 100, 10000)
        self.assertTrue(png.primality_test(12, (2, 3)))

    def test_false_primality_mr(self):
        png = mr(10, 100, 10000)
        self.assertFalse(png.primality_test(26, (1, 13)))

    # fermat ##################################################################
    def test_true_primality_fermat(self):
        png = fermat(10, 100, 10000)
        self.assertTrue(png.primality_test(8837))

    def test_false_primality_fermat(self):
        png = fermat(10, 100, 10000)
        self.assertFalse(png.primality_test(297))

    # lucas ###################################################################
    def test_right_prime_factors(self):
        png = lucas(10, 100, 10000)
        self.assertEqual(png.prime_factors(75), [3, 5, 5])

    def test_wrong_prime_factors(self):
        png = lucas(10, 100, 10000)
        self.assertNotEqual(png.prime_factors(17), [1, 2, 17])

    def test_true_primality_lucas(self):
        png = lucas(10, 100, 10000)
        self.assertTrue(png.primality_test(1249))

    def test_false_primality_lucas(self):
        png = lucas(10, 100, 10000)
        self.assertFalse(png.primality_test(8826))

if __name__ == '__main__':
    unittest.main()
