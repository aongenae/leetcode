#!/usr/bin/env python3
################################################################################
#
#   Filename:           jewels_and_stones.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #771
#
#   Problem description:
#   https://leetcode.com/problems/jewels-and-stones/description
#
################################################################################


class Solution:

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if len(J) == 0 or len(S) == 0:
            return 0
        jewels = set(J)
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
        return count
