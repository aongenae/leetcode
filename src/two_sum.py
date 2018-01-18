#!/usr/bin/env python3
################################################################################
#
#   Filename:           two_sum.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #1
#
#   Problem description:
#   https://leetcode.com/problems/two-sum/description/
#
################################################################################


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer = {}
        for index, value in enumerate(nums):
            if value in buffer:
                return [buffer[value], index]
            else:
                buffer[target-value] = index
