#!/usr/bin/env python
################################################################################
#
#   Filename:           test_binary_tree_level_order_traversal.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..binary_tree_level_order_traversal import Solution, TreeNode, Queue, Node
from .leetcode_test import LeetcodeTest
from collections import deque


class _Mixin(object):

    def validate(self, tree_as_list, expected):
        solution = Solution().levelOrder(
            self.build_tree_node_from_list(tree_as_list)
        )
        self.assertListEqual(
            solution,
            expected,
            _Mixin._format_error(solution, expected)
        )

    @staticmethod
    def _format_error(solution, expected):
        return (
            'wrong result for the following input:\n'
            '    solution: {!r}\n'
            '    expected: {!r}\n'
            .format(solution, expected)
        )

    @staticmethod
    def build_tree_node_from_list(binary_tree_node_list):
        if len(binary_tree_node_list) == 0:
            return None

        root = TreeNode(binary_tree_node_list[0])

        if len(binary_tree_node_list) == 1:
            return root

        queue = deque()
        queue.appendleft(root)

        idx = 1
        while len(queue) != 0 and idx < len(binary_tree_node_list):
            current = queue.pop()
            if binary_tree_node_list[idx] is not None:
                new_node = TreeNode(binary_tree_node_list[idx])
            else:
                new_node = None

            if (idx-1) % 2 == 0:
                current.left = new_node
                queue.append(current)
                queue.appendleft(new_node)
            else:
                current.right = new_node
                queue.appendleft(new_node)
            idx += 1

        return root


class TestBuildBinaryTreeFromList(LeetcodeTest):

    def test_len_0(self):
        tree_as_list = []
        tree = _Mixin.build_tree_node_from_list(tree_as_list)
        self.assertIsNone(tree)

    def test_len_1(self):
        tree_as_list = [1]
        tree = _Mixin.build_tree_node_from_list(tree_as_list)
        self.assertEqual(tree.val, 1)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_len_2(self):
        tree_as_list = [1, 2]
        tree = _Mixin.build_tree_node_from_list(tree_as_list)
        self.assertEqual(tree.val, 1)
        self.assertEqual(tree.left.val, 2)
        self.assertIsNone(tree.right)
        self.assertIsNone(tree.left.left)
        self.assertIsNone(tree.left.right)

    def test_len_7(self):
        tree_as_list = [3, 9, 20, None, None, 15, 7]
        tree = _Mixin.build_tree_node_from_list(tree_as_list)
        self.assertEqual(tree.val, 3)
        self.assertEqual(tree.left.val, 9)
        self.assertEqual(tree.right.val, 20)
        self.assertIsNone(tree.left.left)
        self.assertIsNone(tree.left.right)
        self.assertEqual(tree.right.left.val, 15)
        self.assertEqual(tree.right.right.val, 7)


class TestBinaryTreeLevelOrderTraversal(LeetcodeTest, _Mixin):

    def test_empty(self):
        self.validate(
            [],
            []
        )

    def test_missing_left_left(self):
        self.validate(
            [3, 9, 20, None, None, 15, 7],
            [[3], [9, 20], [15, 7]]
        )

    def test_balanced(self):
        self.validate(
            [3, 9, 20, 5, 10, 15, 7],
            [[3], [9, 20], [5, 10], [15, 7]]
        )

    # def test_missing_in_middle(self):
    #     self.validate(
    #         [1, 2, 3, 4, None, None, 5]
    #         [[1], [2, 3], [4, 5]]
    #     )


class TestQueue(LeetcodeTest):

    def setUp(self):
        self.queue = Queue()

    def test_empty(self):
        self.assertTrue(self.queue.empty())

    def test_one_element(self):
        node = Node(1)
        self.queue.put(node)
        self.assertFalse(self.queue.empty())
        retrieved_node = self.queue.get()
        self.assertIs(node, retrieved_node)

    def test_two_elements(self):
        node_1 = Node(1)
        node_2 = Node(2)
        self.queue.put(node_1)
        self.queue.put(node_2)
        self.assertFalse(self.queue.empty())

        retrieved_node_1 = self.queue.get()
        self.assertIs(node_1, retrieved_node_1)

        retrieved_node_2 = self.queue.get()
        self.assertIs(node_2, retrieved_node_2)

        self.assertTrue(self.queue.empty())
