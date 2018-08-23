#!/usr/bin/env python3
################################################################################
#
#   Filename:           paint_house.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #256
#
#   Problem description:
#   https://leetcode.com/problems/paint-house/description/
#
################################################################################


class Solution(object):

    def minCost(self, costs):
        '''
        :type words: List[List[int]]
        :rtype: int
        '''
        if len(costs) == 0:
            return 0

        if len(costs) == 1:
            return min(costs[0])

        min_red = costs[0][0]
        min_blue = costs[0][1]
        min_green = costs[0][2]

        for index in range(1, len(costs)):
            temp_red = min(min_blue, min_green) + costs[index][0]
            temp_blue = min(min_red, min_green) + costs[index][1]
            temp_green = min(min_red, min_blue) + costs[index][2]
            min_red = temp_red
            min_blue = temp_blue
            min_green = temp_green

        return min(min_red, min_blue, min_green)
