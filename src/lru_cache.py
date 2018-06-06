#!/usr/bin/env python3
################################################################################
#
#   Filename:           lru_cache.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #146
#
#   Problem description:
#   https://leetcode.com/problems/lru-cache/description/
#
################################################################################


class DoubleListNode(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._nb_elements = 0
        self._lookup = {}
        self._head = None
        self._tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._lookup:
            return -1
        touched_node = self._lookup[key]
        self._move_to_tail(touched_node)
        return touched_node.value

    def _move_to_tail(self, node):
        if node is not self._tail:
            self._remove_from_list(node)
            self._position_at_tail(node)

    def _remove_from_list(self, node):
        ''' remove from list to move, not delete for ever, the node stays in
            the lookup
        '''
        if node is self._head and node is self._tail:
            self._head = None
            self._tail = None
        else:
            if node is self._head:
                self._head = node.next
            elif node is self._tail:
                self._tail = node.previous
            else:
                node.previous.next = node.next
                node.next.previous = node.previous

    def _position_at_tail(self, node):
        ''' this is a move, that node is already removed from the list
            the lookup is not impacted nor is the number of node in the list
        '''
        self._tail.next = node
        node.previous = self._tail
        node.next = None
        self._tail = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._lookup:
            self._lookup[key].value = value
            touched_node = self._lookup[key]
            self._move_to_tail(touched_node)
        else:
            new_node = DoubleListNode(key, value)
            if self._tail is None:
                self._tail = new_node
                self._head = new_node
                self._nb_elements += 1
                self._lookup[key] = new_node
            else:
                self._position_at_tail(new_node)
                self._lookup[key] = new_node
                if self._nb_elements == self._capacity:
                    node_to_remove = self._head
                    self._remove_from_list(node_to_remove)
                    del(self._lookup[node_to_remove.key])
                else:
                    self._nb_elements += 1
