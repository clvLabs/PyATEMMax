#!/usr/bin/env python3
# coding: utf-8
"""
ATEMSetterMethods: Blackmagic ATEM switcher setter methods.
Part of the PyATEMMax library.
Methods do keep the order in https://www.skaarhoj.com/fileadmin/BMDPROTOCOL.html
"""

# pylint: disable=too-many-lines, wildcard-import, unused-wildcard-import, protected-access
# pyright: reportPrivateUsage=false, reportUnusedFunction=false, reportUnboundVariable=false

from typing import Union

from .ATEMUtils import mapValue
from .ATEMProtocolEnums import *

# --------------------------------------------------
# This is a trick to have type hints from classes
#  imported without forcing a cyclic import on runtime.
#
# From: https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
#

_____LINTER_TRICK_____ = None
if _____LINTER_TRICK_____:
    from .ATEMProtocol import ATEMProtocol
    from .ATEMSwitcherState import ATEMSwitcherState
    from .ATEMConnectionManager import ATEMConnectionManager
else:
    ATEMProtocol = type(int)
    ATEMSwitcherState = type(int)
    ATEMConnectionManager = type(int)

# --------------------------------------------------


class ATEMSetterMethods():
    """Blackmagic ATEM switcher setter methods

    This class is a port of S kårhøj's ATEMmax class.
    """

    def __init__(self):
        self.switcher: ATEMConnectionManager
        self.data: ATEMSwitcherState
        self.atem: ATEMProtocol


    # #######################################################################
    #
    #  Setter methods
    #

    def setDownConverterMode(self, mode: Union[ATEMConstant, str, int]) -> None:
        """Set Down Converter Mode

        Args:
            mode: see ATEMDownConverterModes
        """

        mode_val = self.atem.downConverterModes[mode].value

        self.switcher._prepareCommandPacket("CDcO", 4)
        self.switcher._outBuf.setU8(0, mode_val)
        self.switcher._finishCommandPacket()


    def setVideoModeFormat(self, format_: Union[ATEMConstant, str, int]) -> None:
        """Set Video Mode Format

        Args:
            format_: see ATEMVideoModeFormats
        """

        format_val = self.atem.videoModeFormats[format_].value

        self.switcher._prepareCommandPacket("CVdM", 4)
        self.switcher._outBuf.setU8(0, format_val)
        self.switcher._finishCommandPacket()

    def setInputLongName(self, videoSource: Union[ATEMConstant, str, int], longName: str) -> None:
        """Set Input Properties Long Name

        Args:
            videoSource: see ATEMVideoSources
            longName(str): long name
        """

        videoSource_val = self.atem.getVideoSrc(videoSource)

        indexMatch:bool = self.switcher._outBuf.getU16(2) == videoSource_val

        self.switcher._prepareCommandPacket("CInL", 32, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._outBuf.setString(4, 20, longName)
        self.switcher._finishCommandPacket()


    def setInputShortName(self, videoSource: Union[ATEMConstant, str, int], shortName: str) -> None:
        """Set Input Properties Short Name

        Args:
            videoSource: see ATEMVideoSources
            shortName(str): short name
        """

        videoSource_val = self.atem.getVideoSrc(videoSource)

        indexMatch:bool = self.switcher._outBuf.getU16(2) == videoSource_val

        self.switcher._prepareCommandPacket("CInL", 32, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._outBuf.setString(24, 4, shortName)
        self.switcher._finishCommandPacket()


    def setInputExternalPortType(self, videoSource: Union[ATEMConstant, str, int], externalPortType: Union[ATEMConstant, str, int]) -> None:
        """Set Input Properties External Port Type

        Args:
            videoSource: see ATEMVideoSources
            externalPortType: see ATEMExternalPortTypes
        """

        videoSource_val = self.atem.getVideoSrc(videoSource)
        externalPortType_val = self.atem.externalPortTypes[externalPortType].value

        indexMatch:bool = self.switcher._outBuf.getU16(2) == videoSource_val

        self.switcher._prepareCommandPacket("CInL", 32, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._outBuf.setU16(28, externalPortType_val)
        self.switcher._finishCommandPacket()


    def setMultiViewerPropertiesLayout(self, multiViewer: Union[ATEMConstant, str, int], layout: Union[ATEMConstant, str, int]) -> None:
        """Set MultiViewer Properties Layout

        Args:
            videoSource: see ATEMVideoSources
            layout: see ATEMMultiViewerLayouts
        """

        multiViewer_val = self.atem.multiViewers[multiViewer].value
        layout_val = self.atem.multiViewerLayouts[layout].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == multiViewer_val

        self.switcher._prepareCommandPacket("CMvP", 4, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)     # Bit 0: Layout OFF
        self.switcher._outBuf.setU8(1, multiViewer_val)
        self.switcher._outBuf.setU8(2, layout_val)
        self.switcher._finishCommandPacket()


    def setMultiViewerInputVideoSource(self, multiViewer: Union[ATEMConstant, str, int], window: Union[ATEMConstant, str, int], videoSource: Union[ATEMConstant, str, int]) -> None:
        """Set MultiViewer Properties Video Source

        Args:
            multiViewer: see ATEMMultiViewers
            window: see ATEMWindows
            videoSource: see ATEMVideoSources
        """

        multiViewer_val = self.atem.multiViewers[multiViewer].value
        window_val = self.atem.windows[window].value
        videoSource_val = self.atem.getVideoSrc(videoSource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == multiViewer_val and \
                    self.switcher._outBuf.getU8(1) == window_val

        self.switcher._prepareCommandPacket("CMvI", 4, indexMatch)
        self.switcher._outBuf.setU8(0, multiViewer_val)
        self.switcher._outBuf.setU8(1, window_val)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._finishCommandPacket()


    def setProgramInputVideoSource(self, mE: Union[ATEMConstant, str, int], videoSource: Union[ATEMConstant, str, int]) -> None:
        """Set Program Input Video Source

        Args:
            mE: see ATEMMixEffects
            videoSource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        videoSource_val = self.atem.getVideoSrc(videoSource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val

        self.switcher._prepareCommandPacket("CPgI", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._finishCommandPacket()


    def setPreviewInputVideoSource(self, mE: Union[ATEMConstant, str, int], videoSource: Union[ATEMConstant, str, int]) -> None:
        """Set Preview Input Video Source

        Args:
            mE: see ATEMMixEffects
            videoSource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        videoSource_val = self.atem.getVideoSrc(videoSource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val

        self.switcher._prepareCommandPacket("CPvI", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU16(2, videoSource_val)
        self.switcher._finishCommandPacket()


    def setTransitionStyle(self, mE: Union[ATEMConstant, str, int], style: Union[ATEMConstant, str, int]) -> None:
        """Set Transition Style

        Args:
            mE: see ATEMMixEffects
            style: see ATEMTransitionStyles
        """

        mE_val = self.atem.mixEffects[mE].value
        style_val = self.atem.transitionStyles[style].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val

        self.switcher._prepareCommandPacket("CTTp", 4, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)     # Bit 0: Transition Style OFF
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, style_val)
        self.switcher._finishCommandPacket()


    def setTransitionNextTransition(self, mE: Union[ATEMConstant, str, int], nextTransition: int) -> None:
        """Set Transition Style Next Transition

        Args:
            mE: see ATEMMixEffects
            nextTransition: see ATEMTransitionStyles
        """

        mE_val = self.atem.mixEffects[mE].value
        nextTransition_val = self.atem.transitionStyles[nextTransition].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val

        self.switcher._prepareCommandPacket("CTTp", 4, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)     # Bit 0: Transition Style ON
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(3, nextTransition_val)
        self.switcher._finishCommandPacket()


    def setTransitionPreviewEnabled(self, mE: Union[ATEMConstant, str, int], enabled: bool) -> None:
        """Set Transition Preview Enabled

        Args:
            mE: see ATEMMixEffects
            enabled (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val

        self.switcher._prepareCommandPacket("CTPr", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, enabled)
        self.switcher._finishCommandPacket()


    def setTransitionPosition(self, mE: Union[ATEMConstant, str, int], position: int) -> None:
        """Set Transition Preview Enabled

        Args:
            mE: see ATEMMixEffects
            position (int): 0-9999
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val

        self.switcher._prepareCommandPacket("CTPs", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU16(2, position)
        self.switcher._finishCommandPacket()


    def setTransitionMixRate(self, mE: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Transition Mix Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val

        self.switcher._prepareCommandPacket("CTMx", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, rate)
        self.switcher._finishCommandPacket()


    def setTransitionDipRate(self, mE: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Transition Dip Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val

        self.switcher._prepareCommandPacket("CTDp", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, rate)
        self.switcher._finishCommandPacket()


    def setTransitionDipInput(self, mE: Union[ATEMConstant, str, int], input_: Union[ATEMConstant, str, int]) -> None:
        """Set Transition Dip Input

        Args:
            mE: see ATEMMixEffects
            input_: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        input_val = self.atem.getVideoSrc(input_)

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val

        self.switcher._prepareCommandPacket("CTDp", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU16(4, input_val)
        self.switcher._finishCommandPacket()


    def setTransitionWipeRate(self, mE: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Transition Wipe Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(3, rate)
        self.switcher._finishCommandPacket()


    def setTransitionWipePattern(self, mE: Union[ATEMConstant, str, int], pattern: Union[ATEMConstant, str, int]) -> None:
        """Set Transition Wipe Pattern

        Args:
            mE: see ATEMMixEffects
            pattern: see ATEMPatternStyles
        """

        mE_val = self.atem.mixEffects[mE].value
        pattern_val = self.atem.patternStyles[pattern]

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 1)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(4, pattern_val)
        self.switcher._finishCommandPacket()


    def setTransitionWipeWidth(self, mE: Union[ATEMConstant, str, int], width: float) -> None:
        """Set Transition Wipe Width

        Args:
            mE: see ATEMMixEffects
            width (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(6, int(width*100))
        self.switcher._finishCommandPacket()


    def setTransitionWipeFillSource(self, mE: Union[ATEMConstant, str, int], fillSource: Union[ATEMConstant, str, int]) -> None:
        """Set Transition Wipe Fill Source

        Args:
            mE: see ATEMMixEffects
            fillSource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        fillSource_val = self.atem.getVideoSrc(fillSource)

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(8, fillSource_val)
        self.switcher._finishCommandPacket()


    def setTransitionWipeSymmetry(self, mE: Union[ATEMConstant, str, int], symmetry: float) -> None:
        """Set Transition Wipe Symmetry

        Args:
            mE: see ATEMMixEffects
            symmetry (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 4)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(10, int(symmetry*100))
        self.switcher._finishCommandPacket()


    def setTransitionWipeSoftness(self, mE: Union[ATEMConstant, str, int], softness: float) -> None:
        """Set Transition Wipe Softness

        Args:
            mE: see ATEMMixEffects
            softness (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 5)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(12, int(softness*100))
        self.switcher._finishCommandPacket()


    def setTransitionWipePositionX(self, mE: Union[ATEMConstant, str, int], positionX: float) -> None:
        """Set Transition Wipe Position X

        Args:
            mE: see ATEMMixEffects
            positionX (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 6)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(14, int(positionX*10000))
        self.switcher._finishCommandPacket()


    def setTransitionWipePositionY(self, mE: Union[ATEMConstant, str, int], positionY: float) -> None:
        """Set Transition Wipe Position Y

        Args:
            mE: see ATEMMixEffects
            positionY (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 7)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(16, int(positionY*10000))
        self.switcher._finishCommandPacket()


    def setTransitionWipeReverse(self, mE: Union[ATEMConstant, str, int], reverse: bool) -> None:
        """Set Transition Wipe Reverse

        Args:
            mE: see ATEMMixEffects
            reverse (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 8)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(18, reverse)
        self.switcher._finishCommandPacket()


    def setTransitionWipeFlipFlop(self, mE: Union[ATEMConstant, str, int], flipFlop: bool) -> None:
        """Set Transition Wipe FlipFlop

        Args:
            mE: see ATEMMixEffects
            flipFlop (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTWp", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 9)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(19, flipFlop)
        self.switcher._finishCommandPacket()


    def setTransitionDVERate(self, mE: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Transition DVE Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(3, rate)
        self.switcher._finishCommandPacket()


    def setTransitionDVEStyle(self, mE: Union[ATEMConstant, str, int], style: Union[ATEMConstant, str, int]) -> None:
        """Set Transition DVE Style

        Args:
            mE: see ATEMMixEffects
            style: see ATEMDVETransitionStyles
        """

        mE_val = self.atem.mixEffects[mE].value
        style_val = self.atem.dVETransitionStyles[style].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(5, style_val)
        self.switcher._finishCommandPacket()


    def setTransitionDVEFillSource(self, mE: Union[ATEMConstant, str, int], fillSource: Union[ATEMConstant, str, int]) -> None:
        """Set Transition DVE Fill Source

        Args:
            mE: see ATEMMixEffects
            fillSource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        fillSource_val = self.atem.getVideoSrc(fillSource)

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(6, fillSource_val)
        self.switcher._finishCommandPacket()


    def setTransitionDVEKeySource(self, mE: Union[ATEMConstant, str, int], keySource: Union[ATEMConstant, str, int]) -> None:
        """Set Transition DVE Key Source

        Args:
            mE: see ATEMMixEffects
            keySource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        keySource_val = self.atem.getVideoSrc(keySource)

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 4)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(8, keySource_val)
        self.switcher._finishCommandPacket()


    def setTransitionDVEEnableKey(self, mE: Union[ATEMConstant, str, int], enableKey: bool) -> None:
        """Set Transition DVE Enable Key

        Args:
            mE: see ATEMMixEffects
            enableKey (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 5)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(10, enableKey)
        self.switcher._finishCommandPacket()


    def setTransitionDVEPreMultiplied(self, mE: Union[ATEMConstant, str, int], preMultiplied: bool) -> None:
        """Set Transition DVE Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            preMultiplied (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 6)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(11, preMultiplied)
        self.switcher._finishCommandPacket()


    def setTransitionDVEClip(self, mE: Union[ATEMConstant, str, int], clip: float) -> None:
        """Set Transition DVE Clip

        Args:
            mE: see ATEMMixEffects
            clip (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 7)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(12, int(clip*10))
        self.switcher._finishCommandPacket()


    def setTransitionDVEGain(self, mE: Union[ATEMConstant, str, int], gain: float) -> None:
        """Set Transition DVE Gain

        Args:
            mE: see ATEMMixEffects
            gain (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 8)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(14, int(gain*10))
        self.switcher._finishCommandPacket()


    def setTransitionDVEInvertKey(self, mE: Union[ATEMConstant, str, int], invertKey: bool) -> None:
        """Set Transition DVE Invert Key

        Args:
            mE: see ATEMMixEffects
            invertKey (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 9)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(16, invertKey)
        self.switcher._finishCommandPacket()


    def setTransitionDVEReverse(self, mE: Union[ATEMConstant, str, int], reverse: bool) -> None:
        """Set Transition DVE Reverse

        Args:
            mE: see ATEMMixEffects
            reverse (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 10)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(17, reverse)
        self.switcher._finishCommandPacket()


    def setTransitionDVEFlipFlop(self, mE: Union[ATEMConstant, str, int], flipFlop: bool) -> None:
        """Set Transition DVE FlipFlop

        Args:
            mE: see ATEMMixEffects
            flipFlop (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTDv", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 11)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(18, flipFlop)
        self.switcher._finishCommandPacket()


    def setTransitionStingerSource(self, mE: Union[ATEMConstant, str, int], source: Union[ATEMConstant, str, int]) -> None:
        """Set Transition Stinger Source

        Args:
            mE: see ATEMMixEffects
            source: see ATEMMediaPlayers
        """

        mE_val = self.atem.mixEffects[mE].value
        source_val = self.atem.mediaPlayers[source].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(3, source_val)
        self.switcher._finishCommandPacket()


    def setTransitionStingerPreMultiplied(self, mE: Union[ATEMConstant, str, int], preMultiplied: bool) -> None:
        """Set Transition Stinger Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            preMultiplied (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 1)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(4, preMultiplied)
        self.switcher._finishCommandPacket()


    def setTransitionStingerClip(self, mE: Union[ATEMConstant, str, int], clip: float) -> None:
        """Set Transition Stinger Clip

        Args:
            mE: see ATEMMixEffects
            clip (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(6, int(clip*10))
        self.switcher._finishCommandPacket()


    def setTransitionStingerGain(self, mE: Union[ATEMConstant, str, int], gain: float) -> None:
        """Set Transition Stinger Gain

        Args:
            mE: see ATEMMixEffects
            gain (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(8, int(gain*10))
        self.switcher._finishCommandPacket()


    def setTransitionStingerInvertKey(self, mE: Union[ATEMConstant, str, int], invertKey: bool) -> None:
        """Set Transition Stinger Invert Key

        Args:
            mE: see ATEMMixEffects
            invertKey (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 4)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU8(10, invertKey)
        self.switcher._finishCommandPacket()


    def setTransitionStingerPreRoll(self, mE: Union[ATEMConstant, str, int], preRoll: int) -> None:
        """Set Transition Stinger Pre Roll

        Args:
            mE: see ATEMMixEffects
            preRoll (int): frames
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 5)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(12, preRoll)
        self.switcher._finishCommandPacket()


    def setTransitionStingerClipDuration(self, mE: Union[ATEMConstant, str, int], clipDuration: int) -> None:
        """Set Transition Stinger Clip Duration

        Args:
            mE: see ATEMMixEffects
            clipDuration (int): frames
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 6)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(14, clipDuration)
        self.switcher._finishCommandPacket()


    def setTransitionStingerTriggerPoint(self, mE: Union[ATEMConstant, str, int], triggerPoint: int) -> None:
        """Set Transition Stinger Trigger Point

        Args:
            mE: see ATEMMixEffects
            triggerPoint (int): frames
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 7)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(16, triggerPoint)
        self.switcher._finishCommandPacket()


    def setTransitionStingerMixRate(self, mE: Union[ATEMConstant, str, int], mixRate: int) -> None:
        """Set Transition Stinger Mix Rate

        Args:
            mE: see ATEMMixEffects
            mixRate (int): frames
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(2) == mE_val

        self.switcher._prepareCommandPacket("CTSt", 20, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 8)
        self.switcher._outBuf.setU8(2, mE_val)
        self.switcher._outBuf.setU16(18, mixRate)
        self.switcher._finishCommandPacket()


    def setKeyerOnAirEnabled(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], enabled: bool) -> None:
        """Set Keyer On Air Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            enabled (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val and \
                    self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CKOn", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU8(2, enabled)
        self.switcher._finishCommandPacket()


    def setKeyerType(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], type_: Union[ATEMConstant, str, int]) -> None:
        """Set Key Type Type

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            type_: see ATEMKeyerTypes
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        type_val = self.atem.keyerTypes[type_].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKTp", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(3, type_val)
        self.switcher._finishCommandPacket()


    def setKeyerFlyEnabled(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], flyEnabled: bool) -> None:
        """Set Key Type Fly Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            flyEnabled (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKTp", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(4, flyEnabled)
        self.switcher._finishCommandPacket()


    def setKeyerMasked(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], masked: bool) -> None:
        """Set Key Mask Masked

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            masked (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKMs", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(3, masked)
        self.switcher._finishCommandPacket()


    def setKeyerTop(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], top: float) -> None:
        """Set Key Mask Top

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            top (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKMs", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8Flag(3, 0)   # Masked = True
        self.switcher._outBuf.setS16(4, int(top*1000))
        self.switcher._finishCommandPacket()


    def setKeyerBottom(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], bottom: float) -> None:
        """Set Key Mask Bottom

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKMs", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setS16(6, int(bottom*1000))
        self.switcher._finishCommandPacket()


    def setKeyerLeft(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], left: float) -> None:
        """Set Key Mask Left

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            left (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKMs", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)

        value = int(mapValue(left, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(8, value)

        self.switcher._finishCommandPacket()


    def setKeyerRight(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], right: float) -> None:
        """Set Key Mask Right

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            right (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKMs", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 4)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)

        value = int(mapValue(right, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(10, value)

        self.switcher._finishCommandPacket()


    def setKeyerFillSource(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], fillSource: Union[ATEMConstant, str, int]) -> None:
        """Set Key Fill Fill Source

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            fillSource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        fillSource_val = self.atem.getVideoSrc(fillSource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val and \
                    self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CKeF", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(2, fillSource_val)
        self.switcher._finishCommandPacket()


    def setKeyerKeySource(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], keySource: Union[ATEMConstant, str, int]) -> None:
        """Set Key Cut Key Source

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keySource: see ATEMVideoSources
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        keySource_val = self.atem.getVideoSrc(keySource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val and \
                    self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CKeC", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(2, keySource_val)
        self.switcher._finishCommandPacket()


    def setKeyLumaPreMultiplied(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], preMultiplied: bool) -> None:
        """Set Key Luma Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            preMultiplied (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKLm", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(3, preMultiplied)
        self.switcher._finishCommandPacket()


    def setKeyLumaClip(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], clip: float) -> None:
        """Set Key Luma Clip

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            clip (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKLm", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(4, int(clip*10))
        self.switcher._finishCommandPacket()


    def setKeyLumaGain(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], gain: float) -> None:
        """Set Key Luma Gain

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            gain (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKLm", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(6, int(gain*10))
        self.switcher._finishCommandPacket()


    def setKeyLumaInvertKey(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], invertKey: bool) -> None:
        """Set Key Luma Invert Key

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            invertKey (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKLm", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(8, invertKey)
        self.switcher._finishCommandPacket()


    def setKeyChromaHue(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], hue: float) -> None:
        """Set Key Chroma Hue

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            hue (float): 0.0-359.9 (degrees)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKCk", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(4, int(hue*10))
        self.switcher._finishCommandPacket()


    def setKeyChromaGain(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], gain: float) -> None:
        """Set Key Chroma Gain

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            gain (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKCk", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(6, int(gain*10))
        self.switcher._finishCommandPacket()


    def setKeyChromaYSuppress(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], ySuppress: float) -> None:
        """Set Key Chroma Y Suppress

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            ySuppress (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKCk", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(8, int(ySuppress*10))
        self.switcher._finishCommandPacket()


    def setKeyChromaLift(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], lift: float) -> None:
        """Set Key Chroma Lift

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lift (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKCk", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(10, int(lift*10))
        self.switcher._finishCommandPacket()


    def setKeyChromaNarrow(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], narrow: bool) -> None:
        """Set Key Chroma Narrow

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            narrow (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKCk", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 4)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(12, narrow)
        self.switcher._finishCommandPacket()


    def setKeyPatternPattern(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], pattern: Union[ATEMConstant, str, int]) -> None:
        """Set Key Pattern Pattern

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            pattern: see ATEMPatternStyles
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        pattern_val = self.atem.patternStyles[pattern].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(3, pattern_val)
        self.switcher._finishCommandPacket()


    def setKeyPatternSize(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], size: float) -> None:
        """Set Key Pattern Size

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            size (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(4, int(size*100))
        self.switcher._finishCommandPacket()


    def setKeyPatternSymmetry(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], symmetry: float) -> None:
        """Set Key Pattern Symmetry

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            symmetry (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(6, int(symmetry*100))
        self.switcher._finishCommandPacket()


    def setKeyPatternSoftness(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], softness: float) -> None:
        """Set Key Pattern Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            softness (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(8, int(softness*100))
        self.switcher._finishCommandPacket()


    def setKeyPatternPositionX(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], positionX: float) -> None:
        """Set Key Pattern Position X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionX (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 4)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(10, int(positionX*10000))
        self.switcher._finishCommandPacket()


    def setKeyPatternPositionY(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], positionY: float) -> None:
        """Set Key Pattern Position Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionY (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 5)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU16(12, int(positionY*10000))
        self.switcher._finishCommandPacket()


    def setKeyPatternInvertPattern(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], invertPattern: bool) -> None:
        """Set Key Pattern Invert Pattern

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            invertPattern (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("CKPt", 16, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 6)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(14, invertPattern)
        self.switcher._finishCommandPacket()


    def setKeyDVESizeX(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], sizeX: float) -> None:
        """Set Key DVE Size X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            sizeX (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        sizeX_val = int(sizeX*1000)

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 0)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(8, ((sizeX_val>>24) & 0xFF))
        self.switcher._outBuf.setU8(9, ((sizeX_val>>16) & 0xFF))
        self.switcher._outBuf.setU8(10, ((sizeX_val>>8) & 0xFF))
        self.switcher._outBuf.setU8(11, (sizeX_val & 0xFF))
        self.switcher._finishCommandPacket()


    def setKeyDVESizeY(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], sizeY: float) -> None:
        """Set Key DVE Size Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            sizeY (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        sizeY_val = int(sizeY*1000)

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 1)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(12, ((sizeY_val>>24) & 0xFF))
        self.switcher._outBuf.setU8(13, ((sizeY_val>>16) & 0xFF))
        self.switcher._outBuf.setU8(14, ((sizeY_val>>8) & 0xFF))
        self.switcher._outBuf.setU8(15, (sizeY_val & 0xFF))
        self.switcher._finishCommandPacket()


    def setKeyDVEPositionX(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], positionX: float) -> None:
        """Set Key DVE Position X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionX (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        positionX_val = int(positionX*1000)

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 2)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(16, ((positionX_val>>24) & 0xFF))
        self.switcher._outBuf.setU8(17, ((positionX_val>>16) & 0xFF))
        self.switcher._outBuf.setU8(18, ((positionX_val>>8) & 0xFF))
        self.switcher._outBuf.setU8(19, (positionX_val & 0xFF))
        self.switcher._finishCommandPacket()


    def setKeyDVEPositionY(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], positionY: float) -> None:
        """Set Key DVE Position Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionY (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        positionY_val = int(positionY*1000)

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 3)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(20, ((positionY_val>>24) & 0xFF))
        self.switcher._outBuf.setU8(21, ((positionY_val>>16) & 0xFF))
        self.switcher._outBuf.setU8(22, ((positionY_val>>8) & 0xFF))
        self.switcher._outBuf.setU8(23, (positionY_val & 0xFF))
        self.switcher._finishCommandPacket()


    def setKeyDVERotation(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], rotation: float) -> None:
        """Set Key DVE Rotation

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            rotation (float): 0.0-359.9 (degrees)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        rotation_val = int(rotation*1000)

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 4)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(24, ((rotation_val>>24) & 0xFF))
        self.switcher._outBuf.setU8(25, ((rotation_val>>16) & 0xFF))
        self.switcher._outBuf.setU8(26, ((rotation_val>>8) & 0xFF))
        self.switcher._outBuf.setU8(27, (rotation_val & 0xFF))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderEnabled(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderEnabled: bool) -> None:
        """Set Key DVE Border Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderEnabled (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 5)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(28, borderEnabled)
        self.switcher._finishCommandPacket()


    def setKeyDVEShadow(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], shadow: bool) -> None:
        """Set Key DVE Shadow

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            shadow (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 6)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(29, shadow)
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderBevel(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderBevel: Union[ATEMConstant, str, int]) -> None:
        """Set Key DVE Border Bevel

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevel: see ATEMBorderBevels
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        borderBevel_val = self.atem.borderBevels[borderBevel].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(3, 7)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(30, borderBevel_val)
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderOuterWidth(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderOuterWidth: float) -> None:
        """Set Key DVE Border Outer Width

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOuterWidth (float): 0.0-16.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 0)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(32, int(borderOuterWidth*100))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderInnerWidth(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderInnerWidth: float) -> None:
        """Set Key DVE Border Inner Width

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderInnerWidth (float): 0.0-16.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 1)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(34, int(borderInnerWidth*100))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderOuterSoftness(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderOuterSoftness: int) -> None:
        """Set Key DVE Border Outer Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOuterSoftness (int): 0-100 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 2)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(36, borderOuterSoftness)
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderInnerSoftness(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderInnerSoftness: int) -> None:
        """Set Key DVE Border Inner Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderInnerSoftness (int): 0-100 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 3)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(37, borderInnerSoftness)
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderBevelSoftness(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderBevelSoftness: float) -> None:
        """Set Key DVE Border Bevel Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevelSoftness (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 4)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(38, int(borderBevelSoftness*100))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderBevelPosition(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderBevelPosition: float) -> None:
        """Set Key DVE Border Bevel Position

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevelPosition (float): 0.0-1.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 5)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(39, int(borderBevelPosition*100))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderOpacity(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderOpacity: int) -> None:
        """Set Key DVE Border Opacity

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOpacity (int): 0-100 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 6)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(40, borderOpacity)
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderHue(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderHue: float) -> None:
        """Set Key DVE Border Hue

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderHue (float): 0.0-359.9 (degrees)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(2, 7)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(42, int(borderHue*10))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderSaturation(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderSaturation: float) -> None:
        """Set Key DVE Border Saturation

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderSaturation (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(44, int(borderSaturation*10))
        self.switcher._finishCommandPacket()


    def setKeyDVEBorderLuma(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], borderLuma: float) -> None:
        """Set Key DVE Border Luma

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderLuma (float): 0.0-100.0 (%)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 1)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(46, int(borderLuma*10))
        self.switcher._finishCommandPacket()


    def setKeyDVELightSourceDirection(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], lightSourceDirection: float) -> None:
        """Set Key DVE Light Source Direction

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lightSourceDirection (float): 0.0-359.9 (degrees)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(48, int(lightSourceDirection*10))
        self.switcher._finishCommandPacket()


    def setKeyDVELightSourceAltitude(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], lightSourceAltitude: int) -> None:
        """Set Key DVE Light Source Altitude

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lightSourceAltitude (int): 10-100
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(50, lightSourceAltitude)
        self.switcher._finishCommandPacket()


    def setKeyDVEMasked(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], masked: bool) -> None:
        """Set Key DVE Masked

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            masked (bool): On/Off
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 4)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(51, masked)
        self.switcher._finishCommandPacket()


    def setKeyDVETop(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], top: float) -> None:
        """Set Key DVE Top

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            top (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 5)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(52, int(top*1000))
        self.switcher._finishCommandPacket()


    def setKeyDVEBottom(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], bottom: float) -> None:
        """Set Key DVE Bottom

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 6)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU16(54, int(bottom*1000))
        self.switcher._finishCommandPacket()


    def setKeyDVELeft(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], left: float) -> None:
        """Set Key DVE Left

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            left (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 7)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)

        value = int(mapValue(left, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(56, value)

        self.switcher._finishCommandPacket()


    def setKeyDVERight(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], right: float) -> None:
        """Set Key DVE Right

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            right (float): -9.0-9.0
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)

        value = int(mapValue(right, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(58, value)

        self.switcher._finishCommandPacket()


    def setKeyDVERate(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Key DVE Rate

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers-4
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(4) == mE_val and \
                    self.switcher._outBuf.getU8(5) == keyer_val

        self.switcher._prepareCommandPacket("CKDV", 64, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(4, mE_val)
        self.switcher._outBuf.setU8(5, keyer_val)
        self.switcher._outBuf.setU8(60, rate)
        self.switcher._finishCommandPacket()


    def setKeyerFlyKeyFrame(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], keyFrame: Union[ATEMConstant, str, int]) -> None:
        """Set Keyer Fly Key Frame

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keyFrame: see ATEMKeyFrames
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        keyframe_val = self.atem.keyFrames[keyFrame].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == mE_val and \
                    self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("SFKF", 4, indexMatch)
        self.switcher._outBuf.setU8(0, mE_val)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU8(2, keyframe_val)
        self.switcher._finishCommandPacket()


    def setRunFlyingKeyKeyFrame(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], keyFrame: Union[ATEMConstant, str, int]) -> None:
        """Set Run Flying Key Key Frame

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keyFrame: see ATEMKeyFrames
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value
        keyframe_val = self.atem.keyFrames[keyFrame].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("RFlK", 8, indexMatch)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(4, keyframe_val)
        self.switcher._finishCommandPacket()


    def setRunFlyingKeyRuntoInfiniteindex(self, mE: Union[ATEMConstant, str, int], keyer: Union[ATEMConstant, str, int], runtoInfiniteindex: int) -> None:
        """Set Run Flying Key Run-to-Infinite-index

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyerser 1-4
            runtoInfiniteindex (int): index
        """

        mE_val = self.atem.mixEffects[mE].value
        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val and \
                    self.switcher._outBuf.getU8(2) == keyer_val

        self.switcher._prepareCommandPacket("RFlK", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, keyer_val)
        self.switcher._outBuf.setU8(5, runtoInfiniteindex)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerFillSource(self, keyer: Union[ATEMConstant, str, int], fillSource: Union[ATEMConstant, str, int]) -> None:
        """Set Downstream Keyer Fill Source

        Args:
            keyer: see ATEMKeyers
            fillSource: see ATEMVideoSources
        """

        keyer_val = self.atem.keyers[keyer].value
        fillSource_val = self.atem.getVideoSrc(fillSource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == keyer_val

        self.switcher._prepareCommandPacket("CDsF", 4, indexMatch)
        self.switcher._outBuf.setU8(0, keyer_val)
        self.switcher._outBuf.setU16(2, fillSource_val)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerKeySource(self, keyer: Union[ATEMConstant, str, int], keySource: Union[ATEMConstant, str, int]) -> None:
        """Set Downstream Keyer Source

        Args:
            keyer: see ATEMKeyers
            keySource: see ATEMVideoSources
        """

        keyer_val = self.atem.keyers[keyer].value
        keySource_val = self.atem.getVideoSrc(keySource)

        indexMatch:bool = self.switcher._outBuf.getU8(0) == keyer_val

        self.switcher._prepareCommandPacket("CDsC", 4, indexMatch)
        self.switcher._outBuf.setU16(2, keySource_val)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerTie(self, keyer: Union[ATEMConstant, str, int], tie: bool) -> None:
        """Set Downstream Keyer Tie

        Args:
            keyer: see ATEMKeyers
            tie (bool): On/Off
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == keyer_val

        self.switcher._prepareCommandPacket("CDsT", 4, indexMatch)
        self.switcher._outBuf.setU8(0, keyer_val)
        self.switcher._outBuf.setU8(1, tie)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerRate(self, keyer: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Downstream Keyer Rate

        Args:
            keyer: see ATEMKeyers
        rate (int): 1-250 (frames)
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == keyer_val

        self.switcher._prepareCommandPacket("CDsR", 4, indexMatch)
        self.switcher._outBuf.setU8(0, keyer_val)
        self.switcher._outBuf.setU8(1, rate)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerPreMultiplied(self, keyer: Union[ATEMConstant, str, int], preMultiplied: bool) -> None:
        """Set Downstream Keyer Pre Multiplied

        Args:
            keyer: see ATEMKeyers
            preMultiplied (bool): On/Off
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsG", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU8(2, preMultiplied)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerClip(self, keyer: Union[ATEMConstant, str, int], clip: float) -> None:
        """Set Downstream Keyer Clip

        Args:
            keyer: see ATEMKeyersr 1-4
            clip (float): 0.0-100.0 (%)
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsG", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(4, int(clip*10))
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerGain(self, keyer: Union[ATEMConstant, str, int], gain: float) -> None:
        """Set Downstream Keyer Gain

        Args:
            keyer: see ATEMKeyersr 1-4
            gain (float): 0.0-100.0 (%)
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsG", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(6, int(gain*10))
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerInvertKey(self, keyer: Union[ATEMConstant, str, int], invertKey: bool) -> None:
        """Set Downstream Keyer Invert Key(??)

        Args:
            keyer: see ATEMKeyers
            invertKey (bool): On/Off
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsG", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU8(8, invertKey)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerMasked(self, keyer: Union[ATEMConstant, str, int], masked: bool) -> None:
        """Set Downstream Keyer Masked

        Args:
            keyer: see ATEMKeyers 1-4
            masked (bool): On/Off
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsM", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU8(2, masked)
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerTop(self, keyer: Union[ATEMConstant, str, int], top: float) -> None:
        """Set Downstream Keyer Top

        Args:
            keyer: see ATEMKeyers
            top (float): -9.0-9.0
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsM", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(4, int(top*1000))
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerBottom(self, keyer: Union[ATEMConstant, str, int], bottom: float) -> None:
        """Set Downstream Keyer Bottom

        Args:
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsM", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, keyer_val)
        self.switcher._outBuf.setU16(6, int(bottom*1000))
        self.switcher._finishCommandPacket()


    def setDownstreamKeyerLeft(self, keyer: Union[ATEMConstant, str, int], left: float) -> None:
        """Set Downstream Keyer Left

        Args:
            keyer: see ATEMKeyers
            left (float): -9.0-9.0
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsM", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, keyer_val)

        value = int(mapValue(left, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(8, value)

        self.switcher._finishCommandPacket()


    def setDownstreamKeyerRight(self, keyer: Union[ATEMConstant, str, int], right: float) -> None:
        """Set Downstream Keyer Right

        Args:
            keyer: see ATEMKeyers
            right (float): -9.0-9.0
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == keyer_val

        self.switcher._prepareCommandPacket("CDsM", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 4)
        self.switcher._outBuf.setU8(1, keyer_val)

        value = int(mapValue(right, -9.0, 9.0, -16000, 16000))
        self.switcher._outBuf.setS16(10, value)

        self.switcher._finishCommandPacket()


    def setDownstreamKeyerOnAir(self, keyer: Union[ATEMConstant, str, int], onAir: bool) -> None:
        """Set Downstream Keyer On Air

        Args:
            keyer: see ATEMKeyers
            onAir (bool): On/Off
        """

        keyer_val = self.atem.keyers[keyer].value

        indexMatch:bool = self.switcher._outBuf.getU8(0) == keyer_val

        self.switcher._prepareCommandPacket("CDsL", 4, indexMatch)
        self.switcher._outBuf.setU8(0, keyer_val)
        self.switcher._outBuf.setU8(1, onAir)
        self.switcher._finishCommandPacket()


    def setFadeToBlackRate(self, mE: Union[ATEMConstant, str, int], rate: int) -> None:
        """Set Fade-To-Black Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)
        """

        mE_val = self.atem.mixEffects[mE].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mE_val

        self.switcher._prepareCommandPacket("FtbC", 4, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mE_val)
        self.switcher._outBuf.setU8(2, rate)
        self.switcher._finishCommandPacket()


    def setColorGeneratorHue(self, colorGenerator: Union[ATEMConstant, str, int], hue: float) -> None:
        """Set Color Generator Hue

        Args:
            colorGenerator: see ATEMColorGenerators
            hue (float): 0.0-359.9 (degrees)
        """

        colorGenerator_val = self.atem.colorGenerators[colorGenerator].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == colorGenerator_val

        self.switcher._prepareCommandPacket("CClV", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, colorGenerator_val)
        self.switcher._outBuf.setU16(2, int(hue*10))
        self.switcher._finishCommandPacket()


    def setColorGeneratorSaturation(self, colorGenerator: Union[ATEMConstant, str, int], saturation: float) -> None:
        """Set Color Generator Saturation

        Args:
            colorGenerator: see ATEMColorGenerators
            saturation (float): 0.0-100.0 (%)
        """

        colorGenerator_val = self.atem.colorGenerators[colorGenerator].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == colorGenerator_val

        self.switcher._prepareCommandPacket("CClV", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, colorGenerator_val)
        self.switcher._outBuf.setU16(4, int(saturation*10))
        self.switcher._finishCommandPacket()


    def setColorGeneratorLuma(self, colorGenerator: Union[ATEMConstant, str, int], luma: float) -> None:
        """Set Color Generator Luma

        Args:
            colorGenerator: see ATEMColorGenerators
            luma (float): 0.0-100.0 (%)
        """

        colorGenerator_val = self.atem.colorGenerators[colorGenerator].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == colorGenerator_val

        self.switcher._prepareCommandPacket("CClV", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, colorGenerator_val)
        self.switcher._outBuf.setU16(6, int(luma*10))
        self.switcher._finishCommandPacket()


    def setAuxSourceInput(self, auxChannel: Union[ATEMConstant, str, int], input_: Union[ATEMConstant, str, int]) -> None:
        """Set Aux Source Input

        Args:
            auxChannel: see ATEMAUXChannels
            input_: see ATEMVideoSources
        """

        auxChannel_val = self.atem.auxChannels[auxChannel].value
        input_val = self.atem.getVideoSrc(input_)

        indexMatch:bool = self.switcher._outBuf.getU8(1) == auxChannel_val

        self.switcher._prepareCommandPacket("CAuS", 4, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, auxChannel_val)
        self.switcher._outBuf.setU16(2, input_val)
        self.switcher._finishCommandPacket()


    def setCameraControlIris(self, camera: Union[ATEMConstant, str, int], iris: int) -> None:
        """Set Camera Control Iris

        Args:
            camera: see ATEMCameras
            iris (int): 0-2048
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 3)
        self.switcher._outBuf.setU8(4, 0x80)    # Data type: 5.11 floating point
        self.switcher._outBuf.setU8(9, 0x01)    # One byte
        self.switcher._outBuf.setS16(16, iris)
        self.switcher._finishCommandPacket()


    def setCameraControlFocus(self, camera: Union[ATEMConstant, str, int], focus: int) -> None:
        """Set Camera Control Focus

        Args:
            camera: see ATEMCameras
            focus (int): 0-65535
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 0)
        self.switcher._outBuf.setU8(4, 0x80)    # Data type: 5.11 floating point
        self.switcher._outBuf.setU8(9, 0x01)    # One byte
        self.switcher._outBuf.setS16(16, focus)
        self.switcher._finishCommandPacket()


    def setCameraControlAutoFocus(self, camera: Union[ATEMConstant, str, int]) -> None:
        """Set Camera Control Auto focus

        Args:
            camera: see ATEMCameras
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",  24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 1)
        self.switcher._outBuf.setU8(4, 0x00) # Data type: void
        self.switcher._finishCommandPacket()


    def setCameraControlAutoIris(self, camera: Union[ATEMConstant, str, int]) -> None:
        """Set Camera Control Auto iris

        Args:
            camera: see ATEMCameras
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",  24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 5)
        self.switcher._outBuf.setU8(4, 0x00) # Data type: void
        self.switcher._finishCommandPacket()


    def setCameraControlWhiteBalance(self, camera: Union[ATEMConstant, str, int], whiteBalance: int) -> None:
        """Set Camera Control White Balance

        Args:
            camera: see ATEMCameras
            whiteBalance(int): 3200: 3200K, 4500: 4500K, 5000: 5000K, 5600: 5600K, 6500: 6500K, 7500: 7500K
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 1)
        self.switcher._outBuf.setU8(2, 2)
        self.switcher._outBuf.setU8(4, 0x02)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setS16(16, whiteBalance)
        self.switcher._finishCommandPacket()


    def setCameraControlSharpeningLevel(self, camera: Union[ATEMConstant, str, int], detail: Union[ATEMConstant, str, int]) -> None:
        """Set Camera Control Detail level

        Args:
            camera: see ATEMCameras
            detail: see ATEMCamerControlSharpeningLevels
        """

        camera_val = self.atem.cameras[camera].value
        detail_val = self.atem.camerControlSharpeningLevels[detail].value

        self.switcher._prepareCommandPacket("CCmd",  20)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 1)
        self.switcher._outBuf.setU8(2, 8)
        self.switcher._outBuf.setU8(4, 0x01)  # Data type: int8
        # Reduncancy: Support for ATEM Switchers & ATEM Proxy
        self.switcher._outBuf.setU8(7, 0x01)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setU8(16, detail_val & 0xFF)
        self.switcher._finishCommandPacket()


    def setCameraControlZoomNormalized(self, camera: Union[ATEMConstant, str, int], zoomNormalized: float) -> None:
        """Set Camera Control Zoom Normalized

        Args:
            camera: see ATEMCameras
            zoomNormalized (float): ?
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 8)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setS16(16, int(zoomNormalized*10))
        self.switcher._finishCommandPacket()


    def setCameraControlZoomSpeed(self, camera: Union[ATEMConstant, str, int], zoomSpeed: float) -> None:
        """Set Camera Control Zoom

        Args:
            camera: see ATEMCameras
            zoomSpeed (float): 0.0-1.0
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 0)
        self.switcher._outBuf.setU8(2, 9)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x01)

        value = int(mapValue(zoomSpeed, 0.0, 1.0, -2048, 2048))
        self.switcher._outBuf.setS16(16, value)

        self.switcher._finishCommandPacket()


    def setCameraControlColorbars(self, camera: Union[ATEMConstant, str, int], colorbars: int) -> None:
        """Set Camera Control Colorbars

        Args:
            camera: see ATEMCameras
            colorbars: duration in secs (0=disable)
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",  20)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 4)
        self.switcher._outBuf.setU8(2, 4)
        self.switcher._outBuf.setU8(4, 0x01)    # Data type: int8
        # Reduncancy: Support for ATEM Switchers & ATEM Proxy
        self.switcher._outBuf.setU8(7, 0x01)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setU8(16, (colorbars & 0xFF))
        self.switcher._finishCommandPacket()


    def setCameraControlLift(self, camera: Union[ATEMConstant, str, int], liftR: float, liftG: float, liftB: float, liftY: float) -> None:
        """Set Camera Control Lift

        Args:
            camera: see ATEMCameras
            liftR (float): -1.0-1.0
            liftG (float): -1.0-1.0
            liftB (float): -1.0-1.0
            liftY (float): -1.0-1.0
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 0)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x04)

        valueR = int(mapValue(liftR, -1.0, 1.0, -4096, 4096))
        valueG = int(mapValue(liftG, -1.0, 1.0, -4096, 4096))
        valueB = int(mapValue(liftB, -1.0, 1.0, -4096, 4096))
        valueY = int(mapValue(liftY, -1.0, 1.0, -4096, 4096))

        self.switcher._outBuf.setS16(16, valueR)
        self.switcher._outBuf.setS16(18, valueG)
        self.switcher._outBuf.setS16(20, valueB)
        self.switcher._outBuf.setS16(22, valueY)

        self.switcher._finishCommandPacket()


    def setCameraControlLiftR(self, camera: Union[ATEMConstant, str, int], liftR: float) -> None:
        """Set Camera Control Lift R

        Args:
            camera: see ATEMCameras
            liftR (float): -1.0-1.0
        """

        self.setCameraControlLift(camera, \
            liftR, \
            self.data.cameraControl[camera].lift.g, \
            self.data.cameraControl[camera].lift.b, \
            self.data.cameraControl[camera].lift.y, \
            )


    def setCameraControlLiftG(self, camera: Union[ATEMConstant, str, int], liftG: float) -> None:
        """Set Camera Control Lift G

        Args:
            camera: see ATEMCameras
            liftG (float): -1.0-1.0
        """

        self.setCameraControlLift(camera, \
            self.data.cameraControl[camera].lift.r, \
            liftG, \
            self.data.cameraControl[camera].lift.b, \
            self.data.cameraControl[camera].lift.y, \
            )


    def setCameraControlLiftB(self, camera: Union[ATEMConstant, str, int], liftB: float) -> None:
        """Set Camera Control Lift B

        Args:
            camera: see ATEMCameras
            liftB (float): -1.0-1.0
        """

        self.setCameraControlLift(camera, \
            self.data.cameraControl[camera].lift.r, \
            self.data.cameraControl[camera].lift.g, \
            liftB, \
            self.data.cameraControl[camera].lift.y, \
            )


    def setCameraControlLiftY(self, camera: Union[ATEMConstant, str, int], liftY: float) -> None:
        """Set Camera Control Lift Y

        Args:
            camera: see ATEMCameras
            liftY (float): -1.0-1.0
        """

        self.setCameraControlLift(camera, \
            self.data.cameraControl[camera].lift.r, \
            self.data.cameraControl[camera].lift.g, \
            self.data.cameraControl[camera].lift.b, \
            liftY, \
            )


    def setCameraControlGamma(self, camera: Union[ATEMConstant, str, int], gammaR: float, gammaG: float, gammaB: float, gammaY: float) -> None:
        """Set Camera Control Gamma

        Args:
            camera: see ATEMCameras
            gammaR (float): -1.0-1.0
            gammaG (float): -1.0-1.0
            gammaB (float): -1.0-1.0
            gammaY (float): -1.0-1.0
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 1)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x04)

        valueR = int(mapValue(gammaR, -1.0, 1.0, -8192, 8192))
        valueG = int(mapValue(gammaG, -1.0, 1.0, -8192, 8192))
        valueB = int(mapValue(gammaB, -1.0, 1.0, -8192, 8192))
        valueY = int(mapValue(gammaY, -1.0, 1.0, -8192, 8192))

        self.switcher._outBuf.setS16(16, valueR)
        self.switcher._outBuf.setS16(18, valueG)
        self.switcher._outBuf.setS16(20, valueB)
        self.switcher._outBuf.setS16(22, valueY)

        self.switcher._finishCommandPacket()


    def setCameraControlGammaR(self, camera: Union[ATEMConstant, str, int], gammaR: float) -> None:
        """Set Camera Control Gamma R

        Args:
            camera: see ATEMCameras
            gammaR (float): -1.0-1.0
        """

        self.setCameraControlGamma(camera, \
            gammaR, \
            self.data.cameraControl[camera].gamma.g, \
            self.data.cameraControl[camera].gamma.b, \
            self.data.cameraControl[camera].gamma.y, \
            )


    def setCameraControlGammaG(self, camera: Union[ATEMConstant, str, int], gammaG: float) -> None:
        """Set Camera Control Gamma G

        Args:
            camera: see ATEMCameras
            gammaG (float): -1.0-1.0
        """

        self.setCameraControlGamma(camera, \
            self.data.cameraControl[camera].gamma.r, \
            gammaG, \
            self.data.cameraControl[camera].gamma.b, \
            self.data.cameraControl[camera].gamma.y, \
            )


    def setCameraControlGammaB(self, camera: Union[ATEMConstant, str, int], gammaB: float) -> None:
        """Set Camera Control Gamma B

        Args:
            camera: see ATEMCameras
            gammaB (float): -1.0-1.0
        """

        self.setCameraControlGamma(camera, \
            self.data.cameraControl[camera].gamma.r, \
            self.data.cameraControl[camera].gamma.g, \
            gammaB, \
            self.data.cameraControl[camera].gamma.y, \
            )


    def setCameraControlGammaY(self, camera: Union[ATEMConstant, str, int], gammaY: float) -> None:
        """Set Camera Control Gamma Y

        Args:
            camera: see ATEMCameras
            gammaY (float): -1.0-1.0
        """

        self.setCameraControlGamma(camera, \
            self.data.cameraControl[camera].gamma.r, \
            self.data.cameraControl[camera].gamma.g, \
            self.data.cameraControl[camera].gamma.b, \
            gammaY, \
            )


    def setCameraControlGain(self, camera: Union[ATEMConstant, str, int], gain: int) -> None:
        """Set Camera Control Gain

        Args:
            camera: see ATEMCameras
            gain (int): 512: 0db, 1024: 6db, 2048: 12db, 4096: 18db
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 1)
        self.switcher._outBuf.setU8(2, 1)
        self.switcher._outBuf.setU8(4, 0x01)
        # Reduncancy: Support for ATEM Switchers & ATEM Proxy
        self.switcher._outBuf.setU8(7, 0x01)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setS16(16, gain)
        self.switcher._finishCommandPacket()


    def setCameraControlComponentGain(self, camera: Union[ATEMConstant, str, int], gainR: float, gainG: float, gainB: float, gainY: float) -> None:
        """Set Camera Control Component Gain

        Args:
            camera: see ATEMCameras
            gainR (float): 0.0-16.0
            gainG (float): 0.0-16.0
            gainB (float): 0.0-16.0
            gainY (float): 0.0-16.0
        """

        camera_val = self.atem.cameras[camera].value
        valueR = int(mapValue(gainR, 0.0, 16.0, 0, 32767))
        valueG = int(mapValue(gainG, 0.0, 16.0, 0, 32767))
        valueB = int(mapValue(gainB, 0.0, 16.0, 0, 32767))
        valueY = int(mapValue(gainY, 0.0, 16.0, 0, 32767))

        self.switcher._prepareCommandPacket("CCmd",24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 2)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x04)
        self.switcher._outBuf.setS16(16, valueR)
        self.switcher._outBuf.setS16(18, valueG)
        self.switcher._outBuf.setS16(20, valueB)
        self.switcher._outBuf.setS16(22, valueY)
        self.switcher._finishCommandPacket()


    def setCameraControlGainR(self, camera: Union[ATEMConstant, str, int], gainR: float) -> None:
        """Set Camera Control Gain R

        Args:
            camera: see ATEMCameras
            gainR (float): 0.0-16.0
        """

        self.setCameraControlComponentGain(camera, \
            gainR, \
            self.data.cameraControl[camera].gain.g, \
            self.data.cameraControl[camera].gain.b, \
            self.data.cameraControl[camera].gain.y, \
            )


    def setCameraControlGainG(self, camera: Union[ATEMConstant, str, int], gainG: float) -> None:
        """Set Camera Control Gain G

        Args:
            camera: see ATEMCameras
            gainG (float): 0.0-16.0
        """

        self.setCameraControlComponentGain(camera, \
            self.data.cameraControl[camera].gain.r, \
            gainG, \
            self.data.cameraControl[camera].gain.b, \
            self.data.cameraControl[camera].gain.y, \
            )


    def setCameraControlGainB(self, camera: Union[ATEMConstant, str, int], gainB: float) -> None:
        """Set Camera Control Gain B

        Args:
            camera: see ATEMCameras
            gainB (float): 0.0-16.0
        """

        self.setCameraControlComponentGain(camera, \
            self.data.cameraControl[camera].gain.r, \
            self.data.cameraControl[camera].gain.g, \
            gainB, \
            self.data.cameraControl[camera].gain.y, \
            )


    def setCameraControlGainY(self, camera: Union[ATEMConstant, str, int], gainY: float) -> None:
        """Set Camera Control Gain Y

        Args:
            camera: see ATEMCameras
            gainY (float): 0.0-16.0
        """

        self.setCameraControlComponentGain(camera, \
            self.data.cameraControl[camera].gain.r, \
            self.data.cameraControl[camera].gain.g, \
            self.data.cameraControl[camera].gain.b, \
            gainY, \
            )


    def setCameraControlLumMix(self, camera: Union[ATEMConstant, str, int], lumMix: float) -> None:
        """Set Camera Control Lum Mix

        Args:
            camera: see ATEMCameras
            lumMix (float):  0.0-100.0 (%)
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 5)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x01)
        self.switcher._outBuf.setS16(16, int(mapValue(lumMix, 0, 100, 0, 2048)))
        self.switcher._finishCommandPacket()


    def setCameraControlResetAll(self, camera: Union[ATEMConstant, str, int]) -> None:
        """Set Camera Control Reset all

        Args:
            camera: see ATEMCameras
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd",  24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 7)
        self.switcher._outBuf.setU8(4, 0x00) # Data type: void
        self.switcher._finishCommandPacket()


        # Update local state variables to reflect reset values
        self.data.cameraControl[camera_val].gamma.r = 0.0
        self.data.cameraControl[camera_val].gamma.g = 0.0
        self.data.cameraControl[camera_val].gamma.b = 0.0
        self.data.cameraControl[camera_val].gamma.y = 0.0
        self.data.cameraControl[camera_val].lift.r = 0.0
        self.data.cameraControl[camera_val].lift.g = 0.0
        self.data.cameraControl[camera_val].lift.b = 0.0
        self.data.cameraControl[camera_val].lift.y = 0.0
        self.data.cameraControl[camera_val].gain.r = mapValue(2048, 0, 32767, 0.0, 16.0)
        self.data.cameraControl[camera_val].gain.g = mapValue(2048, 0, 32767, 0.0, 16.0)
        self.data.cameraControl[camera_val].gain.b = mapValue(2048, 0, 32767, 0.0, 16.0)
        self.data.cameraControl[camera_val].gain.y = mapValue(2048, 0, 32767, 0.0, 16.0)
        self.data.cameraControl[camera_val].contrast = 2048
        self.data.cameraControl[camera_val].hue = 0
        self.data.cameraControl[camera_val].saturation = 2048


    def setCameraControlShutter(self, camera: Union[ATEMConstant, str, int], shutter: float) -> None:
        """Set Camera Control Shutter

        Args:
            camera: see ATEMCameras
            shutter (float): 1/50, 1/60, 1/75, 1/90, 1/100, 1/120, 1/150, 1/180, 1/250, 1/360, 1/500, 1/750, 1/1000, 1/1450, 1/2000
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 1)
        self.switcher._outBuf.setU8(2, 5)
        self.switcher._outBuf.setU8(4, 0x03)
        self.switcher._outBuf.setU8(11, 0x01)
        self.switcher._outBuf.setS16(18, int(shutter*1000000))
        self.switcher._finishCommandPacket()


    def setCameraControlContrast(self, camera: Union[ATEMConstant, str, int], contrast: float) -> None:
        """Set Camera Control Contrast

        Args:
            camera: see ATEMCameras
            contrast (float): 0.0-100.0 (%)
        """

        camera_val = self.atem.cameras[camera].value
        contrast_val = int(mapValue(contrast, 0, 100, 0, 4096))

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 4)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x02)
        # Pivot = 0.5 (Fixed16 1024)
        self.switcher._outBuf.setU8(16, 4)
        self.switcher._outBuf.setU8(17, 0)
        self.switcher._outBuf.setS16(18, contrast_val)
        self.switcher._finishCommandPacket()


    def setCameraControlHueSaturation(self, camera: Union[ATEMConstant, str, int], hue: float, saturation: float) -> None:
        """Set Camera Control Hue/Saturation

        Args:
            camera: see ATEMCameras
            hue (float): 0.0-359.9 degrees
            saturation (float): 0.0-100.0 (%)
        """

        camera_val = self.atem.cameras[camera].value
        hue_val = int(mapValue(hue, 0, 360, -2048, 2048))
        saturation_val = int(mapValue(saturation, 0, 100, 0, 4096))

        self.switcher._prepareCommandPacket("CCmd",24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 8)
        self.switcher._outBuf.setU8(2, 6)
        self.switcher._outBuf.setU8(4, 0x80)
        self.switcher._outBuf.setU8(9, 0x02)
        self.switcher._outBuf.setS16(16, hue_val)
        self.switcher._outBuf.setS16(18, saturation_val)
        self.switcher._finishCommandPacket()


    def setCameraControlHue(self, camera: Union[ATEMConstant, str, int], hue: float) -> None:
        """Set Camera Control Hue

        Args:
            camera: see ATEMCameras
            hue (float): 0.0-359.9 degrees
        """

        self.setCameraControlHueSaturation(camera, hue, self.data.cameraControl[camera].saturation)


    def setCameraControlSaturation(self, camera: Union[ATEMConstant, str, int], saturation: float) -> None:
        """Set Camera Control Saturation

        Args:
            camera: see ATEMCameras
            saturation (float):  0.0-100.0 (%)
        """

        self.setCameraControlHueSaturation(camera, self.data.cameraControl[camera].hue, saturation)


    def setCameraControlVideomode(self, camera: Union[ATEMConstant, str, int], fps: int, resolution: int, interlaced: int) -> None:
        """Set Camera Control Video Mode

        Args:
            camera: see ATEMCameras
            fps (int): ?
            resolution (int): ?
            interlaced (int): ?
        """

        camera_val = self.atem.cameras[camera].value

        self.switcher._prepareCommandPacket("CCmd", 24)
        self.switcher._outBuf.setU8(0, camera_val)
        self.switcher._outBuf.setU8(1, 1)
        self.switcher._outBuf.setU8(2, 0)
        self.switcher._outBuf.setU8(4, 0x01)   # Data type: int8
        self.switcher._outBuf.setU8(7, 0x05)   # 5 Byte array
        #self.switcher._outBuf.setU8(9, 0x05)   # 5 byte array
        self.switcher._outBuf.setU8(16, fps)
        self.switcher._outBuf.setU8(17, 0x00)   # Regular M-rate
        self.switcher._outBuf.setU8(18, resolution)
        self.switcher._outBuf.setU8(19, interlaced)
        self.switcher._outBuf.setU8(20, 0x00)   # YUV
        self.switcher._finishCommandPacket()


    def setClipPlayerPlaying(self, mediaPlayer: Union[ATEMConstant, str, int], playing: bool) -> None:
        """Set Clip Player Playing

        Args:
            mediaPlayer: see ATEMMediaPlayers
            playing (bool): On/Off
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("SCPS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(2, playing)
        self.switcher._finishCommandPacket()


    def setClipPlayerLoop(self, mediaPlayer: Union[ATEMConstant, str, int], loop: bool) -> None:
        """Set Clip Player Loop

        Args:
            mediaPlayer: see ATEMMediaPlayers
            loop (bool): On/Off
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("SCPS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(3, loop)
        self.switcher._finishCommandPacket()


    def setClipPlayerAtBeginning(self, mediaPlayer: Union[ATEMConstant, str, int], atBeginning: bool) -> None:
        """Set Clip Player At Beginning

        Args:
            mediaPlayer: see ATEMMediaPlayers
            atBeginning (bool): On/Off
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("SCPS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(4, atBeginning)
        self.switcher._finishCommandPacket()


    def setClipPlayerClipFrame(self, mediaPlayer: Union[ATEMConstant, str, int], clipFrame: int) -> None:
        """Set Clip Player Clip Frame

        Args:
            mediaPlayer: see ATEMMediaPlayers
            clipFrame (int): frame
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("SCPS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU16(6, clipFrame)
        self.switcher._finishCommandPacket()


    def setMediaPlayerSourceType(self, mediaPlayer: Union[ATEMConstant, str, int], type_: Union[ATEMConstant, str, int]) -> None:
        """Set Media Player Source Type

        Args:
            mediaPlayer: see ATEMMediaPlayers
            type_: see ATEMMediaPlayerSourceTypes
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value
        type_val = self.atem.mediaPlayerSourceTypes[type_].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("MPSS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(2, type_val)
        self.switcher._finishCommandPacket()


    def setMediaPlayerSourceStillIndex(self, mediaPlayer: Union[ATEMConstant, str, int], stillIndex: int) -> None:
        """Set Media Player Source Still Index

        Args:
            mediaPlayer: see ATEMMediaPlayers
            stillIndex (int): 0-x: Still 1-x
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("MPSS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(3, stillIndex)
        self.switcher._finishCommandPacket()


    def setMediaPlayerSourceClipIndex(self, mediaPlayer: Union[ATEMConstant, str, int], clipIndex: int) -> None:
        """Set Media Player Source Clip Index

        Args:
            mediaPlayer: see ATEMMediaPlayers
            clipIndex (int): 0-x: Clip 1-x
        """

        mediaPlayer_val = self.atem.mediaPlayers[mediaPlayer].value

        indexMatch:bool = self.switcher._outBuf.getU8(1) == mediaPlayer_val

        self.switcher._prepareCommandPacket("MPSS", 8, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(1, mediaPlayer_val)
        self.switcher._outBuf.setU8(4, clipIndex)
        self.switcher._finishCommandPacket()


    def setMediaPoolStorageClip1MaxLength(self, clip1MaxLength: int) -> None:
        """Set Media Pool Storage Clip 1 Max Length

        Args:
            clip1MaxLength (int): frames
        """

        self.switcher._prepareCommandPacket("CMPS", 4)
        self.switcher._outBuf.setU16(0, clip1MaxLength)
        self.switcher._finishCommandPacket()


    def setMacroAction(self, macro: Union[ATEMConstant, str, int], action: Union[ATEMConstant, str, int]) -> None:
        """Set Macro Action Action

        Args:
            macro: see ATEMMacros (to stop, use macros.stop)
            action: see ATEMMacroActions
        """

        macro_val = self.atem.macros[macro].value
        action_val = self.atem.macroActions[action].value

        indexMatch:bool = self.switcher._outBuf.getU16(0) == macro_val

        self.switcher._prepareCommandPacket("MAct", 4, indexMatch)
        self.switcher._outBuf.setU16(0, macro_val)
        self.switcher._outBuf.setU8(2, action_val)
        self.switcher._finishCommandPacket()


    def setMacroRunChangePropertiesLooping(self, looping: bool) -> None:
        """Set Macro Run Change Properties Looping

        Args:
            looping (bool): On/Off
        """

        self.switcher._prepareCommandPacket("MRCP", 4)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, looping)
        self.switcher._finishCommandPacket()


    def setMacroAddPauseFrames(self, frames: int) -> None:
        """Set Macro Add Pause Frames

        Args:
            frames (int): number of frames
        """

        self.switcher._prepareCommandPacket("MSlp", 4)
        self.switcher._outBuf.setU16(2, frames)
        self.switcher._finishCommandPacket()


    def setSuperSourceFillSource(self, fillSource: Union[ATEMConstant, str, int]) -> None:
        """Set Super Source Fill Source

        Args:
            fillSource: see ATEMVideoSources
        """

        fillSource_val = self.atem.getVideoSrc(fillSource)

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 0)
        self.switcher._outBuf.setU16(4, fillSource_val)
        self.switcher._finishCommandPacket()


    def setSuperSourceKeySource(self, keySource: Union[ATEMConstant, str, int]) -> None:
        """Set Super Source Key Source

        Args:
            keySource: see ATEMVideoSources
        """

        keySource_val = self.atem.getVideoSrc(keySource)

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 1)
        self.switcher._outBuf.setU16(6, keySource_val)
        self.switcher._finishCommandPacket()


    def setSuperSourceForeground(self, foreground: bool) -> None:
        """Set Super Source Foreground

        Args:
            foreground (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 2)
        self.switcher._outBuf.setU8(8, foreground)
        self.switcher._finishCommandPacket()


    def setSuperSourcePreMultiplied(self, preMultiplied: bool) -> None:
        """Set Super Source Pre Multiplied

        Args:
            preMultiplied (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 3)
        self.switcher._outBuf.setU8(9, preMultiplied)
        self.switcher._finishCommandPacket()


    def setSuperSourceClip(self, clip: float) -> None:
        """Set Super Source Clip

        Args:
            clip (float): 0.0-100.0 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 4)
        self.switcher._outBuf.setU16(10, int(clip*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceGain(self, gain: float) -> None:
        """Set Super Source Gain

        Args:
            gain (float): 0.0-100.0 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 5)
        self.switcher._outBuf.setU16(12, int(gain*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceInvertKey(self, invertKey: bool) -> None:
        """Set Super Source Invert Key

        Args:
            invertKey (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 6)
        self.switcher._outBuf.setU8(14, invertKey)
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderEnabled(self, borderEnabled: bool) -> None:
        """Set Super Source Border Enabled

        Args:
            borderEnabled (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(3, 7)
        self.switcher._outBuf.setU8(15, borderEnabled)
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderBevel(self, borderBevel: Union[ATEMConstant, str, int]) -> None:
        """Set Super Source Border Bevel

        Args:
            borderBevel: see ATEMBorderBevels
        """

        borderBevel_val = self.atem.borderBevels[borderBevel].value

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 0)
        self.switcher._outBuf.setU8(16, borderBevel_val)
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderOuterWidth(self, borderOuterWidth: float) -> None:
        """Set Super Source Border Outer Width

        Args:
            borderOuterWidth (float): 0.0-16.0
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 1)
        self.switcher._outBuf.setU16(18, int(borderOuterWidth*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderInnerWidth(self, borderInnerWidth: float) -> None:
        """Set Super Source Border Inner Width

        Args:
            borderInnerWidth (float): 0.0-16.0
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 2)
        self.switcher._outBuf.setU16(20, int(borderInnerWidth*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderOuterSoftness(self, borderOuterSoftness: int) -> None:
        """Set Super Source Border Outer Softness

        Args:
            borderOuterSoftness (int): 0-100 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 3)
        self.switcher._outBuf.setU8(22, borderOuterSoftness)
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderInnerSoftness(self, borderInnerSoftness: int) -> None:
        """Set Super Source Border Inner Softness

        Args:
            borderInnerSoftness (int): 0-100 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 4)
        self.switcher._outBuf.setU8(23, borderInnerSoftness)
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderBevelSoftness(self, borderBevelSoftness: float) -> None:
        """Set Super Source Border Bevel Softness

        Args:
            borderBevelSoftness (float): 0.0-1.0
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 5)
        self.switcher._outBuf.setU8(24, int(borderBevelSoftness*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderBevelPosition(self, borderBevelPosition: float) -> None:
        """Set Super Source Border Bevel Position

        Args:
            borderBevelPosition (float): 0.0-1.0
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 6)
        self.switcher._outBuf.setU8(25, int(borderBevelPosition*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderHue(self, borderHue: float) -> None:
        """Set Super Source Border Hue

        Args:
            borderHue (float): 0.0-359.9 (degrees)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(2, 7)
        self.switcher._outBuf.setU16(26, int(borderHue*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderSaturation(self, borderSaturation: float) -> None:
        """Set Super Source Border Saturation

        Args:
            borderSaturation (float): 0.0-100.0 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU16(28, int(borderSaturation*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceBorderLuma(self, borderLuma: float) -> None:
        """Set Super Source Border Luma

        Args:
            borderLuma (float): 0.0-100.0 (%)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(1, 1)
        self.switcher._outBuf.setU16(30, int(borderLuma*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceLightSourceDirection(self, lightSourceDirection: float) -> None:
        """Set Super Source Light Source Direction

        Args:
            lightSourceDirection (float): 0.0-359.9 (degrees)
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU16(32, int(lightSourceDirection*10))
        self.switcher._finishCommandPacket()


    def setSuperSourceLightSourceAltitude(self, lightSourceAltitude: int) -> None:
        """Set Super Source Light Source Altitude

        Args:
            lightSourceAltitude (int): 10-100
        """

        self.switcher._prepareCommandPacket("CSSc", 36)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(34, lightSourceAltitude)
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersEnabled(self, box: Union[ATEMConstant, str, int], enabled: bool) -> None:
        """Set Super Source Box Parameters Enabled

        Args:
            box: see ATEMBoxes
            enabled (bool): On/Off
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 0)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU8(3, enabled)
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersInputSource(self, box: Union[ATEMConstant, str, int], inputSource: Union[ATEMConstant, str, int]) -> None:
        """Set Super Source Box Parameters Input Source

        Args:
            box: see ATEMBoxes
            inputSource: see ATEMVideoSources
        """

        box_val = self.atem.boxes[box].value
        inputSource_val = self.atem.getVideoSrc(inputSource)
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 1)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(4, inputSource_val)
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersPositionX(self, box: Union[ATEMConstant, str, int], positionX: float) -> None:
        """Set Super Source Box Parameters Position X

        Args:
            box: see ATEMBoxes
            positionX (float): -48.0-48.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 2)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(6, int(positionX*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersPositionY(self, box: Union[ATEMConstant, str, int], positionY: float) -> None:
        """Set Super Source Box Parameters Position Y

        Args:
            box: see ATEMBoxes
            positionY (float): -27.0-27.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 3)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(8, int(positionY*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersSize(self, box: Union[ATEMConstant, str, int], size: float) -> None:
        """Set Super Source Box Parameters Size

        Args:
            box: see ATEMBoxes
            size (float): 0.07-1.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 4)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(10, int(size*100))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersCropped(self, box: Union[ATEMConstant, str, int], cropped: bool) -> None:
        """Set Super Source Box Parameters Cropped

        Args:
            box: see ATEMBoxes
            cropped (bool): On/Off
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 5)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU8(12, cropped)
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersCropTop(self, box: Union[ATEMConstant, str, int], cropTop: float) -> None:
        """Set Super Source Box Parameters Crop Top

        Args:
            box: see ATEMBoxes
            cropTop (float): 0.0-18.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 6)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(14, int(cropTop*1000))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersCropBottom(self, box: Union[ATEMConstant, str, int], cropBottom: float) -> None:
        """Set Super Source Box Parameters Crop Bottom

        Args:
            box: see ATEMBoxes
            cropBottom (float): 0.0-18.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(1, 7)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(16, int(cropBottom*1000))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersCropLeft(self, box: Union[ATEMConstant, str, int], cropLeft: float) -> None:
        """Set Super Source Box Parameters Crop Left

        Args:
            box: see ATEMBoxes
            cropLeft (float): 0.0-32.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(18, int(cropLeft*1000))
        self.switcher._finishCommandPacket()


    def setSuperSourceBoxParametersCropRight(self, box: Union[ATEMConstant, str, int], cropRight: float) -> None:
        """Set Super Source Box Parameters Crop Right

        Args:
            box: see ATEMBoxes
            cropRight (float): 0.0-32.0
        """

        box_val = self.atem.boxes[box].value
        indexMatch:bool = self.switcher._outBuf.getU8(2) == box_val

        self.switcher._prepareCommandPacket("CSBP", 24, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU8(2, box_val)
        self.switcher._outBuf.setU16(20, int(cropRight*1000))
        self.switcher._finishCommandPacket()


    def setAudioMixerInputMixOption(self, audioSource: Union[ATEMConstant, str, int], mixOption: Union[ATEMConstant, str, int]) -> None:
        """Set Audio Mixer Input Mix Option

        Args:
            audioSource: see ATEMAudioSources
            mixOption: see ATEMAudioMixerInputMixOptions
        """

        audioSource_val = self.atem.getAudioSrc(audioSource)
        mixOption_val = self.atem.audioMixerInputMixOptions[mixOption].value

        indexMatch:bool = self.switcher._outBuf.getU16(2) == audioSource_val

        self.switcher._prepareCommandPacket("CAMI", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU16(2, audioSource_val)
        self.switcher._outBuf.setU8(4, mixOption_val)
        self.switcher._finishCommandPacket()


    def setAudioMixerInputVolume(self, audioSource: Union[ATEMConstant, str, int], db: float) -> None:
        """Set Audio Mixer Input Volume

        Args:
            audioSource: see ATEMAudioSources
            db (float): volume in dB
        """

        audioSource_val = self.atem.getAudioSrc(audioSource)
        volume = self.atem.audioDb2Word(db)

        indexMatch:bool = self.switcher._outBuf.getU16(2) == audioSource_val

        self.switcher._prepareCommandPacket("CAMI", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU16(2, audioSource_val)
        self.switcher._outBuf.setU16(6, volume)
        self.switcher._finishCommandPacket()


    def setAudioMixerInputBalance(self, audioSource: Union[ATEMConstant, str, int], balance: float) -> None:
        """Set Audio Mixer Input Balance

        Args:
            audioSource: see ATEMAudioSources
            balance (float): -1.0-1.0: Left/Right Extremes
        """

        audioSource_val = self.atem.getAudioSrc(audioSource)

        indexMatch:bool = self.switcher._outBuf.getU16(2) == audioSource_val

        self.switcher._prepareCommandPacket("CAMI", 12, indexMatch)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU16(2, audioSource_val)
        self.switcher._outBuf.setS16(8, int(balance*10000))
        self.switcher._finishCommandPacket()


    def setAudioMixerMasterVolume(self, db: float) -> None:
        """Set Audio Mixer Master Volume

        Args:
            db (float): volume in dB
        """

        volume = self.atem.audioDb2Word(db)

        self.switcher._prepareCommandPacket("CAMM", 8)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU16(2, volume)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorMonitorAudio(self, monitorAudio: bool) -> None:
        """Set Audio Mixer Monitor Monitor Audio

        Args:
            monitorAudio (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 0)
        self.switcher._outBuf.setU8(1, monitorAudio)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorVolume(self, db: float) -> None:
        """Set Audio Mixer Monitor Volume

        Args:
            db (float): volume in dB
        """

        volume = self.atem.audioDb2Word(db)

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU16(2, volume)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorMute(self, mute: bool) -> None:
        """Set Audio Mixer Monitor Mute

        Args:
            mute (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(4, mute)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorSolo(self, solo: bool) -> None:
        """Set Audio Mixer Monitor Solo

        Args:
            solo (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 3)
        self.switcher._outBuf.setU8(5, solo)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorSoloInput(self, soloInput: Union[ATEMConstant, str, int]) -> None:
        """Set Audio Mixer Monitor Solo Input

        Args:
            soloInput: see ATEMAudioSources
        """

        soloInput_val = self.atem.getAudioSrc(soloInput)

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 4)
        self.switcher._outBuf.setU16(6, soloInput_val)
        self.switcher._finishCommandPacket()


    def setAudioMixerMonitorDim(self, dim: bool) -> None:
        """Set Audio Mixer Monitor Dim

        Args:
            dim (bool): On/Off
        """

        self.switcher._prepareCommandPacket("CAMm", 12)
        self.switcher._outBuf.setU8Flag(0, 5)
        self.switcher._outBuf.setU8(8, dim)
        self.switcher._finishCommandPacket()


    def setAudioLevelsEnable(self, enable: bool) -> None:
        """Set Audio Levels Enable

        Args:
            enable (bool): On/Off
        """

        self.switcher._prepareCommandPacket("SALN", 4)
        self.switcher._outBuf.setU8(0, enable)
        self.switcher._finishCommandPacket()


    def setResetAudioMixerPeaksInputSource(self, inputSource: Union[ATEMConstant, str, int]) -> None:
        """Set Reset Audio Mixer Peaks Input Source

        Args:
            inputSource: see ATEMAudioSources
        """

        inputSource_val = self.atem.getVideoSrc(inputSource)

        self.switcher._prepareCommandPacket("RAMP", 8)
        self.switcher._outBuf.setU8Flag(0, 1)
        self.switcher._outBuf.setU16(2, inputSource_val)
        self.switcher._finishCommandPacket()


    def setResetAudioMixerPeaksMaster(self, master: bool) -> None:
        """Set Reset Audio Mixer Peaks Master

        Args:
            master (bool): Yes/No
        """

        self.switcher._prepareCommandPacket("RAMP", 8)
        self.switcher._outBuf.setU8Flag(0, 2)
        self.switcher._outBuf.setU8(4, master)
        self.switcher._finishCommandPacket()
