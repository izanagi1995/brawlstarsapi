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
from api.clubs_api import ClubsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClubsApi(unittest.TestCase):
    """ClubsApi unit test stubs"""

    def setUp(self):
        self.api = api.clubs_api.ClubsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_club(self):
        """Test case for get_club

        Get club information.  # noqa: E501
        """
        pass

    def test_get_club_members(self):
        """Test case for get_club_members

        List club members.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
