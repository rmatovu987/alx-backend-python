#!/usr/bin/env python3
"""In this task you will write
the first unit test for utils.access_nested_map"""
import unittest
from utils import *

from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """tests the  utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Args:
            nested_map Mapping: nested map
            path tuple: a sequence
            expected value from last path input
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access nested map raises a KeyError
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual((path[len(path) - 1]), context.exception.args[0])
