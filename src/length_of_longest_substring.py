#!/usr/bin/env python
################################################################################
#
#   Filename:           length_of_longest_substring.py
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
#        print(' ')
        longest = 0
        current_length = 0
        lookup = {}
        previous = ''
        for character in s:
            if character in lookup:
                if character == previous:
                    current_length = 1
            else:
                current_length += 1
                lookup[character] = None
            if current_length > longest:
                longest = current_length
#            print('character "{}", current "{}"'.format(character, current_length))
            previous = character
        return longest
