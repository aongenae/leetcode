#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_string_to_integer_atoi.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..string_to_integer_atoi import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, expected):
        self.assertEqual(
            Solution().myAtoi(string),
            expected,
            'input string "{}"'.format(string)
        )


class TestStringToInteger(LeetcodeTest, _Mixin):

    def test_zero(self):
        self.validate('0', 0)

    def test_empty(self):
        self.validate('', 0)

    def test_positive(self):
        self.validate('10', 10)

    def test_positive_leading_spaces(self):
        self.validate('   10101', 10101)

    def test_positive_trailing_spaces(self):
        self.validate('33  ', 33)

    def test_positive_leading_letters(self):
        self.validate(' l   10', 0)

    def test_positive_trailing_letters(self):
        self.validate('10456l', 10456)

    def test_positive_trailing_letters_with_leading_spaces(self):
        self.validate('   22r', 22)

    def test_explicit_positive_sign(self):
        self.validate('+10', 10)

    def test_explicit_positive_sign_leading_spaces(self):
        self.validate('   +10101', 10101)

    def test_explicit_positive_sign_trailing_spaces(self):
        self.validate('+33  ', 33)

    def test_explicit_positive_sign_leading_letters(self):
        self.validate(' l   +10', 0)

    def test_explicit_positive_sign_trailing_letters(self):
        self.validate('+10456l', 10456)

    def test_explicit_positive_sign_trailing_letters_with_leading_spaces(self):
        self.validate('   +22r', 22)

    def test_negative(self):
        self.validate('-99', -99)

    def test_negative_leading_spaces(self):
        self.validate('   -20202', -20202)

    def test_negative_trailing_spaces(self):
        self.validate('-33  ', -33)

    def test_negative_leading_letters(self):
        self.validate(' l   -10', 0)

    def test_negative_trailing_letters(self):
        self.validate('-10457l', -10457)

    def test_negative_trailing_letters_with_leading_spaces(self):
        self.validate('   -44556677r', -44556677)

    def test_positive_overflow(self):
        self.validate('91283472332', 2147483647)

    def test_negative_overflow(self):
        self.validate('-91283472332', -2147483648)
