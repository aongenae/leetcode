#!/usr/bin/env python3
################################################################################
#
#   Filename:           min_stack.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #155
#
#   Problem description:
#   https://leetcode.com/problems/min-stack/description/
#
################################################################################


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._stack:
            _, current_min = self._stack[-1]
            local_min = min(x, current_min)
        else:
            local_min = x
        self._stack.append((x, local_min))

    def pop(self):
        """
        :rtype: void
        """
        assert len(self._stack) > 0
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        assert len(self._stack) > 0
        top, _ = self._stack[-1]
        return top

    def getMin(self):
        """
        :rtype: int
        """
        assert len(self._stack) > 0
        _, current_min = self._stack[-1]
        return current_min
