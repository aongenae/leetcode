#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_longest_univalue_path.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..longest_univalue_path import Solution
from ..util import TreeNode
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, root, expected):
        solution = Solution().longestUnivaluePath(root)
        self.assertEqual(
            solution,
            expected,
            'computed "{}", expected "{}"'.format(solution, expected)
        )


class TestLongestUnivaluePath(LeetcodeTest, _Mixin):

    def test_right_from_root(self):
        '''
            5
           / \
          4   5
         / \   \
        1   1   5
        '''
        root = TreeNode(5)
        l1 = TreeNode(4)
        r1 = TreeNode(5)
        root.left = l1
        root.right = r1
        ll2 = TreeNode(1)
        lr2 = TreeNode(1)
        l1.left = ll2
        l1.right = lr2
        rr1 = TreeNode(5)
        r1.right = rr1
        self.validate(root, 2)

    def test_left_not_straight(self):
        '''
            1
           / \
          4   5
         / \   \
        4   4   5
        '''
        root = TreeNode(1)
        l1 = TreeNode(4)
        r1 = TreeNode(5)
        root.left = l1
        root.right = r1
        ll2 = TreeNode(4)
        lr2 = TreeNode(4)
        l1.left = ll2
        l1.right = lr2
        rr1 = TreeNode(5)
        r1.right = rr1
        self.validate(root, 2)
