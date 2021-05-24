#!/usr/bin/env python3
################################################################################
#
#   Filename:           word_break.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #139
#
#   Problem description:
#   https://leetcode.com/problems/word-break/description/
#
################################################################################
from queue import Queue


class Solution(object):

    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        '''
        string_length = len(s)
        wordDictSet = set(wordDict)
        queue = Queue()
        visited = [0]*string_length
        queue.put(0)

        while not queue.empty():
            start = queue.get()
            if visited[start] == 0:
                for end in range(start+1, string_length+1):
                    if s[start:end] in wordDictSet:
                        queue.put(end)
                        if end == string_length:
                            return True
                visited[start] = 1
        return False

    def wordBreak_brute_force(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        '''
        self.wordDictSet = set(wordDict)
        return self._wordBreak(s, 0)

    def _wordBreak_brute_force(self, s, start):
        if start == len(s):
            return True

        for end in range(start+1, len(s)+1):
            if s[start:end] in self.wordDictSet and \
                    self._wordBreak_brute_force(s, end):
                return True

        return False

    def wordBreak_brute_force_w_memoization(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        '''
        self.wordDictSet = set(wordDict)
        return self._wordBreak_memo(s, 0, {})

    def _wordBreak_memo(self, s, start, memo):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        for end in range(start+1, len(s)+1):
            if s[start:end] in self.wordDictSet and \
                    self._wordBreak_memo(s, end, memo):
                memo[start] = True
                return True

        return False
