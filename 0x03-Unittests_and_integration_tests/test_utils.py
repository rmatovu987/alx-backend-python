#!/usr/bin/env python3
"""In this task you will write
the first unit test for utils.access_nested_map"""
import unittest
from typing import Mapping, Sequence, Any
from utils import *

import parameterized as parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
