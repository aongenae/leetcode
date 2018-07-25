#!/usr/bin/env python3
################################################################################
#
#   Filename:           single_number.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #43, #137
#
#   Problem description:
#   https://leetcode.com/problems/single-number/description/
#   https://leetcode.com/problems/single-number-ii/description/
#
################################################################################


class Solution(object):
    # same solution for both problem 43 and 137
    # I use the 'duplicate' variable to define the number of duplicate
    # Problem  43: 2 duplicates
    # Problem 137: 3 duplicates

    def singleNumber(self, nums, duplicate):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]

        sorted_nums = sorted(nums)
        current = 0
        while current < length-duplicate:
            if sorted_nums[current] != sorted_nums[current+1]:
                return sorted_nums[current]
            else:
                current += duplicate
        return sorted_nums[-1]
