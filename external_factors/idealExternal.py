#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Class for ideal external factors with no influence on the prisoner's dilemma
problem.

License: MIT License
"""

from externalFactors import ExternalFactors


class IdealExternal(ExternalFactors):

    def __init__(self):
        pass

    def change_perception(self, move):
        return move

    def change_result(self, move):
        return move

        