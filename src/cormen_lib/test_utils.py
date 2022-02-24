"""This module provides utilities related to unit testing.

This module contains the `build_and_run_watched_suite`, `assert_array_equals`, `behavior_test`, `generic_test`,
`cormen_equals` and the `to_cormen_string` functions, as well as `UnexpectedReturnWarning`.
"""
import copy
import inspect
import math
import traceback
import unittest
import warnings
from multiprocessing import Process

from cormen_lib.arrays import Array, Array2D
from cormen_lib.factory_utils import copy_stack
from cormen_lib.graphs import Graph, Vertex
from cormen_lib.linked_lists import SinglyLinkedListNode
from cormen_lib.queues import Queue
from cormen_lib.sets import Set
from cormen_lib.stacks import Stack
from cormen_lib.trees import BinaryTreeNode, NaryTreeNode


def build_and_run_watched_suite(cases, timeout=None, show_tb=False, grading_file=None, warning_filter="once"):
    """Runs a set of test cases, ensuring that they do not run longer than `timeout` seconds. Optionally,
    writes comma-separated test results to a file.

    Args:
        cases: A list of TestCases to be run.
        timeout: Number of seconds to allow each test case to run for.
        show_tb: Boolean toggle for stack trace.
        grading_file: Output file path to store comma-separated test results.
        warning_filter: A `warnings.simplefilter` action. Default value ensures that warnings are only displayed once.
                        Choose `"ignore"` to suppress warnings.

    If `grading_file` is not specified, the test logs will be dumped to console.
    """

    def _warning(
            message,
            category,
            filename,
            lineno,
            file=None,
            line=None):
        print(f'{__bcolors.WARNING}{category.__name__}: {message}{__bcolors.ENDC}')

    warnings.showwarning = _warning
    warnings.simplefilter(warning_filter, UnexpectedReturnWarning)
    warnings.simplefilter("once", DeprecationWarning)
    watcher = _Watcher(show_tb)
    suite = unittest.TestSuite()
    for case in cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(case)
        suite.addTests(tests)
    for test in suite:
        __run_timed_test(test, watcher, timeout)
    if grading_file is not None:
        watcher.print_columns(grading_file)
    else:
        watcher.print_log()


def assert_array_equals(expected, actual, msg=None):
    """Asserts that two `cormen_lib.arrays.Array`s are equal, displaying a custom message if specified.

    Args:
        expected: The expected `cormen_lib.arrays.Array`.
        actual: The actual `cormen_lib.arrays.Array`.
        msg: The message to display on `AssertionError`, if not specified, then a default message is displayed.

    Raises:
        AssertionError: If `expected` != `actual`.
    """
    assert isinstance(actual, Array)
    assert expected.length() == actual.length(), f"Expected Array length = {expected.length()}, Actual Array length = {actual.length()}" if msg is None else msg
    for i in range(expected.length()):
        assert expected[i] == actual[
            i], f"Expected {expected[i]} at index {i}, Actual = {actual[i]}" if msg is None else msg


def behavior_test(behavior, objects):
    """Test the behavior of an object.

    Args:
        behavior: a `list` of `tuple`s of the form `(RESULT, METHOD, PARAMETERS)`.
        objects: a `list` of objects who's parameters are being called.

    Raises:
        AssertionError: If `METHOD(PARAMETERS) != RESULT`.

    For each tuple in behavior this test asserts that `METHOD(PARAMETERS) = RESULT`.

    In each `tuple` `METHOD` should an uncalled `callable`, for example:
    >>> stack = Stack()
    >>> uncalled_callable = stack.pop

    Notes:
    - If `METHOD` requires multiple parameters, then `PARAMETERS` can be passed as a `tuple`.
    - If `METHOD` has no required return, then `RESULT` can be omitted in favor of `(METHOD, PARAMETERS)`.
    - If `METHOD` has no parameters, then `PARAMETERS` can be omitted in favor of `(RESULT, METHOD)`.

    Example:

    >>> stack = Stack()
    >>> behavior = [ (stack.push, 1), (1, stack.pop) ]

    The objects parameter is the object who's behavior is being tested, which will be used for the test log.
    If multiple objects are being tested, pass a tuple of objects.
    """
    msg = f'Behavior:\ninit {", ".join(type(obj).__name__ for obj in objects) if isinstance(objects, list) else type(objects).__name__}\n'
    passed = True
    expected, method, params, result = None, None, None, None
    if not isinstance(behavior, list): behavior = [behavior]
    try:
        for event in behavior:
            if len(event) == 2 and callable(event[0]) and not isinstance(event[0], type): event = (None,) + event
            expected = event[0]
            method = event[1]
            if len(event) > 2:
                params = (event[2],)
                result = method(*params)
                msg += f'{__method_to_string((method,) + params)} {to_cormen_string(result)}'
            else:
                result = method()
                msg += f'{__method_to_string(method)} {to_cormen_string(result)}'
                params = None
            if cormen_equals(result, expected):
                msg += ' ✓\n'
                continue
            msg += f' ✗\nexpected {to_cormen_string(expected)}'
            passed = False
            break
    except Exception as e:
        # If expected is an exception then check that exception thrown matches expected exception
        msg += f'{__method_to_string((method,) + params if params is not None else method)} {to_cormen_string(result)} ✗\n'
        if type(expected) == type and isinstance(e, expected): return
        # error_message = e.args[0] if len(e.args) > 0 else e.with_traceback
        assert False, f'{msg}Unexpected error: {type(e).__name__}'
    assert passed, msg


def run_generic_test(params, expected, method, custom_comparator=None, in_place=False, enforce_no_mod=False,
                     init_params=None,
                     init_expected=None, params_to_string=None, expected_to_string=None, output_to_string=None):
    """Test the output of a function.

    Warnings:
        Deprecated in 1.1.0, to be removed. Use the generic_test function instead.

    Args:
        params: Parameters to be passed into the function being tested. This argument can either be a single parameter,
                or a list of parameters.
        expected: Expected return value of tested function with parameters specified by params.
        method: Function being tested. Must be a `callable`.
        custom_comparator: Function for determining if method output equals expected. Must be a `callable`.
        in_place: `True` if `expected` should be compared against `params`.
        enforce_no_mod: `bool` or a `list` of `bool` indicating which args should not be modified. Default `False`
                        allows modification of all args.
        init_params: Function for initializing parameters. Must be a `callable`.
        init_expected: Function for initializing expected output. Must be a `callable`.
        params_to_string: Function for displaying the parameters. Must be a `callable`.
        expected_to_string: Function for displaying the expected output. Must be a `callable`.
        output_to_string: Function for displaying the actual output. Must be a `callable`.

    Raises:
        AssertionError: If the test fails.
        UnexpectedReturnWarning: If `in_place` is set to `True` but `method` still returns a value.
        DeprecationWarning: If used in version >= 1.1.0.

    If `expected` is an `Exception`, the test will assert that the function tested on the given parameters throws the
    expected `Exception`. If no custom `to_string`s are specified, the `to_cormen_string` method will be used for
    displaying parameters, input and output.
    """
    warnings.warn("run_generic_test is deprecated after version 1.1.0, use generic_test instead.", DeprecationWarning,
                  stacklevel=2)
    params = init_params(params) if init_params is not None else params
    expected = init_expected(expected) if init_expected is not None else expected
    generic_test(params, expected, method, custom_comparator=custom_comparator, in_place=in_place,
                 enforce_no_mod=enforce_no_mod,
                 params_to_string=params_to_string, expected_to_string=expected_to_string,
                 output_to_string=output_to_string)


def generic_test(params, expected, method, custom_comparator=None, in_place=False, enforce_no_mod=False,
                 params_to_string=None, expected_to_string=None, output_to_string=None):
    """Test the output of a function.

    Args:
        params: Parameters to be passed into the function being tested. This argument can either be a single parameter,
                or a list of parameters.
        expected: Expected return value of tested function with parameters specified by params. If `expected` is an
                  `Exception`, the test will assert that the function tested on the given parameters throws the expected
                  `Exception`.
        method: Function being tested. Must be a `callable`.
        custom_comparator: Function for determining if method output equals expected. Must be a `callable`. Default
                           `None` which means that `cormen_equals` will be used.
        in_place: `True` if `expected` should be compared against `params`. By default this is `False`.
        enforce_no_mod: `bool` or a `list` of `bool` indicating which args should not be modified. Default `False`
                        allows modification of all args.
        params_to_string: Function for displaying the parameters. Must be a `callable`. Default `None` which means that
                          `cormen_to_string` will be used instead.
        expected_to_string: Function for displaying the expected output. Must be a `callable`. Default `None` which
                            means that `cormen_to_string` will be used instead.
        output_to_string: Function for displaying the actual output. Must be a `callable`. Default `None` which means
                          that `cormen_to_string` will be used instead.

    Raises:
        AssertionError: If the test fails.
        UnexpectedReturnWarning: If `in_place` is set to `True` but `method` still returns a value.
    """
    msg = f"Input: {to_cormen_string(params) if params_to_string is None else params_to_string(params)}\nExpected: {to_cormen_string(expected) if expected_to_string is None else expected_to_string(expected)}\n"
    params_copy = copy.deepcopy(params) if isinstance(params, list) else [copy.deepcopy(params)]
    passed = True
    try:
        result = method(*params) if isinstance(params, list) else method(params)
        if in_place:
            if result is not None:
                warnings.warn("A function that is meant to modify its argument(s) returned a non-None value.",
                              UnexpectedReturnWarning, stacklevel=2)
            result = params
        result_string = output_to_string(result) if output_to_string is not None else to_cormen_string(result)
        if custom_comparator is None:
            if not cormen_equals(expected, result):
                msg = f"{msg}Output: {result_string}"
                passed = False
        elif not custom_comparator(expected, result):
            msg = f"{msg}Output: {result_string}"
            passed = False
    except Exception as e:
        # If expected is an exception then check that exception thrown matches expected exception
        if type(expected) == type and isinstance(e, expected): return
        error_message = e.args[0] if len(e.args) > 0 else e.with_traceback
        assert False, f"{msg}Output: {error_message}"
    assert passed, msg
    enforce_no_mod = [enforce_no_mod] * len(params_copy) if isinstance(enforce_no_mod, bool) else enforce_no_mod
    modified_params_string = to_cormen_string(params) if params_to_string is None else params_to_string(params)
    if not isinstance(params, list): params = [params]
    for i, no_mod in enumerate(enforce_no_mod):
        if no_mod:
            assert cormen_equals(params_copy[i], params[
                i]), f"{msg}Output: The {str(i + 1) + __append_int(i + 1)} input argument should not have been modified.\nArguments: {modified_params_string}"


def cormen_equals(first, second):
    """Tests equality between two objects. If the objects are from the Cormen-Lib, they are compared using their own
    custom comparator.

    `cormen_equals` supports equality for the following objects: `cormen_lib.arrays.Array`, `cormen_lib.arrays.Array2D`,
    `cormen_lib.queues.Queue`, `cormen_lib.stacks.Stack`, `cormen_lib.sets.Set`,
    `cormen_lib.linked_lists.SinglyLinkedListNode`. For `cormen_lib.linked_lists.SinglyLinkedListNode`, checks that all
    nodes next of the passed `cormen_lib.linked_lists.SinglyLinkedListNode`s are the same. For instances of `float`s,
    `math.isclose` is used for comparison.

    Args:
        first: The first element to be tested.
        second: The second element to be tested

    Returns:
        `True` if `first = second` otherwise `False`.
    """
    if isinstance(first, Array) and isinstance(second, Array):
        return __array_equals(first, second)
    if isinstance(first, Array2D) and isinstance(second, Array2D):
        return __array2d_equals(first, second)
    if isinstance(first, Queue) and isinstance(second, Queue):
        return __queue_equals(first, second)
    if isinstance(first, Stack) and isinstance(second, Stack):
        return __stack_equals(first, second)
    if isinstance(first, Set) and isinstance(second, Set):
        return __set_equals(first, second)
    if isinstance(first, SinglyLinkedListNode) and isinstance(second, SinglyLinkedListNode):
        return __singly_linked_list_equals(first, second)
    if isinstance(first, float) and isinstance(second, float):
        return math.isclose(first, second)
    return first == second


def to_cormen_string(obj):
    """Generates a string representation of a Cormen-Lib object if passed object is from Cormen-Lib, otherwise calls
    native str method.

    to_cormen_string supports the following objects: `cormen_lib.arrays.Array`, `cormen_lib.arrays.Array2D`,
    `cormen_lib.queues.Queue`, `cormen_lib.stacks.Stack`, `cormen_lib.sets.Set`,
    `cormen_lib.linked_lists.SinglyLinkedListNode`, `cormen_lib.trees.BinaryTreeNode`, `cormen_lib.trees.NaryTreeNode`,
    `cormen_lib.graphs.Vertex`, and `cormen_lib.graphs.Graph`.

    Returns:
        string representation of `obj`.

    Args:
        obj: The object to convert to string
    """
    if isinstance(obj, list):
        return "[" + ", ".join(to_cormen_string(elem) for elem in obj) + "]"
    if isinstance(obj, Array):
        return __array_to_string(obj)
    if isinstance(obj, Array2D):
        return __array2d_to_string(obj)
    if isinstance(obj, Queue):
        return __queue_to_string(obj)
    if isinstance(obj, Stack):
        return __stack_to_string(obj)
    if isinstance(obj, Set):
        return __set_to_string(obj)
    if isinstance(obj, SinglyLinkedListNode):
        return __singly_linked_list_to_string(obj)
    if isinstance(obj, BinaryTreeNode):
        return __binary_tree_to_string(obj)
    if isinstance(obj, NaryTreeNode):
        return __nary_tree_to_string(obj)
    if isinstance(obj, Vertex):
        return __vertex_to_string(obj)
    if isinstance(obj, Graph):
        return __graph_to_string(obj)
    try:
        return str(obj)
    except:
        return obj


class UnexpectedReturnWarning(Warning):
    """A `Warning` subclass for instances where functions are expected to modify their arguments but return values instead."""
    pass


class _TestTimeoutError(Exception):
    def __init__(self, timeout):
        super().__init__(f'Test timed out after {timeout}s.')


class _Watcher(unittest.TestResult):

    def __init__(self, show_tb):
        super().__init__()
        self.test_ids = list()
        self.results = list()
        self.details = list()
        self.show_tb = show_tb

    @staticmethod
    def parse_id(test_id):
        return test_id[test_id.index('.') + 1:]

    @staticmethod
    def get_description(test):
        if test.shortDescription() is None: return '\n'
        lines = test._testMethodDoc.split('\n')
        return "\n".join(line.strip() for line in lines) + "Output:\t"

    def addSuccess(self, test) -> None:
        self.test_ids.append(_Watcher.parse_id(test.id()))
        self.results.append(1)

    def addFailure(self, test, err) -> None:
        self.test_ids.append(_Watcher.parse_id(test.id()))
        self.results.append(0)
        tb_str = ''
        if self.show_tb:
            tb_str = '\n' + ''.join(traceback.format_tb(err[2]))
        self.details.append((_Watcher.get_description(test), str(err[1]) + tb_str, _Watcher.parse_id(test.id())))

    def addError(self, test, err):
        self.test_ids.append(_Watcher.parse_id(test.id()))
        self.results.append(0)
        tb_str = ''
        if self.show_tb:
            tb_str = '\n' + ''.join(traceback.format_tb(err[2]))
        self.details.append(
            (_Watcher.get_description(test), err[0], str(err[1]) + tb_str, _Watcher.parse_id(test.id())))

    # Note The order in which the various tests will be run is determined by sorting the test method names with respect
    # to the built-in ordering for strings.
    def print_columns(self, fp):
        with open(fp, mode='w+', encoding='utf-8') as f:
            f.write(",".join(self.test_ids))
            f.write('\n')
            f.write(",".join(str(e) for e in self.results))

    def print_log(self):
        log = list()
        for detail in self.details:
            if len(detail) == 3:
                log.append(f'{detail[2].split("Test.")[0]} test failed.\n{detail[0]}{detail[1]}')
            else:
                log.append(f'{detail[0]} raised {detail[1]}.\nMessage: {detail[2]}')
        print("\n" + ("\n" + "-" * 40 + "\n").join(
            log) + f"\n{'=' * 40}\n{sum(self.results)}/{len(self.results)} tests passed.\n")


def __run_timed_test(test, watcher, timeout):
    if timeout is not None:
        p = Process(target=test.run)
        p.start()
        p.join(timeout=timeout)
        if p.is_alive():
            p.terminate()
            watcher.addError(test, (_TestTimeoutError, _TestTimeoutError(timeout)))
            return
    test.run(watcher)


def __array_to_string(array):
    out = "["
    for i in range(array.length()):
        out += f'{to_cormen_string(array[i])}, '
    return out[:-2] + "]" if array.length() > 0 else out + "]"


def __array2d_to_string(array):
    out = "["
    for i in range(array.rows()):
        out += "["
        for j in range(array.columns()):
            out += f'{to_cormen_string(array[(i, j)])}, '
        out = out[:-2] + "]\n "
    return out[:-2] + "]"


def __queue_to_string(queue):
    out = []
    for _ in range(queue.size()):
        next = queue.dequeue()
        out.append(to_cormen_string(next))
        queue.enqueue(next)
    return "[" + ", ".join(out) + "]"


def __stack_to_string(stack):
    out = []
    temp_stack = Stack()
    for _ in range(stack.size()):
        next = stack.pop()
        out.insert(0, to_cormen_string(next))
        temp_stack.push(next)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return "[" + ", ".join(out) + "]"


def __set_to_string(s):
    out = []
    for elem in s:
        out.append(to_cormen_string(elem))
    return "{" + ", ".join(out) + "}"


def __singly_linked_list_to_string(head):
    out = list()
    seen = set()
    while head is not None:
        if head in seen:
            out.append("cycle")
            break
        seen.add(head)
        out.append(to_cormen_string(head.data))
        head = head.next
    return "➔ ".join(out)


def __strip_trailing_nones(ls):
    while len(ls) > 0 and ls[-1] is None:
        ls.pop()


def __binary_tree_to_string(root):
    # https://leetcode.com/problems/balanced-binary-tree/
    if root is None:
        return ""

    out_buf = list()
    q = list()
    q.append(root)
    all_none_level = False
    while not all_none_level:
        k = len(q)
        all_none_level = True
        for _ in range(k):
            curr = q.pop(0)
            if curr is not None:
                q.append(curr.left)
                q.append(curr.right)
                out_buf.append(to_cormen_string(curr.data))
                all_none_level = False
            else:
                out_buf.append(None)
    __strip_trailing_nones(out_buf)
    return str(out_buf)


def __vertex_to_string(vertex):
    return vertex.get_name()


def __graph_to_string(graph):
    contents = list()
    for vertex in graph.vertices():
        edges = list()
        for dest in graph.adj(vertex):
            edge_str = f'{dest.get_name()}'
            weight = graph.weight(vertex, dest)
            if weight is not None:
                edge_str += f' <{weight}>'
            edges.append(edge_str)
        edges = ', '.join(edges)
        contents.append(f'{vertex.get_name()}: {edges}')
    contents = '\n'.join(contents)
    return contents


def __nary_tree_to_string(root):
    # https://leetcode.com/problems/n-ary-tree-preorder-traversal/
    if root is None:
        return ""
    out = list()
    q = [root, root.right_sibling]
    while len(q) > 0:
        k = len(q)
        for _ in range(k):
            curr = q.pop(0)
            if curr is None:
                out.append(None)
            else:
                out.append(to_cormen_string(curr.data))
                lm_child = curr.leftmost_child
                q.append(lm_child)
                while lm_child is not None:
                    lm_child = lm_child.right_sibling
                    q.append(lm_child)
    __strip_trailing_nones(out)
    return str(out)


def __array_equals(expected, actual):
    if expected.length() != actual.length(): return False
    for i in range(expected.length()):
        if expected[i] != actual[i]: return False
    return True


def __array2d_equals(expected, actual):
    if expected.rows() != actual.rows() or expected.columns() != actual.columns(): return False
    for i in range(expected.rows()):
        for j in range(expected.columns()):
            if expected[i, j] != actual[i, j]: return False
    return True


def __queue_equals(expected, actual):
    for _ in range(expected.size()):
        expected_elem = expected.dequeue()
        actual_elem = actual.dequeue()
        if expected_elem != actual_elem: return False
        expected.enqueue(expected_elem)
        actual.enqueue(actual_elem)
    return expected.size() == actual.size()


def __stack_equals(expected, actual):
    if expected.size() != actual.size(): return False
    expected_cpy = copy_stack(expected)
    actual_cpy = copy_stack(actual)
    i = 0
    while not expected_cpy.is_empty():
        e = expected_cpy.pop()
        a = actual_cpy.pop()
        if e != a: return False
        i += 1
    return True


def __set_equals(expected, actual):
    expected_set = set()
    actual_set = set()
    for elem in expected:
        expected_set.add(elem)
    for elem in actual:
        actual_set.add(elem)
    return expected_set == actual_set


def __singly_linked_list_equals(expected, actual):
    seen = set()
    while (expected is not None and actual is not None):
        if actual in seen: return False
        seen.add(actual)
        if expected != actual: return False
        expected = expected.next
        actual = actual.next
    return expected is None and actual is None


def __method_to_string(method):
    new_line = "\n"
    if isinstance(method, tuple):
        return f'({str(inspect.getsourcelines(method[0])[0][0]).strip(new_line).strip().split()[1].replace("(self,", "")}, {", ".join(str(param) for param in method[1:])})'
    return str(inspect.getsourcelines(method)[0][0]).strip("\n").strip().split()[1].replace('(self):', '()')


def __append_int(num):
    if num > 9:
        secondToLastDigit = str(num)[-2]
        if secondToLastDigit == '1':
            return 'th'
    lastDigit = num % 10
    if (lastDigit == 1):
        return 'st'
    elif (lastDigit == 2):
        return 'nd'
    elif (lastDigit == 3):
        return 'rd'
    else:
        return 'th'


class __bcolors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
