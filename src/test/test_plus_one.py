#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_plus_one.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..plus_one import Solution
from .leetcode_test import LeetcodeTest


class TestPlusOne(LeetcodeTest):

    def test_zero(self):
        self.assertListEqual(
            Solution().plusOne([0]),
            [1]
        )

    def test_one(self):
        self.assertListEqual(
            Solution().plusOne([2]),
            [3]
        )

    def test_one_becomes_two(self):
        self.assertListEqual(
            Solution().plusOne([9]),
            [1, 0]
        )

    def test_two_stays_two(self):
        self.assertListEqual(
            Solution().plusOne([1, 9]),
            [2, 0]
        )

    def test_two_becomes_three(self):
        self.assertListEqual(
            Solution().plusOne([9, 9]),
            [1, 0, 0]
        )

    def test_three_stays_three(self):
        self.assertListEqual(
            Solution().plusOne([8, 9]),
            [9, 0]
        )

    def test_three_becomes_four(self):
        self.assertListEqual(
            Solution().plusOne([9, 9, 9]),
            [1, 0, 0, 0]
        )
