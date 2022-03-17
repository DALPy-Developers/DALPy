"""Module that holds classes and functions related to 1 and 2 dimensional arrays.

This module contains the `Array` and `Array2D` classes and the `sort` function. `Array` represents a 1D array. `Array2D`
represents a 2D array. `sort` can be used to return a sorted copy of an `Array`.

Examples:
    Creating an `Array`, setting its elements, and getting a sorted copy:

        a = Array(3)
        a[0] = 1
        a[1] = 4
        a[2] = 2
        b = sort(a)

    Creating an `Array2D` and setting its elements:

        c = Array2D(3,2)
        for i in range(3):
            for j in range(2):
                c[i,j] = i + j
"""


class Array:
    """Represents a 1D array.

    This class represents a 1D fixed length array. It should be used like a Java array. That is, you cannot increase
    its length, slice it, or index it with negative numbers like a Python `list`. One cannot iterate over an `Array`
    like a Python `list` either. For example, `for e in a` will raise a `RuntimeError` for an `Array` `a`. A user should
    assume that indexing into an `Array` (either for getting or setting elements) is done in `O(1)` time with respect to
    the length of the `Array`.

    Examples:
        After constructing an `Array`, one can get an element at a particular index using square brackets `[]` as
        follows:

            a = Array(2)
            b = a[0]

        Here, `b` will store the first element in `a`.

        Similarly, one can set an element of an `Array` using a combination of `[]` and the assignment operator `=`

            a = Array(2)
            a[0] = 1

        Here, the first element of `a` is set to 1.

        Note that an `IndexError` will be raised in the event one supplies an index in `[]` that is negative or greater
        than or equal to the length of the `Array`.
    """

    def __init__(self, length):
        """Initializes an `Array` to be a particular length.

        Each of the length elements of this `Array` will be set to `None`. One should assume this runs in `O(length)`
        time.

        Args:
            length: An integer specifying the length of the `Array`.

        Raises:
            ValueError: If `length < 0`.
        """
        if length < 0:
            raise ValueError(f'length ({length}) can\'t be < 0')
        self.__buf = [None] * length

    def length(self):
        """Returns the integer length of this `Array` in `O(1)` time with respect to the length of the `Array`."""
        return len(self.__buf)

    def sort(self):
        """Sorts the elements of this `Array` in place.

        Note that this modifies this `Array`, it does not return a sorted copy. The user must make sure that the
        elements of the `Array` can be compared. For example, an empty `Array` cannot be sorted as `NoneType` (`None`)
        elements cannot be compared. A user may assume that this method runs in `O(n * log(n))` time where `n` is the
        length of the `Array`.
        """
        self.__buf.sort()

    def __getitem__(self, index):
        self.__check_index(index)
        return self.__buf[index]

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__buf[index] = value

    def __iter__(self):
        # Disables the users' ability to do for e in a for an Array a. Without disabling this, the default Python
        # __iter__ will call __getitem__ with an int.
        raise RuntimeError('Not allowed to iterate over Array like an iterable. Must go through `[]` with indices.')

    def __check_index(self, index):
        if index < 0 or index >= len(self.__buf):
            raise IndexError(f'index ({index}) can\'t be < 0 or >= length ({len(self.__buf)})')


class Array2D:
    """Represents a 2D Array.

    This class represents a 2D array with a fixed number of rows and columns. It should be used like a Java
    two-dimensional array. That is, you cannot increase its dimensions, slice it, or index it with negative numbers like
    a Python list. A user should assume that indexing into an `Array2D` (either for getting or setting) is done in
    `O(1)` time with respect to the dimensions of the `Array2D`.

    Examples:
        After constructing an `Array2D`, one can get an element at a particular (row, column) index using square
        brackets `[]` as follows:

            a = Array2D(2,2)
            b = a[0,1]

        Here, `b` will store the element in the second column of the first row of `a`.

        Similarly, one can set an element of an `Array2D` using a combination of `[]` and the assignment operator `=`

            a = Array2D(2,2)
            a[0,1] = 2

        Here, the element in the second column of the first of `a` is set to 2.

        Note that an `IndexError` will be raised in the event one supplies an index in `[]` that (i) has a row that is
        negative or greater than or equal to the number of rows of the `Array2D` or (ii) a column that is negative or
        greater than or equal to the number of columns of the `Array2D`.
    """

    def __init__(self, num_rows, num_columns):
        """Initializes an `Array2D` to be a particular number of rows and columns.

        Each of the `num_rows * num_columns` elements of this `Array` will be set to `None`. A user may assume that this
        method runs in `O(num_rows * num_columns)` time.

        Args:
            num_rows: An integer specifying the number of rows this `Array2D` should have.
            num_columns: An integer specifying the number of columns each of the rows of this `Array2D` should have.

        Raises:
            ValueError: If `num_rows <= 0` or `num_columns <= 0`.
        """
        if num_rows <= 0 or num_columns <= 0:
            raise ValueError(f'both num_rows ({num_rows}) and num_cols ({num_columns}) must be > 0')
        self.__buf = list()
        for _ in range(num_rows):
            self.__buf.append([None] * num_columns)

    def rows(self):
        """Gets the number of rows in this `Array2D`.

        A user should assume this runs in `O(1)` time with respect to the dimensions of this `Array2D`.

        Returns:
            The integer number of rows of this `Array2D`.
        """
        return len(self.__buf)

    def columns(self):
        """Gets the number of columns in this `Array2D`.

        A user should assume this runs in `O(1)` time with respect to the dimensions of this `Array2D`.

        Returns:
            The integer number of columns of this `Array2D`.
        """
        return len(self.__buf[0])

    def __iter__(self):
        # Disables the users' ability to do for e in a for an Array2D a. Without disabling this, the default Python
        # __iter__ will try to call __getitem__ with an int leading to a TypeError which is somewhat confusing.
        raise RuntimeError('Not allowed to iterate over Array2D like an iterable. Must go through `[]` with indices.')

    def __getitem__(self, index):
        row, column = self.__get_row_and_column(index)
        return self.__buf[row][column]

    def __setitem__(self, index, value):
        row, column = self.__get_row_and_column(index)
        self.__buf[row][column] = value

    def __get_row_and_column(self, index):
        row, column = index
        if row < 0 or row >= len(self.__buf):
            raise IndexError(f'row index ({row}) can\'t be < 0 or >= num_rows ({len(self.__buf)})')
        if column < 0 or column >= len(self.__buf[0]):
            raise IndexError(f'column index ({column}) can\'t be < 0 or >= num_columns ({len(self.__buf[0])})')
        return row, column


def sort(a):
    """Gets a sorted copy of an `Array`.

    This does not sort the `Array` in place. A user should assume this runs in `O(n * log(n))` time where `n` is the
    length of the input `Array`.

    Args:
        a: An `Array` to be sorted.

    Returns:
        A sorted (`Array`) copy of `a`.

    Raises:
        TypeError: If `a` is not an `Array`.
    """
    if not isinstance(a, Array):
        raise TypeError(f'can only sort Array objects')
    copy = Array(a.length())
    for i in range(a.length()):
        copy[i] = a[i]
    copy.sort()
    return copy
