#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: ProgramInput
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class ProgramInput():
    def __init__(self):
        self.videoSource: ATEMConstant = ATEMConstant()

class ProgramInputList(ATEMValueDict[ProgramInput]):
    def __init__(self):
        super().__init__(ProgramInput, ATEMProtocol.mixEffects)
