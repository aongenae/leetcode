#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_intersection_of_two_linked_lists.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..intersection_of_two_linked_lists import Solution
from ..util import ListNode
from .leetcode_test import LeetcodeTest


class TestIntersectionOfTwoLinkedLists(LeetcodeTest):

    def test_none(self):
        a1 = ListNode('a1')
        a2 = ListNode('a2')
        a1.next = a2
        self.assertIsNone(Solution().getIntersectionNode(a1, None))

    def test_intersection(self):
        a1 = ListNode('a1')
        a2 = ListNode('a2')
        b1 = ListNode('b1')
        b2 = ListNode('b2')
        b3 = ListNode('b3')
        c1 = ListNode('c1')
        c2 = ListNode('c2')
        c3 = ListNode('c3')
        a1.next = a2
        a2.next = c1
        b1.next = b2
        b2.next = b3
        b3.next = c1
        c1.next = c2
        c2.next = c3

        self.assertIs(Solution().getIntersectionNode(a1, b1), c1)

    def test_no_intersection(self):
        a1 = ListNode('a1')
        a2 = ListNode('a2')
        b1 = ListNode('b1')
        b2 = ListNode('b2')
        b3 = ListNode('b3')
        a1.next = a2
        b1.next = b2
        b2.next = b3

        self.assertIsNone(Solution().getIntersectionNode(a1, b1))
