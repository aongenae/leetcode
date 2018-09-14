#!/usr/bin/env python3
################################################################################
#
#   Filename:           goat_latin.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #824
#
#   Problem description:
#   https://leetcode.com/problems/goat-latin/description/
#
################################################################################

vowels = frozenset(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',])


class Solution(object):

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        sentence = S

        if len(sentence) == 0:
            return ''

        return ' '.join(
            append_correct_number_of_a(
                convert_word_to_goat_latin(word),
                index
            )
            for index, word in enumerate(sentence.split(), 1)
        )

def convert_word_to_goat_latin(word):
    if start_with_consonant(word):
        return convert_word_using_consonant_rule(word)
    return convert_word_using_vowel_rule(word)

def start_with_consonant(word):
    return word[0] not in vowels

def convert_word_using_consonant_rule(word):
    if len(word) > 1:
        return '{}{}ma'.format(word[1:], word[0])
    return '{}ma'.format(word)

def convert_word_using_vowel_rule(word):
    return '{}ma'.format(word)

def append_correct_number_of_a(word, index):
    return '{}{}'.format(word, index*'a')
