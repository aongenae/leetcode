#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_zigzag_conversion.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..util import StringBinaryTree
from ..zigzag_conversion import Solution
import unittest


class _Mixin(object):

    def validate(self, string, num_rows, expected):
        self.assertEqual(
            Solution().convert(string, num_rows),
            expected,
            '\n -> considering the input "{}", nb rows "{}"'.format(
                string,
                num_rows
            )
        )


class TestZigzagConvert(unittest.TestCase, _Mixin):

    def _not_enabled_test_example(self):
        self.validate('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')


class TestZigzagConvertUtil(unittest.TestCase):

    def setUp(self):
        '''
        Build the tree
                  P
                 / \
                /   \
               /     \
              /       \
             A         A
            / \       / \
           Y   P     L   \
                    / \   \
                   I   S   H
                          / \
                         /   \
                        /     \
                       I      N
                      / \    /
                     R   I  G
        '''
        self.original_string = 'PAYPALISHIRING'
        self.num_rows = 3
        self.max_edge = self.num_rows - 1

        self.tree = StringBinaryTree('P')

        tl = StringBinaryTree('A', self.tree)
        self.tree.left = tl

        tll = StringBinaryTree('Y', tl)
        tl.left = tll

        tlr = StringBinaryTree('P', tl)
        tl.right = tlr

        tr = StringBinaryTree('A', self.tree)
        self.tree.right = tr

        trl = StringBinaryTree('L', tr)
        tr.left = trl

        trll = StringBinaryTree('I', trl)
        trl.left = trll

        trlr = StringBinaryTree('S', trl)
        trl.right = trlr

        trr = StringBinaryTree('H', tr)
        tr.right = trr

        trrl = StringBinaryTree('I', trr)
        trr.left = trrl

        trrll = StringBinaryTree('R', trrl)
        trrl.left = trrll

        trrlr = StringBinaryTree('I', trrl)
        trrl.right = trrlr

        trrr = StringBinaryTree('N', trr)
        trr.right = trrr

        trrrl = StringBinaryTree('G', trrr)
        trrr.left = trrrl

    def test(self):
        manual = StringBinaryTree.format_values(self.tree)

        solution = Solution()
        solution._store(None, 'PAYPALISHIRING', 0)
        automated = StringBinaryTree.format_values(solution.root)
        self.assertEqual(
            automated,
            manual,
            'expected automated "{}" == "{}"'.format(automated, manual)
        )
