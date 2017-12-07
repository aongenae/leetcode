#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..binary_tree import BinaryTree, reverse_binary_tree
import unittest


class TestSymmetricBinaryTree(unittest.TestCase):

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
        self.tree = BinaryTree('t')
        self.left = BinaryTree('l')
        self.right = BinaryTree('r', parent=self.tree)
        self.tree.left = self.left
        self.tree.right = self.right

        self.left.left = BinaryTree('tll')
        self.left.right = BinaryTree('tlr')
        self.left.parent = self.tree

        self.right.left = BinaryTree('trl')
        self.right.right = BinaryTree('trr')

        self.left.left.parent = self.left
        self.left.right.parent = self.left

        self.right.left.parent = self.right
        self.right.right.parent = self.right

    def test_tree_has_nodes(self):
        self.assertFalse(self.tree.has_parent())
        self.assertTrue(self.tree.has_left())
        self.assertTrue(self.tree.has_right())

    def test_tree_value(self):
        self.assertTrue(self.tree.has_value())
        self.assertEqual(self.tree.value, 't')

    def test_left_tree_has_nodes(self):
        self.assertTrue(self.left.has_parent())
        self.assertTrue(self.left.has_left())
        self.assertTrue(self.left.has_right())

    def test_left_tree_value(self):
        self.assertTrue(self.left.has_value())
        self.assertEqual(self.left.value, 'l')

    def test_right_tree_has_nodes(self):
        self.assertTrue(self.right.has_parent())
        self.assertTrue(self.right.has_left())
        self.assertTrue(self.right.has_right())

    def test_right_tree_value(self):
        self.assertTrue(self.right.has_value())
        self.assertEqual(self.right.value, 'r')

    def test_left_left_leaf_has_nodes(self):
        left_left_leaf = self.left.left
        self.assertTrue(left_left_leaf.has_parent())
        self.assertFalse(left_left_leaf.has_left())
        self.assertFalse(left_left_leaf.has_right())

    def test_left_right_leaf_has_nodes(self):
        left_right_leaf = self.left.right
        self.assertTrue(left_right_leaf.has_parent())
        self.assertFalse(left_right_leaf.has_left())
        self.assertFalse(left_right_leaf.has_right())

    def test_left_left_leaf_value(self):
        left_left_leaf = self.left.left
        self.assertTrue(left_left_leaf.has_value())
        self.assertEqual(left_left_leaf.value, 'tll')

    def test_left_right_leaf_value(self):
        left_right_leaf = self.left.right
        self.assertTrue(left_right_leaf.has_value())
        self.assertEqual(left_right_leaf.value, 'tlr')

    def test_right_left_leaf_has_nodes(self):
        right_left_leaf = self.right.left
        self.assertTrue(right_left_leaf.has_parent())
        self.assertFalse(right_left_leaf.has_left())
        self.assertFalse(right_left_leaf.has_right())

    def test_right_right_leaf_has_nodes(self):
        right_right_leaf = self.right.right
        self.assertTrue(right_right_leaf.has_parent())
        self.assertFalse(right_right_leaf.has_left())
        self.assertFalse(right_right_leaf.has_right())

    def test_right_left_leaf_value(self):
        right_left_leaf = self.right.left
        self.assertTrue(right_left_leaf.has_value())
        self.assertEqual(right_left_leaf.value, 'trl')

    def test_right_right_leaf_value(self):
        right_right_leaf = self.right.right
        self.assertTrue(right_right_leaf.has_value())
        self.assertEqual(right_right_leaf.value, 'trr')

    def test_symmetric(self):
        self.assertTrue(self.tree.is_symmetric())

    def test_iter(self):
        ''' Confirm __iter__ function is the same as iter_self_left_right '''
        [
            self.assertEqual(n1, n2)
            for n1, n2 in zip(self.tree, self.tree.iter_self_left_right())
        ]

    def test_reverse_binary_tree(self):
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
            self._format_values(reverse_binary_tree(self.tree)),
            't r trr trl l tlr tll'
        )
        # normal (ensures that the reverse_binary_tree creates a copy)
        self.assertEqual(
            self._format_values(self.tree),
            't l tll tlr r trl trr'
        )

    def _format_values(self, binary_tree_iterator, separator=' '):
        return separator.join(self._iter_values(binary_tree_iterator))

    def _iter_values(self, binary_tree_iterator):
        return (node.value for node in binary_tree_iterator)
