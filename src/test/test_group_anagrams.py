#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_group_anagrams.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..group_anagrams import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, strs, expected):
        solution = Solution().groupAnagrams(strs)
        self._sort_lists(solution),
        self._sort_lists(expected),
        self.assertListEqual(
            solution,
            expected,
            '\n \nConsidering the string list {}\n'
            '    computed {}\n'
            '    expected {}'.format(
                strs,
                solution,
                expected
            )
        )

    @staticmethod
    def _sort_lists(a_list_of_lists):
        for element in a_list_of_lists:
            element.sort()
        a_list_of_lists.sort()


class TestGroupAnagrams(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate([], [])

    def test_3_different_anagrams(self):
        self.validate(
            ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            [
                ['ate', 'eat', 'tea'],
                ['nat', 'tan'],
                ['bat']
            ]
        )
