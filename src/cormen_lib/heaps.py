"""This module holds classes and functions related to heaps and priority queues.

This module contains `PriorityQueue`, an implementation of a priority queue, and `PriorityQueueUnderflowError`, an error
raised by `PriorityQueue`. This module also contains the function `build_min_heap` which modifies the elements of an
`cormen_lib.arrays.Array` so that they construct a min heap.

Examples:
    Initializing, adding, and removing elements from a `PriorityQueue`:

        q = PriorityQueue()
        q.insert('a', 2)
        q.insert('b', 1)
        q.extract_min()

    The following code will raise a `PriorityQueueUnderflowError` because the second extract min is done on an empty
    `PriorityQueue`:

        q.extract_min()
        q.extract_min()
"""

from cormen_lib.arrays import Array
from heapq import heapify


class PriorityQueueUnderflowError(Exception):
    """This class is used by `PriorityQueue` to raise errors for operations done on an empty `PriorityQueue`."""

    def __init__(self, operation):
        """Initializes a `PriorityQueueUnderflowError` that will be raised associated with a `PriorityQueue` operation.

        Args:
            operation: a string specifying the operation to raise an error on
        """
        super().__init__(f'Cannot perform {operation} on an empty priority queue.')


class PriorityQueue:
    """This class represents a minimum priority queue.

    One may assume that this `PriorityQueue` has no maximum capacity.

    Examples:
        To initialize a `PriorityQueue`:

            q = PriorityQueue()

        To add elements to `q`:

            q.insert('a', 2)
            q.insert('b', 1)

        To remove and return the minimum priority element of `q` (in this case `x = 'b'`):

            x = q.extract_min()

        To see the minimum priority element of `q` (in this case `y = 'a'`):

            y = q.front()

        To decrease the priority of an element in `q`:

            q.decrease_key('a', 0)
    """

    def __init__(self):
        """Initializes an empty `PriorityQueue` in `O(1)` time."""
        self.__buf = list()

    def insert(self, element, priority):
        """Inserts an element into the `PriorityQueue` with an associated priority.

        One may assume that this operation runs in `O(log(n))` time where `n` is the size of this `Queue`.

        Args:
            element: An element to add to this `PriorityQueue`. This can be of any type.
            priority: The integer priority `element` should have in this `PriorityQueue`.
        """
        i = 0
        while i < len(self.__buf) and self.__buf[i][0] <= priority:
            i += 1
        self.__buf.insert(i, (priority, element))

    def extract_min(self):
        """Removes the minimum priority element of this `PriorityQueue`.

        One may assume that this operation runs in `O(log(n))` time where `n` is the size of this `PriorityQueue`.

        Returns:
            The element with the minimum priority in this `PriorityQueue`.

        Raises:
             PriorityQueueUnderflowError: If this `PriorityQueue` is empty.
        """
        if len(self.__buf) == 0:
            raise PriorityQueueUnderflowError('extract_min()')
        return self.__buf.pop(0)[1]

    def minimum(self):
        """Gets the minimum priority element of this `PriorityQueue`.

        One may assume that this operation runs in `O(1)` time with respect to the size of this `PriorityQueue`.

        Returns:
            The element with the minimum priority in this `PriorityQueue`.

        Raises:
             PriorityQueueUnderflowError: If this `PriorityQueue` is empty.
        """
        if len(self.__buf) == 0:
            raise PriorityQueueUnderflowError('minimum()')
        return self.__buf[0][1]

    def decrease_key(self, element, new_priority):
        """Decreases the priority of an element in this `PriorityQueue`.

        One may assume that this operation runs in `O(log(n))` time where `n` is the size of this `PriorityQueue`.

        Args:
            element: The element whose priority is being updated.
            new_priority: The new priority of `element`. It should be `<=` its existing priority.

        Raises:
            ValueError: If `element` is not in this `PriorityQueue` or `new_priority` is greater than the existing
                        priority of `element`.
        """
        idx = -1
        for i, (_, e) in enumerate(self.__buf):
            if e == element:
                idx = i
                break
        if idx == -1:
            raise ValueError(f'{element} does not exist in PriorityQueue')
        priority = self.__buf[idx][0]
        if new_priority > priority:
            raise ValueError(f'new priority {new_priority} must be <= current priority {priority}')
        if new_priority < priority:
            self.__buf.pop(idx)
            self.insert(element, new_priority)

    def size(self):
        """Returns the size of this `PriorityQueue` in `O(1)` time w/r/t the size of this `PriorityQueue`.

        Returns:
            The integer number of elements in this `PriorityQueue`.
        """
        return len(self.__buf)

    def is_empty(self):
        """Returns whether this `PriorityQueue` is empty in `O(1)` time w/r/t the size of this `PriorityQueue`.

        Returns:
            `True` if this `PriorityQueue` is empty, `False` otherwise.
        """
        return len(self.__buf) == 0


def build_min_heap(arr):
    """Modifies an `cormen_lib.arrays.Array` so that its elements make up a min heap.

    This method does not return a copy of the provided `cormen_lib.arrays.Array` whose elements make up a heap, it modifies it in place.
    Furthermore, all the elements (starting from index 0) are in a min heap. A user may assume that this method runs in
    `O(n)` time where `n` is the length of the input `cormen_lib.arrays.Array`.

    Args:
        arr: The input `cormen_lib.arrays.Array`. Its elements should be comparable with `<`, `>=`, etc.

    Raises:
        TypeError: If `arr` is not an `cormen_lib.arrays.Array`'.
    """
    if not isinstance(arr, Array):
        raise TypeError('can only build min heap of an Array')
    ls = [arr[i] for i in range(arr.length())]
    heapify(ls)
    for i in range(arr.length()):
        arr[i] = ls[i]
