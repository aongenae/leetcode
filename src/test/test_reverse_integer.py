#!/usr/bin/env python
################################################################################
#
#   Filename:           test_reverse_integer.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..reverse_integer import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, x, expected):
        computed_solution = Solution().reverse(x)
        self.assertEqual(
            computed_solution,
            expected,
            'Expected "{}" to be "{}"'.format(computed_solution, expected)
        )


class TestReverseInteger(LeetcodeTest, _Mixin):

    def test_positive(self):
        self.validate(123, expected=321)

    def test_negative(self):
        self.validate(-123, expected=-321)

    def test_tailing_zero(self):
        self.validate(120, expected=21)

    def test_overflow(self):
        self.validate(1534236469, expected=0)
