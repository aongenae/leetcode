#!/usr/bin/env python3
################################################################################
#
#   Filename:           binary_tree_vertical_order_traversal.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #314
#
#   Problem description:
#   https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
################################################################################
from collections import defaultdict


class Solution(object):

    def verticalOrder(self, root):
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        if not root:
            return []

        columns = defaultdict(list)
        parents = [(root, 0)]
        while parents:
            children = []
            for parent, col in parents:
                columns[col].append(parent.val)
                if parent.left:
                    children.append((parent.left, col-1))
                if parent.right:
                    children.append((parent.right, col+1))
            parents = children

        return [columns[key] for key in sorted(columns)]
