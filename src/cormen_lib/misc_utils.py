"""This module provides miscellaneous utility functions and constants.

Currently, this module holds utilities only related to mathematical operations, but operations related to other aspects
of Python that should be wrapped into Cormen-Lib could be added here (e.g. related to strings).
"""

import sys
import math

INF = sys.maxsize
"""Integer constant representing infinity."""

NEG_INF = -sys.maxsize
"""Integer constant representing negative infinity."""


def ceil(x):
    """Returns x rounded up to the nearest integer."""
    return math.ceil(x)


def floor(x):
    """Returns x truncated."""
    return math.floor(x)
