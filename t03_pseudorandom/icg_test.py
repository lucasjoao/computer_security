import unittest
from icg import icg


class TestIcg(unittest.TestCase):
    def test_modular_inverse(self):
        tmp = icg(100, 7, 1, 1)
        self.assertEqual(5, tmp.modular_inverse(3))

    def test_modular_inverse_again(self):
        tmp = icg(100, 6, 1, 1)
        with self.assertRaises(Exception):
            tmp.modular_inverse(2)

    def test_generate(self):
        tmp = icg(1, 5, 2, 3)
        self.assertEqual([1, 0, 3, 2, 4], tmp.generate(4))

if __name__ == '__main__':
    unittest.main()
