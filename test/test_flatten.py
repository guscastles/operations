# -*- coding: utf-8 -*-
"""
Test module for the flatten function.
"""
import pytest
from operations.list.flatten import flatten, __flattened__


@pytest.mark.wip
def test_flattened_on_empty_list():
    assert __flattened__([])


@pytest.mark.wip
def test_flattened_on_not_flattened():
    assert not __flattened__([[1]])


def test_flattened():
    assert __flattened__([1, 2, 3, 4])


def test_flatten_an_empty_list():
    assert flatten([]) == []


def test_flatten_a_flattened_list():
    assert flatten([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_flatten_list_and_number():
    assert flatten([1, [2, 3, 4]]) == [1, 2, 3, 4]


def test_flatten_nested_lists():
    assert flatten([[[1, 2, 3]], 1]) == [1, 2, 3, 1]
