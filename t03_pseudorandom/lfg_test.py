import unittest
from lfg import lfg


class TestLfg(unittest.TestCase):
    def test_lenght_seed(self):
        tmp = lfg((70, 100), 4)
        tmp.make_seed()
        self.assertEqual(100, len(tmp.seed))

    def test_valid_amount(self):
        tmp = lfg((70, 100), 4)
        self.assertEqual(True, tmp.valid_amount(150))

    def test_invalid_amount(self):
        tmp = lfg((7, 10), 4)
        with self.assertRaises(Exception):
            tmp.alfg_generate(150)

    def test_lenght_result(self):
        tmp = lfg((700, 1000), 4)
        self.assertEqual(1500, len(tmp.alfg_generate(1500)))

if __name__ == '__main__':
    unittest.main()
