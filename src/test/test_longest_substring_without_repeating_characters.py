#!/usr/bin/env python
################################################################################
#
#   Filename:           test_longest_substring_without_repeating_characters.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..longest_substring_without_repeating_characters import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, expected):
        self.assertEqual(
            Solution().lengthOfLongestSubstring(string),
            expected,
            '\n considering the string "{}"'.format(string)
        )


class TestLengthOfLongestSubstring(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate('', 0)

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

    def test_unique_2(self):
        self.validate('ckilbkd', 5)
