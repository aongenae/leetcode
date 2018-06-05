#!/usr/bin/env python3
################################################################################
#
#   Filename:           intersection_of_two_linked_lists.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #160
#
#   Problem description:
#   https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
################################################################################


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        '''
        :type head1, head1: ListNode
        :rtype: ListNode
        '''
        if headA is None or headB is None:
            return None

        current = headA
        while current is not None:
            current.marked = True
            current = current.next

        current = headB
        while current is not None:
            if hasattr(current, 'marked'):
                return current
            current = current.next
        return None
