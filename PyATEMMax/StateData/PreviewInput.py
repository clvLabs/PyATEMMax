#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: PreviewInput
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class PreviewInput():
    def __init__(self):
        self.videoSource: ATEMConstant = ATEMConstant()

class PreviewInputList(ATEMValueDict[PreviewInput]):
    def __init__(self):
        super().__init__(PreviewInput, ATEMProtocol.mixEffects)
