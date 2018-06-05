#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_merge_two_sorted_lists.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..merge_two_sorted_lists import Solution
from ..util import ListNode, SingleLinkedList
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, l1, l2, expected_list):
        solution = SingleLinkedList(
            Solution().mergeTwoLists(
                ListNode.build_from_list(l1),
                ListNode.build_from_list(l2)
            )
        )
        expected = SingleLinkedList(ListNode.build_from_list(expected_list))
        for n1, n2 in zip(solution, expected):
            self.assertEqual(n1.val, n2.val)


class TestMergeTwoSortedLists(_Mixin, LeetcodeTest):

    def test(self):
        self.validate([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_single_l1_bigger(self):
        self.validate([2], [1], [1, 2])

    def test_l1_bigger(self):
        self.validate([5], [1, 2, 4], [1, 2, 4, 5])

    def test_with_negatives(self):
        self.validate(
            [-10, -9, -6, -4, 1, 9, 9],
            [-5, -3, 0, 7, 8, 8],
            [-10, -9, -6, -5, -4, -3, 0, 1, 7, 8, 8, 9, 9]
        )
