#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_palindrome_linked_list.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..palindrome_linked_list import Solution
from .leetcode_test import LeetcodeTest
from ..util import ListNode


class TestPalindromeLinkedList(LeetcodeTest):

    def _test_1(self):
        n1 = ListNode('1')
        n2 = ListNode('2')
        n1.next = n2
        self.assertFalse(Solution().isPalindrome(n1))

    def test_2(self):
        n1 = ListNode('1')
        n2 = ListNode('2')
        n3 = ListNode('2')
        n4 = ListNode('1')
        n1.next = n2
        n2.next = n3
        n3.next = n4
        self.assertTrue(Solution().isPalindrome(n1))
