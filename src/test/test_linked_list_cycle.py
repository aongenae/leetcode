#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_linked_list_cycle.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..linked_list_cycle import ListNode, Solution
from .leetcode_test import LeetcodeTest


class TestLinkedListCycle(LeetcodeTest):

    def test_no_node(self):
        self.assertFalse(Solution().hasCycle(None))

    def test_one_node_no_circle(self):
        self.assertFalse(Solution().hasCycle(ListNode('n1')))

    def test_one_node_circle(self):
        n1 = ListNode('n1')
        n1.next = n1
        self.assertTrue(Solution().hasCycle(n1))

    def test_three_nodes_one_simple_circle(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n1.next = n2
        n2.next = n3
        n3.next = n1
        self.assertTrue(Solution().hasCycle(n1))

    def test_three_nodes_no_circle(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n1.next = n2
        n2.next = n3
        self.assertFalse(Solution().hasCycle(n1))

    def test_five_nodes_no_circle(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n4 = ListNode('n4')
        n5 = ListNode('n5')
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        self.assertFalse(Solution().hasCycle(n1))

    def test_five_nodes_simple_circle(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n4 = ListNode('n4')
        n5 = ListNode('n5')
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n1
        self.assertTrue(Solution().hasCycle(n1))

    def test_five_nodes_mid_course_circle(self):
        n1 = ListNode('n1')
        n2 = ListNode('n2')
        n3 = ListNode('n3')
        n4 = ListNode('n4')
        n5 = ListNode('n5')
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n3
        self.assertTrue(Solution().hasCycle(n1))
