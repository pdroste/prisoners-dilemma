#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Contestant class handling the move selection and tracking based on a specific
strategy to the prisoner's dilemma problem.

License: MIT License
"""

from .strategies.strategy import Strategy


class Contestant:

    def __init__(self, selected_strategy: Strategy):
        """
        Constructor for the `Contestant` class.

        :param selected_strategy:   strategy to be used by contestant
        :type selected_strategy:    `Strategy`
        """
        self.strategy = selected_strategy
        self.previous_moves = []

    @property
    def strategy(self):
        """
        Property storing which strategy is used by the contestant.

        :return:    strategy object used by the contestant
        :rtype:     `Strategy`
        """
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy):
        """
        Property setter for strategy to be used by the contestant.

        :type new_strategy:    strategy object to be used by the contestant
        :type:                `Strategy`
        """
        self.__strategy = new_strategy
        print(f"Contest {self} has changed strategy to {new_strategy}.")

    @property
    def previous_moves(self):
        """
        Property storing the previous moves of the contestant.
        `True` indicates cooperation, `False` indicates defection.

        :return:    list of the contestants previous moves
        :rtype:     list(bool)
        """
        return self.__previous_moves

    @previous_moves.setter
    def previous_moves(self, new_previous_moves):
        """
        Property setter for the list of previous moves to be used by the
        contestant.

        :param new_previous_moves:  list of new previous moves
        :type new_previous_moves:   list(bool)
        """
        if not new_previous_moves:
            self.__previous_moves = []
            print(f"Contestant {self} has reset their previous moves.")
        elif len(self.previous_moves) == len(new_previous_moves):
            self.__previous_moves = new_previous_moves
            print(f"Contestant {self} has changed their previous moves to:\n"
                  f"{new_previous_moves}")
        else:
            raise ValueError(f"New set of previous moves must either be empty "
                             f"(move reset) or contain the same number of "
                             f"moves as the previous set of moves (move "
                             f"exchange).")

    def next_move(self, second_contestant_moves=None):
        """
        Returns the next move chosen by the contestant.

        :param second_contestant_moves: list containing the previous moves of
                                        the second contestant.
        :type second_contestant_moves:  list(bool)
        :return:                        boolean indicating the next move of
                                        the contestant
        :rtype:                         bool
        """
        next_move = self.strategy.next_move(self.previous_moves,
                                            second_contestant_moves)
        self.track_move(next_move)
        return next_move

    def track_move(self, new_move):
        """
        Adds a move to the list of previous moves.
        :param new_move:    new move to be added to the list of previous moves.
        :return:            bool
        """
        self.previous_moves.append(new_move)

    def strategy_is_nice(self):
        """
        Returns whether the strategy used by the contestant is "nice",
        i.e. whether it can defect first.

        :return:    boolean indicating whether strategy is "nice"
        :rtype:     bool
        """
        return self.strategy.is_nice
