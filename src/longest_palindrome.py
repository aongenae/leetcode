#!/usr/bin/env python3
################################################################################
#
#   Filename:           add_strings.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #5
#
#   Problem description:
#   https://leetcode.com/problems/longest-palindromic-substring/description/
#
################################################################################


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_string = len(s)
        if len_string == 1:
            return s

        longest = s[0]
        len_longest = 1

        half = len_string // 2

        for idx in range(len_string):
            if idx > half and len_longest > half:
                return longest
            for runner in range(len_string - 1, idx, -1):
                if runner-idx < len_longest:
                    break
                if s[idx] == s[runner] and self._is_palindrome(s[idx:runner+1]):
                    longest = s[idx:runner+1]
                    len_longest = len(longest)

        return longest

    @staticmethod
    def _is_palindrome(candidate):
        begin = 0
        end = len(candidate) - 1

        while begin < end:
            if candidate[begin] != candidate[end]:
                return False
            begin += 1
            end -= 1

        return True
