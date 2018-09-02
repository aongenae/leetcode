#!/usr/bin/env python3
################################################################################
#
#   Filename:           maximum_subarray.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #53
#
#   Problem description:
#   https://leetcode.com/problems/maximum-subarray/description/
#
################################################################################


class Solution(object):

    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        # assumption, zero is the minimum sum
        current_sum = nums[0]
        max_sum = nums[0]

        for current in range(0, len(nums)):
            current_val = nums[current]
            current_sum += current_val
            if current_sum > max_sum:
                max_sum = current_sum
            elif current_sum < 0:
                current_sum = 0
        return max_sum
