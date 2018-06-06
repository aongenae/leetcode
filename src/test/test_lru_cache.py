#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_lru_cache.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..lru_cache import LRUCache
from .leetcode_test import LeetcodeTest


class TestLRUCacheEmpty(LeetcodeTest):

    def setUp(self):
        self.lru_cache = LRUCache(3)

    def test_empty(self):
        self.assertEqual(self.lru_cache.get(5), -1)


class TestLRUCacheOneElement(LeetcodeTest):

    def setUp(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.put(5, 5)

    def test_in_lookup(self):
        self.assertIn(5, self.lru_cache._lookup)

    def test_head(self):
        self.assertIs(self.lru_cache._lookup[5], self.lru_cache._head)

    def test_tail(self):
        self.assertIs(self.lru_cache._lookup[5], self.lru_cache._tail)

    def test_get(self):
        self.assertEqual(self.lru_cache.get(5), 5)

    def test_still_in_after_get(self):
        self.lru_cache.get(5)
        self.assertIsNotNone(self.lru_cache._head)
        self.assertIsNotNone(self.lru_cache._tail)
        self.assertEqual(self.lru_cache._nb_elements, 1)


class TestLRUCachePut(LeetcodeTest):

    def test_put_one_element_with_room(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.put(1, 1)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[1])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[1])

    def test_put_two_elements_with_room(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[1])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[2])
        self.assertIs(self.lru_cache._head.next, self.lru_cache._tail)

    def test_put_two_elements_at_capacity(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[1])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[2])

    def test_put_three_elements_over_capacity(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.lru_cache.put(3, 3)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[2])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[3])

    def test_put_three_elements_with_room(self):
        self.lru_cache = LRUCache(4)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.lru_cache.put(3, 3)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[1])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[3])

    def test_put_three_elements_at_capacity(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.lru_cache.put(3, 3)
        self.assertIs(self.lru_cache._head, self.lru_cache._lookup[1])
        self.assertIs(self.lru_cache._tail, self.lru_cache._lookup[3])


class TestLRUCacheTwoElementsWithRoom(LeetcodeTest):

    def setUp(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)

    def test_in_lookup(self):
        self.assertIn(1, self.lru_cache._lookup)
        self.assertIn(2, self.lru_cache._lookup)

    def test_head_init(self):
        self.assertIs(self.lru_cache._lookup[1], self.lru_cache._head)

    def test_tail_init(self):
        self.assertIs(self.lru_cache._lookup[2], self.lru_cache._tail)

    def test_head_tail_after_get(self):
        self.lru_cache.get(1)
        self.assertIs(self.lru_cache._lookup[1], self.lru_cache._tail)
        self.assertIs(self.lru_cache._lookup[2], self.lru_cache._head)


class TestLRUCacheTwoElementsAtCapacity(LeetcodeTest):

    def setUp(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.lru_cache.put(3, 3)

    def test_in_lookup(self):
        self.assertNotIn(1, self.lru_cache._lookup)
        self.assertIn(2, self.lru_cache._lookup)
        self.assertIn(3, self.lru_cache._lookup)

    def test_numbers(self):
        self.assertEqual(len(self.lru_cache._lookup), 2)
        self.assertEqual(self.lru_cache._nb_elements, 2)

    def test_head(self):
        self.assertIs(self.lru_cache._lookup[2], self.lru_cache._head)

    def test_tail(self):
        self.assertIs(self.lru_cache._lookup[3], self.lru_cache._tail)

    def test_get(self):
        self.assertEqual(self.lru_cache.get(2), 2)

    def test_after_get(self):
        self.lru_cache.get(2)
        self.assertIn(2, self.lru_cache._lookup)

    def test_replace_value(self):
        self.lru_cache.put(3, 5)
        self.assertEqual(self.lru_cache.get(3), 5)


class TestLRUCacheSequences(LeetcodeTest):

    def test_sequence_1(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 2)
        self.assertEqual(self.lru_cache.get(1), 1)
        self.lru_cache.put(3, 3)
        self.assertEqual(self.lru_cache.get(2), -1)
        self.lru_cache.put(4, 4)
        self.assertEqual(self.lru_cache.get(1), -1)
        self.assertEqual(self.lru_cache.get(3), 3)
        self.assertEqual(self.lru_cache.get(4), 4)

    def test_sequence_2(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(2, 1)
        self.lru_cache.put(2, 2)
        self.assertEqual(self.lru_cache.get(2), 2)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(4, 1)
        self.lru_cache.get(2)
        self.assertEqual(self.lru_cache.get(2), -1)

    def test_sequence_3(self):
        self.lru_cache = LRUCache(2)
        self.lru_cache.put(2, 1)
        self.lru_cache.put(1, 1)
        self.lru_cache.put(2, 3)
        self.lru_cache.put(4, 1)
        self.assertEqual(self.lru_cache.get(1), -1)
        self.assertEqual(self.lru_cache.get(2), 3)
