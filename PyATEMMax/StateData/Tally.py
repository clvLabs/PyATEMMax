#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Tally
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from typing import List

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class Tally():

    class Flags():
        def __init__(self): # Tally.Flags
            self.program: bool = False
            self.preview: bool = False

        def __str__(self):
            if not self.program and not self.preview:
                return "[]"

            return f"{'[PGM]' if self.program else ''}{'[PVW]' if self.preview else ''}"

        def __format__(self, format_spec: str) -> str:
            return format(str(self), format_spec)


    class FlagsDict(ATEMValueDict[Flags]):
        def __init__(self): # Tally.FlagsDict
            super().__init__(Tally.Flags, ATEMProtocol.videoSources)


    class ByIndex():
        def __init__(self): # Tally.ByIndex
            self.sources: int = 0
            # WARNING: This is a list "by index", we cannot use an ATEMValueDict here...
            self.flags: List[Tally.Flags] = [Tally.Flags() for _ in range(len(ATEMProtocol.videoSources))]


    class SourceDict(ATEMValueDict[ATEMConstant]):
        def __init__(self): # Tally.SourceDict
            super().__init__(ATEMConstant, ATEMProtocol.videoSources)


    class BySource():
        def __init__(self): # Tally.BySource
            self.sources: int = 0
            self.flags: Tally.FlagsDict = Tally.FlagsDict()


    class ChannelConfig():
        def __init__(self): # Tally.ChannelConfig
            self.tallyChannels: int = 0


    def __init__(self): # Tally
        self.byIndex: Tally.ByIndex = Tally.ByIndex()
        self.bySource: Tally.BySource = Tally.BySource()
        self.channelConfig: Tally.ChannelConfig = Tally.ChannelConfig()
