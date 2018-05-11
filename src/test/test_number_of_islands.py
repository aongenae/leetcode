#!/usr/bin/env python
################################################################################
#
#   Filename:           test_number_of_islands.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..number_of_islands import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, grid, expected):
        solution = Solution().numIslands(grid)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(grid, solution, expected)
        )

    @staticmethod
    def _format_error(grid, solution, expected):
        return (
            'wrong result for the following grid:\n'
            '\n'
            '{}\n'
            '\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format('\n'.join(_Mixin._format_grid(grid)), solution, expected)
        )

    @staticmethod
    def _format_grid(grid):
        for rows in grid:
            yield ''.join(col for col in rows)


class TestLongestCommonPrefix(LeetcodeTest, _Mixin):

    def test_one_island_1(self):
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.validate(grid, expected=1)

    def test_three_islands_1(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        self.validate(grid, expected=3)
