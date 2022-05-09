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
