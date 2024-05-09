#!/usr/bin/env python3
"""
MODULE TO TEST!
"""

from unittest.mock import MagicMock
# from nose.tools import assert_equal
from parameterized import parameterized
import unittest
from utils import access_nested_map
import math


class TestAccessNestedMap(unittest.TestCase) :
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expctd_rslts):
        """
        method to test that the method
        returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expctd_rslts)
        return 

