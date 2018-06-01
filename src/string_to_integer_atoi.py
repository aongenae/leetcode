#!/usr/bin/env python3
################################################################################
#
#   Filename:           string_to_integer_atoi.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #8
#
#   Problem description:
#   https://leetcode.com/problems/string-to-integer-atoi/description
#
################################################################################


class Solution(object):

    def myAtoi(self, str):
        '''
        :type str: str
        :rtype: int
        '''
        integers = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        sign_found = False
        sign = 1
        result = 0

        for char in str:
            if char in integers:
                if not sign_found:
                    sign_found = True
                result = 10 * result + integers[char]
                if result > 2147483647:
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648
            elif not sign_found:
                if char == '-':
                    sign_found = True
                    sign = -1
                elif char == '+':
                    sign_found = True
                elif char == ' ':
                    continue
                else:
                    break
            else:
                break

        return sign * result
