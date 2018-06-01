#!/usr/bin/env python3
################################################################################
#
#   Filename:           add_two_numbers.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #2
#
#   Problem description:
#   https://leetcode.com/problems/add-two-numbers/description/
#
################################################################################
from .util import ListNode


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        carry_over, rest = divmod(l1.val + l2.val, 10)
        first_node = ListNode(rest)
        Solution._build_solution(l1.next, l2.next, carry_over, first_node)
        return first_node

    @staticmethod
    def _build_solution(l1, l2, carry_over, solution):
        if l1 is None and l2 is None:
            if carry_over != 0:
                node = ListNode(carry_over)
                solution.next = node
            return

        if l1 is None:
            l1_val = 0
            l1_next = None
        else:
            l1_val = l1.val
            l1_next = l1.next

        if l2 is None:
            l2_val = 0
            l2_next = None
        else:
            l2_val = l2.val
            l2_next = l2.next

        sum = l1_val + l2_val + carry_over
        carry_over, rest = divmod(sum, 10)
        node = ListNode(rest)
        solution.next = node
        Solution._build_solution(l1_next, l2_next, carry_over, node)
