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
        nums.sort()
        result = set()
        visited = set()
        length_nums = len(nums)
        for current in range(length_nums-1):
            current_value = nums[current]
            tmp_lookup = {}
            target = -current_value
            if current_value not in visited:
                for runner in range(current+1, length_nums):
                    runner_value = nums[runner]
                    if runner_value not in tmp_lookup:
                        tmp_lookup[target - runner_value] = runner
                    else:
                        result.add(
                            (current_value, target-runner_value, runner_value)
                        )
                    visited.add(current_value)
        return list(result)

    def threeSum_slow(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        solution = set()
        nums.sort()

        stack = [(1, nums)]
        while len(stack):
            moving_idx, nums = stack.pop()

            if len(nums) <= 1:
                break

            if moving_idx == len(nums) - 1:
                stack.append((1, nums[1:]))
                continue

            a = nums[0]
            b = nums[moving_idx]
            c = nums[-1]
            abc = a + b + c

            if abc < 0:
                stack.append((moving_idx+1, nums))
                state = (moving_idx+1, nums)
            elif abc == 0:
                solution.add((a, b, c))
                state = (moving_idx+1, nums)
            elif abc > 0:
                state = (1, nums[:-1])

            stack.append(state)

        return [list(e) for e in solution]


class SolutionRecursive:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return [list(e) for e in Solution._helper(1, nums, set())]

    @staticmethod
    def _helper(moving_idx, nums, solution):

        if len(nums) <= 1:
            return solution

        if moving_idx == len(nums) - 1:
            return Solution._helper(1, nums[1:], solution)

        a = nums[0]
        b = nums[moving_idx]
        c = nums[-1]
        abc = a + b + c

        if abc < 0:
            return Solution._helper(moving_idx+1, nums, solution)
        if abc == 0:
            solution.add((a, b, c))
            return Solution._helper(moving_idx+1, nums, solution)
        if abc > 0:
            return Solution._helper(1, nums[:-1], solution)
