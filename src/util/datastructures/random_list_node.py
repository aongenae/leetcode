#!/usr/bin/env python3
################################################################################
#
#   Filename:           list_node.py
#
#   Author:             Leetcode
#
#   Description:        Definition for singly-linked list.
#
################################################################################
from .list_node import ListNode


class RandomListNode(ListNode):

    def __init__(self, x):
        super(RandomListNode, self).__init__(x)
        self.random = None
        self.label = x

    @property
    def label(self):
        return self.val

    @label.setter
    def label(self, x):
        self.x = x
