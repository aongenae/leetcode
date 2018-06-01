#!/usr/bin/env python3
################################################################################
#
#   Filename:           linked_list_cycle.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #141
#
#   Problem description:
#   https://leetcode.com/problems/linked-list-cycle/description/
#
################################################################################


class Solution(object):

    def hasCycle(self, head):
        '''
        :type head: ListNode
        :rtype: bool
        '''
        if head is None or head.next is None:
            return False

        if head.next is head:
            return True

        current = head
        runner = current.next

        count = 0
        while runner.next is not None and runner.next is not current:
            runner = runner.next

            # current moves also, but twice a slow
            if count % 2:
                current = current.next
            count += 1

        return runner.next is current
