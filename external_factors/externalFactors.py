#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Abstract strategy class template for external factors influencing the
prisoner's dilemma problem.

License: MIT License
"""

from abc import ABC, abstractmethod

class ExternalFactors(ABC):

    @abstractmethod
    def __init__(self):
        """
        Constructor for the `ExternalFactors` class.
        """
        pass

    @abstractmethod
    def change_perception(self, move, *args):
        """
        Method for changing the perception of a contestant's move in the eyes of
        the second contestant.

        :param move:        move to change perception of
        :type move:         bool
        :param args:        additional arguments to be specified by
                            implementation of method
        :return:            new perception of given move
        :rtype:             bool
        """
        pass

    @abstractmethod
    def change_result(self):
        """
        Method for changing the result of a contestant's move in the eyes of
        both contestants.

        :param move:        move to change result of
        :type move:         bool
        :param args:        additional arguments to be specified by
                            implementation of method
        :return:            new result of given move
        :rtype:             bool
        """
        pass
