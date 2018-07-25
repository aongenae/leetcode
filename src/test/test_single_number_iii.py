#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_single_number_iii.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..single_number_iii import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums, expected):
        solution = Solution().singleNumber(nums)
        sorted(solution)
        sorted(expected)
        self.assertListEqual(
            solution,
            expected,
            _Mixin._format_error(nums, solution, expected)
        )

    @staticmethod
    def _format_error(nums, solution, expected):
        return (
            '\n \nConsidering the list {}\n'
            '    computed {}\n'
            '    expected {}'.format(
                nums,
                solution,
                expected
            )
        )


class TestSingleNumber(LeetcodeTest, _Mixin):

    def test_two_elements(self):
        self.validate([3, 7], [3, 7])

    def test_both_in_middle(self):
        self.validate([1, 2, 1, 3, 5, 5], [2, 3])

    def test_front_and_end(self):
        self.validate([1, 2, 3, 3, 2, 5], [1, 5])

    def test_front_and_middle(self):
        self.validate([1, 2, 5, 5, 2, 3], [1, 3])

    def test_two_first(self):
        self.validate([1, 2, 5, 5, 3, 3], [1, 2])

    def test_two_last(self):
        self.validate([1, 2, 5, 1, 2, 3], [3, 5])
