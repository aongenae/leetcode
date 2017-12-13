#!/usr/bin/env python3
################################################################################
#
#   Filename:           tree_traversal.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
import queue


def iter_breadth_first(start_node):
    ''' impact the tree by removing the value !!!
        Todo add a flag in tree
    '''
    q = queue.Queue

    yield start_node.value
    start_node.value = None
    q.put(start_node)

    while not q.empty():
        node = q.get()
        yield node
        for child in node.iter_children():
            if not child.marked:
                child.marked = True
                q.put(child)
