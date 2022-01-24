import unittest

from cormen_lib.heaps import build_min_heap, PriorityQueue, PriorityQueueUnderflowError
from cormen_lib.arrays import Array


class PriorityQueueTest(unittest.TestCase):
    def test_init(self):
        q = PriorityQueue()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_empty_ops(self):
        q = PriorityQueue()
        self.assertRaises(PriorityQueueUnderflowError, lambda: q.extract_min())
        self.assertRaises(PriorityQueueUnderflowError, lambda: q.minimum())

    def test_insert(self):
        q = PriorityQueue()
        q.insert('hw', 1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.minimum(), 'hw')
        self.assertFalse(q.is_empty())

    def test_insert_extract_min(self):
        q = PriorityQueue()
        q.insert('hw', 1)
        self.assertEqual(q.extract_min(), 'hw')
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_insert(self):
        q = PriorityQueue()
        activities = ['games', 'test', 'hw', 'quiz']
        priorities = [4, 1, 3, 2]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        self.assertEqual(q.extract_min(), 'test')
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.extract_min(), 'quiz')
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.extract_min(), 'hw')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.extract_min(), 'games')
        self.assertTrue(q.is_empty())

    def test_insert_at_end(self):
        q = PriorityQueue()
        activities = ['games', 'test', 'hw', 'quiz']
        priorities = [1, 2, 3, 4]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        for a in activities:
            self.assertEqual(a, q.extract_min())

    def test_decrease_key(self):
        q = PriorityQueue()
        activities = ['games', 'test', 'hw', 'quiz']
        priorities = [4, 1, 3, 5]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        q.decrease_key('quiz', 2)
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.extract_min(), 'test')
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.extract_min(), 'quiz')
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.extract_min(), 'hw')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.extract_min(), 'games')
        self.assertTrue(q.is_empty())

    def test_invalid_decrease_key(self):
        q = PriorityQueue()
        activities = ['games', 'test', 'hw', 'quiz']
        priorities = [4, 1, 3, 2]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        self.assertRaises(ValueError, lambda: q.decrease_key('quiz', 3))

    def test_insert_to_front(self):
        q = PriorityQueue()
        activities = ['games', 'hw', 'quiz', 'test']
        priorities = [4, 3, 2, 1]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
            self.assertEqual(q.minimum(), a)

    def test_decrease_key_to_front(self):
        q = PriorityQueue()
        activities = ['games', 'hw', 'quiz', 'test']
        priorities = [4, 3, 2, 1]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        q.decrease_key('games', 0)
        self.assertEqual('games', q.minimum())
        self.assertEqual(q.size(), 4)

    def test_decrease_key_no_move(self):
        q = PriorityQueue()
        activities = ['games', 'hw', 'quiz', 'test']
        priorities = [4, 3, 1, 0]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        q.decrease_key('hw', 2)
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.extract_min(), 'test')
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.extract_min(), 'quiz')
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.extract_min(), 'hw')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.extract_min(), 'games')
        self.assertTrue(q.is_empty())

    def test_decrease_key_nonexistent(self):
        q = PriorityQueue()
        activities = ['games', 'hw', 'quiz', 'test']
        priorities = [4, 3, 1, 0]
        for a, p in zip(activities, priorities):
            q.insert(a, p)
        self.assertRaises(ValueError, lambda: q.decrease_key('project', 2))


class BuildMinHeapTest(unittest.TestCase):
    def test_build_min_heap(self):
        a = Array(5)
        a[0] = 7
        a[1] = 4
        a[2] = 3
        a[3] = 1
        a[4] = 2
        self.assertIsNone(build_min_heap(a))
        self.assertEqual(a[0], 1)
        self.assertEqual(a[1], 2)
        self.assertEqual(a[2], 3)
        self.assertEqual(a[3], 4)
        self.assertEqual(a[4], 7)

    def test_build_min_heap_invalid(self):
        ls = [7, 4, 3, 1, 2]
        self.assertRaises(TypeError, lambda: build_min_heap(ls))


if __name__ == '__main__':
    unittest.main()
