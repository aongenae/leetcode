#!/usr/bin/env python3
################################################################################
#
#   Filename:           permutations.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #46
#
#   Problem description:
#   https://leetcode.com/problems/permutations/description/
#
################################################################################


class Solution(object):

    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        if len(nums) == 1:
            return [nums]

        return [
            [nums[index]] + permutation
            for index in range(0, len(nums))
            for permutation in self.permute(nums[:index] + nums[index + 1:])
        ]
