# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.players_api import PlayersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_battle_log(self):
        """Test case for get_battle_log

        Get log of recent battles for a player.  # noqa: E501
        """
        pass

    def test_get_player(self):
        """Test case for get_player

        Get player information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
