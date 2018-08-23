#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_find_leaves_of_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..find_leaves_of_binary_tree import Solution
from ..util import TreeNode
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate_find_leaves(self, root, expected):
        solution = Solution().findLeaves(root)
        self.assertEqual(
            solution,
            expected,
            'computed "{}", expected "{}"'.format(solution, expected)
        )


class TestFindLeavesOfBinaryTree(LeetcodeTest, _Mixin):

    def setUp(self):
        '''
            1
           / \
          2   3
         / \
        4   5
        '''
        self.root = TreeNode(1)
        l1 = TreeNode(2)
        r1 = TreeNode(3)
        self.root.left = l1
        self.root.right = r1
        l2 = TreeNode(4)
        r2 = TreeNode(5)
        l1.left = l2
        l1.right = r2

    def test_find_leaves(self):
        self.validate_find_leaves(self.root, [[4, 5, 3], [2], [1]])
