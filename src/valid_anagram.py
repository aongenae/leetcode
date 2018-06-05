#!/usr/bin/env python3
################################################################################
#
#   Filename:           valid_anagram.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #242
#
#   Problem description:
#   https://leetcode.com/problems/valid-anagram/description/
#
################################################################################


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return all(False for e1, e2 in zip(sorted(s), sorted(t)) if e1 != e2)
