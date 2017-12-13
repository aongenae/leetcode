#!/usr/bin/env python3
################################################################################
#
#   Filename:           tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################


class Tree(object):

    def __init__(self, value=None):
        self.value = value
        self._marked = False
        self._children = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def has_value(self):
        return self._value is not None

    @property
    def marked(self):
        return self._marked

    @marked.setter
    def marked(self, boolean):
        self._marked = boolean

    def iter_children(self):
        return (child for child in self._children)

    @staticmethod
    def iter_values(binary_tree_iterator):
        return (node.value for node in binary_tree_iterator)
