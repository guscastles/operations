# -*- coding: utf-8 -*-
"""
Provides functions for flattening a list.
"""


def __change__(element):
    return element if isinstance(element, list) else [element]


def __flattened__(elements):
    return not [element for element in elements if isinstance(element, list)]
    

def flatten(elements):
    """Flattens a list of elements"""
    if __flattened__(elements):
        return elements
    return flatten([el for elem in elements for el in __change__(elem)])
