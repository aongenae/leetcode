#!/usr/bin/env python3
################################################################################
#
#   Filename:           three_sum.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #15
#
#   Problem description:
#   https://leetcode.com/problems/3sum/description/
#
################################################################################


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        nums.sort()
        result = set()
        visited = set()
        length_nums = len(nums)
        for current in range(length_nums-1):
            current_value = nums[current]
            tmp_lookup = {}
            target = -current_value
            if current_value not in visited:
                for runner in range(current+1, length_nums):
                    runner_value = nums[runner]
                    if runner_value not in tmp_lookup:
                        tmp_lookup[target - runner_value] = runner
                    else:
                        result.add(
                            (current_value, target-runner_value, runner_value)
                        )
                    visited.add(current_value)
        return list(result)
