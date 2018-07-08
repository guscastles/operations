# -*- coding: utf-8 -*-
"""
Module for the addition operation.
"""
from functools import reduce
from operations.list.flatten import flatten


def __execute__(first_element, second_element):
    return first_element + second_element


def addition(*args):
    """Adds any quantity of numbers"""

    def __initial_value__():
        return None if not args else 0

    return reduce(__execute__, flatten(args), __initial_value__())
