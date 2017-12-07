#!/usr/bin/env python3
################################################################################
#
#   Filename:           binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################

def reverse_binary_tree(tree):
    ''' Creates a new tree '''
    reversed_tree = BinaryTree()
    if tree is None:
        return None
    reversed_tree.value = tree.value
    left = reverse_binary_tree(tree.right)
    right = reverse_binary_tree(tree.left)
    if left is not None:
        reversed_tree.left = left
    if right is not None:
        reversed_tree.right = right
    return reversed_tree


class BinaryTree(object):

    def __init__(self, value=None, parent=None):
        self.value = value
        self._left = None
        self._right = None
        self.parent = parent

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
        BinaryTree._assert_is_binary_tree(node)
        self._left = node

    def has_left(self):
        return self._left is not None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        BinaryTree._assert_is_binary_tree(node)
        self._right = node

    def has_right(self):
        return self._right is not None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        BinaryTree._assert_is_binary_tree_or_none(node)
        self._parent = node

    def has_parent(self):
        return self._parent is not None

    def is_symmetric(self):
        return BinaryTree._is_symmetric_helper(self._left, self._right)

    @staticmethod
    def iter_values(binary_tree_iterator):
        return (node.value for node in binary_tree_iterator)

    def iter_left_self_right(self):
        if self._left:
            yield from self._left.iter_left_self_right()
        yield self
        if self._right:
            yield from self._right.iter_left_self_right()

    def iter_right_self_left(self):
        if self._right:
            yield from self._right.iter_right_self_left()
        yield self
        if self._left:
            yield from self._left.iter_right_self_left()

    def iter_self_left_right(self):
        yield self
        if self._left:
            yield from self._left.iter_self_left_right()
        if self._right:
            yield from self._right.iter_self_left_right()

    def iter_self_right_left(self):
        yield self
        if self._right:
            yield from self._right.iter_self_right_left()
        if self._left:
            yield from self._left.iter_self_right_left()

    def iter_left_right_self(self):
        if self._left:
            yield from self._left.iter_left_right_self()
        if self._right:
            yield from self._right.iter_left_right_self()
        yield self

    def iter_right_left_self(self):
        if self._right:
            yield from self._right.iter_right_left_self()
        if self._left:
            yield from self._left.iter_right_left_self()
        yield self

    def __iter__(self):
        return self.iter_self_left_right()

    def __str__(self):
        return (
            'value:     "{}"\n'
            'has parent: {}\n'
            'has left:   {}\n'
            'has right:  {}'
            .format(
                self._value,
                self.has_parent(),
                self.has_left(),
                self.has_right()
            )
        )

    @staticmethod
    def _is_symmetric_helper(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (
            BinaryTree._is_symmetric_helper(left.left, left.right) and
            BinaryTree._is_symmetric_helper(right.left, right.right)
        )

    @staticmethod
    def _assert_is_binary_tree(node):
        assert isinstance(node, BinaryTree), (
            'The node must be a BinaryTree, got "{}"'.format(node)
        )

    @staticmethod
    def _assert_is_binary_tree_or_none(node):
        if node is not None:
            BinaryTree._assert_is_binary_tree(node)
