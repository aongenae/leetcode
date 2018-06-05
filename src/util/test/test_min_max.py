#!/usr/bin/env python3
################################################################################
#
#   Filename:           test_min_max.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ...test import LeetcodeTest
from ..min_max import find_max, find_max_with_index, find_min_with_index


class _Mixin(object):

    def _validate(self, solution, elements, expected):
        self.assertEqual(
            solution,
            expected,
            self._format_error(elements, solution, expected)
        )

    @staticmethod
    def _format_error(elements, solution, expected):
        return (
            'wrong result for the following input:\n'
            '    elements: {}\n'
            '    solution: {}\n'
            '    expected: {}\n'
            .format(elements, solution, expected)
        )


class _MixinMaximum(_Mixin):

    def validate(self, elements, expected):
        self._validate(
            find_max(elements),
            elements,
            expected
        )


class TestMaximum(LeetcodeTest, _MixinMaximum):

    def test_max_empty(self):
        with self.assertRaises(AssertionError):
            find_max([])

    def test_max_one_elements(self):
        self.validate(
            elements=[7],
            expected=7
        )

    def test_max_middle(self):
        self.validate(
            elements=[7, 1, 50, 3, 6, 4],
            expected=50
        )

    def test_max_last_element(self):
        self.validate(
            elements=[7, 6, 4, 3, 201],
            expected=201
        )

    def test_max_first_element(self):
        self.validate(
            elements=[10, 7, 6, 4, 3, 1],
            expected=10
        )


class _MixinMaximumWithIndex(_Mixin):

    def validate(self, elements, expected):
        self._validate(
            find_max_with_index(elements),
            elements,
            expected
        )


class TestMaximumWithIndex(LeetcodeTest, _MixinMaximumWithIndex):

    def test_max_middle(self):
        self.validate(
            elements=[7, 1, 50, 3, 6, 4],
            expected=(2, 50)
        )

    def test_max_last_element(self):
        self.validate(
            elements=[7, 6, 4, 3, 201],
            expected=(4, 201)
        )

    def test_max_first_element(self):
        self.validate(
            elements=[10, 7, 6, 4, 3, 1],
            expected=(0, 10)
        )


class _MixinMinimumWithIndex(_Mixin):

    def validate(self, elements, expected):
        self._validate(
            find_min_with_index(elements),
            elements,
            expected
        )


class TestMinimumWithIndex(LeetcodeTest, _MixinMinimumWithIndex):

    def test_min_middle(self):
        self.validate(
            elements=[7, 1, 5, 3, 6, 4],
            expected=(1, 1)
        )

    def test_min_last_element(self):
        self.validate(
            elements=[7, 6, 4, 3, 1],
            expected=(4, 1)
        )

    def test_min_first_element(self):
        self.validate(
            elements=[-1, 7, 6, 4, 3, 1],
            expected=(0, -1)
        )
