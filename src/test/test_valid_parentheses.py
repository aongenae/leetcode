#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_valid_parentheses.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..valid_parentheses import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate_true(self, input_string):
        self.assertTrue(
            Solution().isValid(input_string),
            '"{}" is balanced'.format(input_string)
        )

    def validate_false(self, input_string):
        self.assertFalse(
            Solution().isValid(input_string),
            '"{}" is not balanced'.format(input_string)
        )


class TestValidParentheses(_Mixin, LeetcodeTest):

    def test_empty(self):
        self.validate_true('')

    def test_two_symbols_balanced(self):
        self.validate_true('()')

    def test_two_symbols_unbalanced(self):
        self.validate_false('(]')

    def test_two_symbols_unbalanced_open(self):
        self.validate_false('){')

    def test_two_symbols_unbalanced_same_open(self):
        self.validate_false('((')

    def test_three_symbols_unbalanced(self):
        self.validate_false('()]')

    def test_four_symbols_balanced(self):
        self.validate_true('{[]}')

    def test_four_symbols_unbalanced(self):
        self.validate_false('([)]')

    def test_six_symbols_balanced(self):
        self.validate_true('()[]{}')
