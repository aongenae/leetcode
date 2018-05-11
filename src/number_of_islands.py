#!/usr/bin/env python3
################################################################################
#
#   Filename:           number_of_islands.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #200
#
#   Problem description:
#   https://leetcode.com/problems/number-of-islands/description/
#
################################################################################
# from queue import Queue
from collections import deque


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.nb_row = len(grid)
        if self.nb_row == 0:
            return 0
        self.nb_col = len(grid[0])
        if self.nb_col == 0:
            return 0

        nb_islands = 0

        for row in range(self.nb_row):
            for col in range(self.nb_col):
                if grid[row][col] == '1':
                    nb_islands += 1
                    self._bfs(row, col)

        return nb_islands

    def _bfs(self, row, col):
        queue = deque()
        queue.append((row, col))
        while len(queue) > 0:
            r, c = queue.popleft()
            for neighbor_r, neighbor_c in self._iter_neighbors(r, c):
                self.grid[neighbor_r][neighbor_c] = '0'
                queue.append((neighbor_r, neighbor_c))

    def _iter_neighbors(self, row, col):
        if row > 0 and self.grid[row-1][col] == '1':
            yield (row-1, col)

        if row < self.nb_row-1 and self.grid[row+1][col] == '1':
            yield (row+1, col)

        if col > 0 and self.grid[row][col-1] == '1':
            yield (row, col-1)

        if col < self.nb_col-1 and self.grid[row][col+1] == '1':
            yield (row, col+1)
