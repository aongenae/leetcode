#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_letter_combinations.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..letter_combinations import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, digits, expected):
        solution = Solution().letterCombinations(digits)
        self.assertEqual(
            solution,
            expected,
            'considering the digits: "{}"'.format(digits)
        )


class TestLetterCombinations(LeetcodeTest, _Mixin):

    def test_one_digit(self):
        self.validate(
            digits='5',
            expected=['j', 'k', 'l']
        )

    def test_two_digits(self):
        self.validate(
            digits='23',
            expected=['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        )

    def test_two_digits_duplicate(self):
        self.validate(
            digits='22',
            expected=['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
        )

    def test_two_digits_with_digit_one(self):
        self.validate(
            digits='31',
            expected=['d', 'e', 'f']
        )

    def test_two_digits_with_zero(self):
        self.validate(
            digits='20',
            expected=['a ', 'b ', 'c ']
        )

    def test_empty(self):
        self.validate(
            digits='',
            expected=[]
        )
