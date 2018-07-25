#!/usr/bin/env python3
################################################################################
#
#   Filename:           single_number.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #43
#
#   Problem description:
#   https://leetcode.com/problems/single-number/description/
#
################################################################################


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]

        sorted_nums = sorted(nums)
        current = 0
        while current < length-2:
            if sorted_nums[current] != sorted_nums[current+1]:
                return sorted_nums[current]
            else:
                current += 2
        return sorted_nums[-1]
