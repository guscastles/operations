# -*- coding: utf-8 -*-
"""
Test module for additions.
"""
from operations.addition import addition


def test_addition_of_no_number():
    assert addition() is None


def test_addition_of_1_number():
    assert addition(1) == 1


def test_addition_of_2_numbers():
    assert addition(1, 2) == 3


def test_addition_of_4_numbers():
    assert addition(1, 2, 4, 3) == 10


def test_addition_of_an_array_of_numbers():
    assert addition([1, 2, 4, 3]) == 10


def test_addition_of_diverse_elements():
    assert addition(1, [1, 2, 4, 3], 0) == 11


def test_addition_with_nested_lists():
    assert addition(1, [1, 2, 4, [3]], 0, [[[[[[4]], 5, 6]]]]) == 26
