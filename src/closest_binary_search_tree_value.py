#!/usr/bin/env python3
################################################################################
#
#   Filename:           closest_binary_search_tree_value.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #270, # 272
#
#   Problem description:
#   https://leetcode.com/problems/closest-binary-search-tree-value/description/
#   https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
################################################################################
import heapq


class Solution(object):

    def closestKValue(self, root, target, k):
        '''
        :type root: TreeNode
        :type target: float
        :rtype: int
        '''
        heap = []

        def bst(node):
            if node:
                heapq.heappush(heap, (abs(node.val - target), node.val))
                bst(node.left)
                bst(node.right)

        bst(root)
        return [value for _, value in heapq.nsmallest(k, heap)]

    def closestValue(self, root, target):
        return self.closestKValue(root, target, 1)[0]
