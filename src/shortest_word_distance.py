#!/usr/bin/env python3
################################################################################
#
#   Filename:           shortest_word_distance_ii.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #243, #244
#
#   Problem description:
#   https://leetcode.com/problems/shortest-word-distance/description/
#   https://leetcode.com/problems/shortest-word-distance-ii/description/
#
################################################################################


class Solution(object):

    def shortestDistance(self, words, word1, word2):
        '''
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        '''
        return WordDistance(words).shortest(word1, word2)


class WordDistance(object):

    def __init__(self, words):
        '''
        :type words: List[str]
        '''
        self._lookup = {}
        for index, word in enumerate(words):
            if word in self._lookup:
                self._lookup[word].add(index)
            else:
                self._lookup[word] = {index}

    def shortest(self, word1, word2):
        '''
        :type word1: str
        :type word2: str
        :rtype: int
        '''
        return min(
            abs(word_1 - word_2)
            for word_1 in self._lookup[word1]
            for word_2 in self._lookup[word2]
        )
