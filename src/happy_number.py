#!/usr/bin/env python3
################################################################################
#
#   Filename:           happy_number.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #202
#
#   Problem description:
#   https://leetcode.com/problems/happy_number/description/
#
################################################################################


class Solution(object):

    def isHappy(self, n):
        '''
        :type n: int
        :rtype: bool
        '''
        already_seen = set()

        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in already_seen:
                return False
            else:
                already_seen.add(n)
        return True
