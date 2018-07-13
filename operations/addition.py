# -*- coding: utf-8 -*-
"""
Module for the addition operation.
"""
from functools import reduce
from operations.list.flatten import flatten


def _execute(first_element, second_element):
    return first_element + second_element


def addition(*args):
    """Adds any quantity of numbers"""

    def _initial_value():
        return None if not args else 0

    return reduce(_execute, flatten(args), _initial_value())
