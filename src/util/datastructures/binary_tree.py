#!/usr/bin/env python
################################################################################
#
#   Filename:           binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################


class BinaryTree(object):

    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None
        self._parent = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def has_value(self):
        return self._value is not None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    def has_left(self):
        return self._left is not None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    def has_right(self):
        return self._right is not None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def has_parent(self):
        return self._parent is not None
