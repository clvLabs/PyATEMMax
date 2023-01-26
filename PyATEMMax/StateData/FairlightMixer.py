#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Fairlight Mixer
Part of the PyATEMMax library.

New implementation of the Fairlight Audio Mixer not included
in the skaarhoj library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMValueDict import ATEMValueDict


class FairlightMixer():
    """Blackmagic ATEM switcher: fairlightAudioMixer state data"""

    # #######################################################################
    #
    #  Class members
    #

    class Config():
        def __init__(self): # FairlightMixer.Config
            self.audioChannels: int = 0
            self.hasMonitor: bool = False


    class Equalizer():
        def __init__(self): # FairlightMixer.Equalizer
            self.enabled: bool = False
            self.gain: int = 0
            self.bandCount: int = 0
            self.band: list[FairlightMixer.Equalizer.Band] = [self.Band()] * 6

        class Band(): # FairlightMixer.Equalizer.Band
            def __init__(self) -> None:
                self.enabled: bool = False
                self.supported_filters: list[ATEMConstant] = []
                self.filter: ATEMConstant = ATEMConstant()
                self.supported_frequency_ranges: list[ATEMConstant] = []
                self.frequency_range: ATEMConstant = ATEMConstant()
                self.frequency: int = 0
                self.gain: float = 0.0
                self.qFactor: float = 0.0


    class Dynamics():
        def __init__(self): # FairlightMixer.Dynamics
            self.enabled: bool = False
            self.makeUpGain: int = 0


    class Input():
        def __init__(self): # FairlightMixer.Input
            self.maxFramesDelay: int = 0
            self.hasStereoSimulation:bool = False
            self.validMixOptions:list[int] = []

            self.framesDelay: int = 0
            self.stereoSimulation: int = 0
            self.gain: float = 0
            self.balance: float = 0.0
            self.volume: float = 0
            self.type: ATEMConstant = ATEMConstant()
            self.mixOption: ATEMConstant = ATEMConstant()

            self.equalizer: FairlightMixer.Equalizer = FairlightMixer.Equalizer()
            self.dynamics: FairlightMixer.Dynamics = FairlightMixer.Dynamics()


    class InputList(ATEMValueDict[Input]):
        def __init__(self): # FairlightMixer.InputList
            super().__init__(FairlightMixer.Input, ATEMProtocol.audioSources)


    class Master():
        def __init__(self): # FairlightMixer.Master
            self.volume: float = 0
            self.followFadeToBlack: bool = False

            self.equalizer: FairlightMixer.Equalizer = FairlightMixer.Equalizer()
            self.dynamics: FairlightMixer.Dynamics = FairlightMixer.Dynamics()


    class Monitor():
        # Future implementation
        pass


    class Levels():
        # Future implementation
        pass


    class Tally():
        # Future implementation
        pass


    def __init__(self): # FairlightMixer
        self.config = FairlightMixer.Config()
        self.input: FairlightMixer.InputList = FairlightMixer.InputList()
        self.master: FairlightMixer.Master = FairlightMixer.Master()

        # Future implementation
        self.monitor = FairlightMixer.Monitor()
        self.tally = FairlightMixer.Tally()
        self.levels: FairlightMixer.Levels = FairlightMixer.Levels()
