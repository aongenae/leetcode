#!/usr/bin/env python
################################################################################
#
#   Filename:           test_reverse_words_in_string.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..reverse_words_in_string import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, expected):
        solution = Solution().reverseWords(string)
        self.assertEqual(
            solution,
            expected,
            '\n considering the string "{}"\n'
            'computed "{}"\n'
            'expected "{}"'.format(
                string,
                solution,
                expected
            )
        )


class TestReverseWordsInString(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate(
            '',
            ''
        )

    def test_one_space(self):
        self.validate(
            ' ',
            ''
        )

    def test_one_letter(self):
        self.validate(
            'a',
            'a'
        )

    def test_non_empty_no_extra_spaces(self):
        self.validate(
            'the sky is blue',
            'blue is sky the'
        )

    def test_non_empty_leading_spaces(self):
        self.validate(
            '    the sky is blue',
            'blue is sky the'
        )

    def test_non_empty_trailing_spaces(self):
        self.validate(
            'the sky is blue   ',
            'blue is sky the'
        )

    def test_non_empty_leading_trailing_spaces(self):
        self.validate(
            '   the sky is blue   ',
            'blue is sky the'
        )

    def test_multiple_in_between_spaces(self):
        self.validate(
            'the sky   is   blue',
            'blue is sky the'
        )
