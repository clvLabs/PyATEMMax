#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: ClipPlayer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class ClipPlayer():
    def __init__(self):
        self.atBeginning: bool = False
        self.clipFrame: int = 0
        self.loop: bool = False
        self.playing: bool = False


class ClipPlayerList(ATEMValueDict[ClipPlayer]):
    def __init__(self):
        super().__init__(ClipPlayer, ATEMProtocol.mediaPlayers)
