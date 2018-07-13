# -*- coding: utf-8 -*-
"""
Provides functions for flattening a list.
"""


def _change(element):
    return element if isinstance(element, list) else [element]


def flattened(elements):
    return not [element for element in elements if isinstance(element, list)]
    

def flatten(elements):
    """Flattens a list of elements"""
    if flattened(elements):
        return elements
    return flatten([el for elem in elements for el in _change(elem)])
