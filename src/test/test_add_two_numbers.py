#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_add_strings.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..add_two_numbers import Solution
from ..util import ListNode
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nb1, nb2, expected):
        l1 = _Mixin._build_list_node(nb1)
        l2 = _Mixin._build_list_node(nb2)
        solution = Solution().addTwoNumbers(l1, l2)

        try:
            self._validate_solution(solution, expected)
        except AssertionError as e:
            _Mixin._print_error(nb1, nb2, l1, l2, solution, expected, e)

    def _validate_solution(self, solution, expected):
        if solution is None:
            return
        self.assertEqual(
            solution.val,
            expected[0],
            'expected: "{}" got "{}"'.format(solution.val, expected[0])
        )
        self._validate_solution(solution.next, expected[1:])

    @staticmethod
    def _print_error(nb1, nb2, l1, l2, solution, expected, e):
        print('\n -> error "{}"'.format(e))
        print('nb1 "{}", l1'.format(nb1))
        _Mixin._format_listnode(l1)
        print('nb2 "{}", l2'.format(nb2))
        _Mixin._format_listnode(l2)
        print('solution')
        _Mixin._format_listnode(solution)
        print('expected "{}"'.format(expected))

    @staticmethod
    def _build_list_node(integer):

        def helper(integer, rest, previous_node):
            integer, rest = divmod(integer, 10)
            if rest == 0:
                return
            node = ListNode(rest)
            previous_node.next = node
            helper(integer, rest, node)

        integer, rest = divmod(integer, 10)
        first_node = ListNode(rest)
        helper(integer, rest, first_node)
        return first_node

    @staticmethod
    def _format_listnode(list_node):
        print(list_node.val)
        if list_node.next is None:
            return
        _Mixin._format_listnode(list_node.next)


class TestaddTwoNumbers(LeetcodeTest, _Mixin):
    ''' The test below are integer based
        We first convert the integer in a ListNode,
        Then run the Solution
        Finally validate the result
        '''

    def test_same_length(self):
        self.validate(nb1=342, nb2=465, expected=[7, 0, 8])

    def test_l1_longer(self):
        self.validate(nb1=89, nb2=1, expected=[0, 9])

    def test_l1_much_longer(self):
        self.validate(nb1=89999, nb2=1, expected=[0, 0, 0, 0, 9])

    def test_l2_longer(self):
        self.validate(nb1=0, nb2=73, expected=[3, 7])

    def test_sum_is_ten(self):
        self.validate(nb1=5, nb2=5, expected=[0, 1])


class TestMixin(LeetcodeTest, _Mixin):
    ''' Test the mixin utilities used in the tests '''

    def not_active_test_format_listnode(self):
        ''' This was a visual test, not enabled '''
        n2 = ListNode(2)
        n4 = ListNode(4)
        n3 = ListNode(3)

        n2.next = n4
        n4.next = n3

        self._format_listnode(n2)
