#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_intersection_of_two_arrays.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..intersection_of_two_arrays import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums1, nums2, expected_list):
        solution = Solution().intersection(nums1, nums2)
        self.assertListEqual(solution, expected_list)


class TestIntersectionOfTwoArrays(_Mixin, LeetcodeTest):

    def test_nums1_larger(self):
        self.validate(
            [1, 2, 2, 1],
            [2, 2],
            [2]
        )

    def test_nums1_smaller(self):
        self.validate(
            [4, 9, 5],
            [9, 4, 9, 8, 4],
            [9, 4]
        )
