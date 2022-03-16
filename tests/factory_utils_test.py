import unittest
from cormen_lib.factory_utils import *
from cormen_lib.test_utils import build_and_run_watched_suite, generic_test

class CopyStackTest(unittest.TestCase):

    def test_copy_stack(self):
        s = make_stack([1, 2, 3, 4, 5])
        expected = make_stack([1, 2, 3, 4, 5])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)

    def test_empty_stack(self):
        s = make_stack([])
        expected = make_stack([])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)
    
    def test_singleton_stack(self):
        s = make_stack([1])
        expected = make_stack([1])
        generic_test(s, expected, copy_stack, enforce_no_mod=True)

if __name__ == '__main__':
    build_and_run_watched_suite([CopyStackTest])