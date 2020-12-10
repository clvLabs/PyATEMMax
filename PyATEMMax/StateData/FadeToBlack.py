#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: FadeToBlack
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class FadeToBlack():

    class State():
        def __init__(self):
            self.framesRemaining: int = 0
            self.fullyBlack: bool = False
            self.inTransition: bool = False

    def __init__(self):
        self.rate: int = 0
        self.state: FadeToBlack.State = FadeToBlack.State()


class FadeToBlackList(ATEMValueDict[FadeToBlack]):
    def __init__(self):
        super().__init__(FadeToBlack, ATEMProtocol.mixEffects)
