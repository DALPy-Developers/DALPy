"""Module that holds classes related to sets.

This module contains the `Set` class. `Set` represents a set.

Examples:
    Creating a `Set`, adding elements, and checking membership:

        s = Set()
        s.union(Set(1))
        s.union(Set(2,3))
        if 1 in s:
            print("1")

    Removing elements from a `Set`:

        t = Set(3,4)
        s.difference(t)
"""


class Set:
    """Represents a set.

    This class represents a set that preserves insertion order. This allows for it to be used in cases where the order
    of the set's contents must be deterministic.

    Examples:
        To initialize an empty `Set`:

            s = Set()

        To add elements to `s` use `union` with another `Set`:

            s.union(Set(1))
            r = Set(2,3)
            s.union(r)

        To check if `s` contains an element:

            if 1 in s:
                # Do something

        To remove a Set of elements from `s`, make use of difference:

            t = Set(2,3)
            s.difference(t)

        To remove one element from `s`, make use of the ability to create a singleton set combined with difference:

            s.difference(Set(1))

        To iterate over a `Set`:

            for e in s:
                # Do something with e
    """

    def __init__(self, *initial_elements):
        """Initializes a `Set` in `O(1)` time.

        Args:
            initial_elements: To initialize the `Set` to contain some elements, pass any number of arguments separated
                              by commas that will be passed via this variable length arguments parameter.
        """

        # https://docs.python.org/3/library/stdtypes.html#dict
        # Dictionaries preserve insertion order. Note that updating a key does not affect the order.
        # Keys added after deletion are inserted at the end.
        self.__set = dict()
        for initial_element in initial_elements:
            self.__set[initial_element] = None

    def union(self, other_set):
        """Performs a set union operation on this `Set`.

        This method adds all the elements from another `Set` into this `Set` that do not already exist in this `Set`.
        Calling `s.union(Set(1))` on a `Set` `s` is akin to `s = s U {1}`. This runs in `O(n)` time where `n` is the
        size of the other `Set`.

        Args:
            other_set: Another `Set` specifying the elements to be added to this `Set` if they do not already exist.
                       This `Set` is unaffected by this method.

        Raises:
            TypeError: If `other_set` is not a `Set`.
        """
        if not isinstance(other_set, Set):
            raise TypeError(f'can only perform set union between Sets')
        self.__set.update(other_set.__set)

    def difference(self, other_set):
        """Performs a set difference operation on this `Set`.

        This method removes all the elements from this `Set` that occur in another set. Calling `s.difference(Set(1))`
        on a `Set` `s` is akin to `s = s - {1}`. This runs in `O(n)` time where `n` is the size of the other `Set`.

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
        yield from self.__set
