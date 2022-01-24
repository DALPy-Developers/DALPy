"""This module holds classes related to LIFO stacks.

This module contains `Stack`, an implementation of a LIFO stack, and `StackUnderflowError`, an error raised by `Stack`.

Examples:
    Initializing, adding, and removing elements from a `Stack`:

        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()

    The following code will raise a `StackUnderflowError` because the second pop is done on an empty `Stack`:

        s.pop()
        s.pop()
"""


class StackUnderflowError(Exception):
    """This class is used by `Stack` to raise errors for operations done on an empty `Stack`."""

    def __init__(self, operation):
        """Initializes a `StackUnderflowError` that will be raised associated with a particular `Stack` operation.

        Args:
            operation: a string specifying the operation to raise an error on
        """
        super().__init__(f'Cannot perform {operation} on an empty stack.')


class Stack:
    """This class represents a LIFO stack.

    One may assume that this `Stack` has no maximum capacity.

    Examples:
        To initialize a `Stack`:

            s = Stack()

        To add elements to the end of `s`:

            s.push(1)
            s.push(2)

        To remove and return the element at the top of `s` (in this case `x = 2`):

            x = s.pop()

        To see the element at the top of `s` (in this case `y = 1`):

            y = s.top()
    """

    def __init__(self):
        """Initializes an empty `Stack` in `O(1)` time."""
        self.__buf = list()

    def top(self):
        """Gets the element at the top of this `Stack`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Stack`.

        Returns:
            The element at the top of the `Stack`. That is, the element that was last added to this `Stack` of the
            elements in it.

        Raises:
             StackUnderflowError: If this `Stack` is empty.
        """
        if len(self.__buf) == 0:
            raise StackUnderflowError('top()')
        return self.__buf[-1]

    def pop(self):
        """Removes the element at the top of this `Stack`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Stack`.

        Returns:
            The element at the top of the `Stack` that was removed. That is, the element that was last added to this
            `Stack` of the elements in it.

        Raises:
             StackUnderflowError: If this `Stack` is empty.
        """
        if len(self.__buf) == 0:
            raise StackUnderflowError('pop()')
        return self.__buf.pop()

    def push(self, value):
        """Adds an element to the top of this `Stack`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Stack`.

        Args:
            value: Element to add to this `Stack`. It can be of any type.
        """
        self.__buf.append(value)

    def is_empty(self):
        """Returns `True` if this `Stack` is empty, `False` otherwise in `O(1)` time w/r/t the size of this `Stack`."""
        return len(self.__buf) == 0

    def size(self):
        """Returns the integer number of elements in this `Stack` in `O(1)` time w/r/t the size of this `Stack`."""
        return len(self.__buf)
