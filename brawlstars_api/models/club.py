# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Club(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag': 'str',
        'name': 'str',
        'description': 'str',
        'trophies': 'int',
        'required_trophies': 'int',
        'members': 'ClubMemberList',
        'type': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'description': 'description',
        'trophies': 'trophies',
        'required_trophies': 'requiredTrophies',
        'members': 'members',
        'type': 'type'
    }

    def __init__(self, tag=None, name=None, description=None, trophies=None, required_trophies=None, members=None, type=None):  # noqa: E501
        """Club - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._description = None
        self._trophies = None
        self._required_trophies = None
        self._members = None
        self._type = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if trophies is not None:
            self.trophies = trophies
        if required_trophies is not None:
            self.required_trophies = required_trophies
        if members is not None:
            self.members = members
        if type is not None:
            self.type = type

    @property
    def tag(self):
        """Gets the tag of this Club.  # noqa: E501


        :return: The tag of this Club.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Club.


        :param tag: The tag of this Club.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this Club.  # noqa: E501


        :return: The name of this Club.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Club.


        :param name: The name of this Club.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Club.  # noqa: E501


        :return: The description of this Club.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Club.


        :param description: The description of this Club.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def trophies(self):
        """Gets the trophies of this Club.  # noqa: E501


        :return: The trophies of this Club.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this Club.


        :param trophies: The trophies of this Club.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def required_trophies(self):
        """Gets the required_trophies of this Club.  # noqa: E501


        :return: The required_trophies of this Club.  # noqa: E501
        :rtype: int
        """
        return self._required_trophies

    @required_trophies.setter
    def required_trophies(self, required_trophies):
        """Sets the required_trophies of this Club.


        :param required_trophies: The required_trophies of this Club.  # noqa: E501
        :type: int
        """

        self._required_trophies = required_trophies

    @property
    def members(self):
        """Gets the members of this Club.  # noqa: E501


        :return: The members of this Club.  # noqa: E501
        :rtype: ClubMemberList
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Club.


        :param members: The members of this Club.  # noqa: E501
        :type: ClubMemberList
        """

        self._members = members

    @property
    def type(self):
        """Gets the type of this Club.  # noqa: E501


        :return: The type of this Club.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Club.


        :param type: The type of this Club.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Club, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Club):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
