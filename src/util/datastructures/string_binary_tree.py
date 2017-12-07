#!/usr/bin/env python3
################################################################################
#
#   Filename:           string_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from .binary_tree import BinaryTree


def reverse_string_binary_tree(tree):
    ''' Creates a new tree '''
    reversed_tree = StringBinaryTree()
    if tree is None:
        return None
    reversed_tree.value = tree.value
    left = reverse_string_binary_tree(tree.right)
    right = reverse_string_binary_tree(tree.left)
    if left is not None:
        reversed_tree.left = left
    if right is not None:
        reversed_tree.right = right
    return reversed_tree


class StringBinaryTree(BinaryTree):
    ''' BinaryTree where values are String or None '''

    def __init__(self, value=None, parent=None):
        super(StringBinaryTree, self).__init__(value, parent)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        StringBinaryTree._assert_is_string_or_none(value)
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        StringBinaryTree._assert_is_string_binary_tree(node)
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        StringBinaryTree._assert_is_string_binary_tree(node)
        self._right = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        StringBinaryTree._assert_is_string_binary_tree_or_none(node)
        self._parent = node

    @staticmethod
    def format_values(binary_tree_iterator, separator=' '):
        return separator.join(BinaryTree.iter_values(binary_tree_iterator))

    @staticmethod
    def _assert_is_string(node):
        assert isinstance(node, str), (
            'The value must be a string, got "{}"'.format(node)
        )

    @staticmethod
    def _assert_is_string_or_none(node):
        if node is not None:
            StringBinaryTree._assert_is_string(node)

    @staticmethod
    def _assert_is_string_binary_tree(node):
        assert isinstance(node, StringBinaryTree), (
            'The node must be a StringBinaryTree, got "{}"'.format(node)
        )

    @staticmethod
    def _assert_is_string_binary_tree_or_none(node):
        if node is not None:
            StringBinaryTree._assert_is_string_binary_tree(node)
