#!/usr/bin/env python
################################################################################
#
#   Filename:           test_palindrome_number.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..palindrome_number import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, expected):
        self.assertEqual(
            Solution().lengthOfLongestSubstring(string),
            expected,
            '\n considering the string "{}"'.format(string)
        )


class TestLengthOfLongestSubstring(LeetcodeTest, _Mixin):

    def test_negative(self):
        self.assertFalse(Solution().isPalindrome(-121))

    def test_one_digit(self):
        self.assertTrue(Solution().isPalindrome(1))

    def test_two_different_digits(self):
        self.assertFalse(Solution().isPalindrome(10))

    def test_three_digits_true(self):
        self.assertTrue(Solution().isPalindrome(121))

    def test_three_digits_false(self):
        self.assertFalse(Solution().isPalindrome(122))

    def test_four_digits_true(self):
        self.assertTrue(Solution().isPalindrome(1221))

    def test_four_digits_false_tail(self):
        self.assertFalse(Solution().isPalindrome(1222))

    def test_four_digits_false_front(self):
        self.assertFalse(Solution().isPalindrome(2221))

    def test_five_true(self):
        self.assertTrue(Solution().isPalindrome(12321))

    def test_five_false__fist_digit(self):
        self.assertFalse(Solution().isPalindrome(12522))

    def test_five_false__second_digit(self):
        self.assertFalse(Solution().isPalindrome(21222))

    def test_five_false__fourth_digit(self):
        self.assertFalse(Solution().isPalindrome(22212))

    def test_five_false__last_digit(self):
        self.assertFalse(Solution().isPalindrome(22323))
