#!/usr/bin/env python3
################################################################################
#
#   Filename:           group_anagrams.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #49
#
#   Problem description:
#   https://leetcode.com/problems/group-anagrams/description/
#
################################################################################


class Solution(object):

    def groupAnagrams(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[str]
        '''

        if len(strs) == 0:
            return []

        lookup = defaultdict(list)
        for word in strs:
            lookup[''.join(sorted(word))].append(word)

        return list(lookup.values())
