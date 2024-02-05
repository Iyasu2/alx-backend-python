#!/usr/bin/env python3
'''
this is a test module
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    '''
    this is a class
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        this is a function
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
        this is a function
        '''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    '''
    class for get json
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        '''
        a function
        '''
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(json=lambda: test_payload)
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)
