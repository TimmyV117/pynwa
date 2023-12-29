#!/usr/bin/env python

"""Tests for `pynwa` package."""


import unittest
import os
import yaml
import requests
# from unittest.mock import patch
# from click.testing import CliRunner

from pynwa.BasicDataFetch import *

PYNWA_CONFIG_PATH = '/pynwa/pynwa'
PYNWA_CONFIG = 'config.yaml'
PYNWA_CONFIG_FILEPATH = os.path.join(PYNWA_CONFIG_PATH, PYNWA_CONFIG)

with open(PYNWA_CONFIG_FILEPATH, 'r', encoding='utf-8') as file:
    CONFIG = yaml.safe_load(file)



class TestBasicDataFetch(unittest.TestCase):
    """Tests for `pynwa.BasicDataFetch` package."""
    
#TODO these can't check response code since that is already handled
#TODO instead check for datatype
    def test_successful_basic_stats(self):
        """Checks to ensure basic status URL can be reached successfully"""
        response = requests.get(CONFIG.get('URL_BASIC_LIVERPOOL_STATS'), timeout=10)
        self.assertEqual(response.status_code, 200)
        
    def test_get_standard_player_stats_request_response(self):
        """Makes sure that function is able to make successful GET request"""
        df = get_standard_player_stats()
        self.assertIn(df., 200)
    
    def test_get_scores_and_fixtures_response(self):
        """Makes sure that function is able to make successful GET request."""
        response = get_scores_and_fixtures()
        self.assertEqual(response.status_code, 200)
    
    def test_get_shooting_stats_response(self):
        """Makes sure that function is able to make successful GET request"""
        response = get_shooting_stats()
        self.assertEqual(response.status_code, 200)
    
    def test_get_goal_and_shot_creations_stats_response(self):
        """Makes sure that function is able to make successful GET request"""
        response = get_goal_and_shot_creation_stats()
        self.assertEqual(response.status_code, 200)

    # def tearDown(self):
    #     """Tear down test fixtures, if any."""

    # def test_000_something(self):
    #     """Test something."""

    # def test_command_line_interface(self):
    #     """Test the CLI."""
    #     runner = CliRunner()
    #     result = runner.invoke(cli.main)
    #     assert result.exit_code == 0
    #     assert 'pynwa.cli.main' in result.output
    #     help_result = runner.invoke(cli.main, ['--help'])
    #     assert help_result.exit_code == 0
    #     assert '--help  Show this message and exit.' in help_result.output

if __name__ == '__main__':
    unittest.main()