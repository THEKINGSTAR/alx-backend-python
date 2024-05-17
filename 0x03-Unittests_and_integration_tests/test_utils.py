#!/usr/bin/env python3
"""
MODULE TO TEST!
"""

from unittest.mock import MagicMock, patch, Mock
from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map, memoize
from utils import get_json
from typing import Dict, Tuple, Union


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
        Use the assertRaises context manager to test that
        a KeyError is raised for the following inputs
        (use @parameterized.expand):
        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Familiarize yourself with the utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def _test_get_json(self, test_url: str, test_payload: dict) -> None:
        """
        method to test that utils.get_json returns the expected result.
        Use unittest.mock.patch to patch requests.get.
        returns a Mock object with a json method that
        returns
        test_payload which you parametrize alongside
        the test_url that you will pass to get_json
        """
        attrs = {'json.return_value': test_payload}
        mock_response = Mock(**attrs)
        with patch('requests.get', return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """

    """
    def test_memoize(self):
        """

        """
        class TestClass:
            """
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
