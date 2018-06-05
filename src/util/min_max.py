#!/usr/bin/env python3
################################################################################
#
#   Filename:           min_max.py
#
#   Author:             Arnaud Ongenae
#
################################################################################


def find_max(elements):
    assert len(elements) > 0, 'no max for an empty list of elements'
    maximum = elements[0]
    if len(elements) > 1:
        for element in elements[1:]:
            if element > maximum:
                maximum = element
    return maximum


def find_max_with_index(elements):
    maximum = (0, elements[0])
    for idx, element in enumerate(elements):
        _, max_value = maximum
        if element > max_value:
            maximum = (idx, element)
    return maximum


def find_min_with_index(elements):
    minimum = (0, elements[0])
    for idx, element in enumerate(elements):
        _, min_value = minimum
        if element < min_value:
            minimum = (idx, element)
    return minimum
