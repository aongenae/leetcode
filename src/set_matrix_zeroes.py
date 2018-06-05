#!/usr/bin/env python3
################################################################################
#
#   Filename:           set_matrix_zeroes.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #73
#
#   Problem description:
#   https://leetcode.com/problems/set-matrix-zeroes/description/
#
################################################################################


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        nb_rows = len(matrix)

        if nb_rows == 0:
            return

        nb_cols = len(matrix[0])
        if nb_cols == 0:
            return

        col_has_zeroes = any(
            c+1
            for c in range(0, nb_cols)
            if matrix[0][c] == 0
        )

        row_has_zeroes = any(
            r+1
            for r in range(0, nb_rows)
            if matrix[r][0] == 0
        )

        if nb_rows == 1:
            if row_has_zeroes:
                print('here row')
                self._nullify_row(matrix, 0)
            return

        if nb_cols == 1:
            if col_has_zeroes:
                print('here col')
                self._nullify_col(matrix, 0)
            return

        for r in range(1, len(matrix[0])):
            for c in range(1, len(matrix)):
                if matrix[c][r] == 0:
                    matrix[c][0] = 0
                    matrix[0][r] = 0

        [
            self._nullify_row(matrix, r)
            for r in range(1, len(matrix[0]))
            if matrix[0][r] == 0
        ]

        [
            self._nullify_col(matrix, c)
            for c in range(1, len(matrix))
            if matrix[c][0] == 0
        ]

        if row_has_zeroes:
            self._nullify_row(matrix, 0)

        if col_has_zeroes:
            self._nullify_col(matrix, 0)

    @staticmethod
    def _nullify_row(matrix, row):
        for c in range(0, len(matrix[0])):
            matrix[row][c] = 0

    @staticmethod
    def _nullify_col(matrix, col):
        for r in range(0, len(matrix)):
            matrix[r][col] = 0
