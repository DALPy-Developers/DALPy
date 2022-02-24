"""This module provides factory functions for creating Cormen-Lib objects.

This module contains the `make_queue`, `make_stack`, `copy_stack` and `make_array`.
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
        buf.push(s.pop())
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
