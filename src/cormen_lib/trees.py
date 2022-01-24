"""Module that holds classes and functions related to trees.

This module contains the `BinaryTreeNode` and `NaryTreeNode` classes. `BinaryTreeNode` can be used to recursively define
a binary tree. `NaryTreeNode` can be used to recursively define a doubly linked list. Problems or algorithms that
operate on trees should take an object of either of these classes. This module also contains the `depth` function which
computes the depth of an `NaryTreeNode` in a tree.

Examples:
    A binary tree can be created as follows:

        bt = BinaryTreeNode(1)
        bt.left = BinaryTreeNode(2)
        bt.right = BinaryTreeNode(3)

    An n-ary tree can be created as follows, where one can also get the depth of one of the children:

        nt = NaryTreeNode(1)
        c1 = NaryTreeNode(2)
        c2 = NaryTreeNode(3)
        c3 = NaryTreeNode(4)
        c1.parent = nt
        c2.parent = nt
        c3.parent = nt
        nt.leftmost_child = c1
        c1.right_sibling = c2
        c2.right_sibling = c3
        x = depth(c3)
"""


class BinaryTreeNode:
    """Represents a binary tree node.

    Attributes:
        data: The data stored in the node. This can be any type.
        left: A `BinaryTreeNode` representing the node that is to the left of this node in a tree.
        right: A `BinaryTreeNode` representing the node that is to the right of this node in a tree.
    """

    def __init__(self, data=None, left=None, right=None):
        """Initializes a `BinaryTreeNode` in `O(1)` time.

        Args:
            data: The data to be stored in the node. This can be of any type. By default, this is `None`.
            left: A `BinaryTreeNode` representing the node that is to the left of this node in a tree. By default this
                  is `None`.
            right: A `BinaryTreeNode` representing the node that is to the right of this node in a tree. By default this
                  is `None`.
        """
        self.data = data
        self.left = left
        self.right = right


class NaryTreeNode:
    """Represents a n-ary tree node.

    Attributes:
        data: The data stored in the node. This can be any type.
        parent: A `NaryTreeNode` representing the node that is the parent of this node in a tree.
        leftmost_child: A `NaryTreeNode` representing the node that is the leftmost child of this node in a tree.
        right_sibling: A `NaryTreeNode` representing the node that is the right sibling of this node in a tree.
    """

    def __init__(self, data=None, parent=None, leftmost_child=None, right_sibling=None):
        """Initializes a `NaryTreeNode` in `O(1)` time.

        Args:
            data: The data to be stored in the node. This can be of any type. By default, this is `None`.
            parent: A `NaryTreeNode` representing the node that is the parent of this node in a tree. By default, this
                    is `None`.
            leftmost_child: A `NaryTreeNode` representing the node that is the leftmost child of this node in a tree. By
                            default, this is `None`.
            right_sibling: A `NaryTreeNode` representing the node that is the right sibling of this node in a tree. By
                           default, this is `None`.
        """
        self.data = data
        self.parent = parent
        self.leftmost_child = leftmost_child
        self.right_sibling = right_sibling


def depth(node):
    """Computes the depth of a n-ary tree node.

    The depth of a node `v` is the number of edges on the path from the root to the node. One may assume this function
    runs in `O(h)` time where `h` is the height of tree the input node is contained in.

    Args:
        node: an `NaryTreeNode`.

    Returns:
        The integer depth of node in the tree its contained in.

    Raises:
        TypeError: If `node` is not an `NaryTreeNode`.
    """
    if not isinstance(node, NaryTreeNode):
        raise TypeError(f'Can only calculate depth of NnaryTreeNode not {type(node)}')
    levels = 0
    while node.parent is not None:
        node = node.parent
        levels += 1
    return levels
