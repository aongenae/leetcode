#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_best_time_to_buy_and_sell_stock.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..best_time_to_buy_and_sell_stock import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, prices, expected):
        solution = Solution().maxProfit(prices)
        self.assertEqual(
            solution,
            expected,
            self._format_error(prices, solution, expected)
        )

    @staticmethod
    def _format_error(prices, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    prices:   {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(prices, solution, expected)
        )


class TestMaxProfit(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate(
            prices=[],
            expected=0
        )

    def test_single(self):
        self.validate(
            prices=[1],
            expected=0
        )

    def test_1(self):
        self.validate(
            prices=[7, 1, 5, 3, 6, 4],
            expected=5
        )

    def test_2(self):
        self.validate(
            prices=[7, 10, 1, 30, 6, 4, 2, 9],
            expected=29
        )

    def test_3(self):
        self.validate(
            prices=[2, 4, 1],
            expected=2
        )

    def test_4(self):
        self.validate(
            prices=[2, 1, 2, 1, 0, 1, 2],
            expected=2
        )

    def test_5(self):
        self.validate(
            prices=list(range(10000, 0, -1)),
            expected=0
        )

    def test_no_profit(self):
        self.validate(
            prices=[7, 6, 4, 3, 1],
            expected=0
        )
