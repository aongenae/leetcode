#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_add_two_numbers.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..add_strings import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string_1, string_2, expected):
        self.assertEqual(
            Solution().addStrings(string_1, string_2),
            expected,
            _Mixin._format_error(string_1, string_2)
        )

    @staticmethod
    def _format_error(string_1, string_2):
        return (
            'wrong result for the following input:\n'
            '    string_1: {!r}\n'
            '    string_2: {!r}\n'
            .format(string_1, string_2)
        )


class TestAddStrings(LeetcodeTest, _Mixin):

    def test_small_numbers_sum_less_than_ten(self):
        self.validate('4', '5', expected='9')

    def test_small_numbers_sum_more_than_ten(self):
        self.validate('6', '5', expected='11')

    def test_two_digits(self):
        self.validate('11', '22', expected='33')

    def test_num1_longer_than_num2(self):
        self.validate('11', '2', expected='13')

    def test_num2_longer_than_num1(self):
        self.validate('101', '3003', expected='3104')

    def test_large_number(self):
        self.validate(
            '544984101010101023430583548588439443994394394394394949490',
            '300330030003000300300303030030303003030030039093829839301',
            expected='845314131013101323730886578618742447024424433488224788791'
        )
