#!/usr/bin/env python3
################################################################################
#
#   Filename:           copy_list_with_random_pointer.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #138
#
#   Problem description:
#   https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
################################################################################
from .util import RandomListNode


class Solution(object):

    def copyRandomList(self, head):
        '''
        :type head: RandomListNode
        :rtype: RandomListNode
        '''
        if head is None:
            return None

        memo = {}

        current = head
        while current is not None:
            memo[current] = RandomListNode(current.label)
            current = current.next

        current = head
        while current is not None:
            if current.next is not None:
                memo[current].next = memo[current.next]
            if current.random is not None:
                memo[current].random = memo[current.random]
            current = current.next

        return memo[head]
