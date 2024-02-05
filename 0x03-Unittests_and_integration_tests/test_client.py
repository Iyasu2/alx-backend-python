#!/usr/bin/env python3
'''
this is the module
'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
import fixtures


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
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the
        expected one based on the mocked payload"""
        payload = {"repos_url": "mocked_url"}
        mock_org.return_value = payload

        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client._public_repos_url, "mocked_url")

    @patch('client.get_json', return_value=[
        {"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
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
    def test_has_license(self, repo, license_key, expected):
        """Test that the has_license method returns the expected value"""
        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class(
    [
        {
            "org_payload": fixtures.org_payload,
            "repos_payload": fixtures.repos_payload,
            "expected_repos": fixtures.expected_repos,
            "apache2_repos": fixtures.apache2_repos
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''
    this ia class
    '''
    @classmethod
    def setUpClass(cls):
        """Set up class method for TestIntegrationGithubOrgClient"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith("/orgs/org"):
                return Mock(json=lambda: cls.org_payload)
            elif url.endswith("/orgs/org/repos"):
                return Mock(json=lambda: cls.repos_payload)
            else:
                return Mock(json=lambda: [])

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method for TestIntegrationGithubOrgClient"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that the list of repos is what
        you expect from the chosen payload"""
        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.mock_get.assert_called_once()

    def test_public_repos_with_license(self):
        """Test that the list of repos with a specific license
        is what you expect from the chosen payload"""
        test_client = GithubOrgClient("org_name")
        self.assertEqual(
                test_client.public_repos(license="apache-2.0"),
                self.apache2_repos)
        self.mock_get.assert_called_once()
