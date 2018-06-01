#!/usr/bin/env python3
################################################################################
#
#   Filename:           longest_substring_without_repeating_characters.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #3
#
#   Problem description:
#   https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
################################################################################


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        string_length = len(s)

        if string_length == 0:
            return 0

        if string_length == 1:
            return 1

        longest = 1
        current = 0
        runner = 1

        while current < string_length-1:
            if string_length - current < longest:
                return longest
            runner = current + 1
            tmp_lookup = {s[current]: current}
            while runner < string_length:
                runner_value = s[runner]
                if runner_value not in tmp_lookup:
                    tmp_lookup[runner_value] = runner
                    if runner == string_length-1:
                        if len(tmp_lookup) > longest:
                            longest = len(tmp_lookup)
                        return longest
                else:
                    if len(tmp_lookup) > longest:
                        longest = len(tmp_lookup)
                    current = tmp_lookup[runner_value]+1
                    break
                runner += 1

        return longest
