#!/usr/bin/env python3
################################################################################
#
#   Filename:           best_time_to_buy_and_sell_stock.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #121
#
#   Problem description:
#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
################################################################################


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_day = 0
        profit = 0
        for idx, price in enumerate(prices):
            if price < prices[buy_day]:
                buy_day = idx
            profit = max(profit, price - prices[buy_day])
        return profit
