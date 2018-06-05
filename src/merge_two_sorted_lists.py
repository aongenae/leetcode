#!/usr/bin/env python3
################################################################################
#
#   Filename:           merge_two_sorted_lists.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #21
#
#   Problem description:
#   https://leetcode.com/problems/merge-two-sorted-lists/description/
#
################################################################################


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            previous_node = l1
            node_a = l1.next
            node_b = l2
            head = l1
        else:
            previous_node = l2
            node_a = l2.next
            node_b = l1
            head = l2
        while node_b is not None:

            if node_a is None:
                previous_node.next = node_b
                return head
            if node_b.val < node_a.val:
                tmp = node_b.next
                previous_node.next = node_b
                node_b.next = node_a
                previous_node = node_b
                node_b = tmp
            else:
                previous_node = node_a
                node_a = node_a.next
        return head
