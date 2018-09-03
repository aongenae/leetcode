#!/usr/bin/env python3
################################################################################
#
#   Filename:           merge_intervals.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #56
#
#   Problem description:
#   https://leetcode.com/problems/merge-intervals/description/
#
################################################################################


class Interval(object):
    ''' Definition for an interval. '''

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        '''
        :type intervals: List[Interval]
        :rtype: List[Interval]
        '''
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda interval: interval.start)

        merged = [intervals[0]]
        for current in range(1, len(intervals)):
            if self._overvalps(merged[-1], intervals[current]):
                merged.append(self._merge(merged.pop(), intervals[current]))
            else:
                merged.append(intervals[current])

        return merged

    @staticmethod
    def _overvalps(interval_1, interval_2):
        return interval_1.end >= interval_2.start

    @staticmethod
    def _merge(interval_1, interval_2):
        return Interval(
            min(interval_1.start, interval_2.start),
            max(interval_1.end, interval_2.end)
        )

    @staticmethod
    def _print(intervals):
        print(
            ''.join(
                '{}-{} '.format(interval.start, interval.end)
                for interval in intervals
            )
        )
