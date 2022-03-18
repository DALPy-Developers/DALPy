import unittest
from dalpy.factory_utils import *
from dalpy.test_utils import build_and_run_watched_suite, generic_test
from dalpy.trees import NaryTreeNode


class CopyStackTest(unittest.TestCase):

    def test_copy_stack(self):
        s = make_stack([1, 2, 3, 4, 5])
        expected = make_stack([1, 2, 3, 4, 5])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)

    def test_empty_stack(self):
        s = make_stack([])
        expected = make_stack([])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)

    def test_singleton_stack(self):
        s = make_stack([1])
        expected = make_stack([1])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)


class AddChildrenTest(unittest.TestCase):
    def test_add_no_children(self):
        root = NaryTreeNode('a')
        nary_add_children(root, [])
        self.assertIsNone(root.leftmost_child)

    def test_add_1_child(self):
        root = NaryTreeNode('a')
        children = [NaryTreeNode('b')]
        nary_add_children(root, children)
        self.assertEqual(root.leftmost_child.data, 'b')
        self.assertEqual(children[0].parent.data, 'a')
        self.assertIsNone(children[0].right_sibling)

    def test_add_3_children(self):
        root = NaryTreeNode('a')
        children = [NaryTreeNode('b'), NaryTreeNode('c'), NaryTreeNode('d')]
        nary_add_children(root, children)
        self.assertEqual(root.leftmost_child.data, 'b')
        self.assertEqual(children[0].parent.data, 'a')
        self.assertEqual(children[1].parent.data, 'a')
        self.assertEqual(children[2].parent.data, 'a')
        self.assertEqual(children[0].right_sibling.data, 'c')
        self.assertEqual(children[1].right_sibling.data, 'd')
        self.assertIsNone(children[2].right_sibling)

    def test_add_grandchildren(self):
        root = NaryTreeNode('a')
        level1 = [NaryTreeNode('b'), NaryTreeNode('c')]
        level2 = [NaryTreeNode('d'), NaryTreeNode('e')]
        nary_add_children(root, level1)
        nary_add_children(level1[0], level2)
        self.assertEqual(root.leftmost_child.data, 'b')
        self.assertEqual(level1[0].parent.data, 'a')
        self.assertEqual(level1[1].parent.data, 'a')
        self.assertEqual(level1[0].right_sibling.data, 'c')
        self.assertIsNone(level1[1].right_sibling)
        self.assertEqual(level1[0].leftmost_child.data, 'd')
        self.assertEqual(level2[0].parent.data, 'b')
        self.assertEqual(level2[1].parent.data, 'b')
        self.assertEqual(level2[0].right_sibling.data, 'e')
        self.assertIsNone(level2[1].right_sibling)


if __name__ == '__main__':
    build_and_run_watched_suite([CopyStackTest, AddChildrenTest])
