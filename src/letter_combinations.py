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
        if len(digits) == 0:
            return []
        result_set = ['']
        for digit in digits:
            result_set = Solution._combinations(
                result_set,
                Solution.mapping[digit]
            )
        return list(result_set)

    @staticmethod
    def _combinations(iterator, l):
        # using iterator, this is error prone but faster
        # there is a tradeoff readibility vs efficiency
        return (e1+e2 for e1 in iterator for e2 in l)
