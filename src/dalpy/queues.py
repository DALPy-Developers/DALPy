"""This module holds classes related to FIFO queues.

This module contains `Queue`, an implementation of a FIFO queue, and `QueueUnderflowError`, an error raised by `Queue`.

Examples:
    Initializing, adding, and removing elements from a `Queue`:

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()

    The following code will raise a `QueueUnderflowError` because the second dequeue is done on an empty `Queue`:

        q.dequeue()
        q.dequeue()
"""


class QueueUnderflowError(Exception):
    """This class is used by `Queue` to raise errors for operations done on an empty `Queue`."""

    def __init__(self, operation):
        """Initializes a `QueueUnderflowError` that will be raised associated with a particular `Queue` operation.

        Args:
            operation: a string specifying the operation to raise an error on
        """
        super().__init__(f'Cannot perform {operation} on an empty queue.')


class Queue:
    """This class represents a FIFO queue.

    One may assume that this `Queue` has no maximum capacity.

    Examples:
        To initialize a `Queue`:

            q = Queue()

        To add elements to the end of `q`:

            q.enqueue(1)
            q.enqueue(2)

        To remove and return the element at the front of `q` (in this case `x = 1`):

            x = q.dequeue()

        To see the element at the front of `q` (in this case `y = 2`):

            y = q.front()
    """

    def __init__(self):
        """Initializes an empty `Queue` in `O(1)` time."""
        self.__buf = list()

    def front(self):
        """Gets the element at the front of this `Queue`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Queue`.

        Returns:
            The element at the front of the `Queue`. That is, the element that was first added to this `Queue` of the
            elements in it.

        Raises:
             QueueUnderflowError: If this `Queue` is empty.
        """
        if len(self.__buf) == 0:
            raise QueueUnderflowError('front()')
        return self.__buf[0]

    def dequeue(self):
        """Removes the element at the front of this `Queue`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Queue`.

        Returns:
            The element at the front of the `Queue` that was removed. That is, the element that was first added to this
            `Queue` of the elements in it.

        Raises:
             QueueUnderflowError: If this `Queue` is empty.
        """
        if len(self.__buf) == 0:
            raise QueueUnderflowError('dequeue()')
        return self.__buf.pop(0)

    def enqueue(self, value):
        """Adds an element to the end of this `Queue`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `Queue`.

        Args:
            value: Element to add to this `Queue`. It can be of any type.
        """
        self.__buf.append(value)

    def is_empty(self):
        """Returns `True` if this `Queue` is empty, `False` otherwise in `O(1)` time w/r/t the size of this `Queue`."""
        return len(self.__buf) == 0

    def size(self):
        """Returns the integer number of elements in this `Queue` in `O(1)` time w/r/t the size of this `Queue`."""
        return len(self.__buf)
