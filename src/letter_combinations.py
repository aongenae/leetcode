#!/usr/bin/env python3
################################################################################
#
#   Filename:          letter_combinations.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #17
#
#   Problem description:
#   https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
################################################################################


class Solution(object):

    mapping = {
        '0': [' '],
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        length_digits = len(digits)
        if length_digits == 0:
            return []
        result_set = ['']
        for digit in digits:
            if digit == '1':
                length_digits -= 1
                continue
            result_set += Solution._permutation(
                result_set,
                Solution.mapping[digit]
            )
        return [e for e in result_set if len(e) == length_digits]

    @staticmethod
    def _permutation(l1, l2):
        return [e1+e2 for e1 in l1 for e2 in l2]
