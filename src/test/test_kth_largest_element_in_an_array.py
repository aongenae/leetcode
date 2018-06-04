#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_kth_largest_element_in_an_array.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..kth_largest_element_in_an_array import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums, k, expected):
        solution = Solution().findKthLargest(nums, k)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(nums, k, solution, expected)
        )

    @staticmethod
    def _format_error(nums, k, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    nums:     {}\n'
            '    k:        {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(nums, k, solution, expected)
        )


class TestFindKthLargest(LeetcodeTest, _Mixin):

    def test_1(self):
        self.validate(
            nums=[3, 2, 1, 5, 6, 4],
            k=2,
            expected=5
        )

    def test_2(self):
        self.validate(
            nums=[3, 2, 3, 1, 2, 4, 5, 5, 6],
            k=4,
            expected=4
        )
