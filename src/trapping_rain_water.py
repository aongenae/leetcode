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
        print()
        len_height = len(height)
        if len(height) < 3:
            return 0

        current = self._find_montain(height)
        if current >= len_height-1:
            return 0
        runner = current

        trapped = 0
        while runner < len_height:
            print('current {}'.format(current))
            valley = self._find_valley(height[current:])
            print('valley {}'.format(valley))
            runner = self._find_montain(height[valley+1:])
            print('runner {}"'.format(runner))
            if valley == len(height)-1:
                return trapped
            runner += valley + 1
            print('adjusted runner {}"'.format(runner))
            trapped += self._process_valley(height, current, runner)
            print('====== trapped {}'.format(trapped))
            current = runner

        return trapped

    def _find_montain(self, heights):
        print()
        print('    _find_montain {}'.format(heights))
        current = 0
        for value in heights[1:]:
            if value <= heights[current]:
                return current
            else:
                current += 1
        return len(heights) - 1

    def _find_valley(self, heights):
        print()
        print('    _find_valley {}'.format(heights))
        current = 0
        for value in heights[1:]:
            if value >= heights[current]:
                return current
            else:
                current += 1
        return len(heights) - 1

    def _find_montain_(self, heights, base=0):
        print('_find_montain {} base {}'.format(heights, base))
        current = 0
        for value in heights[1:]:
            if value >= base and value <= heights[current]:
                return current
            else:
                current += 1
        if heights[-1] > base:
            return len(heights)
        return 0


    def _process_valley(self, heights, lower, upper):
        print('-> heights {}'.format(heights))
        print('   lower {} upper {}'.format(lower, upper))
        print('         {}       {}'.format(heights[lower], heights[upper]))
        lowest_montain = min(heights[lower], heights[upper])
        print('   lowest_montain {}'.format(lowest_montain))
        trapped = 0
        for element in heights[lower+1:upper]:
            print('element {} newlytrapped {}'.format(
                element, lowest_montain - element))
            trapped += lowest_montain - element
        return trapped
