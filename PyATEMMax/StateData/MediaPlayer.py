#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: MediaPlayer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class MediaPlayer():

    class StillFile():
        def __init__(self):
            self.fileName: str = ""
            self.isUsed: bool = False


    class StillFileList(ATEMValueDict[StillFile]):
        def __init__(self):
            super().__init__(MediaPlayer.StillFile, ATEMProtocol.stillBanks)


    class Source():
        def __init__(self):
            self.clipIndex: int = 0
            self.stillIndex: int = 0
            self.type: ATEMConstant = ATEMConstant()


    class SourceList(ATEMValueDict[Source]):
        def __init__(self):
            super().__init__(MediaPlayer.Source, ATEMProtocol.mediaPlayers)


    class ClipSource():
        def __init__(self):
            self.fileName: str = ""
            self.frames: int = 0
            self.isUsed: bool = False


    class ClipSourceList(ATEMValueDict[ClipSource]):
        def __init__(self):
            super().__init__(MediaPlayer.ClipSource, ATEMProtocol.clipBanks)


    class AudioSource():
        def __init__(self):
            self.fileName: str = ""
            self.isUsed: bool = False


    class AudioSourceList(ATEMValueDict[AudioSource]):
        def __init__(self):
            super().__init__(MediaPlayer.AudioSource, ATEMProtocol.clipBanks)


    def __init__(self): # MediaPlayer
        self.clipBanks: int = 0
        self.stillBanks: int = 0
        self.audioSource: MediaPlayer.AudioSourceList = MediaPlayer.AudioSourceList()
        self.clipSource: MediaPlayer.ClipSourceList = MediaPlayer.ClipSourceList()
        self.source: MediaPlayer.SourceList = MediaPlayer.SourceList()
        self.stillFile: MediaPlayer.StillFileList = MediaPlayer.StillFileList()
