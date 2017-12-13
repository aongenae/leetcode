#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..string_binary_tree import StringBinaryTree, reverse_string_binary_tree
import unittest


class TestSymmetricStringBinaryTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        build the following tree:

               t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        cls.tree = StringBinaryTree('t')
        cls.left = StringBinaryTree('l')
        cls.right = StringBinaryTree('r', parent=cls.tree)
        cls.tree.left = cls.left
        cls.tree.right = cls.right

        cls.left.left = StringBinaryTree('tll')
        cls.left.right = StringBinaryTree('tlr')
        cls.left.parent = cls.tree

        cls.right.left = StringBinaryTree('trl')
        cls.right.right = StringBinaryTree('trr')

        cls.left.left.parent = cls.left
        cls.left.right.parent = cls.left

        cls.right.left.parent = cls.right
        cls.right.right.parent = cls.right

    def test_iter_left_self_right(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_left_self_right()),
            'tll l tlr t trl r trr'
        )

    def test_iter_right_self_left(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_right_self_left()),
            'trr r trl t tlr l tll'
        )

    def test_iter_self_left_right(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_self_left_right()),
            't l tll tlr r trl trr'
        )

    def test_iter_self_right_left(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_self_right_left()),
            't r trr trl l tlr tll'
        )

    def test_iter_left_right_self(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_left_right_self()),
            'tll tlr l trl trr r t'
        )

    def test_iter_right_left_self(self):
        '''    t
              / \
             /   \
            l     r
           /\     /\
          /  \   /  \
        tll tlr trl trr
        '''
        self.assertEqual(
            StringBinaryTree.format_values(self.tree.iter_right_left_self()),
            'trr trl r tlr tll l t'
        )

    def test_reverse_string_binary_tree(self):
        '''
        normal:               reversed:
               t                    t
              / \                  / \
             /   \                /   \
            l     r              r     l
           /\     /\            /\     /\
          /  \   /  \          /  \   /  \
        tll tlr trl trr      trr trl tlr tll
        '''
        # reversed
        self.assertEqual(
            StringBinaryTree.format_values(
                reverse_string_binary_tree(self.tree)
            ),
            't r trr trl l tlr tll'
        )
        # normal (ensures that the reverse_binary_tree creates a copy)
        self.assertEqual(
            StringBinaryTree.format_values(self.tree),
            't l tll tlr r trl trr'
        )
