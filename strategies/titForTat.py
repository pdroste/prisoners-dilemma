#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Strategy class for the "Tit for Tat" strategy for the prisoner's dilemma
thought experiment.

License: MIT License
"""

from strategy import Strategy


class TitForTat(Strategy):
    descriptor = "The Tit for Tat strategy always cooperates, unless the " \
                 "other contestant has defected in the previous round in " \
                 "which case it defects itself."

    @property
    def is_nice(self):
        """
        A property storing whether the strategy is "nice", i.e. whether it can
        defect first.

        :return:    boolean indicating whether strategy is "nice"
        :rtype:     bool
        """
        return True

    def __init__(self):
        """
        Constructor for the 'Tit for Tat' strategy class.
        """
        pass

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
        if not second_contestant_moves:
            return True
        else:
            return bool(second_contestant_moves[-1])
