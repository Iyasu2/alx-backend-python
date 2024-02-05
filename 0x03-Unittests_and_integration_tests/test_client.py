#!/usr/bin/env python3
'''
this is the module
'''
from typing import Any
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    this is a class
    '''
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        '''
        this is the function
        '''
        test_client = GithubOrgClient(org_name)
        self.assertEqual(test_client.org, {"payload": True})
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """Test that the result of _public_repos_url is the
        expected one based on the mocked payload"""
        payload = {"repos_url": "mocked_url"}
        mock_org.return_value = payload

        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client._public_repos_url, "mocked_url")

    @patch('client.get_json', return_value=[
        {"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test that the list of repos is what you
        expect from the chosen payload"""
        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "mocked_url"
            test_client = GithubOrgClient("org_name")
            self.assertEqual(test_client.public_repos(), ["repo1", "repo2"])
            mock_get_json.assert_called_once_with("mocked_url")
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self,
            repo: Dict[str, Dict[str, str]],
            license_key: str,
            expected: bool) -> None:
        """Test that the has_license method returns the expected value"""
        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client.has_license(repo, license_key), expected)
