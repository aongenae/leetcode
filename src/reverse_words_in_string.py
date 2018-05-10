#!/usr/bin/env python3
################################################################################
#
#   Filename:           reverse_words_in_string.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #151
#
#   Problem description:
#   https://leetcode.com/problems/reverse-words-in-a-string/description/
#
################################################################################


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(
            s[first:last+1]
            for (first, last) in Solution._iter_words(s)
        )

    @staticmethod
    def _iter_words(s):
        letter = False
        space = False
        upper = len(s)-1
        first = upper
        last = upper
        for char_idx in range(upper, -1, -1):
            if s[char_idx] == ' ':
                space = True
            else:
                if not letter:
                    last = char_idx
                    space = False
                letter = True
                first = char_idx
            if letter:
                if space or char_idx == 0:
                    yield (first, last)
                    letter = False

    def reverseWords_not_mine_but_smart(self, s):
        ''' credit to Vineet Kumar'''
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
