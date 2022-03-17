"""Module that holds classes related to hashing.

This module contains the `HashTable` class. `HashTable` represents a hash table.

Examples:
    Creating a `HashTable`, adding key-value pairs, and retrieving values:

        t = HashTable()
        t.insert('a', 1)
        t.insert('b', 2)
        t.insert('c', 3)
        x = t.get_value('a')

    Removing elements from a `HashTable`:

        t.delete('a')
"""


class HashTable:
    """Represents a hash table that stores key-value pairs.

    Examples:
        To initialize a `HashTable`:

            t = HashTable()

        To insert key-value pairs:

            t.insert('a', 1)
            t.insert('b', 2)

        To check if `t` contains a key:

            if t.contains_key('a'):
                # Do something

        To remove a key-value pair:

            t.delete('a')
    """

    def __init__(self):
        """Initializes an empty `HashTable` in `O(1)` time."""
        self.__table = dict()

    def insert(self, key, value):
        """Inserts a key-value pair into this `HashTable`.

        One should assume that this runs in `O(1)` time w/r/t the number of entries in this `HashTable`.

        Args:
            key: A key. If its a new key, then a new entry will be added to this `HashTable` a new pair is added. This
                 can be of any type.
            value: A value to be associated with `key`. If `key` is already in this `HashTable`, then it will now have
                   `value` associated with it and the number of entries in the `HashTable` will not change. This can
                   be of any type including `None`.
        """
        self.__table[key] = value

    def contains_key(self, key):
        """Returns whether this `HashTable` contains a particular key.

        One should assume that this runs in `O(1)` time w/r/t the number of entries in this `HashTable`.

        Args:
            key: The key being searched.

        Returns:
            `True` if `key` is in this `HashTable` and `False` otherwise.
        """
        return key in self.__table

    def get_value(self, key):
        """Gets the value associated with a key in the `HashTable`.

        One should assume that this runs in `O(1)` time w/r/t the number of entries in this `HashTable`.

        Args:
            key: The key whose value is being retrieved. This can be of any type.

        Returns:
            The value associated with `key` if `key` is in this `HashTable`.

        Raises:
            KeyError: If `key` is not in this `HashTable`.
        """
        if key not in self.__table:
            raise KeyError(f'{key} not in table')
        return self.__table[key]

    def delete(self, key):
        """Removes the key-value pair with a particular key in the `HashTable`.

        One should assume that this runs in `O(1)` time w/r/t the number of entries in this `HashTable`.

        Args:
            key: The key specifying which key-value pair in the table should be removed. This can be of any type.

        Returns:
            The value that was previously associated with `key` if `key` is in this `HashTable` (before the key-value
            pair was removed).

        Raises:
            KeyError: If `key` is not in this `HashTable`.
        """
        if key not in self.__table:
            raise KeyError(f'cannot delete {key} as it does not exist in table')
        return self.__table.pop(key)
