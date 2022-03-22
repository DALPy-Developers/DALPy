import unittest
from dalpy.sets import Set


class SetTest(unittest.TestCase):
    def test_init(self):
        s = Set()
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)
        s = Set(1)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.size(), 1)
        self.assertTrue(1 in s)
        s = Set(1, 2, 3, 4)
        self.assertEqual(s.size(), 4)
        self.assertTrue(all(i in s for i in range(1, 5)))

    def test_union(self):
        s = Set()
        s.union(Set('a'))
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())
        self.assertTrue('a' in s)

    def test_contains(self):
        s = Set()
        self.assertFalse('a' in s)
        s.union(Set('a'))
        self.assertTrue('a' in s)
        self.assertFalse('b' in s)

    def test_many_union(self):
        s = Set()
        s.union(Set('a'))
        s.union(Set('b'))
        s.union(Set('c'))
        self.assertTrue('a' in s)
        self.assertTrue('b' in s)
        self.assertTrue('c' in s)
        self.assertEqual(s.size(), 3)

    def test_big_union(self):
        s = Set()
        s.union(Set('a', 'b', 'c'))
        self.assertTrue('a' in s)
        self.assertTrue('b' in s)
        self.assertTrue('c' in s)
        self.assertEqual(s.size(), 3)

    def test_iter(self):
        s = Set('a', 'b', 'c')
        set_elements = set()
        for e in s:
            set_elements.add(e)
        self.assertTrue('a' in set_elements)
        self.assertTrue('b' in set_elements)
        self.assertTrue('c' in set_elements)

    def test_difference(self):
        s = Set('a', 'b', 'c')
        s2 = Set('b')
        s.difference(s2)
        self.assertEqual(s.size(), 2)
        self.assertTrue('a' in s)
        self.assertTrue('c' in s)
        self.assertEqual(s2.size(), 1)
        self.assertTrue('b' in s2)

    def test_invalid_difference(self):
        s = Set('a', 'b', 'c')
        self.assertRaises(TypeError, lambda: s.difference('b'))

    def test_invalid_union(self):
        s = Set('a', 'b', 'c')
        self.assertRaises(TypeError, lambda: s.union('b'))

    def test_duplicates(self):
        s = Set()
        s.union(Set('a'))
        s.union(Set('a'))
        self.assertEqual(s.size(), 1)
        s = Set('a', 'a')
        self.assertEqual(s.size(), 1)

    def test_deterministic(self):
        s = Set()
        correct = ['a', 'b', 'c']
        for c in correct:
            s.union(Set(c))
        for _ in range(100):
            for i, e in enumerate(s):
                self.assertEqual(correct[i], e)

    def test_remove(self):
        s = Set('a', 'b', 'c')
        s.difference(Set('a'))
        self.assertFalse('a' in s)
        s.difference(Set('a'))
        self.assertTrue('b' in s and 'c' in s)

    def test_add_none(self):
        s = Set(None)
        self.assertTrue(None in s)
        s = Set()
        s.union(Set(None))
        self.assertTrue(None in s)


if __name__ == '__main__':
    unittest.main()
