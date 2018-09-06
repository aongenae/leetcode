#!/usr/bin/env python3
################################################################################
#
#   Filename:           serialize_and_deserialize_binary_tree.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #297
#
#   Problem description:
#   https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
################################################################################
from .util import TreeNode


class Codec(object):

    def serialize(self, root):
        '''Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        '''
        if not root:
            return None
        return (
            root.val,
            self.serialize(root.left),
            self.serialize(root.right)
        )

    def deserialize(self, data):
        '''Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        '''
        if not data:
            return None

        root_value, left, right = data
        root = TreeNode(root_value)

        if left is not None:
            root.left = self.deserialize(left)
        if right is not None:
            root.right = self.deserialize(right)

        return root
