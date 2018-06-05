#!/usr/bin/env python3
################################################################################
#
#   Filename:           palindrome_linked_list.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #234
#
#   Problem description:
#   https://leetcode.com/problems/palindrome-linked-list/description/
#
################################################################################


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        previous = None
        while current is not None:
            current.previous = previous
            previous = current
            current = current.next

        forward = head
        backward = previous
        while forward is not None and backward is not None:
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.previous

        return not (
            (forward is None and backward is not None) and
            (forward is not None and backward is None)
        )
