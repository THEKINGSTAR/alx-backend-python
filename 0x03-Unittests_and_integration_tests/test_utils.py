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


if __name__ == '__main__':
    unittest.main()
