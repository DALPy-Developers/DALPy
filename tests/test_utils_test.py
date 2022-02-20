import unittest
import warnings
from cormen_lib.arrays import Array
from cormen_lib.test_utils import  run_generic_test, build_and_run_watched_suite, UnexpectedReturnWarning
from cormen_lib.factory_utils import make_array



class WarningTest(unittest.TestCase):
    
    def test_trigger_warning_and_pass(self):
        a = Array(0)
        b = Array(0)
        with warnings.catch_warnings(record=True) as w:
            run_generic_test(a, b, lambda x: make_array([1]), in_place=True)
            assert len(w) == 1
            assert issubclass(w[-1].category, UnexpectedReturnWarning)
            assert "modify its argument(s)" in str(w[-1].message)

    def test_trigger_warning_and_fail(self):
        a = Array(0)
        b = Array(1)
        with warnings.catch_warnings(record=True) as w:
            try:
                run_generic_test(a, b, lambda x: make_array([1]), in_place=True)
            except AssertionError:
                pass
            assert len(w) == 1
            assert issubclass(w[-1].category, UnexpectedReturnWarning)
            assert "modify its argument(s)" in str(w[-1].message)

    def test_trigger_warning_and_display(self):
        a = Array(0)
        b = Array(0)
        run_generic_test(a, b, lambda x: make_array([1]), in_place=True)

    def test_trigger_warning_and_display2(self):
        a = Array(0)
        b = Array(0)
        run_generic_test(a, b, lambda x: make_array([1]), in_place=True)

if __name__ == '__main__':
    build_and_run_watched_suite([WarningTest])
