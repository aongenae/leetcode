#!/usr/bin/env python3
################################################################################
#
#   Filename:           insert_delete_getrandom_o1.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #380
#
#   Problem description:
#   https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
################################################################################
import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._set = set()

    def insert(self, val):
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._set:
            return False
        self._set.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._set:
            self._set.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self._set, 1)[0]
