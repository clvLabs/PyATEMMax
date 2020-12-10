#!/usr/bin/env python3
# coding: utf-8
"""
ATEMCommandHandlers: Blackmagic ATEM switcher command handlers.
Part of the PyATEMMax library.
Methods do keep the order in https://www.skaarhoj.com/fileadmin/BMDPROTOCOL.html
"""

# pylint: disable=too-many-lines, wildcard-import, unused-wildcard-import, protected-access
# pyright: reportPrivateUsage=false, reportUnusedFunction=false, reportUnboundVariable=false

from typing import Callable

from .ATEMUtils import boolBit, mapValue
from .ATEMProtocolEnums import *
from .ATEMException import ATEMException

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
    from .ATEMBuffer import ATEMBuffer
else:
    ATEMProtocol = type(int)
    ATEMSwitcherState = type(int)
    ATEMConnectionManager = type(int)
    ATEMBuffer = type(int)

# --------------------------------------------------


class ATEMCommandHandlers():
    """Blackmagic ATEM switcher command handlers

    This class is a port of Skårhøj's ATEMmax class.
    """

    # These handlers manage their initial buffer read by themselves
    _AUTOMANAGED_HANDLERS = [ 'AMLv', 'TlSr' ]

    # All command handler methods MUST have this prefix
    _HANDLER_PREFIX = "_handle"


    def __init__(self, switcher: ATEMConnectionManager, data: ATEMSwitcherState, atem: ATEMProtocol):
        # Using "hidden" names to avoid recurrent exposure (switcher.switcher)
        self._sw: ATEMConnectionManager = switcher
        self._inBuf: ATEMBuffer = switcher._inBuf
        self._d: ATEMSwitcherState = data
        self._p: ATEMProtocol = atem

        self.cmdStr:str = ""


    # #######################################################################
    #
    #  Handler management
    #


    def registerAllHandlers(self):
        """Register all handlers"""

        for attr in dir(self):
            funcname = attr

            if funcname[:len(self._HANDLER_PREFIX)] == self._HANDLER_PREFIX:
                funccmd = funcname[len(self._HANDLER_PREFIX):]
                if funccmd != 'NOTIMPLEMENTED':
                    self._sw._registerCmdHandler(funccmd, self._mainHandler)

        for funccmd in self._p.commands:
            if funccmd not in self._sw._cmdHandlers:
                self._sw._registerCmdHandler(funccmd, self._mainHandler)


    def _mainHandler(self, cmdStr:str) -> None:
        '''This is the main handler, it redirects calls'''

        if cmdStr not in self._AUTOMANAGED_HANDLERS:
            self._sw._read2InBuf()

        self.cmdStr = cmdStr
        self._getHandler(cmdStr)()  # Call specific handler


    def _getHandler(self, cmdStr:str) -> Callable[[], None]:
        """Get handler by command name"""

        funcname = self._HANDLER_PREFIX + cmdStr
        if funcname in dir(self):
            return self.__getattribute__(funcname)
        else:
            return self._handleNOTIMPLEMENTED


    def _getBufEnum(self, offset: int, bits: int, enum: ATEMConstantList) -> ATEMConstant:
        """Get an enumerated value from input buffer"""

        const_val = self._inBuf.getInt(offset, False, bits)
        retval = enum.byValue(const_val)
        if retval.value is None:
            raise ATEMException(f"UNKNOWN {enum.__class__.__name__} {const_val}")
        return retval


    def _getBufVideoSource(self, offset: int) -> ATEMConstant:
        """Get an enumerated video source from input buffer"""

        videoSrc = self._inBuf.getU16(offset)
        return self._p.videoSources[videoSrc]


    def _getBufAudioSource(self, offset: int) -> ATEMConstant:
        """Get an enumerated audio source from input buffer"""

        audioSrc = self._inBuf.getU16(offset)
        return self._p.audioSources[audioSrc]


    def _getBufMixEffect(self, offset: int) -> ATEMConstant:
        """Get an enumerated mix effect from input buffer"""

        mE = self._inBuf.getU8(offset)
        return self._p.mixEffects[mE]


    def _getBufKeyer(self, offset: int) -> ATEMConstant:
        """Get an enumerated keyer from input buffer"""

        keyer = self._inBuf.getU8(offset)
        return self._p.keyers[keyer]


    def _getBufDsk(self, offset: int) -> ATEMConstant:
        """Get an enumerated dsk from input buffer"""

        dsk = self._inBuf.getU8(offset)
        return self._p.dsks[dsk]


    # #######################################################################
    #
    #  Command handler methods
    #

    def _handle_ver(self) -> None:
        self._d.protocolVersion.major = self._inBuf.getU16(0)
        self._d.protocolVersion.minor = self._inBuf.getU16(2)

    def _handle_pin(self) -> None:
        self._d.atemModel = self._inBuf.getString(0, 44)


    def _handleWarn(self) -> None:
        self._d.warningText = self._inBuf.getString(0, 44)


    def _handle_top(self) -> None:
        self._d.topology.mEs = self._inBuf.getU8(0)
        self._d.topology.sources = self._inBuf.getU8(1)
        self._d.topology.colorGenerators = self._inBuf.getU8(2)
        self._d.topology.auxBusses = self._inBuf.getU8(3)
        self._d.topology.downstreamKeyers = self._inBuf.getU8(4)
        self._d.topology.stingers = self._inBuf.getU8(5)
        self._d.topology.dVEs = self._inBuf.getU8(6)
        self._d.topology.superSources = self._inBuf.getU8(7)
        self._d.topology.hasSDOutput = self._inBuf.getU8Flag(9, 0)


    def _handle_MeC(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.mixEffect.config[mE].keyers = self._inBuf.getU8(1)


    def _handle_mpl(self) -> None:
        self._d.mediaPlayer.stillBanks = self._inBuf.getU8(0)
        self._d.mediaPlayer.clipBanks = self._inBuf.getU8(1)


    def _handle_MvC(self) -> None:
        self._d.multiViewer.config.multiViewers = self._inBuf.getU8(0)


    def _handle_SSC(self) -> None:
        self._d.superSource.config.boxes = self._inBuf.getU8(0)


    def _handle_TlC(self) -> None:
        self._d.tally.channelConfig.tallyChannels = self._inBuf.getU8(4)


    def _handle_AMC(self) -> None:
        self._d.audioMixer.config.audioChannels = self._inBuf.getU8(0)
        self._d.audioMixer.config.hasMonitor = self._inBuf.getU8Flag(1, 0)


    def _handle_VMC(self) -> None:
        # Trick to get 3 byte integer from position 1
        flags:int = self._inBuf.getInt(0, False, 32) & 0x00FFFFFF

        self._d.videoMixer.config.modes.f525i59_94_NTSC = boolBit(flags, 0)
        self._d.videoMixer.config.modes.f625i_50_PAL = boolBit(flags, 1)
        self._d.videoMixer.config.modes.f525i59_94_NTSC_16_9 = boolBit(flags, 2)
        self._d.videoMixer.config.modes.f625i_50_PAL_16_9 = boolBit(flags, 3)
        self._d.videoMixer.config.modes.f720p50 = boolBit(flags, 4)
        self._d.videoMixer.config.modes.f720p59_94 = boolBit(flags, 5)
        self._d.videoMixer.config.modes.f1080i50 = boolBit(flags, 6)
        self._d.videoMixer.config.modes.f1080i59_94 = boolBit(flags, 7)
        self._d.videoMixer.config.modes.f1080p23_98 = boolBit(flags, 8)
        self._d.videoMixer.config.modes.f1080p24 = boolBit(flags, 9)
        self._d.videoMixer.config.modes.f1080p25 = boolBit(flags, 10)
        self._d.videoMixer.config.modes.f1080p29_97 = boolBit(flags, 11)
        self._d.videoMixer.config.modes.f1080p50 = boolBit(flags, 12)
        self._d.videoMixer.config.modes.f1080p59_94 = boolBit(flags, 13)
        self._d.videoMixer.config.modes.f2160p23_98 = boolBit(flags, 14)
        self._d.videoMixer.config.modes.f2160p24 = boolBit(flags, 15)
        self._d.videoMixer.config.modes.f2160p25 = boolBit(flags, 16)
        self._d.videoMixer.config.modes.f2160p29_97 = boolBit(flags, 17)


    def _handle_MAC(self) -> None:
        self._d.macro.pool.banks = self._inBuf.getU8(0)


    def _handlePowr(self) -> None:
        self._d.power.status.main = self._inBuf.getU8Flag(0, 0)
        self._d.power.status.backup = self._inBuf.getU8Flag(0, 1)


    def _handleDcOt(self) -> None:
        self._d.downConverter.mode = self._getBufEnum(0, 8, self._p.downConverterModes)


    def _handleVidM(self) -> None:
        self._d.videoMode.format = self._getBufEnum(0, 8, self._p.videoModeFormats)


    def _handleInPr(self) -> None:
        videoSource = self._getBufVideoSource(0)

        self._d.inputProperties[videoSource].longName = self._inBuf.getString(2, 20)
        self._d.inputProperties[videoSource].shortName = self._inBuf.getString(22, 4)

        self._d.inputProperties[videoSource].availableExternalPortTypes.sdi = self._inBuf.getU8Flag(27, 0)
        self._d.inputProperties[videoSource].availableExternalPortTypes.hdmi = self._inBuf.getU8Flag(27, 1)
        self._d.inputProperties[videoSource].availableExternalPortTypes.component = self._inBuf.getU8Flag(27, 2)
        self._d.inputProperties[videoSource].availableExternalPortTypes.composite = self._inBuf.getU8Flag(27, 3)
        self._d.inputProperties[videoSource].availableExternalPortTypes.sVideo = self._inBuf.getU8Flag(27, 4)

        self._d.inputProperties[videoSource].externalPortType = self._getBufEnum(29, 8, self._p.externalPortTypes)

        self._d.inputProperties[videoSource].portType = self._getBufEnum(30, 8, self._p.switcherPortTypes)

        self._d.inputProperties[videoSource].availability.auxiliary = self._inBuf.getU8Flag(34, 0)
        self._d.inputProperties[videoSource].availability.multiviewer = self._inBuf.getU8Flag(34, 1)
        self._d.inputProperties[videoSource].availability.superSourceArt = self._inBuf.getU8Flag(34, 2)
        self._d.inputProperties[videoSource].availability.superSourceBox = self._inBuf.getU8Flag(34, 3)
        self._d.inputProperties[videoSource].availability.keySourcesEverywhere = self._inBuf.getU8Flag(34, 4)

        self._d.inputProperties[videoSource].mEAvailability.mE1FillSources = self._inBuf.getU8Flag(35, 0)
        self._d.inputProperties[videoSource].mEAvailability.mE2FillSources = self._inBuf.getU8Flag(35, 1)


    def _handleMvPr(self) -> None:
        multiViewer = self._getBufEnum(0, 8, self._p.multiViewers)
        self._d.multiViewer.properties[multiViewer].layout = self._getBufEnum(1, 8, self._p.multiViewerLayouts)


    def _handleMvIn(self) -> None:
        multiViewer = self._getBufEnum(0, 8, self._p.multiViewers)
        windowIndex = self._getBufEnum(1, 8, self._p.windows)
        self._d.multiViewer.input[multiViewer][windowIndex].videoSource = self._getBufVideoSource(2)


    def _handlePrgI(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.programInput[mE].videoSource = self._getBufVideoSource(2)


    def _handlePrvI(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.previewInput[mE].videoSource = self._getBufVideoSource(2)


    def _handleTrSS(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].style = self._getBufEnum(1, 8, self._p.transitionStyles)
        self._d.transition[mE].nextTransition.background = self._inBuf.getU8Flag(2, 0)
        self._d.transition[mE].nextTransition.key1 = self._inBuf.getU8Flag(2, 1)
        self._d.transition[mE].nextTransition.key2 = self._inBuf.getU8Flag(2, 2)
        self._d.transition[mE].nextTransition.key3 = self._inBuf.getU8Flag(2, 3)
        self._d.transition[mE].nextTransition.key4 = self._inBuf.getU8Flag(2, 4)
        self._d.transition[mE].styleNext = self._getBufEnum(3, 8, self._p.transitionStyles)
        self._d.transition[mE].nextTransitionNext.background = self._inBuf.getU8Flag(4, 0)
        self._d.transition[mE].nextTransitionNext.key1 = self._inBuf.getU8Flag(4, 1)
        self._d.transition[mE].nextTransitionNext.key2 = self._inBuf.getU8Flag(4, 2)
        self._d.transition[mE].nextTransitionNext.key3 = self._inBuf.getU8Flag(4, 3)
        self._d.transition[mE].nextTransitionNext.key4 = self._inBuf.getU8Flag(4, 4)


    def _handleTrPr(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].preview.enabled = self._inBuf.getU8Flag(1, 0)


    def _handleTrPs(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].inTransition = self._inBuf.getU8Flag(1, 0)
        self._d.transition[mE].framesRemaining = self._inBuf.getU8(2)
        self._d.transition[mE].position = self._inBuf.getU16(4)


    def _handleTMxP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].mix.rate = self._inBuf.getU8(1)


    def _handleTDpP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].dip.rate = self._inBuf.getU8(1)
        self._d.transition[mE].dip.input = self._getBufVideoSource(2)


    def _handleTWpP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].wipe.rate = self._inBuf.getU8(1)
        self._d.transition[mE].wipe.pattern = self._getBufEnum(2, 8, self._p.patternStyles)
        self._d.transition[mE].wipe.width = self._inBuf.getFloat(4, False, 16, 100)
        self._d.transition[mE].wipe.fillSource = self._getBufVideoSource(6)
        self._d.transition[mE].wipe.symmetry = self._inBuf.getFloat(8, False, 16, 100)
        self._d.transition[mE].wipe.softness = self._inBuf.getFloat(10, False, 16, 100)
        self._d.transition[mE].wipe.position.x = self._inBuf.getFloat(12, False, 16, 10000)
        self._d.transition[mE].wipe.position.y = self._inBuf.getFloat(14, False, 16, 10000)
        self._d.transition[mE].wipe.reverse = self._inBuf.getU8Flag(16, 0)
        self._d.transition[mE].wipe.flipFlop = self._inBuf.getU8Flag(17, 0)


    def _handleTDvP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].dVE.rate = self._inBuf.getU8(1)
        self._d.transition[mE].dVE.style = self._getBufEnum(3, 8, self._p.dVETransitionStyles)
        self._d.transition[mE].dVE.fillSource = self._getBufVideoSource(4)
        self._d.transition[mE].dVE.keySource = self._getBufVideoSource(6)
        self._d.transition[mE].dVE.enableKey = self._inBuf.getU8Flag(8, 0)
        self._d.transition[mE].dVE.preMultiplied = self._inBuf.getU8Flag(9, 0)
        self._d.transition[mE].dVE.clip = self._inBuf.getFloat(10, False, 16, 10)
        self._d.transition[mE].dVE.gain = self._inBuf.getFloat(12, False, 16, 10)
        self._d.transition[mE].dVE.invertKey = self._inBuf.getU8Flag(14, 0)
        self._d.transition[mE].dVE.reverse = self._inBuf.getU8Flag(15, 0)
        self._d.transition[mE].dVE.flipFlop = self._inBuf.getU8Flag(16, 0)


    def _handleTStP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.transition[mE].stinger.source = self._getBufEnum(1, 8, self._p.mediaPlayers)
        self._d.transition[mE].stinger.preMultiplied = self._inBuf.getU8Flag(2, 0)
        self._d.transition[mE].stinger.clip = self._inBuf.getFloat(4, False, 16, 10)
        self._d.transition[mE].stinger.gain = self._inBuf.getFloat(6, False, 16, 10)
        self._d.transition[mE].stinger.invertKey = self._inBuf.getU8Flag(8, 0)
        self._d.transition[mE].stinger.preRoll = self._inBuf.getU16(10)
        self._d.transition[mE].stinger.clipDuration = self._inBuf.getU16(12)
        self._d.transition[mE].stinger.triggerPoint = self._inBuf.getU16(14)
        self._d.transition[mE].stinger.mixRate = self._inBuf.getU16(16)


    def _handleKeOn(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.keyer[mE][keyer].onAir.enabled = self._inBuf.getU8Flag(2, 0)


    def _handleKeBP(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.keyer[mE][keyer].type = self._getBufEnum(2, 8, self._p.keyerTypes)
        self._d.keyer[mE][keyer].fly.enabled = self._inBuf.getU8Flag(5, 0)
        self._d.keyer[mE][keyer].fillSource = self._getBufVideoSource(6)
        self._d.keyer[mE][keyer].keySource = self._getBufVideoSource(8)
        self._d.keyer[mE][keyer].masked = self._inBuf.getU8Flag(10, 0)
        self._d.keyer[mE][keyer].top = self._inBuf.getFloat(12, True, 16, 1000)
        self._d.keyer[mE][keyer].bottom = self._inBuf.getFloat(14, True, 16, 1000)

        value = self._inBuf.getS16(16)
        self._d.keyer[mE][keyer].left = mapValue(value, -16000, 16000, -9.0, 9.0)

        value = self._inBuf.getS16(18)
        self._d.keyer[mE][keyer].right = mapValue(value, -16000, 16000, -9.0, 9.0)


    def _handleKeLm(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.key[mE][keyer].luma.preMultiplied = self._inBuf.getU8Flag(2, 0)
        self._d.key[mE][keyer].luma.clip = self._inBuf.getFloat(4, False, 16, 10)
        self._d.key[mE][keyer].luma.gain = self._inBuf.getFloat(6, False, 16, 10)
        self._d.key[mE][keyer].luma.invertKey = self._inBuf.getU8Flag(8, 0)


    def _handleKeCk(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.key[mE][keyer].chroma.hue = self._inBuf.getFloat(2, False, 16, 10)
        self._d.key[mE][keyer].chroma.gain = self._inBuf.getFloat(4, False, 16, 10)
        self._d.key[mE][keyer].chroma.ySuppress = self._inBuf.getFloat(6, False, 16, 10)
        self._d.key[mE][keyer].chroma.lift = self._inBuf.getFloat(8, False, 16, 10)
        self._d.key[mE][keyer].chroma.narrow = self._inBuf.getU8Flag(10, 0)


    def _handleKePt(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.key[mE][keyer].pattern.pattern = self._getBufEnum(2, 8, self._p.patternStyles)
        self._d.key[mE][keyer].pattern.size = self._inBuf.getFloat(4, False, 16, 100)
        self._d.key[mE][keyer].pattern.symmetry = self._inBuf.getFloat(6, False, 16, 100)
        self._d.key[mE][keyer].pattern.softness = self._inBuf.getFloat(8, False, 16, 100)
        self._d.key[mE][keyer].pattern.position.x = self._inBuf.getFloat(10, False, 16, 10000)
        self._d.key[mE][keyer].pattern.position.y = self._inBuf.getFloat(12, False, 16, 10000)
        self._d.key[mE][keyer].pattern.invertPattern = self._inBuf.getU8Flag(14, 0)


    def _handleKeDV(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.key[mE][keyer].dVE.size.x = self._inBuf.getFloat(4, False, 32, 1000)
        self._d.key[mE][keyer].dVE.size.y = self._inBuf.getFloat(8, False, 32, 1000)
        self._d.key[mE][keyer].dVE.position.x = self._inBuf.getFloat(12, True, 32, 1000)
        self._d.key[mE][keyer].dVE.position.y = self._inBuf.getFloat(16, True, 32, 1000)
        self._d.key[mE][keyer].dVE.rotation = self._inBuf.getFloat(20, False, 32, 10)
        self._d.key[mE][keyer].dVE.border.enabled = self._inBuf.getU8Flag(24, 0)
        self._d.key[mE][keyer].dVE.shadow = self._inBuf.getU8Flag(25, 0)
        self._d.key[mE][keyer].dVE.border.bevel.type = self._getBufEnum(26, 8, self._p.borderBevels)
        self._d.key[mE][keyer].dVE.border.outer.width = self._inBuf.getFloat(28, False, 16, 100)
        self._d.key[mE][keyer].dVE.border.inner.width = self._inBuf.getFloat(30, False, 16, 100)
        self._d.key[mE][keyer].dVE.border.outer.softness = self._inBuf.getU8(32)
        self._d.key[mE][keyer].dVE.border.inner.softness = self._inBuf.getU8(33)
        self._d.key[mE][keyer].dVE.border.bevel.softness = self._inBuf.getFloat(34, False, 8, 100)
        self._d.key[mE][keyer].dVE.border.bevel.position = self._inBuf.getFloat(35, False, 8, 100)
        self._d.key[mE][keyer].dVE.border.opacity = self._inBuf.getU8(36)
        self._d.key[mE][keyer].dVE.border.hue = self._inBuf.getFloat(38, False, 16, 10)
        self._d.key[mE][keyer].dVE.border.saturation = self._inBuf.getFloat(40, False, 16, 10)
        self._d.key[mE][keyer].dVE.border.luma = self._inBuf.getFloat(42, False, 16, 10)
        self._d.key[mE][keyer].dVE.lightSource.direction = self._inBuf.getFloat(44, False, 16, 10)
        self._d.key[mE][keyer].dVE.lightSource.altitude = self._inBuf.getU8(46)
        self._d.key[mE][keyer].dVE.masked = self._inBuf.getU8Flag(47, 0)
        self._d.key[mE][keyer].dVE.top = self._inBuf.getFloat(48, True, 16, 1000)
        self._d.key[mE][keyer].dVE.bottom = self._inBuf.getFloat(50, True, 16, 1000)

        value = self._inBuf.getS16(52)
        self._d.key[mE][keyer].dVE.left = mapValue(value, -16000, 16000, -9.0, 9.0)

        value = self._inBuf.getS16(54)
        self._d.key[mE][keyer].dVE.right = mapValue(value, -16000, 16000, -9.0, 9.0)

        self._d.key[mE][keyer].dVE.rate = self._inBuf.getU8(56)


    def _handleKeFS(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        self._d.keyer[mE][keyer].fly.isASet = self._inBuf.getU8Flag(2, 0)
        self._d.keyer[mE][keyer].fly.isBSet = self._inBuf.getU8Flag(3, 0)
        self._d.keyer[mE][keyer].fly.isAtKeyFrame.a = self._inBuf.getU8Flag(6, 0)
        self._d.keyer[mE][keyer].fly.isAtKeyFrame.b = self._inBuf.getU8Flag(6, 1)
        self._d.keyer[mE][keyer].fly.isAtKeyFrame.full = self._inBuf.getU8Flag(6, 2)
        self._d.keyer[mE][keyer].fly.isAtKeyFrame.runToInfinite = self._inBuf.getU8Flag(6, 3)
        self._d.keyer[mE][keyer].fly.runtoInfiniteindex = self._inBuf.getU8(7)


    def _handleKKFP(self) -> None:
        mE = self._getBufMixEffect(0)
        keyer = self._getBufKeyer(1)
        keyFrame = self._getBufEnum(2, 8, self._p.keyFrames)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].size.x = self._inBuf.getFloat(4, False, 32, 1000)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].size.y = self._inBuf.getFloat(8, False, 32, 1000)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].position.x = self._inBuf.getFloat(12, True, 32, 1000)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].position.y = self._inBuf.getFloat(16, True, 32, 1000)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].rotation = self._inBuf.getFloat(20, False, 32, 10)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.outer.width = self._inBuf.getFloat(24, False, 16, 100)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.inner.width = self._inBuf.getFloat(26, False, 16, 100)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.outer.softness = self._inBuf.getU8(28)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.inner.softness = self._inBuf.getU8(29)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.bevel.softness = self._inBuf.getFloat(30, False, 8, 100)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.bevel.position = self._inBuf.getFloat(31, False, 8, 100)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.opacity = self._inBuf.getU8(32)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.hue = self._inBuf.getFloat(34, False, 16, 10)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.saturation = self._inBuf.getFloat(36, False, 16, 10)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].border.luma = self._inBuf.getFloat(38, False, 16, 10)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].lightSource.direction = self._inBuf.getFloat(40, False, 16, 10)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].lightSource.altitude = self._inBuf.getU8(42)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].top = self._inBuf.getFloat(44, True, 16, 1000)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].bottom = self._inBuf.getFloat(46, True, 16, 1000)

        value = self._inBuf.getS16(48)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].left = mapValue(value, -16000, 16000, -9.0, 9.0)

        value = self._inBuf.getS16(50)
        self._d.keyer[mE][keyer].fly.keyFrame[keyFrame].right = mapValue(value, -16000, 16000, -9.0, 9.0)



    def _handleDskB(self) -> None:
        dsk = self._getBufDsk(0)
        self._d.downstreamKeyer[dsk].fillSource = self._getBufVideoSource(2)
        self._d.downstreamKeyer[dsk].keySource = self._getBufVideoSource(4)


    def _handleDskP(self) -> None:
        dsk = self._getBufDsk(0)
        self._d.downstreamKeyer[dsk].tie = self._inBuf.getU8Flag(1, 0)
        self._d.downstreamKeyer[dsk].rate = self._inBuf.getU8(2)
        self._d.downstreamKeyer[dsk].preMultiplied = self._inBuf.getU8Flag(3, 0)
        self._d.downstreamKeyer[dsk].clip = self._inBuf.getFloat(4, False, 16, 10)
        self._d.downstreamKeyer[dsk].gain = self._inBuf.getFloat(6, False, 16, 10)
        self._d.downstreamKeyer[dsk].invertKey = self._inBuf.getU8Flag(8, 0)
        self._d.downstreamKeyer[dsk].masked = self._inBuf.getU8Flag(9, 0)
        self._d.downstreamKeyer[dsk].top = self._inBuf.getFloat(10, True, 16, 1000)
        self._d.downstreamKeyer[dsk].bottom = self._inBuf.getFloat(12, True, 16, 1000)

        value = self._inBuf.getS16(4)
        self._d.downstreamKeyer[dsk].left = mapValue(value, -16000, 16000, -9.0, 9.0)

        value = self._inBuf.getS16(16)
        self._d.downstreamKeyer[dsk].right = mapValue(value, -16000, 16000, -9.0, 9.0)


    def _handleDskS(self) -> None:
        dsk = self._getBufDsk(0)
        self._d.downstreamKeyer[dsk].onAir = self._inBuf.getU8Flag(1, 0)
        self._d.downstreamKeyer[dsk].inTransition = self._inBuf.getU8Flag(2, 0)
        self._d.downstreamKeyer[dsk].isAutoTransitioning = self._inBuf.getU8Flag(3, 0)
        self._d.downstreamKeyer[dsk].framesRemaining = self._inBuf.getU8(4)


    def _handleFtbP(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.fadeToBlack[mE].rate = self._inBuf.getU8(1)


    def _handleFtbS(self) -> None:
        mE = self._getBufMixEffect(0)
        self._d.fadeToBlack[mE].state.fullyBlack = self._inBuf.getU8Flag(1, 0)
        self._d.fadeToBlack[mE].state.inTransition = self._inBuf.getU8Flag(2, 0)
        self._d.fadeToBlack[mE].state.framesRemaining = self._inBuf.getU8(3)


    def _handleColV(self) -> None:
        colorGenerator = self._getBufEnum(0, 8, self._p.colorGenerators)
        self._d.colorGenerator[colorGenerator].hue = self._inBuf.getFloat(2, False, 16, 10)
        self._d.colorGenerator[colorGenerator].saturation = self._inBuf.getFloat(4, False, 16, 10)
        self._d.colorGenerator[colorGenerator].luma = self._inBuf.getFloat(6, False, 16, 10)


    def _handleAuxS(self) -> None:
        aUXChannel = self._getBufEnum(0, 8, self._p.auxChannels)
        self._d.auxSource[aUXChannel].input = self._getBufVideoSource(2)


    def _handleCCdP(self) -> None:
        camera = self._getBufEnum(0, 8, self._p.cameras)
        feature = self._inBuf.getU8(2)
        adjustmentDomain = self._inBuf.getU8(1)
        DOM_LENS = 0
        DOM_CAMERA = 1
        DOM_COLORBARS = 4
        DOM_CHIP = 8

        if adjustmentDomain == DOM_LENS:
            FEAT_LENS_FOCUS = 0
            # FEAT_LENS_AUTOFOCUSED = 1    # Documented, but not implemented
            FEAT_LENS_IRIS = 3
            FEAT_LENS_ZOOMNORMALIZED = 8 # Not docummented
            FEAT_LENS_ZOOM = 9

            if feature == FEAT_LENS_IRIS:
                self._d.cameraControl[camera].iris = self._inBuf.getS16(16)
            elif feature == FEAT_LENS_FOCUS:
                self._d.cameraControl[camera].focus = self._inBuf.getS16(16)
            elif feature == FEAT_LENS_ZOOMNORMALIZED:
                self._d.cameraControl[camera].zoom.normalized = self._inBuf.getFloat(16, True, 16, 10)
            elif feature == FEAT_LENS_ZOOM:
                value = self._inBuf.getS16(16)
                self._d.cameraControl[camera].zoom.speed = mapValue(value, -2048, 2048, 0.0, 1.0)
            else:
                self._sw.log.warn(f"UNKNOWN lens feature ({feature})")

        elif adjustmentDomain == DOM_CAMERA:
            FEAT_CAMERA_GAIN = 1
            FEAT_CAMERA_WHITEBALANCE = 2
            FEAT_CAMERA_SHUTTER = 5
            FEAT_CAMERA_DETAIL = 8 # Docummented in LibAtem/LibAtem

            if feature == FEAT_CAMERA_GAIN:
                self._d.cameraControl[camera].gain.value = self._inBuf.getS16(16)
            elif feature == FEAT_CAMERA_WHITEBALANCE:
                self._d.cameraControl[camera].whiteBalance = self._inBuf.getS16(16)
            elif feature == FEAT_CAMERA_SHUTTER:
                self._d.cameraControl[camera].shutter = self._inBuf.getFloat(18, True, 16, 1000000)
            elif feature == FEAT_CAMERA_DETAIL:
                self._d.cameraControl[camera].sharpeningLevel = self._inBuf.getS16(16)
            else:
                self._sw.log.warn(f"UNKNOWN camera feature ({feature})")

        elif adjustmentDomain == DOM_COLORBARS:
            FEAT_COLORBARS = 4 # Not docummented

            if feature == FEAT_COLORBARS:
                self._d.cameraControl[camera].colorbars = self._inBuf.getS16(16)
            else:
                self._sw.log.warn(f"UNKNOWN colorBars feature ({feature})")

        elif adjustmentDomain == DOM_CHIP:
            FEAT_CHIP_LIFT = 0
            FEAT_CHIP_GAMMA = 1
            FEAT_CHIP_GAIN = 2
            # FEAT_CHIP_APERTURE = 3    # Documented, but not implemented
            FEAT_CHIP_CONTRAST = 4
            FEAT_CHIP_LUMMIX = 5
            FEAT_CHIP_HUESATURATION = 6

            if feature == FEAT_CHIP_LIFT:
                valueR = self._inBuf.getS16(16)
                valueG = self._inBuf.getS16(18)
                valueB = self._inBuf.getS16(20)
                valueY = self._inBuf.getS16(22)
                self._d.cameraControl[camera].lift.r = mapValue(valueR, -4096, 4096, -1.0, 1.0)
                self._d.cameraControl[camera].lift.g = mapValue(valueG, -4096, 4096, -1.0, 1.0)
                self._d.cameraControl[camera].lift.b = mapValue(valueB, -4096, 4096, -1.0, 1.0)
                self._d.cameraControl[camera].lift.y = mapValue(valueY, -4096, 4096, -1.0, 1.0)
            elif feature == FEAT_CHIP_GAMMA:
                valueR = self._inBuf.getS16(16)
                valueG = self._inBuf.getS16(18)
                valueB = self._inBuf.getS16(20)
                valueY = self._inBuf.getS16(22)
                self._d.cameraControl[camera].gamma.r = mapValue(valueR, -8192, 8192, -1.0, 1.0)
                self._d.cameraControl[camera].gamma.g = mapValue(valueG, -8192, 8192, -1.0, 1.0)
                self._d.cameraControl[camera].gamma.b = mapValue(valueB, -8192, 8192, -1.0, 1.0)
                self._d.cameraControl[camera].gamma.y = mapValue(valueY, -8192, 8192, -1.0, 1.0)
            elif feature == FEAT_CHIP_GAIN:
                valueR = self._inBuf.getS16(16)
                valueG = self._inBuf.getS16(18)
                valueB = self._inBuf.getS16(20)
                valueY = self._inBuf.getS16(22)
                self._d.cameraControl[camera].gain.r = mapValue(valueR, 0, 32767, 0.0, 16.0)
                self._d.cameraControl[camera].gain.g = mapValue(valueG, 0, 32767, 0.0, 16.0)
                self._d.cameraControl[camera].gain.b = mapValue(valueB, 0, 32767, 0.0, 16.0)
                self._d.cameraControl[camera].gain.y = mapValue(valueY, 0, 32767, 0.0, 16.0)
            elif feature == FEAT_CHIP_CONTRAST:
                self._d.cameraControl[camera].contrast = self._inBuf.getS16(18)
            elif feature == FEAT_CHIP_LUMMIX:
                lummix_value = self._inBuf.getS16(16)
                self._d.cameraControl[camera].lumMix = mapValue(lummix_value, 0, 2048, 0, 100)
            elif feature == FEAT_CHIP_HUESATURATION:
                hue_value = self._inBuf.getS16(16)
                saturation_value = self._inBuf.getS16(18)
                self._d.cameraControl[camera].hue = mapValue(hue_value, -2048, 2048, 0, 360)
                self._d.cameraControl[camera].saturation = mapValue(saturation_value, 0, 4096, 0, 100)
            else:
                self._sw.log.warn(f"UNKNOWN chip feature ({feature})")


    def _handleRCPS(self) -> None:
        mediaPlayer = self._getBufEnum(0, 8, self._p.mediaPlayers)
        self._d.clipPlayer[mediaPlayer].playing = self._inBuf.getU8Flag(1, 0)
        self._d.clipPlayer[mediaPlayer].loop = self._inBuf.getU8Flag(2, 0)
        self._d.clipPlayer[mediaPlayer].atBeginning = self._inBuf.getU8Flag(3, 0)
        self._d.clipPlayer[mediaPlayer].clipFrame = self._inBuf.getU16(4)


    def _handleMPCE(self) -> None:
        mediaPlayer = self._getBufEnum(0, 8, self._p.mediaPlayers)
        self._d.mediaPlayer.source[mediaPlayer].type = self._getBufEnum(1, 8, self._p.mediaPlayerSourceTypes)
        self._d.mediaPlayer.source[mediaPlayer].stillIndex = self._inBuf.getU8(2)
        self._d.mediaPlayer.source[mediaPlayer].clipIndex = self._inBuf.getU8(3)


    def _handleMPSp(self) -> None:
        self._d.mediaPoolStorage.clip1MaxLength = self._inBuf.getU16(0)
        self._d.mediaPoolStorage.clip2MaxLength = self._inBuf.getU16(2)


    def _handleMPCS(self) -> None:
        clipBank = self._getBufEnum(0, 8, self._p.clipBanks)
        self._d.mediaPlayer.clipSource[clipBank].isUsed = self._inBuf.getU8Flag(1, 0)
        self._d.mediaPlayer.clipSource[clipBank].fileName = self._inBuf.getString(2, 16)
        self._d.mediaPlayer.clipSource[clipBank].frames = self._inBuf.getU16(66)


    def _handleMPAS(self) -> None:
        clipBank = self._getBufEnum(0, 8, self._p.clipBanks)
        self._d.mediaPlayer.audioSource[clipBank].isUsed = self._inBuf.getU8Flag(1, 0)
        self._d.mediaPlayer.audioSource[clipBank].fileName = self._inBuf.getString(18, 16)


    def _handleMPfe(self) -> None:
        stillBank = self._getBufEnum(3, 8, self._p.stillBanks)
        if self._inBuf.getU8(0) == 0:
            self._d.mediaPlayer.stillFile[stillBank].isUsed = self._inBuf.getU8Flag(4, 0)
            fileNameLen = self._inBuf.getU8(23)
            if fileNameLen > 0:
                self._d.mediaPlayer.stillFile[stillBank].fileName = self._inBuf.getString(24, fileNameLen)


    def _handleMRPr(self) -> None:
        self._d.macro.runStatus.state.running = self._inBuf.getU8Flag(0, 0)
        self._d.macro.runStatus.state.waiting = self._inBuf.getU8Flag(0, 1)
        self._d.macro.runStatus.isLooping = self._inBuf.getU8Flag(1, 0)
        self._d.macro.runStatus.index = self._inBuf.getU16(2)


    def _handleMPrp(self) -> None:
        macroIndex = self._getBufEnum(1, 8, self._p.macros)
        self._d.macro.properties[macroIndex].isUsed = self._inBuf.getU8Flag(2, 0)
        bytecount = self._inBuf.getU8(5)
        self._d.macro.properties[macroIndex].name = self._inBuf.getString(8, bytecount)


    def _handleMRcS(self) -> None:
        self._d.macro.recordingStatus.isRecording = self._inBuf.getU8Flag(0, 0)
        self._d.macro.recordingStatus.index = self._inBuf.getU16(2)


    def _handleSSrc(self) -> None:
        self._d.superSource.fillSource = self._getBufVideoSource(0)
        self._d.superSource.keySource = self._getBufVideoSource(2)
        self._d.superSource.foreground = self._inBuf.getU8Flag(4, 0)
        self._d.superSource.preMultiplied = self._inBuf.getU8Flag(5, 0)
        self._d.superSource.clip = self._inBuf.getFloat(6, False, 16, 10)
        self._d.superSource.gain = self._inBuf.getFloat(8, False, 16, 10)
        self._d.superSource.invertKey = self._inBuf.getU8Flag(10, 0)
        self._d.superSource.border.enabled = self._inBuf.getU8Flag(11, 0)
        self._d.superSource.border.bevel.value = self._getBufEnum(12, 8, self._p.borderBevels)
        self._d.superSource.border.outer.width = self._inBuf.getFloat(14, False, 16, 100)
        self._d.superSource.border.inner.width = self._inBuf.getFloat(16, False, 16, 100)
        self._d.superSource.border.outer.softness = self._inBuf.getU8(18)
        self._d.superSource.border.inner.softness = self._inBuf.getU8(19)
        self._d.superSource.border.bevel.softness = self._inBuf.getFloat(20, False, 8, 100)
        self._d.superSource.border.bevel.position = self._inBuf.getFloat(21, False, 8, 100)
        self._d.superSource.border.hue = self._inBuf.getFloat(22, False, 16, 10)
        self._d.superSource.border.saturation = self._inBuf.getFloat(24, False, 16, 10)
        self._d.superSource.border.luma = self._inBuf.getFloat(26, False, 16, 10)
        self._d.superSource.lightSource.direction = self._inBuf.getFloat(28, False, 16, 10)
        self._d.superSource.lightSource.altitude = self._inBuf.getU8(30)


    def _handleSSBP(self) -> None:
        box = self._getBufEnum(3, 8, self._p.boxes)
        self._d.superSource.boxParameters[box].enabled = self._inBuf.getU8Flag(1, 0)
        self._d.superSource.boxParameters[box].inputSource = self._getBufVideoSource(2)
        self._d.superSource.boxParameters[box].position.x = self._inBuf.getFloat(4, True, 16, 100)
        self._d.superSource.boxParameters[box].position.y = self._inBuf.getFloat(6, True, 16, 100)
        self._d.superSource.boxParameters[box].size = self._inBuf.getFloat(8, False, 16, 100)
        self._d.superSource.boxParameters[box].cropped = self._inBuf.getU8Flag(10, 0)
        self._d.superSource.boxParameters[box].crop.top = self._inBuf.getFloat(12, False, 16, 1000)
        self._d.superSource.boxParameters[box].crop.bottom = self._inBuf.getFloat(14, False, 16, 1000)
        self._d.superSource.boxParameters[box].crop.left = self._inBuf.getFloat(16, False, 16, 1000)
        self._d.superSource.boxParameters[box].crop.right = self._inBuf.getFloat(18, False, 16, 1000)


    def _handleAMIP(self) -> None:
        audioSource = self._getBufAudioSource(0)
        self._d.audioMixer.input[audioSource].type = self._getBufEnum(2, 8, self._p.audioMixerInputTypes)
        self._d.audioMixer.input[audioSource].fromMediaPlayer = self._inBuf.getU8Flag(6, 0)
        self._d.audioMixer.input[audioSource].plugtype = self._getBufEnum(7, 8, self._p.audioMixerInputPlugTypes)
        self._d.audioMixer.input[audioSource].mixOption = self._getBufEnum(8, 8, self._p.audioMixerInputMixOptions)
        self._d.audioMixer.input[audioSource].volume = self._p.audioWord2Db(self._inBuf.getU16(10))
        self._d.audioMixer.input[audioSource].balance = self._inBuf.getFloat(12, True, 16, 10000)


    def _handleAMMO(self) -> None:
        self._d.audioMixer.master.volume = self._p.audioWord2Db(self._inBuf.getU16(0))


    def _handleAMmO(self) -> None:
        self._d.audioMixer.monitor.monitorAudio = self._inBuf.getU8Flag(0, 0)
        self._d.audioMixer.monitor.volume = self._p.audioWord2Db(self._inBuf.getU16(2))
        self._d.audioMixer.monitor.mute = self._inBuf.getU8Flag(4, 0)
        self._d.audioMixer.monitor.solo = self._inBuf.getU8Flag(5, 0)
        self._d.audioMixer.monitor.soloInput = self._getBufAudioSource(6)
        self._d.audioMixer.monitor.dim = self._inBuf.getU8Flag(8, 0)


    def _handleAMLv(self) -> None:

        # This handler does NOT use autoReadBuffer
        self._sw._read2InBuf(36)

        numSources = self._inBuf.getU16(0)
        self._d.audioMixer.levels.numSources = numSources
        self._d.audioMixer.levels.master.left = self._inBuf.getU16(5)         # 4 bytes in docs (?)
        self._d.audioMixer.levels.master.right = self._inBuf.getU16(9)        # 4 bytes in docs (?)
        self._d.audioMixer.levels.master.peak.left = self._inBuf.getU16(13)   # 4 bytes in docs (?)
        self._d.audioMixer.levels.master.peak.right = self._inBuf.getU16(17)  # 4 bytes in docs (?)
        self._d.audioMixer.levels.monitor = self._inBuf.getU16(21)            # 4 bytes in docs (?)

        self._sw._read2InBuf(numSources*2)
        audioSources = []
        for a in range(numSources):
            audioSources[a] = self._inBuf.getU16(a<<1)

        # We must read 4-byte chunks, so compensate if sources was an odd number
        if numSources & 1:
            self._sw._read2InBuf(2)

        for a in range(numSources):
            self._sw._read2InBuf(16)
            self._d.audioMixer.levels.sources[audioSources[a]].left = self._inBuf.getU16(1)         # 4 bytes in docs (?)
            self._d.audioMixer.levels.sources[audioSources[a]].right = self._inBuf.getU16(5)        # 4 bytes in docs (?)
            self._d.audioMixer.levels.sources[audioSources[a]].peak.left = self._inBuf.getU16(9)    # 4 bytes in docs (?)
            self._d.audioMixer.levels.sources[audioSources[a]].peak.right = self._inBuf.getU16(13)  # 4 bytes in docs (?)


    def _handleAMTl(self) -> None:
        numAudioSources = self._inBuf.getU16(0)
        if numAudioSources >= len(self._p.audioSources):
            self._sw.log.debug(f"UNKNOWN numAudioSources ({numAudioSources}) in [{self.cmdStr}]")
            return

        self._d.audioMixer.tally.numSources = numAudioSources

        for a in range(numAudioSources):
            byteOffset = 2+(3*a)
            audioSource = self._getBufAudioSource(byteOffset).value
            self._d.audioMixer.tally.sources[audioSource].isMixedIn = self._inBuf.getU8Flag(byteOffset+2, 0)


    def _handleTlIn(self) -> None:
        numVideoSources = self._inBuf.getU16(0)
        if numVideoSources >= len(self._p.videoSources):
            self._sw.log.debug(f"UNKNOWN numVideoSources ({numVideoSources}) in [{self.cmdStr}]")
            return

        self._d.tally.byIndex.sources = numVideoSources
        for a in range(numVideoSources):
            self._d.tally.byIndex.flags[a].program = self._inBuf.getU8Flag(2+a, 0)
            self._d.tally.byIndex.flags[a].preview = self._inBuf.getU8Flag(2+a, 1)


    def _handleTlSr(self) -> None:

        # This handler does NOT use autoReadBuffer
        readBytesForTlSr = int(((self._p.inputBufferLength-2)/3)*3+2)
        self._sw._read2InBuf(readBytesForTlSr)

        numVideoSources = self._inBuf.getU16(0)
        if numVideoSources >= len(self._p.videoSources):
            self._sw.log.debug(f"UNKNOWN numVideoSources ({numVideoSources}) in [{self.cmdStr}]")
            return

        self._d.tally.bySource.sources = numVideoSources

        readBytesForTlSr = len(self._inBuf)
        readComp = 2
        for a in range(numVideoSources):
            if 2+(3*a) == readBytesForTlSr:
                readComp -= readBytesForTlSr
                self._sw._read2InBuf()

            byteOffset = readComp+(3*a)
            videoSource = self._getBufVideoSource(byteOffset).value
            self._d.tally.bySource.flags[videoSource].program = self._inBuf.getU8Flag(byteOffset+2, 0)
            self._d.tally.bySource.flags[videoSource].preview = self._inBuf.getU8Flag(byteOffset+2, 1)


    def _handleTime(self) -> None:
        self._d.lastStateChange.timeCode.hour = self._inBuf.getU8(0)
        self._d.lastStateChange.timeCode.minute = self._inBuf.getU8(1)
        self._d.lastStateChange.timeCode.second = self._inBuf.getU8(2)
        self._d.lastStateChange.timeCode.frame = self._inBuf.getU8(3)


    def _handleNOTIMPLEMENTED(self) -> None:
        pass
