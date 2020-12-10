#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: AudioMixer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMValueDict import ATEMValueDict


class AudioMixer():
    """Blackmagic ATEM switcher: audioMixer state data"""

    # #######################################################################
    #
    #  Class members
    #

    class Config():
        def __init__(self): # AudioMixer.Config
            self.audioChannels: int = 0
            self.hasMonitor: bool = False


    class Input():
        def __init__(self): # AudioMixer.Input
            self.balance: float = 0.0
            self.fromMediaPlayer: bool = False
            self.mixOption: ATEMConstant = ATEMConstant()
            self.plugtype: ATEMConstant = ATEMConstant()
            self.type: ATEMConstant = ATEMConstant()
            self.volume: float = 0


    class InputList(ATEMValueDict[Input]):
        def __init__(self): # AudioMixer.InputList
            super().__init__(AudioMixer.Input, ATEMProtocol.audioSources)


    class Levels():
        class Master():
            class Peak():
                def __init__(self): # AudioMixer.Levels.Master.Peak
                    self.left: int = 0
                    self.right: int = 0


            def __init__(self): # AudioMixer.Levels.Master
                self.left: int = 0
                self.right: int = 0
                self.peak = AudioMixer.Levels.Master.Peak()


        class Source():
            class Peak():
                def __init__(self): # AudioMixer.Levels.Source.Peak
                    self.left: int = 0
                    self.right: int = 0


            def __init__(self): # AudioMixer.Levels.Source
                self.left: int = 0
                self.right: int = 0
                self.peak = AudioMixer.Levels.Source.Peak()


        class SourceList(ATEMValueDict[Source]):
            def __init__(self): # AudioMixer.Levels.SourceList
                super().__init__(AudioMixer.Levels.Source, ATEMProtocol.audioSources)


        def __init__(self): # AudioMixer.Levels
            self.master = AudioMixer.Levels.Master()
            self.monitor: int = 0
            self.numSources: int = 0
            self.sources: AudioMixer.Levels.SourceList = AudioMixer.Levels.SourceList()


    class Master():
        def __init__(self): # AudioMixer.Master
            self.volume: float = 0


    class Monitor():
        def __init__(self): # AudioMixer.Monitor
            self.dim: bool = False
            self.monitorAudio: bool = False
            self.mute: bool = False
            self.solo: bool = False
            self.soloInput: ATEMConstant = ATEMConstant()
            self.volume: float = 0


    class Tally():
        class Source():
            def __init__(self): # AudioMixer.Tally.Source
                self.isMixedIn: bool = False


        class SourceList(ATEMValueDict[Source]):
            def __init__(self): # AudioMixer.Tally.SourceList
                super().__init__(AudioMixer.Tally.Source, ATEMProtocol.audioSources)


        def __init__(self): # AudioMixer.Tally
            self.numSources: int = 0
            self.sources: AudioMixer.Tally.SourceList = AudioMixer.Tally.SourceList()


    def __init__(self): # AudioMixer
        self.config = AudioMixer.Config()
        self.input: AudioMixer.InputList = AudioMixer.InputList()
        self.levels: AudioMixer.Levels = AudioMixer.Levels()
        self.master: AudioMixer.Master = AudioMixer.Master()
        self.monitor = AudioMixer.Monitor()
        self.tally = AudioMixer.Tally()
