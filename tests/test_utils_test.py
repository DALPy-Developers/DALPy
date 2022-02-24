import unittest
import warnings
import math
from cormen_lib.arrays import Array
from cormen_lib.graphs import Graph, Vertex
from cormen_lib.test_utils import cormen_equals, generic_test, build_and_run_watched_suite, UnexpectedReturnWarning
from cormen_lib.factory_utils import make_array


class WarningTest(unittest.TestCase):
    
    def test_trigger_warning_and_pass(self):
        a = Array(0)
        b = Array(0)
        with warnings.catch_warnings(record=True) as w:
            generic_test(a, b, lambda x: make_array([1]), in_place=True)
            assert len(w) == 1
            assert issubclass(w[-1].category, UnexpectedReturnWarning)
            assert "modify its argument(s)" in str(w[-1].message)

    def test_trigger_warning_and_fail(self):
        a = Array(0)
        b = Array(1)
        with warnings.catch_warnings(record=True) as w:
            try:
                generic_test(a, b, lambda x: make_array([1]), in_place=True)
            except AssertionError:
                pass
            assert len(w) == 1
            assert issubclass(w[-1].category, UnexpectedReturnWarning)
            assert "modify its argument(s)" in str(w[-1].message)

    def test_trigger_warning_and_display(self):
        a = Array(0)
        b = Array(0)
        generic_test(a, b, lambda x: make_array([1]), in_place=True)

    def test_trigger_warning_and_display2(self):
        a = Array(0)
        b = Array(0)
        generic_test(a, b, lambda x: make_array([1]), in_place=True)


class GenericTesterTest(unittest.TestCase):
    
    def basic_generic_test(self):
        a = Array(1)
        b = Array(1)
        generic_test(a, b, lambda x: x, enforce_no_mod=True)
    
    def test_requiring_no_modification_fail(self):
        a = Array(1)
        b = Array(1)
        b[0] = 1
        def fnc_that_modifies(x):
            x[0] = 1
            return x
        try:
            generic_test(a, b, fnc_that_modifies, enforce_no_mod=True)
        except AssertionError as e:
            assert "1st" in e.args[0], e.args[0]
            assert "[1]" in e.args[0], e.args[0]

    def test_requiring_no_modification_pass(self):
        a = Array(1)
        b = Array(1)
        b[0] = 1
        def fnc_that_doesnt_modify(x):
            c = Array(1)
            c[0] = 1
            return c
        generic_test(a, b, fnc_that_doesnt_modify, enforce_no_mod=True)

    def test_requiring_second_argument_no_modification(self):
        a = make_array([1, 2])
        b = make_array([1, 2])
        c = make_array([1, 3])
        def fnc_that_modifies_second(x, y):
            x[1] = 4
            y[1] = 3
            return y
        try:
            generic_test([a,b], c, fnc_that_modifies_second, enforce_no_mod=[False, True])
        except AssertionError as e:
            assert "[[1, 4], [1, 3]]" in e.args[0], e.args[0]
            assert "2nd" in e.args[0], e.args[0]
    
    def test_multiple_larger(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_edge(a, b, 0)
        g.add_edge(a, c, 0)
        g.add_edge(b, c, 2)
        g.add_edge(c, a, 3)
        x = list(range(15))
        def fnc_that_modifies(graph, x):
            e = Vertex('e')
            g.add_vertex(e)
            g.add_edge(e, c, 1)
        try:
            generic_test([g,x], None, fnc_that_modifies, enforce_no_mod=True, custom_comparator=lambda x,y:True)
        except AssertionError as e:
            assert '1st' in e.args[0], e.args[0]
            assert 'e: c <1>' in e.args[0], e.args[0]

    def test_larger_object(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_edge(a, b, 0)
        g.add_edge(a, c, 0)
        g.add_edge(b, c, 2)
        g.add_edge(c, a, 3)
        def fnc_that_modifies(graph):
            e = Vertex('e')
            g.add_vertex(e)
            g.add_edge(e, c, 1)
        try:
            generic_test(g, None, fnc_that_modifies, enforce_no_mod=True, custom_comparator=lambda x,y:True)
        except AssertionError as e:
            assert 'e: c <1>' in e.args[0], e.args[0]


    def test_requiring_second_argument_no_modification_arrays(self):
        a = make_array([1, 2, 3, 4, 5])
        b = make_array([6, 7, 8, 9,])
        c = 1
        def fnc_that_modifies_second(x, y):
            y[0] = -1000
            return 1
        try:
            generic_test([a,b], c, fnc_that_modifies_second, enforce_no_mod=[True, True])
        except AssertionError as e:
            assert '[-1000, 7, 8, 9]' in e.args[0], e.args[0]
            assert '2nd' in e.args[0], e.args[0]


class CormenEqualsTest(unittest.TestCase):

    def test_floats(self):
        x = math.sqrt(7)*math.sqrt(7)
        y = 7.0
        assert cormen_equals(x, y), f'y={y}, x={x}'



if __name__ == '__main__':
    build_and_run_watched_suite([WarningTest, GenericTesterTest, CormenEqualsTest])
