#!/usr/bin/env python3
################################################################################
#
#   Filename:           rotate_image.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #48
#
#   Problem description:
#   https://leetcode.com/problems/rotate-image/description/
#
################################################################################


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        if size <= 1:
            return matrix

        for row in range(0, size//2):
            first = row
            last = size - 1 - row
            for col in range(first, last):
                offset = col - first
                tmp = matrix[first][col]
                matrix[first][col] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[col][last]
                matrix[col][last] = tmp
        return matrix
