#!/usr/bin/env python3
################################################################################
#
#   Filename:           find_leaves_of_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #366
#
#   Problem description:
#   https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
################################################################################


class Solution(object):

    def findLeaves(self, root):
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        all_leafs = []

        while root:
            current_leafs = []
            root = self._helper(root, current_leafs)
            all_leafs.append(current_leafs)

        return all_leafs

    def _helper(self, root, current_leafs):
        if not root:
            return

        if not root.right and not root.left:
            current_leafs.append(root.val)
            return None

        root.left = self._helper(root.left, current_leafs)
        root.right = self._helper(root.right, current_leafs)

        return root
