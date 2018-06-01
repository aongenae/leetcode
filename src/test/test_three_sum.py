#!/usr/bin/env python
################################################################################
#
#   Filename:           test_reverse_integer.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..three_sum import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums, expected):
        computed_solution = Solution().threeSum(nums)
        self.assertEqual(
            sorted(computed_solution),
            sorted(expected),
            'Expected "{}" to be "{}"'.format(computed_solution, expected)
        )


class TestReverseInteger(LeetcodeTest, _Mixin):

    def test_not_long_enough(self):
        nums = [-1, 0]
        expected = []
        self.validate(nums, expected)

    def test_example(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [(-1, 0, 1), (-1, -1, 2)]
        self.validate(nums, expected)

    def test_no_solution(self):
        nums = [3, -2, 1, 0]
        expected = []
        self.validate(nums, expected)

    def test_zeros(self):
        nums = [0, 0, 0]
        expected = [(0, 0, 0)]
        self.validate(nums, expected)

    def test_2(self):
        nums = [-2, 0, 0, 2, 2]
        expected = [(-2, 0, 2)]
        self.validate(nums, expected)
