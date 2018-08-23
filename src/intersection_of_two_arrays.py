#!/usr/bin/env python3
################################################################################
#
#   Filename:           intersection_of_two_arrays.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #349
#
#   Problem description:
#   https://leetcode.com/problems/intersection-of-two-arrays/description/
#
################################################################################


class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
