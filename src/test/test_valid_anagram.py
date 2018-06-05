#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_valid_anagram.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..valid_anagram import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate_true(self, string, candidate):
        solution = Solution().isAnagram(string, candidate)
        self.assertTrue(
            solution,
            self._format_error(string, candidate)
        )

    def validate_false(self, string, candidate):
        solution = Solution().isAnagram(string, candidate)
        self.assertFalse(
            solution,
            self._format_error(string, candidate)
        )

    @staticmethod
    def _format_error(string, candidate):
        return (
            'wrong result for the following input:\n'
            '    string:    {!r}\n'
            '    candidate: {!r}\n'
            .format(string, candidate)
        )


class TestValidAnagram(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate_true('', '')

    def test_true(self):
        self.validate_true('anagram', 'nagaram')

    def test_false(self):
        self.validate_false('rat', 'car')

    def test_different_length_first_longer(self):
        self.validate_false('ab', 'a')

    def test_different_length_second_longer(self):
        self.validate_false('a', 'ab')
