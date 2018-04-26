#!/usr/bin/env python3
################################################################################
#
#   Filename:           peeking_iterator.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #284
#
#   Problem description:
#   https://leetcode.com/problems/peeking-iterator/description/
#
################################################################################

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object):

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator
        :rtype: int
        """
        if self._buffer is not None:
            return self._buffer
        if self._iterator.hasNext():
            self._buffer = self._iterator.next()
            return self._buffer

    def next(self):
        """
        :rtype: int
        """
        if self._buffer is not None:
            result = self._buffer
            self._buffer = None
            return result
        if self._iterator.hasNext():
            return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._buffer is not None or self._iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
