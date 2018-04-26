#!/usr/bin/env python
################################################################################
#
#   Filename:           test_longest_common_prefix.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..longest_common_prefix import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, strs, expected):
        self.assertEqual(
            Solution().longestCommonPrefix(strs),
            expected,
            _Mixin._format_error(strs, expected)
        )

    @staticmethod
    def _format_error(strs, expected):
        return (
            'wrong result for the following input:\n'
            '    string:   {!r}\n'
            '    expected: {!r}\n'
            .format(strs, expected)
        )


class TestLongestCommonPrefix(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate([], '')

    def test_alone(self):
        self.validate(['alone'], 'alone')

    def test_first_letter__two_elements(self):
        self.validate(
            ['bdad', 'bad'],
            'b'
        )

    def test_two_first_letters__first_smaller(self):
        self.validate(
            ['ba', 'bad'],
            'ba'
        )

    def test_two_first_letters__second_larger(self):
        self.validate(
            ['bad', 'ba'],
            'ba'
        )

    def test_two_first_letters__two_elements(self):
        self.validate(
            ['bab', 'bad'],
            'ba'
        )

    def test_two_first_letters__three_elements(self):
        self.validate(
            ['bab', 'bad', 'bafg'],
            'ba'
        )

    def test_three_first_letters__same(self):
        self.validate(
            ['bab', 'bab'],
            'bab'
        )

    def test_three_first_letters__three_elements(self):
        self.validate(
            ['babg', 'babf', 'babob'],
            'bab'
        )

    def test_three_first_letters__three_elements_first_smaller(self):
        self.validate(
            ['bab', 'babh', 'babg'],
            'bab'
        )

    def test_three_first_letters__three_elements_first_larger(self):
        self.validate(
            ['babhdhdhe', 'babh', 'babg'],
            'bab'
        )
