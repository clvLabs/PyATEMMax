#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: AuxSource
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class AuxSource():
    def __init__(self):
        self.input: ATEMConstant = ATEMConstant()


class AuxSourceList(ATEMValueDict[AuxSource]):
    def __init__(self):
        super().__init__(AuxSource, ATEMProtocol.auxChannels)
