#!/usr/bin/env python3
################################################################################
#
#   Filename:           evaluate_reverse_polish_notation.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #150
#
#   Problem description:
#   https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
################################################################################

_operators = frozenset(('+', '-', '*', '/'))


class Solution(object):

    def evalRPN(self, tokens):
        '''
        :type tokens: List[str]
        :rtype: int
        '''
        stack = []
        for token in tokens:
            if token in _operators:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if token == '+':
                    result = operand_2 + operand_1
                elif token == '-':
                    result = operand_2 - operand_1
                elif token == '*':
                    result = operand_2 * operand_1
                else:
                    result = int(float(operand_2) / operand_1)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
