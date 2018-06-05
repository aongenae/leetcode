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

    def test_0(self):
        self.validate([], 0)

    def test_1(self):
        self.validate([1], 0)

    def test_2(self):
        self.validate([1, 1], 0)

    def test_increasing(self):
        self.validate([1, 2, 3, 4, 5], 0)

    def test_decreasing(self):
        self.validate([5, 4, 3, 2, 1], 0)

    def test_one_valley(self):
        self.validate([1, 0, 2], 1)

    def test_one_valley_in_middle(self):
        self.validate([0, 1, 0, 2, 1, 0], 1)

    def test_one_valley_end(self):
        self.validate([5, 4, 1, 2], 1)

    def test_one_deep_valley(self):
        self.validate([5, 2, 1, 2, 1, 5], 14)

    def test_one_deep_valley_in_middle(self):
        self.validate([0, 2, 1, 0, 1, 3, 2, 1], 4)

    def test_three_valleys(self):
        self.validate([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)


class TestFindSummits(LeetcodeTest):

    def test_no_summits_increasing(self):
        self.assertListEqual(
            list(Solution()._find_summits([1, 2, 3])),
            []
        )

    def test_no_summits_decreasing(self):
        self.assertListEqual(
            list(Solution()._find_summits([3, 2, 1])),
            []
        )

    def test_one_summit(self):
        self.assertListEqual(
            list(Solution()._find_summits([1, 0, 1])),
            [(0, 2)]
        )

    def _test_one_summit_two_small_valley(self):
        self.assertListEqual(
            list(Solution()._find_summits([5, 1, 3, 0, 5])),
            [(0, 4)]
        )

    def test_one_summit_with_right_downhill(self):
        self.assertListEqual(
            list(Solution()._find_summits([3, 0, 2, 0])),
            [(0, 2)]
        )

    def test_one_summit_with_left_uphill(self):
        self.assertListEqual(
            list(Solution()._find_summits([0, 3, 1, 2])),
            [(1, 3)]
        )

    def test_two_summit(self):
        self.assertListEqual(
            list(Solution()._find_summits([1, 0, 1, 0, 1])),
            [(0, 2), (2, 4)]
        )

    def test_two_distinct_summits(self):
        self.assertListEqual(
            list(Solution()._find_summits([1, 0, 1, 1, 0, 1])),
            [(0, 2), (2, 5)]
        )

    def test_three_summit(self):
        self.assertListEqual(
            list(Solution()._find_summits([1, 0, 1, 0, 1, 0, 5])),
            [(0, 2), (2, 4), (4, 6)]
        )


class TestFindMountainHelper(LeetcodeTest):

    def test_find_mountain(self):
        self.assertEqual(
            Solution()._find_mountain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
            1
        )

    def test_find_mountain_duplicate(self):
        self.assertEqual(
            Solution()._find_mountain([0, 1, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]),
            1
        )

    def test_find_mountain_increasing(self):
        self.assertEqual(
            Solution()._find_mountain([1, 2, 3]),
            2
        )

    def test_find_mountain_decreasing(self):
        self.assertEqual(
            Solution()._find_mountain([5, 4, 3, 2, 1, 0]),
            0
        )


class TestFindValleyHelper(LeetcodeTest):

    def test_find_valley(self):
        self.assertEqual(
            Solution()._find_valley([4, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]),
            2
        )

    def test_find_valley_duplicate(self):
        self.assertEqual(
            Solution()._find_valley([4, 1, 0, 0, 1, 0, 1, 3, 2, 1, 2, 1]),
            2
        )

    def test_find_valley_increasing(self):
        self.assertEqual(
            Solution()._find_valley([0, 1, 3, 5]),
            0
        )

    def test_find_valley_decreasing(self):
        self.assertEqual(
            Solution()._find_valley([5, 4, 3, 2, 1, 0]),
            5
        )


class TestProcessValley(LeetcodeTest):

    def test_equal_valley(self):
        self.assertEqual(
            Solution()._process_valley([1, 0, 1], 0, 2),
            1
        )

    def test_valley_with_duplicate(self):
        self.assertEqual(
            Solution()._process_valley([1, 1, 0, 1], 0, 3),
            1
        )

    def test_first_is_higher_valley(self):
        self.assertEqual(
            Solution()._process_valley([2, 0, 1], 0, 2),
            1
        )

    def test_second_is_higher_valley(self):
        self.assertEqual(
            Solution()._process_valley([2, 0, 3], 0, 2),
            2
        )

    def test_equal_valley_middle(self):
        self.assertEqual(
            Solution()._process_valley([2, 1, 0, 1, 2], 1, 3),
            1
        )

    def test_first_is_higher_valley_middle(self):
        self.assertEqual(
            Solution()._process_valley([4, 2, 0, 1, 5], 1, 3),
            1
        )

    def test_second_is_higher_valley_middle(self):
        self.assertEqual(
            Solution()._process_valley([4, 2, 0, 3, 1], 1, 3),
            2
        )

    def test_deep_valley(self):
        self.assertEqual(
            Solution()._process_valley([3, 2, 1, 0, 1, 2, 3], 0, 6),
            9
        )

    def test_deep_unbalanced_first_is_higher_valley(self):
        self.assertEqual(
            Solution()._process_valley([3, 0, 1, 2, 3, 0, 1], 0, 4),
            6
        )

    def test_deep_unbalanced_second_is_higher_valley(self):
        self.assertEqual(
            Solution()._process_valley([4, 1, 0, 8], 0, 3),
            7
        )
