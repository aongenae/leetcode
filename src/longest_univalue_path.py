#!/usr/bin/env python3
################################################################################
#
#   Filename:           longest_univalue_path.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #687
#
#   Problem description:
#   https://leetcode.com/problems/longest-univalue-path/description/
#
################################################################################


class Solution(object):

    def longestUnivaluePath(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        self.longest_path = 0
        self._longest_univalue_path(root)
        return self.longest_path

    def _longest_univalue_path(self, node):
        if not node:
            return 0

        # Get the length on left and right
        left_length = self._longest_univalue_path(node.left)
        right_length = self._longest_univalue_path(node.right)

        # Add ourself if we have the same value as left node
        left_side = 0
        if node.left and node.left.val == node.val:
            left_side = left_length + 1

        # Add ourself if we have the same value as right node
        right_side = 0
        if node.right and node.right.val == node.val:
            right_side = right_length + 1

        # evaluate if we find something bigger than already seen
        self.longest_path = max(self.longest_path, left_side+right_side)

        # continue with the longest so far
        return max(left_side, right_side)
