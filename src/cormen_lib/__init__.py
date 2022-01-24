"""The Cormen-lib module is an insular data structures and algorithms library based on the Thomas H. Cormen's
*Introduction to Algorithms Third Edition.* This library was made specifically for administering and grading assignments related
to data structure and algorithms in computer science.

With this module students can receive progress reports on their problem sets in real time as they complete assignments.
Additionally, student submission assessment is done with unit tests, instead of hand-tracing, ensuring that the grades
that students receive accurately reflect their submissions.

The Cormen-lib testing suite offers extremely lightweight and flexible unit testing utilities that can be used on any
kind of assignment, whether to write functions or build classes. Course administration can be easily streamlined by
restricting which library data structures students are allowed to use on any particular assignment.

Cormen-lib began as a project by two Brandeis University undergraduate students to replace hand-written problem sets
written in pseudocode.

## Provided Data Structures
The Cormen-lib library offers a set of fundamental data structures and algorithms, with behavior as specified by H.
Cormen's Introduction to Algorithms. The following structures (separated by module) are supported:

* arrays
    * Array
    * Array2D
* queues
    * Queue
* stacks
    * Stack
* sets
    * Set
* linked_lists
    * SinglyLinkedListNode
    * DoublyLinkedListNode
* trees
    * BinaryTreeNode
    * NaryTreeNode
    * depth(NaryTreeNode)
* hashing
    * HashTable
* heaps
    * PriorityQueue
    * build_min_heap(Array)
* graphs
    * Vertex
    * Graph

## Unit Testing
Along with the Cormen-lib data structures come test utilities for writing test cases. The testing framework allows a
course administer to easily write test cases for either expected function output or general class behavior. Test cases
can then be compiled into a testing suite which runs all test cases. The testing suite has the capability set a test
case run-time timeout and two record comma-separated test results for administrative use.

Consider the example test case below:

    import unittest
    from cormen_lib.factory_utils import make_stack
    from cormen_lib.stacks import Stack
    from cormen_lib.test_utils import build_and_run_watched_suite, run_generic_test

    from student_submission import student_function

    # TestCase class for testing student_function
    class StudentFunctionTest(unittest.TestCase):

        # A single test case
        def simple_test_case(self):
            stack = make_stack([1, 2, 3])
            expected = make_stack([1, 1, 2, 2, 3, 3])
            run_generic_test(stack, expected, student_function, in_place=True)

    # Run the test cases using build_and_run_watched_suite
    if __name__ == '__main__':
        build_and_run_watched_suite([StudentFunctionTest], 4)


## Installation

Cormen-lib is available on PyPI, and can be installed with pip.

Cormen-lib has the following dependencies:

    Python >= 3.6

## Issues

We encourage you to report issues using the Github tracker. We welcome all kinds of issues, especially those related to
correctness, documentation and feature requests.

## Academic Usage

If you are planning to use Cormen-lib for a university course and have questions, feel free to reach out by email.
"""