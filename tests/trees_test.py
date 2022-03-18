import unittest

from dalpy.trees import depth, BinaryTreeNode, NaryTreeNode


class DepthTest(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, lambda: depth(BinaryTreeNode(3)))

    def test_empty(self):
        self.assertRaises(TypeError, lambda: depth(None))

    def test_root(self):
        a = NaryTreeNode('A')
        self.assertEqual(depth(a), 0)

    def test_slides_example(self):
        a = NaryTreeNode('A')
        b = NaryTreeNode('B')
        c = NaryTreeNode('C')
        d = NaryTreeNode('D')
        e = NaryTreeNode('E')
        f = NaryTreeNode('F')
        g = NaryTreeNode('G')
        h = NaryTreeNode('H')
        i = NaryTreeNode('I')

        a.leftmost_child = b
        b.parent = a
        c.parent = a
        b.right_sibling = c
        b.leftmost_child = d
        d.parent = b
        c.leftmost_child = e
        e.parent = c
        f.parent = c
        g.parent = c
        e.right_sibling = f
        f.right_sibling = g
        f.leftmost_child = h
        h.parent = f
        i.parent = f
        h.right_sibling = i

        self.assertEqual(depth(b), 1)
        self.assertEqual(depth(f), 2)
        self.assertEqual(depth(i), 3)
        self.assertEqual(depth(a), 0)


if __name__ == '__main__':
    unittest.main()
