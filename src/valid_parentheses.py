#!/usr/bin/env python3
################################################################################
#
#   Filename:           valid_parentheses.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #20
#
#   Problem description:
#   https://leetcode.com/problems/valid-parentheses/description/
#
################################################################################


class Solution(object):

    def isValid(self, s):
        '''
        :type s: str (charset is exclusively '(', ')', '{', '}', '[' and ']')
        :rtype: bool
        '''
        if s == '':
            return True

        closing_match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        closing_elements = frozenset(list(closing_match))

        stack = []

        for element in s:
            if element in closing_elements:
                if len(stack) == 0 or closing_match[element] != stack.pop():
                    return False
            else:
                stack.append(element)

        return len(stack) == 0
