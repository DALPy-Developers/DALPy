"""This module provides factory functions for creating and modifying Cormen-Lib objects.

The functions contained in this module are meant to be used when writing test cases for problems implemented in
Cormen-Lib.
"""

from cormen_lib.stacks import Stack
from cormen_lib.arrays import Array
from cormen_lib.queues import Queue


def make_queue(ls):
    """Creates a `Queue` from a `list` of elements, enqueueing from left to right.

    Args:
        ls: A `list` of elements to be enqueued into the `Queue`.
    """
    queue = Queue()
    for x in ls:
        queue.enqueue(x)
    return queue


def make_stack(ls):
    """Creates a `Stack` from a `list` of elements, pushing from left to right.

    Args:
        ls: A `list` of elements to be enqueued into the `Stack`.
    """
    s = Stack()
    for e in ls:
        s.push(e)
    return s


def copy_stack(s):
    """Creates a copy of a `Stack`.

    Args:
        s: The `Stack` to copy.
    """
    buf = Stack()
    while not s.is_empty():
        nxt = s.pop()
        buf.push(nxt)
        buf.push(nxt)
    cpy = Stack()
    while not buf.is_empty():
        s.push(buf.pop())
        cpy.push(buf.pop())
    return cpy


def make_array(ls):
    """Makes an `Array` from a `list` of elements.

    Args:
        ls: The `list` of elements to insert into a new `Array`.
    """
    a = Array(len(ls))
    for i, e in enumerate(ls):
        a[i] = e
    return a


def add_children(root, children):
    """Adds `NaryTreeNode`s to be the children of another `NaryTreeNode`.

    Args:
        root: an `NaryTreeNode` to which we will be adding children. This will be modified in place by this function.
        children: a `list` of `NaryTreeNode`s that are the children to be added. These nodes will be added as the
                  children of `root` in the order they occur in this `list`. `children[0]` will be the leftmost child of
                  `root`, `children[1]` will be the right sibling of `children[0]` and so on.
    """

    if len(children) == 0:
        return
    root.leftmost_child = children[0]
    for i, child in enumerate(children):
        child.parent = root
        if i < len(children) - 1:
            child.right_sibling = children[i + 1]
