#!/usr/bin/env python3
"""
MODULE TO TEST!
Parameterize and patch as decorators
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithubOrgClient.
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get):
        """Test GithubOrgClient.org"""
        mock_get.return_value = expected
        goc = GithubOrgClient(org)
        self.assertEqual(goc.org, expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    @parameterized.expand([
        ("my_license", {"license": {"key": "my_license"}}),
        ("other_license", {"license": {"key": "other_license"}})
    ])
    def test_has_license(self, license_key, repo):
        """
        Test GithubOrgClient.has_license method.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as mock_public_repos_url:
                mock_public_repos_url.return_value = [repo]
                goc = GithubOrgClient("test")
                self.assertEqual(goc.has_license(repo, license_key),
                                 repo["license"]["key"] == license_key)
                mock_public_repos_url.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        """
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_repos_url"}
            goc = GithubOrgClient("test")
            self.assertEqual(goc.public_repos(), ["repo1", "repo2"])
            mock_org.assert_called_once()
            mock_get_json.assert_called_once_with("test_repos_url")


@parameterized_class([
    {"org_payload": {"login": "test"},
     "repos_payload": [{"name": "test_repo"}],
     "expected_repos": ["test_repo"],
     "apache2_repos": [{"license": {"key": "apache-2.0"}}]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class for integration tests.
        """
        cls.org_payload = {"login": "test"}
        cls.repos_payload = [{"name": "test_repo"}]
        cls.expected_repos = ["test_repo"]
        cls.apache2_repos = [{"license": {"key": "apache-2.0"}}]

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method.
        """
        with patch('client.get_json', side_effect=[self.org_payload,
                                                   self.repos_payload]):
            goc = GithubOrgClient("test")
            self.assertEqual(goc.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos with license="apache-2.0".
        """
        with patch('client.get_json', side_effect=[self.org_payload,
                                                   self.repos_payload,
                                                   self.apache2_repos]):
            goc = GithubOrgClient("test")
            self.assertEqual(goc.public_repos(
                "apache-2.0"), self.apache2_repos)
