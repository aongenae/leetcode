#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_reverse_words_in_string_2.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..reverse_words_in_string_2 import Solution
from .leetcode_test import LeetcodeTest
import copy


class _Mixin(object):

    def validate(self, str_list, expected):
        original = copy.deepcopy(str_list)
        Solution().reverseWords(str_list)
        self.assertListEqual(
            str_list,
            expected,
            '\n considering the string list "{}"\n'
            'computed "{}"\n'
            'expected "{}"'.format(
                original,
                str_list,
                expected
            )
        )


class TestReverseWordsInString(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate([], [])

    def test_one_space(self):
        self.validate([' '], [' '])

    def test_one_letter(self):
        self.validate(['a'], ['a'])

    def test_non_empty_no_extra_spaces(self):
        self.validate(
            [
                't', 'h', 'e', ' ',
                's', 'k', 'y', ' ',
                'i', 's', ' ',
                'b', 'l', 'u', 'e'
            ],
            [
                'b', 'l', 'u', 'e', ' ',
                'i', 's', ' ',
                's', 'k', 'y', ' ',
                't', 'h', 'e'
            ]
        )


class TestReverse(LeetcodeTest, _Mixin):

    def setUp(self):
        self.str_list = [
            't', 'h', 'e', ' ',
            's', 'k', 'y', ' ',
            'i', 's', ' ',
            'b', 'l', 'u', 'e'
        ]

    def test_substring_begining_list(self):
        Solution._reverse(self.str_list, 0, 2)
        self.assertListEqual(
            self.str_list,
            [
                'e', 'h', 't', ' ',
                's', 'k', 'y', ' ',
                'i', 's', ' ',
                'b', 'l', 'u', 'e'
            ]
        )

    def test_substring_end_list(self):
        Solution._reverse(self.str_list, 11, 14)
        self.assertListEqual(
            self.str_list,
            [
                't', 'h', 'e', ' ',
                's', 'k', 'y', ' ',
                'i', 's', ' ',
                'e', 'u', 'l', 'b'
            ]
        )
