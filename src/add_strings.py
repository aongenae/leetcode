#!/usr/bin/env python3
################################################################################
#
#   Filename:           add_strings.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #415
#
#   Problem description:
#   https://leetcode.com/problems/add-strings/description/
#
################################################################################


class Solution(object):
    ''' Accepted solution but not optimal :'(  '''

    def addStrings(self, num1, num2):
        '''
        :type num1: str
        :type num2: str
        :rtype: str
        '''
        return Solution._add_strings_helper(num1, num2, 0, 1)

    @staticmethod
    def _add_strings_helper(string_1, string_2, sum, multiplier):
        if string_1 == '' and string_2 == '':
            return str(sum)
        rest_1, num_1 = Solution._get_last(string_1)
        rest_2, num_2 = Solution._get_last(string_2)

        return Solution._add_strings_helper(
            rest_1,
            rest_2,
            sum + (num_1 + num_2) * multiplier,
            multiplier*10
        )

    @staticmethod
    def _get_last(string_num):
        if string_num == '':
            return '', 0
        return string_num[:-1], int(string_num[-1])
