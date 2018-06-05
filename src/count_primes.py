#!/usr/bin/env python3
################################################################################
#
#   Filename:           count_primes.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #204
#
#   Problem description:
#   https://leetcode.com/problems/count-primes/description/
#
################################################################################


class Solution(object):

    def countPrimes_slow(self, n):
        # Too slow, need mathematical help on this naive approach
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = set([2])
        for integer in range(3, n):
            if any(p for p in primes if float(integer // p) == integer / p):
                primes.add(integer)

        return len(primes)

    def countPrimes(self, n):
        # Solution from QuanhuaXu
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)
        return sum(s)
