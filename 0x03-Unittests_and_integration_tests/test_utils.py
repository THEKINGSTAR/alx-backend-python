#!/usr/bin/env python3
"""
MODULE TO TEST!
"""


from collections.abc import Mapping
from parameterized import parameterized
import unittest
from utils import access_nested_map, memoize
from unittest.mock import MagicMock, patch, Mock
from typing import Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str], expctd_rslts) -> None:
        """
        method to test that the method
        returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expctd_rslts)
    

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                               path: Tuple[str]) -> None:
        """
        Use the assertRaises context manager
        to test that a KeyError is raised
        for the following inputs:
            (use @parameterized.expand):
            nested_map={}, path=("a",)
            nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


if __name__ == '__main__':
    unittest.main()
