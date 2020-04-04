# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from brawlstars_api.api_client import ApiClient


class RankingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_brawler_rankings(self, country_code, brawler_id, **kwargs):  # noqa: E501
        """Get brawler rankings for a country or global rankings.  # noqa: E501

        Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_brawler_rankings(country_code, brawler_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str brawler_id: Identifier of the brawler. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_brawler_rankings_with_http_info(country_code, brawler_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_brawler_rankings_with_http_info(country_code, brawler_id, **kwargs)  # noqa: E501
            return data

    def get_brawler_rankings_with_http_info(self, country_code, brawler_id, **kwargs):  # noqa: E501
        """Get brawler rankings for a country or global rankings.  # noqa: E501

        Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_brawler_rankings_with_http_info(country_code, brawler_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str brawler_id: Identifier of the brawler. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'brawler_id', 'before', 'after', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_brawler_rankings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_brawler_rankings`")  # noqa: E501
        # verify the required parameter 'brawler_id' is set
        if ('brawler_id' not in params or
                params['brawler_id'] is None):
            raise ValueError("Missing the required parameter `brawler_id` when calling `get_brawler_rankings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501
        if 'brawler_id' in params:
            path_params['brawlerId'] = params['brawler_id']  # noqa: E501

        query_params = []
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/rankings/{countryCode}/brawlers/{brawlerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerRankingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_club_rankings(self, country_code, **kwargs):  # noqa: E501
        """Get club rankings for a country or global rankings.  # noqa: E501

        Get club rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_club_rankings(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: ClubRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_club_rankings_with_http_info(country_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_club_rankings_with_http_info(country_code, **kwargs)  # noqa: E501
            return data

    def get_club_rankings_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """Get club rankings for a country or global rankings.  # noqa: E501

        Get club rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_club_rankings_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: ClubRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'before', 'after', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_club_rankings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_club_rankings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501

        query_params = []
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/rankings/{countryCode}/clubs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClubRankingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_rankings(self, country_code, **kwargs):  # noqa: E501
        """Get player rankings for a country or global rankings.  # noqa: E501

        Get player rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_rankings(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_rankings_with_http_info(country_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_rankings_with_http_info(country_code, **kwargs)  # noqa: E501
            return data

    def get_player_rankings_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """Get player rankings for a country or global rankings.  # noqa: E501

        Get player rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_rankings_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: Two letter country code, or 'global' for global rankings. (required)
        :param str before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param str after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :param int limit: Limit the number of items returned in the response.
        :return: PlayerRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'before', 'after', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_rankings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_player_rankings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501

        query_params = []
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/rankings/{countryCode}/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerRankingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
