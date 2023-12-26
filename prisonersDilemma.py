#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Prisoner's Dilemma class handling mechanics of the prisoner's dilemma problem.

License: MIT License
"""


class PrisonersDilemma:

    """
    Class variable containing the scoring system for each mode of the
    prisoner's dilemma problem. The system is stored as a `dict` where the
    key is used to select the mode and the value describes the scoring
    system. The value is a list containing four separate tuples of size 2, which
    contain the score for contestant 1 and contestant 2, in that order. The
    list elements follow the following pattern:
    Score for mututal cooperation, score for cooperation of contestant 1 and
    defection for contestant 2, score for defection of contestant 1 and
    cooperation of contestant 2, score for mutual defection.
    """
    modes = {'classic': [(3, 3), (0, 5), (5, 0), (1, 1)]}

    def __init__(self, mode='classic'):
        """
        Constructor of the `PrisonersDilemma` class.

        :param mode:    Key specifying which mode to run the prisoner's
                        dilemma problem in. The key must be included in the
                        `PrisonersDilemma.modes` class variable, otherwise a
                        `KeyError` is raised.
        :type mode:     str
        """
        if mode not in self.modes.keys():
            raise KeyError(f"Mode {mode} is not defined in PrisonersDilemma "
                           f"class variable 'modes'")
        self.selected_mode = self.modes.get(mode)

    def score_round(self, move_contestant_1, move_contestant_2):
        """
        Decides the score, i.e. the points gained for each contestant based
        on their moves.

        :param move_contestant_1:   Boolean indicating whether contestant 1
                                    chooses to cooperate. `True` indicates
                                    cooperation,`False` indicates defection.
        :type move_contestant_1:    bool
        :param move_contestant_2:   Boolean indicating whether contestant 2
                                    chooses to cooperate. `True` indicates
                                    cooperation,`False` indicates defection.
        :type move_contestant_2:    bool
        :return:                    Scores of contestant 1 and contestant 2,
                                    respectively.
        :rtype:                     tuple
        """
        # compare moves of contestants
        if move_contestant_1 | move_contestant_2:
            # both contestants choose to cooperate
            return self.selected_mode[0]
        elif move_contestant_1 and not move_contestant_2:
            # only contestant 1 chooses to cooperate
            return self.selected_mode[1]
        elif not move_contestant_1 and move_contestant_2:
            # only contestant 2 chooses to cooperate
            return self.selected_mode[2]
        else:
            # no contestant chooses to cooperate
            return self.selected_mode[3]

