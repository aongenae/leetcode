#!/usr/bin/env python3
################################################################################
#
#   Filename:           missing_ranges.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #163
#
#   Problem description:
#   https://leetcode.com/problems/missing-ranges/description/
#
################################################################################


class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        '''
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        '''
        missing_ranges = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(len(nums)-1):
            if not nums[i+1] <= nums[i]+1:
                if nums[i+1] == nums[i]+2:
                    missing_ranges.append(str(nums[i]+1))
                else:
                    missing_ranges.append(
                        '{}->{}'.format(nums[i]+1, nums[i+1]-1)
                    )
        return missing_ranges
