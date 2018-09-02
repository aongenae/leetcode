#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_missing_ranges.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..missing_ranges import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, nums, lower, upper, expected_list):
        solution = Solution().findMissingRanges(nums, lower, upper)
        self.assertListEqual(solution, expected_list)


class TestIntersectionOfTwoArrays(_Mixin, LeetcodeTest):

    def test__empty_nums__same_lower_upper(self):
        self.validate(
            [],
            99,
            99,
            ['99']
        )

    def test__empty_nums__different_lower_upper(self):
        self.validate(
            [],
            0,
            99,
            ['0->99']
        )

    def test__one_element__equal_to_lower(self):
        self.validate(
            [-1],
            -1,
            0,
            ['0']
        )

    def test__one_element__equal_to_upper(self):
        self.validate(
            [-1],
            -2,
            -1,
            ['-2']
        )

    def test__one_elements__equal_to_both_lower_and_upper(self):
        self.validate(
            [-1],
            -1,
            -1,
            []
        )

    def test__including_lower(self):
        self.validate(
            [0, 1, 3, 50, 75],
            0,
            99,
            ['2', '4->49', '51->74', '76->99']
        )

    def test__including_both_lower_upper_at_boundaries(self):
        self.validate(
            [0, 1, 3, 50, 75, 99],
            0,
            99,
            ['2', '4->49', '51->74', '76->98']
        )

    def test__including_upper(self):
        self.validate(
            [1, 3, 50, 75, 99],
            0,
            99,
            ['0', '2', '4->49', '51->74', '76->98']
        )

    def test__nums_including_neither_lower_upper__upper_just_above(self):
        self.validate(
            [1, 3, 50, 75, 99],
            0,
            100,
            ['0', '2', '4->49', '51->74', '76->98', '100']
        )

    def test__nums_including_neither_lower_upper__upper_much_above(self):
        self.validate(
            [1, 3, 50, 75, 99],
            0,
            110,
            ['0', '2', '4->49', '51->74', '76->98', '100->110']
        )
