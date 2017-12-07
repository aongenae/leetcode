#!/usr/bin/env python
################################################################################
#
#   Filename:           test_length_of_longest_substring.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..length_of_longest_substring import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, expected):
        self.assertEqual(
            Solution().lengthOfLongestSubstring(string),
            expected,
            '\n considering the string "{}"'.format(string)
        )


class TestLengthOfLongestSubstring(LeetcodeTest, _Mixin):

    def test_beginning(self):
        self.validate('abcabcbb', 3)

    def test_unique(self):
        self.validate('bbbbb', 1)

    def test_middle(self):
        self.validate('pwwkew', 3)

    def test_end(self):
        self.validate('abbdef', 4)

    def test_end_2(self):
        self.validate('dvdf', 3)

    def test_begin_2(self):
        self.validate('aab', 2)

    def _not_enabled_test_unique_2(self):
        self.validate('ckilbkd', 5)


#        d 1
#        v 2
#        d 2
#        f 3
