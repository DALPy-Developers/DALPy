import unittest
from cormen_lib.misc_utils import *


class MiscTest(unittest.TestCase):
    def test_infintiy(self):
        self.assertGreater(INF, 0)
        self.assertGreater(INF, NEG_INF)
        self.assertGreater(INF, INF-1)
        self.assertEqual(INF, INF)
    
    def test_neg_infinity(self):
        self.assertLess(NEG_INF, 0)
        self.assertLess(NEG_INF, NEG_INF+1)
        self.assertLess(NEG_INF, INF)
        self.assertEqual(NEG_INF, NEG_INF)

    def test_ceil(self):
        self.assertEqual(ceil(10.5), 11)

    def test_floor(self):
        self.assertEqual(floor(10.5), 10)
    

if __name__ == '__main__':
    unittest.main()