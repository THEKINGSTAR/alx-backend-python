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

    def test_has_license(self, unittest.TestCase):
        """
        test that GithubOrgClient.has_license returns the expected result.
        Use PropertyMock to patch the property of the class
        to return a couple of repos.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as mock_public_repos_url:
                mock_public_repos_url.return_value = ["repo1", "repo2"]
                with patch('client.GithubOrgClient._has_license',
                           return_value=True) as mock_has_license:
                    goc = GithubOrgClient("test")
                    self.assertTrue(goc.has_license("test"))
                    mock_has_license.assert_called_once_with("test")
                    mock_public_repos_url.assert_called_once()

    def public_repos(self, unittest.TestCase):
        """
        test that GithubOrgClient.public_repos returns the expected result.
        Use PropertyMock to patch the property of the class
        to return a couple of repos.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as mock_public_repos_url:
                mock_public_repos_url.return_value = ["repo1", "repo2"]
                goc = GithubOrgClient("test")
                self.assertEqual(goc.public_repos(), ["repo1", "repo2"])
                mock_public_repos_url.assert_called_once()
                mock_org.assert_called_once()

    def test_public_repos(self, unittest.TestCase):
        """
        the test_public_repos method to test GithubOrgClient.public_repos.
        Make sure that the method
        returns the expected results based on the fixtures.
        Implement test_public_repos_with_license
        to test the public_repos
        with the argument license="apache-2.0"
        and
        make sure the result matches the expected value from the fixtures.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as mock_public_repos_url:
                mock_public_repos_url.return_value = ["repo1", "repo2"]
                with patch('client.GithubOrgClient._has_license',
                           return_value=True) as mock_has_license:
                    goc = GithubOrgClient("test")
                    self.assertEqual(goc.public_repos(), ["repo1", "repo2"])
                    mock_public_repos_url.assert_called_once()
                    mock_org.assert_called_once()
                    mock_has_license.assert_called_once_with("test")
                    mock_has_license.reset_mock()
                    mock_has_license.return_value = False
                    self.assertEqual(goc.public_repos(), [])
                    mock_has_license.assert_called_once_with("test")
                    mock_has_license.reset_mock()
                    mock_has_license.return_value = True
                    self.assertEqual(goc.public_repos("apache-2.0"), ["repo1"])
                    mock_has_license.assert_called_once_with("test",
                                                             "apache-2.0")

    def test_public_repos_with_license(self, unittest.TestCase):
        """
        Implement test_public_repos_with_license
        to test the public_repos
        with the argument license="apache-2.0"
        and
        make sure the result matches the expected value from the fixtures.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as mock_public_repos_url:
                mock_public_repos_url.return_value = ["repo1", "repo2"]
                with patch('client.GithubOrgClient._has_license',
                           return_value=True) as mock_has_license:
                    goc = GithubOrgClient("test")
                    self.assertEqual(goc.public_repos(), ["repo1", "repo2"])
                    mock_public_repos_url.assert_called_once()
                    mock_org.assert_called_once()
                    mock_has_license.assert_called_once_with("test")
                    mock_has_license.reset_mock()
                    mock_has_license.return_value = False
                    self.assertEqual(goc.public_repos(), [])
                    mock_has_license.assert_called_once_with("test")
                    mock_has_license.reset_mock()
                    mock_has_license.return_value = True
                    self.assertEqual(goc.public_repos("apache-2.0"), ["repo1"])
                    mock_has_license.assert_called_once_with("test",
                                                             "apache-2.0")
