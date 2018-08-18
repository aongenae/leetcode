#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_closest_binary_search_tree_value.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..closest_binary_search_tree_value import Solution
from ..util import TreeNode
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate_closest(self, root, target, expected):
        solution = Solution().closestValue(root, target)
        self.assertEqual(
            solution,
            expected,
            'computed "{}", expected "{}"'.format(solution, expected)
        )

    def validate_k_closest(self, root, target, k, expected):
        solution = Solution().closestKValue(root, target, k)
        self.assertEqual(
            solution,
            expected,
            'computed "{}", expected "{}"'.format(solution, expected)
        )


class TestClosestBinarySearchTreeValue(LeetcodeTest, _Mixin):

    def setUp(self):
        '''
            4
           / \
          2   5
         / \
        1   3
        '''
        self.root = TreeNode(4)
        l1 = TreeNode(2)
        r1 = TreeNode(5)
        self.root.left = l1
        self.root.right = r1
        l2 = TreeNode(1)
        r2 = TreeNode(3)
        l1.left = l2
        l1.right = r2

    def test_closest(self):
        self.validate_closest(self.root, 3.714286, 4)

    def test_k_closest(self):
        self.validate_k_closest(self.root, 3.714286, 2, [4, 3])
