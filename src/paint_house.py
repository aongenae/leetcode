#!/usr/bin/env python3
################################################################################
#
#   Filename:           paint_house.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #256, #265
#
#   Problem description:
#   https://leetcode.com/problems/paint-house/description/
#   https://leetcode.com/problems/paint-house-ii/description/
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

    def minCostII(self, costs):
        '''
        :type words: List[List[int]]
        :rtype: int
        '''

        if len(costs) == 0:
            return 0

        idx = -1
        min1 = min2 = 0

        for i in range(len(costs)):
            newMin1 = float("inf")
            newMin2 = float("inf")

            for j in range(len(costs[i])):
                if j != idx:
                    costs[i][j] += min1
                else:
                    costs[i][j] += min2

                if costs[i][j] < newMin1:
                    newMin2 = newMin1
                    newMin1 = costs[i][j]
                    newIdx = j
                elif costs[i][j] < newMin2:
                    newMin2 = costs[i][j]

            min1 = newMin1
            min2 = newMin2
            idx = newIdx

        return min(costs[-1][j] for j in range(len(costs[-1])))
