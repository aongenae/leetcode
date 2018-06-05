#!/usr/bin/env python3
################################################################################
#
#   Filename:           kth_largest_element_in_an_array.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #215
#
#   Problem description:
#   https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
################################################################################
import heapq


class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List(int)
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return heapq.nlargest(k, nums)[-1]
