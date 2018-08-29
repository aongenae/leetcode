#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_count_primes.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..evaluate_reverse_polish_notation import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, tokens, expected):
        solution = Solution().evalRPN(tokens)
        self.assertEqual(
            solution,
            expected,
            _Mixin._format_error(tokens, solution, expected)
        )

    @staticmethod
    def _format_error(tokens, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    tokens:   {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(tokens, solution, expected)
        )


class TestEvaluateReversePolishNotation(LeetcodeTest, _Mixin):

    def test_1(self):
        self.validate(['2', '1', '+', '3', '*'], 9)

    def test_2(self):
        self.validate(['4', '13', '5', '/', '+'], 6)

    def test_3(self):
        self.validate(
            [
                '10', '6', '9', '3', '+', '-11', '*',
                '/', '*', '17', '+', '5', '+'
            ],
            22
        )
