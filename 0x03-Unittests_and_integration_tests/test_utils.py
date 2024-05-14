#!/usr/bin/env python3
"""
MODULE TO TEST!
"""

from unittest.mock import MagicMock
# from nose.tools import assert_equal
from parameterized import parameterized
import unittest
from utils import access_nested_map
from utils import get_json
import requests
import math


class TestAccessNestedMap(unittest.TestCase):
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Use the assertRaises context manager to test that
        a KeyError is raised for the following inputs
        (use @parameterized.expand):
        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
        return


class TestGetJson(unittest.TestCase):
    """
    Familiarize yourself with the utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://example.com", {"payload": True})

    ])
    def test_get_json(self, url, payload):
        """
        method to test that utils.get_json returns the expected result.
        returns a Mock object with a json method that returns test_payload
        """
        mock = MagicMock(return_value=payload)
        with unittest.mock.patch('requests.get', mock):
            self.assertEqual(get_json(url), payload)
        return