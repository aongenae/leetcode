#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_exclusive_time_of_functions.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..exclusive_time_of_functions import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, n, logs, expected):
        solution = Solution().exclusiveTime(n, logs)
        self.assertListEqual(
            solution,
            expected,
            _Mixin._format_error(logs, solution, expected)
        )

    @staticmethod
    def _format_error(logs, solution, expected):
        return (
            '\n \nConsidering the list {}\n'
            '    computed {}\n'
            '    expected {}'.format(
                logs,
                solution,
                expected
            )
        )


class TestExclusiveTime(LeetcodeTest, _Mixin):

    def test_one_inner_function(self):
        self.validate(
            2,
            [
                '0:start:0',
                '1:start:2',
                '1:end:5',
                '0:end:6'
            ],
            [3, 4]
        )

    def test_two_consecutives_inner_functions(self):
        self.validate(
            3,
            [
                '0:start:0',
                '1:start:2',
                '1:end:5',
                '2:start:6',
                '2:end:8',
                '0:end:10'
            ],
            [4, 4, 3]
        )

    def test_three_nested_functions(self):
        self.validate(
            3,
            [
                '0:start:0',
                '1:start:2',
                '2:start:5',
                '2:end:7',
                '1:end:9',
                '0:end:11'
            ],
            [4, 5, 3]
        )

    def test_one_function(self):
        self.validate(
            1,
            [
                '0:start:0',
                '0:start:2',
                '0:end:5',
                '0:start:6',
                '0:end:6',
                '0:end:7'
            ],
            [8]
        )

    def test(self):
        self.validate(
            2,
            [
                '0:start:0',
                '0:start:2',
                '0:end:5',
                '1:start:6',
                '1:end:6',
                '0:end:7'
            ],
            [7, 1]
        )
