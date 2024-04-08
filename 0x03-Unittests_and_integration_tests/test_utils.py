#!/usr/bin/env python3
"""
MODULE TO TEST!
"""

from unittest.mock import MagicMock
# from nose.tools import assert_equal
# from parameterized import parameterized, parameterized_class
import unittest
import math



@parameterized.expand([
    {"a": 1}, "expected":"a")
    {"a": {"b": 2}},  "expected":"a",
    {"a": {"b": 2}},  "expected":"a", "b"
])

class TestAccessNestedMap(unittest.TestCase) :
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand
    def test_access_nested_map(self):
        """
        method to test that the method
        returns what it is supposed to.
        """
        return 

