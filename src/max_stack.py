#!/usr/bin/env python3
################################################################################
#
#   Filename:           max_stack.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #716
#
#   Problem description:
#   https://leetcode.com/problems/max-stack/description/
#
################################################################################
import heapq


class MaxStack(object):

    def __init__(self):
        '''
        initialize your data structure here.
        '''
        self._stack = []
        self._heap = []
        self._del_in_stack_not_in_heap = set()
        self._del_in_heap_not_in_stack = set()
        self._id = 0

    def push(self, x):
        '''
        :type x: int
        :rtype: void
        '''
        self._stack.append((self._id, x))
        heapq.heappush(self._heap, (-x, -self._id))
        self._id += 1

    def pop(self):
        '''
        :rtype: int
        '''
        x = self.top()
        self._del_in_stack_not_in_heap.add(self._stack[-1][0])
        self._stack.pop()
        return x

    def top(self):
        '''
        :rtype: int
        '''
        while self._stack[-1][0] in self._del_in_heap_not_in_stack:
            self._del_in_heap_not_in_stack.remove(self._stack[-1][0])
            self._stack.pop()
        return self._stack[-1][1]

    def peekMax(self):
        '''
        :rtype: int
        '''
        while -self._heap[0][1] in self._del_in_stack_not_in_heap:
            self._del_in_stack_not_in_heap.remove(-self._heap[0][1])
            heapq.heappop(self._heap)
        return -self._heap[0][0]

    def popMax(self):
        '''
        :rtype: int
        '''
        x = self.peekMax()
        _, nid = heapq.heappop(self._heap)
        self._del_in_heap_not_in_stack.add(-nid)
        return x
