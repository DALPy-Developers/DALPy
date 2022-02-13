import unittest

from cormen_lib.arrays import Array, Array2D, sort
from cormen_lib.test_utils import cormen_equals


class ArrayTest(unittest.TestCase):
    def test_init(self):
        a = Array(2)
        self.assertIsNone(a[0])
        self.assertIsNone(a[1])

    def test_length(self):
        a = Array(2)
        self.assertEqual(a.length(), 2)

    def test_invalid_indices(self):
        a = Array(2)
        self.assertRaises(IndexError, lambda: a[-1])
        self.assertRaises(IndexError, lambda: a[2])

    def test_invalid_length(self):
        self.assertRaises(ValueError, lambda: Array(-1))

    def test_set_get(self):
        a = Array(2)
        a[0] = 2
        a[1] = 3
        self.assertEqual(a[0], 2)
        self.assertEqual(a[1], 3)

    def test_array_sort(self):
        a = Array(5)
        for i in range(5):
            a[i] = 5 - i
        a.sort()
        for i in range(5):
            self.assertEqual(a[i], i + 1)

    def test_sort(self):
        a = Array(5)
        for i in range(5):
            a[i] = 5 - i
        s = sort(a)
        for i in range(5):
            self.assertEqual(a[i], 5 - i)
            self.assertEqual(s[i], i + 1)


class Array2DTest(unittest.TestCase):
    def test_init(self):
        a = Array2D(1, 2)
        self.assertIsNone(a[0, 0])
        self.assertIsNone(a[0, 1])

    def test_dimensions(self):
        a = Array2D(1, 2)
        self.assertEqual(a.rows(), 1)
        self.assertEqual(a.columns(), 2)

    def test_invalid_indices(self):
        a = Array2D(1, 2)
        self.assertRaises(IndexError, lambda: a[-1, 0])
        self.assertRaises(IndexError, lambda: a[1, 0])
        self.assertRaises(IndexError, lambda: a[0, -1])
        self.assertRaises(IndexError, lambda: a[0, 2])

    def test_invalid_dimensions(self):
        self.assertRaises(ValueError, lambda: Array2D(0, 1))
        self.assertRaises(ValueError, lambda: Array2D(1, 0))

    def test_set_get(self):
        a = Array2D(1, 2)
        a[0, 0] = 2
        a[0, 1] = 3
        self.assertEqual(a[0, 0], 2)
        self.assertEqual(a[0, 1], 3)

    def test_array2d_inequal(self):
        a = Array2D(2, 2)
        a[0, 0] = 2
        a[0, 1] = 3
        a[1, 0] = 4
        a[1, 1] = 1
        b = Array2D(2, 2)
        b[0, 0] = 2
        b[0, 1] = 3
        b[1, 0] = 4
        b[1, 1] = 5
        assert not cormen_equals(a, b)

    def test_array2d_square_equal(self):
        a = Array2D(2, 2)
        a[0, 0] = 2
        a[0, 1] = 3
        a[1, 0] = 4
        a[1, 1] = 1
        b = Array2D(2, 2)
        b[0, 0] = 2
        b[0, 1] = 3
        b[1, 0] = 4
        b[1, 1] = 1
        assert cormen_equals(a, b)

    def test_array2d_rectangle_equal(self):
        a = Array2D(3, 2)
        a[0, 0] = 1
        a[0, 1] = 2
        a[1, 0] = 3
        a[1, 1] = 4
        a[2, 0] = 5
        a[2, 1] = 6
        b = Array2D(3, 2)
        b[0, 0] = 1
        b[0, 1] = 2
        b[1, 0] = 3
        b[1, 1] = 4
        b[2, 0] = 5
        b[2, 1] = 6
        assert cormen_equals(a, b)

if __name__ == '__main__':
    unittest.main()
