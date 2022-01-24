import unittest
from cormen_lib.stacks import Stack, StackUnderflowError


class StackTest(unittest.TestCase):
    def test_init(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)

    def test_empty_ops(self):
        s = Stack()
        self.assertRaises(StackUnderflowError, lambda: s.top())
        self.assertRaises(StackUnderflowError, lambda: s.pop())

    def test_push(self):
        s = Stack()
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())

    def test_push_pop(self):
        s = Stack()
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_many_push(self):
        s = Stack()
        for i in range(3):
            s.push(i)
            self.assertEqual(s.top(), i)
        for i in range(3):
            self.assertEqual(s.top(), 3 - i - 1)
            self.assertEqual(s.pop(), 3 - i - 1)
            self.assertEqual(s.size(), 3 - i - 1)


if __name__ == '__main__':
    unittest.main()
