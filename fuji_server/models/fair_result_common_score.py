# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class FAIRResultCommonScore(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, earned: float=0, total: int=0):  # noqa: E501
        """FAIRResultCommonScore - a model defined in Swagger

        :param earned: The earned of this FAIRResultCommonScore.  # noqa: E501
        :type earned: int
        :param total: The total of this FAIRResultCommonScore.  # noqa: E501
        :type total: int
        """
        self.swagger_types = {
            'earned': float,
            'total': int
        }

        self.attribute_map = {
            'earned': 'earned',
            'total': 'total'
        }
        self._earned = earned
        self._total = total

    @classmethod
    def from_dict(cls, dikt) -> 'FAIRResultCommonScore':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResultCommon_score of this FAIRResultCommonScore.  # noqa: E501
        :rtype: FAIRResultCommonScore
        """
        return util.deserialize_model(dikt, cls)

    @property
    def earned(self) -> float:
        """Gets the earned of this FAIRResultCommonScore.


        :return: The earned of this FAIRResultCommonScore.
        :rtype: float
        """
        return self._earned

    @earned.setter
    def earned(self, earned: float):
        """Sets the earned of this FAIRResultCommonScore.


        :param earned: The earned of this FAIRResultCommonScore.
        :type earned: float
        """

        self._earned = earned

    @property
    def total(self) -> int:
        """Gets the total of this FAIRResultCommonScore.


        :return: The total of this FAIRResultCommonScore.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this FAIRResultCommonScore.


        :param total: The total of this FAIRResultCommonScore.
        :type total: int
        """

        self._total = total
