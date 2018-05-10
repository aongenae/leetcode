#!/usr/bin/env python3
################################################################################
#
#   Filename:           longest_common_prefix.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #14
#
#   Problem description:
#   https://leetcode.com/problems/longest-common-prefix/description/
#
################################################################################


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        idx_longest_prefix = self._idx_longest_char(strs)
        return strs[0][:idx_longest_prefix]

    @staticmethod
    def _idx_longest_char(strs):
        idx = 0
        for char in strs[0]:
            for string in strs[1:]:
                if idx == len(string):
                    return idx
                if char != string[idx]:
                    return idx
            idx += 1
        return idx + 1
