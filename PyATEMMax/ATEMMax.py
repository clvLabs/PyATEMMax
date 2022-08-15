#!/usr/bin/env python3
# coding: utf-8
"""
ATEMMax: Blackmagic ATEM switcher manager class.
Part of the PyATEMMax library.
"""

# pylint: disable=too-many-lines, wildcard-import, unused-wildcard-import, protected-access


from typing import Dict, Any, Union

import logging

from .ATEMConstant import ATEMConstant
from .ATEMConnectionManager import ATEMConnectionManager
from .ATEMCommandHandlers import ATEMCommandHandlers
from .ATEMSetterMethods import ATEMSetterMethods
from .ATEMSwitcherState import ATEMSwitcherState
from .ATEMProtocolEnums import *
from .StateData import *


class ATEMMax(ATEMConnectionManager, ATEMSwitcherState, ATEMSetterMethods):
    """Blackmagic ATEM switcher manager

    This class is a port of Skårhøj's ATEMmax class.
    """

    def __init__(self):
        """Create a new ATEMMax object."""

        self.log = logging.getLogger('ATEMMax')
        self.log.debug("Initializing")
        self.setLogLevel(logging.CRITICAL)  # Initially silent

        super(ATEMMax, self).__init__()

        self.switcher:ATEMConnectionManager = self

        # Init command handlers
        self._commandHandlers = ATEMCommandHandlers(self, self, self.atem)
        self._commandHandlers.registerAllHandlers()

        # Init event handlers
        self.registerEvent(self.atem.events.connect, self._onConnect)
        self.registerEvent(self.atem.events.receive, self._onReceive)


    def setLogLevel(self, level: int) -> None:
        """Set the logging output level for the switcher object.

        Args:
            level (int): logging level as per Python's logging library
        """

        super().setLogLevel(level)
        self.log.setLevel(level)


    # #######################################################################
    #
    #  ATEMConnectionManager events
    #

    def _onConnect(self, params: Dict[Any, Any]) -> None:
        self.log.debug(f"ATEM model: {self.atemModel}")
        self.log.debug(f"ATEM protocol version: {self.protocolVersion.major}.{self.protocolVersion.minor}")


    def _onReceive(self, params: Dict[Any, Any]) -> None:
        if params['cmd'] == "Warn":
            if self.warningText:
                self.log.debug(f"ATEM warning: {self.warningText}")
                self._eventThreadEventQ.put({"name": "warning", "args": {
                    "switcher": self,
                    "msg": self.warningText,
                    }})


    # #######################################################################
    #
    #  "exec" methods
    #

    def execCutME(self, mE: Union[ATEMConstant, str, int]) -> None:
        """Execute: Cut

        Args:
            mE: see ATEMMixEffects
        """

        if not self.connected:
            self.log.warning("execCutME() IGNORED - switcher disconnected")
            return

        mE_val = self.atem.mixEffects[mE].value

        self._prepareCommandPacket("DCut", 4)
        self._outBuf.setU8(0, mE_val)
        self._finishCommandPacket()


    def execAutoME(self, mE: Union[ATEMConstant, str, int]) -> None:
        """Execute: AutoMixEffect

        Args:
            mE: see ATEMMixEffects
        """

        if not self.connected:
            self.log.warning("execAutoME() IGNORED - switcher disconnected")
            return

        mE_val = self.atem.mixEffects[mE].value

        self._prepareCommandPacket("DAut", 4)
        self._outBuf.setU8(0, mE_val)
        self._finishCommandPacket()


    def execDownstreamKeyerAutoKeyer(self, dsk: Union[ATEMConstant, int]) -> None:
        """Execute: DownstreamKeyer AutoKeyer

        Args:
            dsk: see ATEMDSKs
        """

        if not self.connected:
            self.log.warning("execDownstreamKeyerAutoKeyer() IGNORED - switcher disconnected")
            return

        dsk_val = self.atem.dsks[dsk].value

        self._prepareCommandPacket("DDsA", 4)
        self._outBuf.setU8(0, dsk_val)
        self._finishCommandPacket()


    def execFadeToBlackME(self, mE: Union[ATEMConstant, str, int]) -> None:
        """Execute: FadeToBlack

        Args:
            mE: see ATEMMixEffects
        """

        if not self.connected:
            self.log.warning("execFadeToBlackME() IGNORED - switcher disconnected")
            return

        mE_val = self.atem.mixEffects[mE].value

        self._prepareCommandPacket("FtbA", 4)
        self._outBuf.setU8(0, mE_val)
        self._outBuf.setU8(1, 0x02)
        self._finishCommandPacket()


    def execMacroRecord(self, macro: Union[ATEMConstant, str, int], name: str = '', description: str = '') -> None:
        """Execute: Macro Record (use macro.stop to stop recording)

        Args:
            macro: see ATEMMacros
        """

        if not self.connected:
            self.log.warning("execMacroRecord() IGNORED - switcher disconnected")
            return

        name_len = len(name)
        description_len = len(description)
        name_pos = 6
        description_pos = name_pos + name_len

        # 1 byte for name and description are already included
        msg_len = 8 + (name_len-1) + (description_len-1)

        # The total package length is always a multiple of 4
        msg_len += 4-(msg_len%4)

        macro_val = self.atem.macros[macro].value

        self.switcher._prepareCommandPacket("MSRc", msg_len)
        self.switcher._outBuf.setU16(0, macro_val)
        self.switcher._outBuf.setU16(2, len(name))
        self.switcher._outBuf.setU16(4, len(description))
        self.switcher._outBuf.setString(name_pos, len(name), name)
        self.switcher._outBuf.setString(description_pos, len(description), description)
        self.switcher._finishCommandPacket()


    def execMacroStopRecording(self) -> None:
        """Execute: Macro Stop Recording"""

        if not self.connected:
            self.log.warning("execMacroRecord() IGNORED - switcher disconnected")
            return

        self.switcher._prepareCommandPacket("MAct", 4)
        self.switcher._outBuf.setU8(0, 0xff)
        self.switcher._outBuf.setU8(1, 0xff)
        self.switcher._outBuf.setU8(2, 0x02)
        self.switcher._finishCommandPacket()
