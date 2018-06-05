#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_trapping_rain_water.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..trapping_rain_water import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, heights, expected):
        solution = Solution().trap(heights)
        self.assertEqual(
            solution,
            expected,
            self._format_error(heights, solution, expected)
        )

    @staticmethod
    def _format_error(heights, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    heights:  {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(heights, solution, expected)
        )


class TestTrappingRainWater(LeetcodeTest, _Mixin):

    def _test_0(self):
        self.validate([], 0)

    def _test_1(self):
        self.validate([1], 0)

    def _test_2(self):
        self.validate([1, 1], 0)

    def _test_increasing(self):
        self.validate([1, 2, 3, 4, 5], 0)

    def _test_decreasing(self):
        self.validate([5, 4, 3, 2, 1], 0)

    def _test_capture_1_valley(self):
        self.validate(
            [0, 1, 0, 2, 1, 0],
            1
        )

    def test_capture_1_valley_deep(self):
        self.validate(
            [0, 2, 1, 0, 1, 3, 2, 1],
            4
        )

    def _test_capture_3_valleys(self):
        self.validate(
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            6
        )


class TestFindMountainHelper(LeetcodeTest):

    def _test_find_montain(self):
        self.assertEqual(
            Solution()._find_montain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
            1
        )

    def _test_find_montain_increasing(self):
        self.assertEqual(
            Solution()._find_montain([0, 1, 3, 5]),
            3
        )

    def _test_find_montain_decreasing(self):
        self.assertEqual(
            Solution()._find_montain([5, 4, 3, 2, 1, 0]),
            0
        )


class TestFindValleyHelper(LeetcodeTest):

    def _test_find_valley(self):
        self.assertEqual(
            Solution()._find_valley([4, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]),
            2
        )

    def _test_find_valley_increasing(self):
        self.assertEqual(
            Solution()._find_valley([0, 1, 3, 5]),
            0
        )

    def _test_find_valley_decreasing(self):
        self.assertEqual(
            Solution()._find_valley([5, 4, 3, 2, 1, 0]),
            5
        )
