#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_set_matrix_zeroes.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..set_matrix_zeroes import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, matrix, expected):
        Solution().setZeroes(matrix)
        self.assertEqual(
            matrix,
            expected,
            _Mixin._format_error(matrix, expected)
        )

    @staticmethod
    def _format_error(matrix, expected):
        return (
            '\nwrong result for the following input:\n'
            '    ---------\n'
            '    solution:\n'
            '    ---------\n'
            '{}\n'
            '    ---------\n'
            '    expected:\n'
            '    ---------\n'
            '{}\n'
            .format(
                '\n'.join(e for e in _Mixin._format_matrix(matrix)),
                '\n'.join(e for e in _Mixin._format_matrix(expected))
            )
        )

    @staticmethod
    def _format_matrix(matrix):
        for row in matrix:
            yield(' '.join(str(col) for col in row))


class TestSetZeroes(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate([], [])

    def test_empty_1(self):
        self.validate([[]], [[]])

    def _test_three_by_three_1(self):
        self.validate(
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]
        )

    def _test_four_by_three_1(self):
        self.validate(
            [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ],
            [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0]
            ]
        )

    def _test_one_by_three(self):
        self.validate(
            [
                [1, 0, 3]
            ],
            [
                [0, 0, 0]
            ]
        )

    def test_three_by_one(self):
        self.validate(
            [
                [1],
                [0],
                [3]
            ],
            [
                [0],
                [0],
                [0]
            ]
        )
