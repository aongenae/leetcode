#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_paint_house.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..paint_house import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, costs, expected):
        solution = Solution().minCost(costs)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(costs, solution, expected)
        )

    @staticmethod
    def _format_error(nums, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    costs:    {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(nums, solution, expected)
        )


class TestPaintHouse(LeetcodeTest, _Mixin):

    def test_three_houses(self):
        self.validate([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10)
