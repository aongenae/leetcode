#!/usr/bin/env python3
################################################################################
#
#   Filename:           three_sum.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #15
#
#   Problem description:
#   https://leetcode.com/problems/3sum/description/
#
################################################################################


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        print('\n {}'.format(nums))
        solution = set()

        [
            solution.add(tuple(sorted([a, b, c])))
            for idx_a, a in enumerate(nums[:-2], 1)
            for idx_b, b in enumerate(nums[idx_a:-1], idx_a+1)
            for c in nums[idx_b:]
            if a + b + c == 0
        ]
        print('-----------------------')
        print(solution)
        return [list(k) for k in solution]

    def threeSum_dict(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        print('\n {}'.format(nums))
        solution = {}

        def _duplicate_helper(a, b, c):
            solution[tuple(sorted([a, b, c]))] = None

        [
            _duplicate_helper(a, b, c)
            for idx_a, a in enumerate(nums[:-2])
            for idx_b, b in enumerate(nums[idx_a+1:-1])
            for c in nums[idx_a+idx_b+2:]
            if a + b + c == 0
        ]
        print('-----------------------')
        return [list(k) for k in solution]

    def threeSum_comprehension(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        solution = []
        length = len(nums)
        if length < 3:
            return []

        def _duplicate_helper(a, b, c):
            candidate = sorted([a, b, c])
            if candidate not in solution:
                solution.append(candidate)

        [
            _duplicate_helper(a, b, c)
            for idx_a, a in enumerate(nums[:-3])
            for idx_b, b in enumerate(nums[idx_a+1:-2])
            for c in nums[idx_b+1:]
            if a + b + c == 0
        ]
        return solution

    def threeSum_loop(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        print('\n{}'.format(nums))
        solution = []
        length = len(nums)
        if length < 3:
            return []
        for idx_a, a in enumerate(nums[:-3]):
            print('a {}'.format(a))
            for idx_b, b in enumerate(nums[idx_a+1:-2]):
                print('b {}'.format(b))
                for c in nums[idx_b+1:]:
                    print('c {}'.format(c))
                    print('{} {} {}'.format(a, b, c))
                    if a + b + c == 0:
                        candidate = sorted([a, b, c])
                        if candidate not in solution:
                            solution.append(candidate)
        return solution

    def threeSum_slow(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        print('\n{}'.format(nums))
        solution = []
        length = len(nums)
        if length < 3:
            return []
        range_a = length - 2
        range_b = length - 1
        range_c = length
        for idx_a in range(0, range_a):
            a = nums[idx_a]
            for idx_b in range(idx_a + 1, range_b):
                b = nums[idx_b]
                for idx_c in range(idx_a + idx_b + 1, range_c):
                    c = nums[idx_c]
                    print('range     c = {}'.format(c))
                for c in nums[idx_a+idx_b+2:]:
                    print('enumerate c = {}'.format(c))
                    if a + b + c == 0:
                        candidate = sorted([a, b, c])
                        if candidate not in solution:
                            solution.append(candidate)
        return solution
