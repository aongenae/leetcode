#!/usr/bin/env python
################################################################################
#
#   Filename:           test_add_two_numbers.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..binary_tree import BinaryTree
import unittest


class TestBalancedBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree('root')
        self.left = BinaryTree('left')
        self.right = BinaryTree('right')
        self.tree.left = self.left
        self.tree.right = self.right

        self.left.left = BinaryTree('left-left-leaf')
        self.left.right = BinaryTree('left-right-leaf')
        self.left.parent = self.tree

        self.right.left = BinaryTree('right-left-leaf')
        self.right.right = BinaryTree('right-right-leaf')
        self.right.parent = self.tree

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
        self.assertEqual(self.tree.value, 'root')

    def test_left_tree_has_nodes(self):
        self.assertTrue(self.left.has_parent())
        self.assertTrue(self.left.has_left())
        self.assertTrue(self.left.has_right())

    def test_left_tree_value(self):
        self.assertTrue(self.left.has_value())
        self.assertEqual(self.left.value, 'left')

    def test_right_tree_has_nodes(self):
        self.assertTrue(self.right.has_parent())
        self.assertTrue(self.right.has_left())
        self.assertTrue(self.right.has_right())

    def test_right_tree_value(self):
        self.assertTrue(self.right.has_value())
        self.assertEqual(self.right.value, 'right')

    def test_left_left_leaf_has_nodes(self):
        left_left_leaf = self.left.left
        self.assertTrue(left_left_leaf.has_parent())
        self.assertFalse(left_left_leaf.has_left())
        self.assertFalse(left_left_leaf.has_right())

    def test_left_left_leaf_has_nodes(self):
        left_right_leaf = self.left.right
        self.assertTrue(left_right_leaf.has_parent())
        self.assertFalse(left_right_leaf.has_left())
        self.assertFalse(left_right_leaf.has_right())

    def test_left_left_leaf_value(self):
        left_left_leaf = self.left.left
        self.assertTrue(left_left_leaf.has_value())
        self.assertEqual(left_left_leaf.value, 'left-left-leaf')

    def test_left_right_leaf_value(self):
        left_right_leaf = self.left.right
        self.assertTrue(left_right_leaf.has_value())
        self.assertEqual(left_right_leaf.value, 'left-right-leaf')

    def test_right_left_leaf_has_nodes(self):
        right_left_leaf = self.right.left
        self.assertTrue(right_left_leaf.has_parent())
        self.assertFalse(right_left_leaf.has_left())
        self.assertFalse(right_left_leaf.has_right())

    def test_right_left_leaf_has_nodes(self):
        right_right_leaf = self.right.right
        self.assertTrue(right_right_leaf.has_parent())
        self.assertFalse(right_right_leaf.has_left())
        self.assertFalse(right_right_leaf.has_right())

    def test_right_left_leaf_value(self):
        right_left_leaf = self.right.left
        self.assertTrue(right_left_leaf.has_value())
        self.assertEqual(right_left_leaf.value, 'right-left-leaf')

    def test_right_right_leaf_value(self):
        right_right_leaf = self.right.right
        self.assertTrue(right_right_leaf.has_value())
        self.assertEqual(right_right_leaf.value, 'right-right-leaf')
