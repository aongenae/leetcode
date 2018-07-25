#!/usr/bin/env python3
################################################################################
#
#   Filename:           single_number_iii.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #260
#
#   Problem description:
#   https://leetcode.com/problems/single-number-iii/description/
#
################################################################################


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 2:
            return nums

        result = []
        sorted_nums = sorted(nums)
        current = 0
        while current < length-1:
            if sorted_nums[current] != sorted_nums[current+1]:
                result.append(sorted_nums[current])
                if len(result) == 2:
                    return result
                else:
                    current += 1
            else:
                current += 2
        result.append(sorted_nums[-1])
        return result
