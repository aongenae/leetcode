#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_single_number.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..single_number import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums, expected, duplicate=2):
        solution = Solution().singleNumber(nums, duplicate)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(nums, solution, expected)
        )

    @staticmethod
    def _format_error(nums, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    nums:     {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(nums, solution, expected)
        )


class TestSingleNumberTwoDuplicate(LeetcodeTest, _Mixin):

    def test_one_element(self):
        self.validate([5], 5)

    def test_first(self):
        self.validate([2, 2, 1], 1)

    def test_middle(self):
        self.validate([1, 2, 3, 1, 3], 2)

    def test_end(self):
        self.validate([4, 1, 2, 1, 2], 4)


class TestSingleNumberThreeDuplicate(LeetcodeTest, _Mixin):

    def test_one_element(self):
        self.validate([5], 5, 3)

    def test_first(self):
        self.validate([2, 2, 1, 2], 1, 3)

    def test_middle(self):
        self.validate([1, 2, 3, 1, 3, 1, 3], 2, 3)

    def test_end(self):
        self.validate([1, 4, 2, 1, 2, 1, 2], 4, 3)
