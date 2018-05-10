#!/usr/bin/env python3
################################################################################
#
#   Filename:           palindrome_number.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #9
#
#   Problem description:
#   https://leetcode.com/problems/palindrome-number/description/
#
################################################################################
import math


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        exponent = int(math.log10(x))
        # exponent = len(str(x)) - 1  # on leetcode, we cannot import math
        for idx, last_digit in enumerate(self._iter_last_digits(x)):
            first_digit, x = divmod(x, pow(10, exponent-idx))
            if last_digit != first_digit:
                return False
        return True

    @staticmethod
    def _iter_last_digits(x):
        first_digits, last_digit = divmod(x, 10)
        yield last_digit
        while first_digits > 10:
            first_digits, last_digit = divmod(first_digits, 10)
            yield last_digit
