#!/usr/bin/env python3
################################################################################
#
#   Filename:           zigzag-conversion.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #415
#
#   Problem description:
#   https://leetcode.com/problems/zigzag-conversion/description/
#
################################################################################
from .util import StringBinaryTree


class Solution(object):

    def __init__(self):
        self.root = None
        self.max_left_edge = 2

    def convert(self, s, numRows):
        '''
        :type s: str
        :type numRows: int
        :rtype: str
        '''
        self.max_left_edge = numRows - 1
        self.root = StringBinaryTree()
        print('building ')
        self._store(None, s, 0)

#        return 'PAHNAPLSIIGYIR'
        print(' ')
#        return ''
        return Solution._read_binary_tree(self.root, '')

    def _store(self, parent, string, nb_left_edge=0):
        if len(string) == 0:
            return

        current_node = StringBinaryTree(string[0])

        if parent is None:
            self.root = current_node
            return self._store(current_node, string[1:], 0)

        if nb_left_edge < self.max_left_edge:
            parent.left = current_node
            current_node.parent = parent
            return self._store(current_node, string[1:], nb_left_edge + 1)

        if nb_left_edge == self.max_left_edge:
            parent.parent.right = current_node
            current_node.parent = parent.parent
            return self._store(current_node, string[1:], nb_left_edge + 1)

        for i in range(0, self.max_left_edge):
            parent = parent.parent
        parent.right = current_node
        current_node.parent = parent
        return self._store(current_node, string[1:], 0)



#    def _store_string_in_binary_tree_old(self, string, max_left_edge):
#        nb_left_edge = 0
#        current_node = self.root
#        for character in string:
#            print('----------------considered character "{}"'.format(character))
#            current_node = StringBinaryTree(character)
#            if self.root is None:
#                self.root = current_node
#            if nb_left_edge < max_left_edge:
#                current_node.left = StringBinaryTree()
#                current_node.left.parent = current_node
#                current_node = current_node.left
#                nb_left_edge += 1
#            elif nb_left_edge == max_left_edge:
#                current_node.parent.right = StringBinaryTree()
#                current_node.parent.right.parent = current_node.parent
#                current_node = current_node.parent.right
#                nb_left_edge += 1
#            else:
#                for i in range(1, max_left_edge):
#                    current_node = current_node.parent
##                    print('i {} climb "{}"'.format(i, current_node.value))
#                current_node.right = StringBinaryTree()
#                current_node.right.parent = current_node
#                current_node = current_node.right
#                nb_left_edge = 0
##            print('print grand parent')
##            if current_node.parent.has_parent():
##                print(current_node.parent.parent)
##            print('print parent')
##            print(current_node.parent)
#            print('print current')
#            print(current_node)

    @staticmethod
    def _read_binary_tree(node, new_string):
        print(node)
        if node.has_value():
            new_string += node.value
            print(new_string)
            node.value = None
            if node.has_right():
                return Solution._read_binary_tree(node.right, new_string)
        if node.has_parent():
            return Solution._read_binary_tree(node.parent, new_string)
        if node.has_left() and node.left.has_value():
            return Solution._read_binary_tree(node.left, new_string)
        return new_string
