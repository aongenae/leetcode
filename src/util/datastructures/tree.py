#!/usr/bin/env python3
################################################################################
#
#   Filename:           binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################


class Tree(object):

    def __init__(self, value=None):
        self.value = value
        self._marked = False

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
