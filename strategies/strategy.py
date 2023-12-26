#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Abstract strategy class template for specific strategies to inherit from.

License: MIT License
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    descriptor = "This is a placeholder for the description of subclasses."

    @property
    @abstractmethod
    def is_nice(self):
        """
        A property storing whether the strategy is "nice", i.e. whether it can
        defect first.

        :return:    boolean indicating whether strategy is "nice"
        :rtype:     bool
        """
        pass

    @is_nice.setter
    def is_nice(self, new_is_nice):
        """
        Setter for the `is_nice` property.

        Note: It is recommended to leave the body of this setter without
        function, as the `is_nice` property should not be changed at runtime.

        :param new_is_nice: boolean defining whether strategy is
        considered "nice"
        :type new_is_nice:  bool
        :return: None
        """
        pass

    @abstractmethod
    def __init__(self):
        """
        Constructor for the abstract `Strategy` class.
        """
        pass

    @classmethod
    def __repr__(cls):
        """
        Returns the descriptor string of the strategy.

        :return:    descriptor string of the strategy
        :rtype:     String
        """
        return cls.descriptor

    @abstractmethod
    def next_move(self, previous_moves=None, second_contestant_moves=None):
        """
        Returns a boolean indicating whether the strategy will cooperate on the
        next move. `True` indicates cooperation,`False` indicates defection.

        :param previous_moves:          list containing the previous moves of
                                        the contestant applying the strategy.
        :type previous_moves:           list(bool)
        :param second_contestant_moves: list containing the previous moves of
                                        the second contestant.
        :type second_contestant_moves:  list(bool)
        :return:                        boolean indicating whether the strategy
                                        will cooperate on the next move.
        :rtype:                         bool
        """
        pass

