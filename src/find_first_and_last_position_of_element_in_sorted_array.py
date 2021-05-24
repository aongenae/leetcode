#!/usr/bin/env python3
################################################################################
#
#   Filename:           find_first_and_last_position_of_element_in_sorted_array.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #34
#
#   Problem description:
#   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#
################################################################################


class Solution(object):

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self._find_bounds(nums, target, True)
        if (start == -1):
            return [-1, -1]
        end = self._find_bounds(nums, target, False)
        return [start, end]

    def _find_bounds(self, nums: List[int], target: int, search_left: bool) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if search_left:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid -1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
