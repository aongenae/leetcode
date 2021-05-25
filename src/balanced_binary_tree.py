#!/usr/bin/env python3
################################################################################
#
#   Filename:           balanced_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #110
#
#   Problem description:
#   https://leetcode.com/problems/balanced-binary-tree/
#
################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        return self._isBalanced(root)[0]

    def _isBalanced(self, root: TreeNode) -> tuple[bool, int]:
        if not root:
            return True, 0

        is_left_balanced, left_height = self._isBalanced(root.left)
        is_right_balanced, right_height = self._isBalanced(root.right)

        is_balanced = (
            is_left_balanced and
            is_right_balanced and
            -1 <= (left_height - right_height) <= 1
        )
        height = max(left_height, right_height) + 1

        return is_balanced, height
