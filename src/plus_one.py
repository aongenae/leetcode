#!/usr/bin/env python3
################################################################################
#
#   Filename:           plus_one.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #66
#
#   Problem description:
#   https://leetcode.com/problems/plus-one/description/
#
################################################################################


class Solution(object):

    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        last = digits[-1]
        idx = len(digits) - 1
        digits[idx] += 1
        while idx >= 0 and digits[idx] > 9:
            digits[idx] = 10 - digits[idx]
            if idx > 0:
                digits[idx-1] += 1
            else:
                return [1] + digits
            idx -= 1
        return digits
