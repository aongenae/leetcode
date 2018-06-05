#!/usr/bin/env python3
################################################################################
#
#   Filename:           trapping_rain_water.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #42
#
#   Problem description:
#   https://leetcode.com/problems/trapping-rain-water/description/
#
################################################################################


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)

        if len_height <= 2:
            return 0

        left = []
        right = []
        tmp = []
        for i in range(len_height):
            left.append(0)
            right.append(0)
            tmp.append(0)

        for i in range(1, len_height-1):
            left[i] = max(left[i-1], height[i-1])

        for i in range(len_height-2, 0, -1):
            right[i] = max(right[i+1], height[i+1])

        for i in range(1, len_height-1):
            tmp[i] = min(left[i], right[i])
            if height[i] < tmp[i]:
                tmp[i] -= height[i]
            else:
                tmp[i] = 0

        return sum(tmp)

    def trap_(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        trapped = 0
        for left_summit, right_summit in self._find_summits(height):
            trapped += self._process_valley(height, left_summit, right_summit)

        return trapped

    def _find_summits(self, heights):
        found_left_summit = None
        current = 0
        runner = current + 1
        while runner < len(heights):
            if found_left_summit:
                valley = self._find_valley(heights[runner:])
                valley += runner
                if valley == len(heights) - 1:
                    break
                runner = self._find_mountain(heights[valley:])
                runner += valley
                yield (current, runner)
                found_left_summit = False
                current = runner
                runner = current + 1
            else:
                left_mountain = self._find_mountain(heights[current:])
                left_mountain += current
                if left_mountain == len(heights) - 1:
                    break
                current = left_mountain
                found_left_summit = True

    def _find_mountain(self, heights):
        current = 0
        for value in heights[1:]:
            if value <= heights[current]:
                return current
            else:
                current += 1
        return len(heights) - 1

    def _find_valley(self, heights):
        current = 0
        for value in heights[1:]:
            if value >= heights[current]:
                return current
            else:
                current += 1
        return len(heights) - 1

    def _process_valley(self, heights, lower, upper):
        lowest_montain = min(heights[lower], heights[upper])
        trapped = 0
        for element in heights[lower+1:upper]:
            if lowest_montain - element > 0:
                trapped += lowest_montain - element
        return trapped
