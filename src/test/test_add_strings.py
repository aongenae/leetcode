#!/usr/bin/env python
################################################################################
#
#   Filename:           test_add_two_numbers.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..add_strings import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string_1, string_2, expected):
        self.assertEqual(
            Solution().addStrings(string_1, string_2),
            expected,
            _Mixin._format_error(string_1, string_2)
        )

    @staticmethod
    def _format_error(string_1, string_2):
        return (
            'wrong result for the following input:\n'
            '    string_1: {!r}\n'
            '    string_2: {!r}\n'
            .format(string_1, string_2)
        )


class TestAddStrings(LeetcodeTest, _Mixin):

    def test_small_numbers_sum_less_than_ten(self):
        self.validate('4', '5', expected='9')

    def _not_enabled_test_small_numbers_sum_more_than_ten(self):
        self.validate('6', '5', expected='11')
