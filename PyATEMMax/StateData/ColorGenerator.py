#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: ColorGenerator
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class ColorGenerator():
    def __init__(self):
        self.hue: float = 0.0
        self.luma: float = 0.0
        self.saturation: float = 0.0


class ColorGeneratorList(ATEMValueDict[ColorGenerator]):
    def __init__(self):
        super().__init__(ColorGenerator, ATEMProtocol.colorGenerators)
