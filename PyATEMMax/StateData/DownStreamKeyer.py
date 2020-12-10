#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: DownStreamKeyer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class DownStreamKeyer():
    def __init__(self):
        self.bottom: float = 0.0
        self.clip: float = 0.0
        self.fillSource: ATEMConstant = ATEMConstant()
        self.framesRemaining: int = 0
        self.gain: float = 0.0
        self.inTransition: bool = False
        self.invertKey: bool = False
        self.isAutoTransitioning: bool = False
        self.keySource: ATEMConstant = ATEMConstant()
        self.left: float = 0.0
        self.masked: bool = False
        self.onAir: bool = False
        self.preMultiplied: bool = False
        self.rate: int = 0
        self.right: float = 0.0
        self.tie: bool = False
        self.top: float = 0.0


class DownStreamKeyerList(ATEMValueDict[DownStreamKeyer]):
    def __init__(self):
        super().__init__(DownStreamKeyer, ATEMProtocol.dsks)
