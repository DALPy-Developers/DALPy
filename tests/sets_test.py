import unittest
from dalpy.sets import Set


class SetTest(unittest.TestCase):
    def test_init(self):
        s = Set()
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)

    def test_add(self):
        s = Set()
        s.add('a')
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())

    def test_contains(self):
        s = Set()
        self.assertFalse('a' in s)
        s.add('a')
        self.assertTrue('a' in s)
        self.assertFalse('b' in s)

    def test_many_add(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')
        self.assertTrue('a' in s)
        self.assertTrue('b' in s)
        self.assertTrue('c' in s)
        self.assertEqual(s.size(), 3)

    def test_iter(self):
        s = Set()
        elements = {'a', 'b', 'c'}
        for e in elements:
            s.add(e)
        set_elements = set()
        for e in s:
            set_elements.add(e)
        self.assertEqual(set_elements, elements)

    def test_difference(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')
        s2 = Set()
        s2.add('b')
        s.difference(s2)
        self.assertEqual(s.size(), 2)
        self.assertTrue('a' in s)
        self.assertTrue('c' in s)
        self.assertEqual(s2.size(), 1)
        self.assertTrue('b' in s2)

    def test_invalid_difference(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')
        self.assertRaises(TypeError, lambda: s.difference('b'))

    def test_duplicates(self):
        s = Set()
        s.add('a')
        s.add('a')
        self.assertEqual(s.size(), 1)

    def test_deterministic(self):
        s = Set()
        correct = ['a', 'b', 'c']
        for c in correct:
            s.add(c)
        for _ in range(100):
            for i, e in enumerate(s):
                self.assertEqual(correct[i], e)

    def test_remove(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')
        s.difference(Set('a'))
        self.assertFalse('a' in s)
        s.difference(Set('a'))
        self.assertTrue('b' in s and 'c' in s)

    def test_add_none(self):
        s = Set(None)
        self.assertTrue(s.is_empty())
        self.assertRaises(ValueError, lambda: s.add(None))


if __name__ == '__main__':
    unittest.main()
