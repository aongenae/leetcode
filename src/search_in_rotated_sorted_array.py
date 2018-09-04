#!/usr/bin/env python3
################################################################################
#
#   Filename:           search_in_rotated_sorted_array.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #33
#
#   Problem description:
#   https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
################################################################################


class Solution(object):

    def search(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        return self._search(nums, target, 0)

    @classmethod
    def _search(cls, nums, target, index):
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return index

        start = nums[0]
        middle_index = len(nums)//2
        middle = nums[middle_index]
        if middle == target:
            return middle_index + index
        end = nums[-1]

        if target >= start:
            if target <= middle:
                return cls._search(nums[:middle_index], target, index)

        if target > middle:
            if target <= end:
                return cls._search(
                    nums[middle_index:],
                    target,
                    index+middle_index
                )

        if middle > end:
            return cls._search(nums[middle_index:], target, index+middle_index)

        if middle < start:
            return cls._search(nums[:middle_index], target, index)

        return -1
