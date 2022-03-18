"""Module that holds classes related to sets.

This module contains the `Set` class. `Set` represents a set.

Examples:
    Creating a `Set`, adding elements, and checking membership:

        s = Set()
        s.add(1)
        s.add(2)
        s.add(3)
        if 1 in s:
            print("1")

    Removing elements from a `Set`:

        t = Set()
        t.add(3)
        t.add(4)
        s.difference(t)
"""


class Set:
    """Represents a set.

    This class represents a set that preserves insertion order. This allows for it to be used in cases where the order
    of the set's contents must be deterministic.

    Examples:
        To initialize a `Set`:

            s = Set()

        To add elements to `s`:

            s.add(1)
            s.add(2)

        To check if `s` contains an element:

            if 1 in s:
                # Do something

        To remove a Set of elements from `s`, make use of difference:

            t = Set()
            t.add(2)
            t.add(3)
            s.difference(t)

        To remove one element from `s`, make use of the ability to create a singleton set combined with difference:

            s.difference(Set(1))

        To iterate over a `Set`:

            for e in s:
                # Do something with e
    """

    def __init__(self, singleton_elem=None):
        """Initializes a `Set` in `O(1)` time.

        Args:
            singleton_elem: To initialize the `Set` to be a singleton `Set`, pass a non-`None` value as this parameter
                            (of any type). By default, this is `None`, in which case the `Set` is initialized to be
                            empty.
        """

        # https://docs.python.org/3/library/stdtypes.html#dict
        # Dictionaries preserve insertion order. Note that updating a key does not affect the order.
        # Keys added after deletion are inserted at the end.
        self.__set = dict()
        if singleton_elem is not None:
            self.__set[singleton_elem] = None

    def add(self, element):
        """Adds an element to the Set.

        Args:
            element: An element to add. If element is already in the `Set`, then it is not added again.

        Raises:
            ValueError: If element is `None`. This is to preserve the interpretation of `None` when initializing a
                        `Set`.
        """
        if element is None:
            raise ValueError('Cannot add None to a Set.')
        self.__set[element] = None

    def difference(self, other_set):
        """Performs a set difference operation on this `Set`.

        This method removes all the elements from this `Set` that occur in another set. A user should assume this runs
        in `O(n)` time where `n` is the size of the other `Set`.

        Args:
            other_set: Another `Set` specifying the elements to be removed from this `Set`. This `Set` is unaffected by
                       this method.

        Raises:
            TypeError: If `other_set` is not a `Set`.
        """
        if not isinstance(other_set, Set):
            raise TypeError(f'can only perform set difference between Sets')
        for k in other_set.__set:
            if k in self.__set:
                self.__set.pop(k)

    def is_empty(self):
        """Returns `True` if this `Set` is empty, `False` otherwise in `O(1)` time w/r/t the size of this `Set`."""
        return len(self.__set) == 0

    def size(self):
        """Returns the integer number of elements in this `Set` in `O(1)` time w/r/t the size of this `Set`."""
        return len(self.__set)

    def __contains__(self, element):
        return element in self.__set

    def __iter__(self):
        yield from iter(self.__set)
