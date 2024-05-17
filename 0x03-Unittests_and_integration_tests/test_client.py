#!/usr/bin/env python3
"""
MODULE TO TEST!
Parameterize and patch as decorators
"""


import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    method should test that GithubOrgClient.org returns the correct value.
    Use @patch as a decorator to make sure get_json
    is called once with the expected argument
    make sure it is not executed.

    Use @parameterized.expand as a decorator
    to parametrize the test with a couple of org examples
    to pass to GithubOrgClient, in this order:
    google
    abc
    no external HTTP calls should be made.
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get):
        """test GithubOrgClient.org"""
        mock_get.return_value = expected
        goc = GithubOrgClient(org)
        self.assertEqual(goc.org, expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")
