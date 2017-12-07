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

    def setUp(self):
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
        self.tree = StringBinaryTree('t')
        self.left = StringBinaryTree('l')
        self.right = StringBinaryTree('r', parent=self.tree)
        self.tree.left = self.left
        self.tree.right = self.right

        self.left.left = StringBinaryTree('tll')
        self.left.right = StringBinaryTree('tlr')
        self.left.parent = self.tree

        self.right.left = StringBinaryTree('trl')
        self.right.right = StringBinaryTree('trr')

        self.left.left.parent = self.left
        self.left.right.parent = self.left

        self.right.left.parent = self.right
        self.right.right.parent = self.right

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
