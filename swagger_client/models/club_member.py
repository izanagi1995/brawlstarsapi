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


class ClubMember(object):
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
        'trophies': 'int',
        'role': 'str',
        'name_color': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'trophies': 'trophies',
        'role': 'role',
        'name_color': 'nameColor'
    }

    def __init__(self, tag=None, name=None, trophies=None, role=None, name_color=None):  # noqa: E501
        """ClubMember - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._trophies = None
        self._role = None
        self._name_color = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if trophies is not None:
            self.trophies = trophies
        if role is not None:
            self.role = role
        if name_color is not None:
            self.name_color = name_color

    @property
    def tag(self):
        """Gets the tag of this ClubMember.  # noqa: E501


        :return: The tag of this ClubMember.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ClubMember.


        :param tag: The tag of this ClubMember.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this ClubMember.  # noqa: E501


        :return: The name of this ClubMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClubMember.


        :param name: The name of this ClubMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def trophies(self):
        """Gets the trophies of this ClubMember.  # noqa: E501


        :return: The trophies of this ClubMember.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this ClubMember.


        :param trophies: The trophies of this ClubMember.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def role(self):
        """Gets the role of this ClubMember.  # noqa: E501


        :return: The role of this ClubMember.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ClubMember.


        :param role: The role of this ClubMember.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def name_color(self):
        """Gets the name_color of this ClubMember.  # noqa: E501


        :return: The name_color of this ClubMember.  # noqa: E501
        :rtype: str
        """
        return self._name_color

    @name_color.setter
    def name_color(self, name_color):
        """Sets the name_color of this ClubMember.


        :param name_color: The name_color of this ClubMember.  # noqa: E501
        :type: str
        """

        self._name_color = name_color

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
        if issubclass(ClubMember, dict):
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
        if not isinstance(other, ClubMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
