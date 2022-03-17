import unittest
from dalpy.hashing import HashTable


class HashTableSet(unittest.TestCase):
    def test_empty(self):
        t = HashTable()
        self.assertFalse(t.contains_key('a'))
        self.assertRaises(KeyError, lambda: t.get_value('a'))
        self.assertRaises(KeyError, lambda: t.delete('a'))

    def test_insert(self):
        t = HashTable()
        t.insert('a', 1)
        self.assertEqual(1, t.get_value('a'))

    def test_contains(self):
        t = HashTable()
        t.insert('a', 1)
        self.assertTrue(t.contains_key('a'))

    def test_many_insert(self):
        t = HashTable()
        keys = ['a', 'b', 'c']
        for i, k in enumerate(keys):
            t.insert(k, i + 1)
        for i, k in enumerate(keys):
            self.assertTrue(t.contains_key(k))
            self.assertEqual(i + 1, t.get_value(k))

    def test_delete(self):
        t = HashTable()
        t.insert('a', 1)
        self.assertEqual(1, t.delete('a'))
        self.assertRaises(KeyError, lambda: t.delete('a'))

    def test_many_delete(self):
        t = HashTable()
        keys = ['a', 'b', 'c']
        for i, k in enumerate(keys):
            t.insert(k, i + 1)
        for i, k in enumerate(keys):
            self.assertEqual(i + 1, t.delete(k))
            self.assertFalse(t.contains_key(k))

    def test_duplicates(self):
        t = HashTable()
        t.insert('a', 1)
        t.insert('a', 2)
        self.assertEqual(2, t.get_value('a'))
        self.assertEqual(2, t.delete('a'))
        self.assertRaises(KeyError, lambda: t.delete('a'))

    def test_add_none(self):
        t = HashTable()
        t.insert('a', None)
        self.assertTrue(t.contains_key('a'))
        self.assertIsNone(t.get_value('a'))
        self.assertIsNone(t.delete('a'))


if __name__ == '__main__':
    unittest.main()
