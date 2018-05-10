#!/usr/bin/env python3
################################################################################
#
#   Filename:           binary_tree_level_order_traversal.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #102
#
#   Problem description:
#   https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
################################################################################


class TreeNode(object):
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node(object):
    """
    basic node to create a LinkedList
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Queue(object):
    """
    my own queue because I cannot import Python queue
    should use Queue if available
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def put(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get(self):
        node = self.head
        if self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            self.head = node.next
        return node


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result

        queue = Queue()
        root.marked = True
        queue.put(root)
        result.append([root.val])

        while not queue.empty():
            current = queue.get()
            binomial = []
            if current.left is not None:
                if not hasattr(current.left, 'marked'):
                    current.left.marked = True
                    queue.put(current.left)
                    binomial.append(current.left.val)
            if current.right is not None:
                if not hasattr(current.right, 'marked'):
                    current.right.marked = True
                    queue.put(current.right)
                    binomial.append(current.right.val)
            if binomial:
                result.append(binomial)
        return result
