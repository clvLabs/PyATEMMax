#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: MixEffect
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class MixEffect():

    class Config():
        def __init__(self): # MixEffect.Config
            self.keyers: int = 0

    class ConfigList(ATEMValueDict[Config]):
        def __init__(self): # MixEffect.ConfigList
            super().__init__(MixEffect.Config, ATEMProtocol.mixEffects)

    def __init__(self): # MixEffect
        self.config: MixEffect.ConfigList = MixEffect.ConfigList()
