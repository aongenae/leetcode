#!/usr/bin/env python3
################################################################################
#
#   Filename:           reverse_linked_list.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #206
#
#   Problem description:
#   https://leetcode.com/problems/reverse-linked-list/description/
#
################################################################################


class Solution(object):

    def reverseList(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        if head is None or head.next is None:
            return head

        stack = []
        current = head
        while current is not None:
            stack.append(current)
            current = current.next

        new_head = stack.pop()
        current = new_head
        while len(stack) != 0:
            element = stack.pop()
            current.next = element
            current = current.next
        current.next = None

        return new_head
