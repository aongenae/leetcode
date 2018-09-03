#!/usr/bin/env python3
################################################################################
#
#   Filename:           product_of_array_except_self.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #238
#
#   Problem description:
#   https://leetcode.com/problems/product-of-array-except-self/description/
#
################################################################################


class Solution(object):

    def productExceptSelf(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        product = 1
        length = len(nums)
        result = []

        for index in range(0, length):
            result.append(product)
            product *= nums[index]

        product = 1

        for reverse_index in range(length, -1, -1):
            result[reverse_index] *= product
            product *= nums[reverse_index]

        return result
