#!/usr/bin/env python3
################################################################################
#
#   Filename:           reverse_words_in_string_2.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #186
#
#   Problem description:
#   https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
################################################################################


class Solution(object):

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        head = 0

        # reverse all word locally
        while head < len(str):
            head_runner = head
            while head_runner < len(str) and str[head_runner] != ' ':
                head_runner += 1
            self._reverse(str, head, head_runner-1)
            head = head_runner + 1

        # reverse the whole list (each word already reversed)
        self._reverse(str, 0, len(str)-1)

    @staticmethod
    def _reverse(str, start, end):
        while start < end:
            tmp = str[start]
            str[start] = str[end]
            str[end] = tmp
            start += 1
            end -= 1
