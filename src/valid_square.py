#!/usr/bin/env python3
################################################################################
#
#   Filename:           valid_square.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #593
#
#   Problem description:
#   https://leetcode.com/problems/valid_square/description/
#
################################################################################


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        '''
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        '''
        if p1 == p2 == p3 == p4:
            return False

        distances = [
            self._dist(p1, p2),
            self._dist(p1, p3),
            self._dist(p1, p4),
            self._dist(p2, p3),
            self._dist(p2, p4),
            self._dist(p3, p4)
        ]

        distances.sort()
        return (
            (distances[0] == distances[1] == distances[2] == distances[3]) and
            (distances[4] == distances[5])
        )

    @staticmethod
    def _dist(x, y):
        return (x[0] - y[0])**2 + (x[1] - y[1])**2
