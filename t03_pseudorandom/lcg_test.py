import unittest
from lcg import lcg


class Testlcg(unittest.TestCase):
    def test_generate(self):
        tmp = lcg(2, 3, 5, 10)
        self.assertEqual([3, 9, 1, 5, 3, 9, 1, 5], tmp.generate(8))

    def test_one_exception(self):
        with self.assertRaises(Exception):
            tmp = lcg(10, 5, 5, 5)

    def test_lenght_result(self):
        tmp = lcg(1664525, 1013904223, 10, 2**32)
        self.assertEqual(1500, len(tmp.generate(1500)))

if __name__ == '__main__':
    unittest.main()
