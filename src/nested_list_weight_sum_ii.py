#!/usr/bin/env python3
################################################################################
#
#   Filename:           nested_list_weight_sum_ii.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #364
#
#   Problem description:
#   https://leetcode.com/problems/nested-list-weight-sum-ii/description/
#
################################################################################

#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):

    def depthSum(self, nestedList):
        '''
        :type nestedList: List[NestedInteger]
        :rtype: int
        '''
		depth = 0
        result = 0
        level = {}

        while nestedList:
            level[depth] = [
                element.getInteger()
                for element in nestedList
                if element.isInteger()
            ]
            nestedList = sum(
                [
                    element.getList()
                    for element in nestedList
                    if not element.isInteger()
                ],
                []
            )
            depth += 1

        return sum(
            (depth - level_depth) * sum(values)
            for level_depth, values in level.items()
        )
