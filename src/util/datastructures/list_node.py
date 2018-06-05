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


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def build_reversed_from_integer(cls, integer):

        def helper(integer, rest, previous_node):
            integer, rest = divmod(integer, 10)
            if rest == 0:
                return
            node = ListNode(rest)
            previous_node.next = node
            helper(integer, rest, node)

        integer, rest = divmod(integer, 10)
        first_node = ListNode(rest)
        helper(integer, rest, first_node)
        return first_node

    @classmethod
    def print_list_node(cls, list_node):
        print(list_node.val)
        if list_node.next is None:
            return
        ListNode.print_list_node(list_node.next)

    @classmethod
    def build_from_list(cls, l):
        if len(l) == 0:
            return ListNode(None)
        if len(l) == 1:
            return ListNode(l[0])
        head = ListNode(l[0])
        current = head
        for element in l[1:]:
            new_node = ListNode(element)
            current.next = new_node
            current = new_node
        return head


class SingleLinkedList(object):

    def __init__(self, head):
        self.head = head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        tmp = self.current
        self.current = self.current.next
        return tmp
