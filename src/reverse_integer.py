#!/usr/bin/env python3
################################################################################
#
#   Filename:           reverse_integer.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #7
#
#   Problem description:
#   https://leetcode.com/problems/reverse-integer/description/
#
################################################################################


class Solution(object):

    def reverse(self, x):
        negative = x < 0
        result = 0
        x = abs(x)
        while x > 0:
            x, remainder = divmod(x, 10)
            result = result * 10 + remainder
            if result > 2147483647:
                return 0
        if negative:
            return -result
        return result
