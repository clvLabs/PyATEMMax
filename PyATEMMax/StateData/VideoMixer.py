#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: VideoMixer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring


class VideoMixer():
    class Config():
        class ModeFlags():
            def __init__(self): # VideoMixer.Config.ModeFlags
                self.f525i59_94_NTSC: bool = False
                self.f625i_50_PAL: bool = False
                self.f525i59_94_NTSC_16_9: bool = False
                self.f625i_50_PAL_16_9: bool = False
                self.f720p50: bool = False
                self.f720p59_94: bool = False
                self.f1080i50: bool = False
                self.f1080i59_94: bool = False
                self.f1080p23_98: bool = False
                self.f1080p24: bool = False
                self.f1080p25: bool = False
                self.f1080p29_97: bool = False
                self.f1080p50: bool = False
                self.f1080p59_94: bool = False
                self.f2160p23_98: bool = False
                self.f2160p24: bool = False
                self.f2160p25: bool = False
                self.f2160p29_97: bool = False

        def __init__(self): # VideoMixer.Config
            self.modes:VideoMixer.Config.ModeFlags = VideoMixer.Config.ModeFlags()

    def __init__(self): # VideoMixer
        self.config:VideoMixer.Config = VideoMixer.Config()
