import unittest

from dalpy.queues import Queue, QueueUnderflowError


class QueueTest(unittest.TestCase):
    def test_init(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)

    def test_empty_ops(self):
        q = Queue()
        self.assertRaises(QueueUnderflowError, lambda: q.front())
        self.assertRaises(QueueUnderflowError, lambda: q.dequeue())

    def test_enqueue(self):
        q = Queue()
        q.enqueue(2)
        self.assertEqual(q.front(), 2)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_enqueue(self):
        q = Queue()
        for i in range(3):
            q.enqueue(i)
            self.assertEqual(q.front(), 0)
        for i in range(3):
            self.assertEqual(q.front(), i)
            self.assertEqual(q.dequeue(), i)
            self.assertEqual(q.size(), 3 - i - 1)


if __name__ == '__main__':
    unittest.main()
