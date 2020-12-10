#!/usr/bin/env python3
# coding: utf-8
"""
ATEMSwitcherState: Blackmagic ATEM switcher state data class.
Part of the PyATEMMax library.
"""

# pylint: disable=wildcard-import, unused-wildcard-import

from .StateData import *


class ATEMSwitcherState():
    """Blackmagic ATEM switcher state data class

    This class is a port of Skårhøj's ATEMmax class.
    """

    def __init__(self):
        # Data
        self.atemModel: str = ""
        self.audioMixer: AudioMixer = AudioMixer()
        self.auxSource: AuxSourceList = AuxSourceList()
        self.cameraControl: CameraControlList = CameraControlList()
        self.clipPlayer: ClipPlayerList = ClipPlayerList()
        self.colorGenerator: ColorGeneratorList = ColorGeneratorList()
        self.downConverter:DownConverter = DownConverter()
        self.downstreamKeyer: DownStreamKeyerList = DownStreamKeyerList()
        self.fadeToBlack: FadeToBlackList = FadeToBlackList()
        self.inputProperties: InputPropertiesList = InputPropertiesList()
        self.key: KeyList = KeyList()
        self.keyer: KeyerList = KeyerList()
        self.lastStateChange = LastStateChange()
        self.macro = Macro()
        self.mediaPlayer = MediaPlayer()
        self.mediaPoolStorage = MediaPoolStorage()
        self.mixEffect: MixEffect = MixEffect()
        self.multiViewer: MultiViewer = MultiViewer()
        self.power: Power = Power()
        self.previewInput: PreviewInputList = PreviewInputList()
        self.programInput: ProgramInputList = ProgramInputList()
        self.protocolVersion: ProtocolVersion = ProtocolVersion()
        self.superSource: SuperSource = SuperSource()
        self.tally: Tally = Tally()
        self.topology: Topology = Topology()
        self.transition: TransitionList = TransitionList()
        self.videoMixer: VideoMixer = VideoMixer()
        self.videoMode: VideoMode = VideoMode()
        self.warningText: str = ""
