#!/usr/bin/env python3
'''
this is the module
'''
import unittest
from unittest.mock import patch
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
    def test_org(self, org_name, mock_get_json):
        '''
        this is the function
        '''
        test_client = GithubOrgClient(org_name)
        self.assertEqual(test_client.org, {"payload": True})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the
        expected one based on the mocked payload"""
        payload = {"repos_url": "mocked_url"}
        mock_org.return_value = payload

        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client._public_repos_url, "mocked_url")
