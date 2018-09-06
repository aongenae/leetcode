#!/usr/bin/env python3
################################################################################
#
#   Filename:           powx_n.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #50
#
#   Problem description:
#   https://leetcode.com/problems/powx-n/description/
#
################################################################################


class Solution(object):

    def myPow(self, x, n):
        '''
        :type x: float
        :type n: int
        :rtype: float
        '''
        if n == 0:
            return 1.0

        limit = n

        if n < 0:
            x = 1 / x
            limit = -n

        result = 1
        current_product = x
        v = limit
        while v > 0:
            if v % 2 == 1:
                result *= current_product
            current_product *= current_product
            v //= 2

        return result
