#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_count_primes.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..count_primes import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, integer, expected):
        solution = Solution().countPrimes(integer)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(integer, solution, expected)
        )

    @staticmethod
    def _format_error(integer, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    integer:  {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(integer, solution, expected)
        )


class TestCountPrimes(LeetcodeTest, _Mixin):

    def test_0(self):
        self.validate(0, 0)

    def test_1(self):
        self.validate(1, 0)

    def test_2(self):
        self.validate(2, 0)

    def test_3(self):
        self.validate(3, 1)

    def test_10(self):
        self.validate(10, 4)
