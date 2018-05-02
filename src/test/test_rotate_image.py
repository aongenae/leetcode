#!/usr/bin/env python
################################################################################
#
#   Filename:           test_longest_palindrome.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..rotate_image import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, matrix, expected):
        solution = Solution().rotate(matrix)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(matrix, solution, expected)
        )

    @staticmethod
    def _format_error(matrix, solution, expected):
        return (
            '\nwrong result for the following input:\n'
            '    -------\n'
            '    matrix:\n'
            '    -------\n'
            '{}\n'
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
                '\n'.join(e for e in _Mixin._format_matrix(solution)),
                '\n'.join(e for e in _Mixin._format_matrix(expected))
            )
        )

    @staticmethod
    def _format_matrix(matrix):
        for row in matrix:
            yield(' '.join(str(col) for col in row))


class TestRotateImage(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate([], [])

    def test_one(self):
        self.validate([[1]], [[1]])

    def test_three(self):
        self.validate(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
        )

    def test_four(self):
        self.validate(
            [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16]
            ],
            [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11]
            ]
        )
