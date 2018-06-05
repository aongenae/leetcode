#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_reverse_linked_list.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..reverse_linked_list import Solution
from ..util import ListNode
from .leetcode_test import LeetcodeTest


class TestReverseLinkedList(LeetcodeTest):

    def test_no_node(self):
        self.assertIsNone(Solution().reverseList(None))

    def test_three_elements(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n1.next = n2
        n2.next = n3

        e3 = ListNode('n1')
        e2 = ListNode('n2')
        e1 = ListNode('n3')
        e1.next = e2
        e2.next = e3

        current_s = Solution().reverseList(n1)
        current_e = e1
        while current_s is not None:
            self.assertEqual(current_s.val, current_e.val)
            current_s = current_s.next
            current_e = current_e.next
