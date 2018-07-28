#!/usr/bin/env python3
################################################################################
#
#   Filename:           exclusive_time_of_functions.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #636
#
#   Problem description:
#   https://leetcode.com/problems/exclusive-time-of-functions/description/
#
################################################################################
from collections import defaultdict


class Solution(object):

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        time = defaultdict(int)
        stack = []
        for entry in logs:
            pid, start_end, timestamp_str = entry.split(':')
            start = start_end == 'start'
            timestamp = int(timestamp_str)
            if start:
                stack.append([pid, timestamp, 0])
            else:
                start_pid, start_timestamp, non_exclusive = stack.pop()
                time[pid] += timestamp - start_timestamp + 1 - non_exclusive
                if stack:
                    stack[-1][-1] += timestamp - start_timestamp + 1
        return [time[str(i)] for i in range(0, n)]
