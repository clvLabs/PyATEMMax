#!/usr/bin/env python3
# coding: utf-8
"""
ATEMConnectionManager: Blackmagic ATEM switcher connection manager.
Part of the PyATEMMax library.
"""

# pyright: reportGeneralTypeIssues=false, reportUnknownMemberType=false

from typing import Callable, Dict, List, Optional, Any

import abc
import time
import threading
import queue
import logging

from .ATEMProtocol import ATEMProtocol
from .ATEMUtils import hexStr, hasTimedOut
from .ATEMSocket import ATEMUDPSocket
from .ATEMBuffer import ATEMBuffer
from .ATEMException import ATEMException

THREAD_EXIT_MSG = 'exit'


class ATEMConnectionManager():
    """Blackmagic ATEM switcher connection manager

    ATEMConnectionManager is meant to be used as a base class for specific
    implementations (such as ATEMMax).
    It manages the connection and parsing part of the protocol.

    This class is a port of Skårhøj's ATEMbase class.
    """

    def __init__(self):
        """Create a new ATEMConnectionManager object."""

        self.log = logging.getLogger('ATEMConnectionManager')
        self.log.debug("Initializing")
        self.setLogLevel(logging.CRITICAL)  # Initially silent

        super().__init__()

        # Protocol object (never regenerated)
        self.atem: ATEMProtocol = ATEMProtocol()

        # Protocol command handlers
        self._cmdHandlers: Dict[str, Any] = {}

        # Event subscriptions
        self._eventSubscriptions: Dict[str, List[Any]] = {}

        # Event Thread
        self._eventThread = threading.Thread(target=self._eventThreadHandler)
        self._eventThreadCmdQ: queue.Queue[Dict[str, Any]] = queue.Queue()
        self._eventThreadEventQ: queue.Queue[Dict[str, Any]] = queue.Queue()

        # Initialize all data members
        self._resetInternalData()

        # Udp communication object
        self._udp = ATEMUDPSocket()


    def registerEvent(self, event: str, callback: Callable[[Dict[Any, Any]], None])-> None:
        """Register an event handler

        Args:
            event (str): name of the event (see docs)
            callback (Callable[[Dict[Any, Any]], None]): user callback
        """

        if event not in self._eventSubscriptions:
            self._eventSubscriptions[event] = []

        self._eventSubscriptions[event].append(callback)


    def _registerCmdHandler(self, command: str, callback: Callable[[str], None]) -> None:
        """Register a command handler"""

        self._cmdHandlers[command] = { "callback": callback }


    def __del__(self) -> None:
        """Things to do when killed :)"""

        self.log.debug("Destroying object, cleaning up")
        if self.started:
            self.log.debug('Stopping comms')
            self.disconnect()
            self.log.debug('Comms stopped')
        self.log.debug('Finished cleanup')


    # pylint: disable=attribute-defined-outside-init
    def _resetInternalData(self):
        """Reset value of all internal variables. Useful for reconnections"""

        # The most recent Remote Packet Id from switcher.
        self.lastRemotePacketID: int = 0

        # Is the manager started?
        self.started: bool = False

        # Set to True on first packet reception (useful for pings/etc)
        self.switcherAlive: bool = False

        # Set true if we have received a hello packet from the switcher.
        # This can be used (for example) when trying to determine if the switcher
        #  is alive and connected to the network. If it starts handshake we know
        #  it's ok and we don't have to wait for the full handshake to happen
        self.handshakeStarted: bool = False

        # If true, all initial payload packets has been received during requests for resent
        #  - and we are completely ready to rock!
        self.connected: bool = False

        # IP address of the switcher
        self.ip: str = ""

        # Comms Thread
        self._commsThread = threading.Thread(target=self._commsThreadHandler)
        self._commsThreadCmdQ: queue.Queue = queue.Queue()

        # This is our counter for the command packets we might like to send to ATEM.
        self._localPacketIdCounter: int = 0

        # If true, the initial reception of the ATEM memory has passed and
        #  we can begin to respond during the loop.
        self._initPayloadSent: bool = False

        # The Remote Packet ID at which point the initialization payload was completed.
        self._initPayloadSentAtPacketId: int = 0

        # UDP connection timeout
        self._connTimeout: int = 0

        # Ping mode: if True all data will be ignored, no ACKs will be sent
        # This way we don't force the switcher to send us the whole settings data and
        #  to create a new sessionId for the "ping"
        self._pingMode: bool = False

        # Session id of session, given by ATEM switcher.
        self.sessionID: int = 0

        # Last time (millis) the switcher sent a packet to us.
        self._lastContact: float = 0

        # Used to track which initialization packets have been missed.
        self._missedInitializationPackets: List[int] = []

        # Length of packet to be sent.
        self._returnPacketLength: int = 0

        # Used when parsing packets.
        self._cmdLength: int = 0

        # Used when parsing packets.
        self._cmdPointer: int = 0

        # If set, we are building a set-command bundle.
        self._cBundle: bool = False

        # Bundle Buffer Offset; This is an offset if you want to add more commands.
        self._cBBO: int = 0

        # Used for auto-connection.
        self._neverConnected: bool = True

        # Are we waiting for missed packets ?
        self._waitingForIncoming: bool = False

        # Buffers for storing segments of the packets from ATEM and creating answer packets.
        self._inBuf: ATEMBuffer = ATEMBuffer(self.atem.inputBufferLength)
        self._outBuf: ATEMBuffer = ATEMBuffer(self.atem.outputBufferLength)


    def ping(self, ip: str, timeout: int =5) -> None:
        """Ping the switcher.

        Args:
            ip (str): IP address of the switcher
            timeout (int): timeout (seconds)
        """

        self.connect(ip, timeout, pingMode=True)


    def connect(self, ip: str, connTimeout: int =5, pingMode: bool = False) -> None:
        """Connect to the switcher.

        Args:
            ip (str): IP address of the switcher
            connTimeout (int): connection timeout (seconds)
            pingMode (bool): connect in "ping" mode? (ignore data, just wait for UDP conn)
        """

        if self.started:
            self.log.debug("Closing previous connection")
            self.disconnect()

        self.log.info(f"Starting connection with ATEM switcher on {ip}")
        self._neverConnected = True
        self._waitingForIncoming = False

        self.ip = ip
        self._connTimeout = connTimeout
        self._pingMode = pingMode
        self._lastContact = 0

        self.resetCommandBundle()

        self._eventThread = threading.Thread(target=self._eventThreadHandler)
        self._commsThread = threading.Thread(target=self._commsThreadHandler)

        self._eventThread.start()
        self._commsThread.start()
        self.started = True


    def disconnect(self) -> None:
        """Close the connection with the switcher."""

        if not self.started:
            return

        self.log.debug("Stopping connection")
        self.started = False

        self._commsThreadCmdQ.put(THREAD_EXIT_MSG)
        self._commsThread.join()
        self._commsThread = threading.Thread(target=self._commsThreadHandler)

        self._eventThreadCmdQ.put(THREAD_EXIT_MSG)
        self._eventThread.join()
        self._eventThread = threading.Thread(target=self._eventThreadHandler)

        self._udp.stop()
        self._resetInternalData()


    @abc.abstractmethod
    def setLogLevel(self, level: int) -> None:
        """Set the logging output level for the switcher object.

        Args:
            level (int): logging level as per Python's logging library
        """

        self.log.setLevel(level)


    def _connect(self):
        """Internal connect method"""

        # Init localPacketIDCounter to 0
        self._localPacketIdCounter = 0

        # Will be true after initial payload of data is delivered
        #  (regular 12-byte ping packets are transmitted.)
        self._initPayloadSent = False

        # Will be true after initial payload of data is resent and received well
        self.connected = False

        # Will be true after first received UDP packet
        self.switcherAlive = False

        # Will be true after the initial hello-packet handshakes.
        self.handshakeStarted = False

        # Temporary session ID - a new will be given back from ATEM.
        self.sessionID = 0

        # Setting this, because even though we haven't had contact,
        #  it constitutes an attempt that should be responded to at least
        self._lastContact = time.time()

        self._missedInitializationPackets = [
            0xFF for _ in range(int((self.atem.maxInitPacketCount+7)/8)) ]

        self._initPayloadSentAtPacketId = self.atem.maxInitPacketCount    # The max value it can be

        self._udp.connect(self.ip)

        # Send connectString to ATEM:
        self.log.info("Sending HELLO packet")

        self._outBuf.reset()
        self._setCommandHeader(self.atem.cmdFlags.helloPacket.value, self.atem.headerLen+self.atem.cmdHeaderLen)
        self._outBuf.setU8(9, 0x3a)     # Expected on first request.
        self._outBuf.setU8(12, 0x01)    # Expected on first request.
        self._sendCommand(self.atem.headerLen+self.atem.cmdHeaderLen)

        self._eventThreadEventQ.put({"name": "connectAttempt", "args": {
            "switcher": self,
            }})


    def _commsThreadHandler(self):
        self.log.debug("Comms thread started")

        while self._runLoop():
            time.sleep(0.001)

        self.log.debug("Comms thread FINISHED")


    def _runLoop(self, delayTime: float = 0) -> bool:
        """Keep connection to the switcher alive

        This method is called by the internal thread.

        Args:
            delayTime (int, optional): time to spend listening. Defaults to 0.

        Returns:
            (bool): True if we should continue running, False if we have to exit
        """

        if self._neverConnected:
            self._neverConnected = False
            self.log.info("Connecting for the first time")
            self._connect()

        enterTime = time.time()

        while True:         # This is a "do...while" (see the "break" at the end!)
            while True:     # Iterate until UDP buffer is empty

                # ------------------------------------------------
                # Check if a thread exit was requested
                try:
                    msg:str = self._commsThreadCmdQ.get_nowait()
                    if msg == THREAD_EXIT_MSG:
                        self.log.debug("Thread exit requested, closing...")
                        self._commsThreadCmdQ.task_done()
                        # Stop thread loop
                        return False
                except queue.Empty:
                    pass
                # ------------------------------------------------

                packetSize = self._udp.parsePacket()
                if not self._udp.available():
                    break
                else:
                    # When we receive the first UDP packet from the switcher:
                    if not self.switcherAlive:
                        # We know the switcher is alive
                        self.log.debug("Basic UDP connection established, switcher is alive.")
                        self.switcherAlive = True
                        # This break forces the loop to exit, giving the user a chance to
                        #  disconnect() the connection without sending any ACKs (disturbing our switcher)
                        break

                    # If we're in "ping" mode, ignore ALL data...
                    if self._pingMode:
                        self.log.debug("PING mode active, ignoring received data")
                        self._udp.flushInputBuffer()
                        break

                    self._udp.read(self._inBuf, self.atem.headerLen)   # Read header

                    packetSessionID = self._inBuf.getU16(2)

                    if not self.sessionID and packetSessionID:
                        # Get sessionId from the packet ONLY if we don't have a sessionId
                        self.log.debug(f"Received new SessionId: 0x{packetSessionID:x}")
                        self.sessionID = packetSessionID
                    elif packetSessionID != self.sessionID:
                        # Ignore packets from different sessionIds
                        self.log.debug(f"Ignoring packet for SessionId: 0x{packetSessionID:x}")
                        break

                    headerBitmask = self._inBuf.getU8(0) >> 3
                    self.lastRemotePacketID = self._inBuf.getU16(10)

                    if self.lastRemotePacketID < self.atem.maxInitPacketCount:
                        self._missedInitializationPackets[self.lastRemotePacketID>>3] &= ~(1<<(self.lastRemotePacketID & 0x07))

                    packetLength = self._inBuf.getU16(0) & 0x07FF

                    if packetSize >= packetLength:  # Just to make sure we have enough info in the buffer
                        self._lastContact = time.time()
                        self._waitingForIncoming = False

                        if headerBitmask & self.atem.cmdFlags.helloPacket.value:    # Respond to "Hello" packets:
                            # The ATEM will return a "2" in this return packet of same length. If the ATEM returns "3" it means "fully booked" (no more clients can connect)
                            #   and a "4" seems to be a kind of reconnect (seen when you drop the connection and the ATEM desperately tries to figure out what happened...)
                            # self.log.debug(f"- HELLO.bookStatus {helloExtraInfo[0]}")

                            # This number seems to increment with about 3 each time a new client tries to connect to ATEM.
                            #   It may be used to judge how many client connections has been made during the up-time of the switcher?
                            # self.log.debug(f"- HELLO.connectionCount {helloExtraInfo[3]}")

                            helloExtraInfo = self._udp.flushInputBuffer()
                            helloBookStatus = helloExtraInfo[0]
                            helloConnectionCount = helloExtraInfo[3]

                            self.log.debug(f"Received HELLO. bookStatus {helloBookStatus} connectionCount {helloConnectionCount} Extra info: [{hexStr(helloExtraInfo)}]")

                            if helloBookStatus == 3:
                                self.log.warning("Switcher seems to be fully booked, trying to reconnect")

                            else:
                            # elif helloBookStatus == 2:
                                self.log.info("Connected to switcher")
                                self.handshakeStarted = True

                                self.log.debug("Sending HELLO ACK")
                                self._outBuf.reset()
                                self._setCommandHeader(self.atem.cmdFlags.ack.value, self.atem.headerLen)
                                self._outBuf.setU8(9, 0x03)    # This seems to be what the client should send upon first request.
                                self._sendCommand(self.atem.headerLen)


                            # elif helloBookStatus == 4:
                            #     self.log.debug("Ignored HELLO response with bookStatus 4")


                        # If a packet is 12 bytes long it indicates that all the initial information
                        # has been delivered from the ATEM and we can begin to answer back on every request
                        # Currently we don't know any other way to decide if an answer should be sent back...
                        # The QT lib uses the "InCm" command to indicate this, but in the latest version of the firmware (2.14)
                        # all the camera control information comes AFTER this command, so it's not a clear ending token anymore.
                        # However, I'm not sure if I checked the lastRemotePacketID of the packets with the additional camera control info - if it was a resend,
                        # "InCm" may still indicate the number of the last init-packet and that's all I need to request the missing ones....

                        # BTW: It has been observed on an old 10Mbit hub that packets could arrive in a different order than sent and this may
                        # mess things up a bit on the initialization. So it's recommended to has as direct routes as possible.

                        if not self._initPayloadSent and \
                            packetLength == self.atem.headerLen and \
                            self.lastRemotePacketID > 1:

                            self._initPayloadSent = True
                            self._initPayloadSentAtPacketId = self.lastRemotePacketID
                            self.log.debug(f"Initial payload received @rpID 0x{self._initPayloadSentAtPacketId:X} sessionId 0x{self.sessionID:X}")

                        # Respond to request for acknowledge    (and to resends also, whatever)...
                        if (headerBitmask & self.atem.cmdFlags.ackRequest.value) and \
                            (self.connected or not (headerBitmask & self.atem.cmdFlags.resend.value)):

                            # self.log.debug(f"Sending requested ACK for rpID 0x{self.lastRemotePacketID:X}")
                            self._outBuf.reset()
                            self._setCommandHeaderWithPckId(self.atem.cmdFlags.ack.value, self.atem.headerLen, self.lastRemotePacketID)
                            self._sendCommand(self.atem.headerLen)


                        # ATEM is requesting a previously sent packet which must have dropped out of the order.
                        #   We return an empty one so the ATEM doesnt' crash (which some models will,
                        #     if it doesn't get an answer before another 63 commands gets sent from the controller.)
                        elif self._initPayloadSent and \
                            (headerBitmask & self.atem.cmdFlags.requestNextAfter.value) and \
                            self.connected:

                            packetId = self._inBuf.getU16(6)
                            self._outBuf.reset()
                            self._setCommandHeaderWithPckId(self.atem.cmdFlags.ack.value, self.atem.headerLen, 0)

                            # Overruling this. A small trick because createCommandHeader shouldn't increment local packet ID counter
                            self._outBuf.setU8(0, self.atem.cmdFlags.ackRequest.value << 3)

                            self._outBuf.setU16(10, packetId)
                            self._sendCommand(self.atem.headerLen)
                            self.log.debug(f"Received request to resend rpID 0x{packetId:X}")

                        else:
                            # Regular message
                            # self.log.debug("Message considered 'regular', passing")
                            pass

                        if packetLength > self.atem.headerLen:
                            if not (headerBitmask & self.atem.cmdFlags.helloPacket.value):
                                # Packet contains extra data, parse
                                # self._parsePacket(packetLength)
                                self._parsePacket(packetSize) # Parse EVERYTHING, don't trust packetLength !!


                        if self._udp.available():
                            self.log.debug(f"Flushing remaining {self._udp.available()} bytes from socket buffer")
                            self._udp.flushInputBuffer()

                    else:
                        self.log.error(f"Not enough data received: packetSize ({packetSize}) != packetLength ({packetLength})")
                        self.log.debug("Flushing input buffer")
                        self._udp.flushInputBuffer()


            # After initialization, we check which packets were missed and ask for them:
            if not self.connected and self._initPayloadSent and not self._waitingForIncoming:
                for i in range(1, self._initPayloadSentAtPacketId):
                    if i <= self.atem.maxInitPacketCount:
                        if self._missedInitializationPackets[i>>3] & (1<<(i & 0x7)):
                            self.log.debug(f"Asking for rpID 0x{i:x}")
                            self._outBuf.reset()
                            self._setCommandHeader(self.atem.cmdFlags.requestNextAfter.value, self.atem.headerLen)
                            self._outBuf.setU16(6, i-1)  # Resend Packet ID
                            self._outBuf.setU8(8, 0x01)
                            self._sendCommand(self.atem.headerLen)
                            self._waitingForIncoming = True
                            break
                    else:
                        break

                if not self._waitingForIncoming:
                    self.connected = True
                    self._eventThreadEventQ.put({"name": "connect", "args": {
                        "switcher": self,
                        }})


            # This makes the first "while True:" behave as a do...while.
            if delayTime <= 0 or hasTimedOut(enterTime, delayTime):
                break

        # If connection is gone anyway, try to reconnect:
        if hasTimedOut(self._lastContact, self._connTimeout):
            self.log.warning("Connection has timed out - reconnecting")
            if self.connected:
                self._eventThreadEventQ.put({"name": "disconnect", "args": {
                    "switcher": self,
                    }})
            self._connect()

        # Everything OK, continue running
        return True


    def _eventThreadHandler(self):
        self.log.debug("Event thread started")

        while True:
            self._emitEvents()

            # ------------------------------------------------
            # Check if a thread exit was requested
            try:
                msg:str = self._eventThreadCmdQ.get_nowait()
                if msg == THREAD_EXIT_MSG:
                    self.log.debug("Thread exit requested, closing...")
                    self._eventThreadCmdQ.task_done()
                    # Stop thread loop
                    break
            except queue.Empty:
                pass

            time.sleep(0.001)

        self.log.debug("Event thread FINISHED")


    def _emitEvents(self) -> None:
        while not self._eventThreadEventQ.empty():
            event: Dict[str, Any] = self._eventThreadEventQ.get_nowait()
            eventName = event['name']

            if eventName in self._eventSubscriptions:
                for cb in self._eventSubscriptions[eventName]:
                    cb(event['args'])

            self._eventThreadEventQ.task_done()


    def waitForConnection(self, infinite: bool =True, timeout: float =0.0, waitForFullHandshake: bool =True) -> bool:
        """Waits until the switcher initializes.

        Args:
            infinite (bool, default=True): Infinite wait?
            timeout (int, optional): max seconds to wait. If not specified will use protocol defaults.
            waitForFullHandshake (bool, default=True): If False the function will return on initial UDP connection.
        """

        if self._pingMode:
            infinite = False
            waitForFullHandshake = False

        if timeout:
            infinite = False
        elif not infinite:
            if waitForFullHandshake:
                timeout = self.atem.defaultConnectionTimeout
            else:
                timeout = self.atem.defaultHandshakeTimeout

        waitstr: str = f"waiting for {'connection' if waitForFullHandshake else 'first UDP packet' } "
        if infinite:
            waitstr += " (infinite)"
        else:
            waitstr += f" ({timeout}s)"

        startTime = time.time()
        self.log.debug(f"Started {waitstr} ")

        # Step 1 - wait for basic UDP connection
        while not self.switcherAlive:
            if timeout and time.time() - startTime >= timeout:
                self.log.debug(f"Timeout {waitstr}")
                return False
            time.sleep(0.01)

        if waitForFullHandshake:
            # Step 2 - wait for full handshake
            while not self.connected:
                if timeout and time.time() - startTime >= timeout:
                    self.log.debug(f"Timeout {waitstr}")
                    return False
                time.sleep(0.01)

        self.log.debug("Finished waiting for initialization")
        return True


    def setSocketLogLevel(self, level: int) -> None:
        """Set the logging output level for the internal socket.

        Args:
            level (int): logging level as per Python's logging library
        """

        self._udp.setLogLevel(level)


    def commandBundleStart(self) -> None:
        """Start a command bundle"""

        self.resetCommandBundle()
        self._outBuf.reset()
        self._cBundle = True


    def commandBundleEnd(self) -> None:
        """End a command bundle"""

        if self._cBundle and self._returnPacketLength > 0:
            self._setCommandHeader(self.atem.cmdFlags.ackRequest.value, self._returnPacketLength)
            self._sendCommand(self._returnPacketLength)
            self._returnPacketLength = 0

        self.resetCommandBundle()


    def resetCommandBundle(self) -> None:
        """Reset the command bundle"""

        self._cBundle = False
        self._cBBO = 0


    # #######################################################################
    #
    #  Protected methods
    #
    def _setCommandHeader(self, headerCmdFlags: int, lengthOfData: int) -> None:
        """Skårhøj: void _createCommandHeader(const uint8_t headerCmd, const uint16_t lengthOfData)"""

        self._setCommandHeaderWithPckId(headerCmdFlags, lengthOfData, 0)


    def _setCommandHeaderWithPckId(self, headerCmdFlags: int, lengthOfData: int, remotePacketID: int) -> None:
        """Skårhøj: void _createCommandHeader(const uint8_t headerCmd, const uint16_t lengthOfData, const uint16_t remotePacketID)"""

        self._outBuf.setU16(0, (headerCmdFlags << 8+3) | (lengthOfData & 0x07FF))   # Command bits + length
        self._outBuf.setU16(2, self.sessionID)
        self._outBuf.setU16(4, remotePacketID)

        if not (headerCmdFlags & (self.atem.cmdFlags.helloPacket.value | self.atem.cmdFlags.ack.value | self.atem.cmdFlags.requestNextAfter.value)):
            self._localPacketIdCounter += 1

            # Uncommenting this block will jump the local packet ID counter every 15 command - thereby introducing
            #   a stress test of the robustness of the "resent packet" function from the ATEM switcher.
            # - - - - - - - - - - - - - - - - - - - -
            # if self._localPacketIdCounter & 0xF == 0xF:
            #   self._localPacketIdCounter += 1
            # - - - - - - - - - - - - - - - - - - - -

            self._outBuf.setU16(10, self._localPacketIdCounter)

        # self.log.debug(f"Prepared command header: cmdFlags 0x{headerCmdFlags:x} len {lengthOfData} rpID 0x{remotePacketID:x}")


    def _sendCommand(self, bufferlength: int) -> None:
        """Skårhøj: void _sendPacketBuffer(uint8_t length)"""

        payload = bytes(self._outBuf[:bufferlength])
        self._udp.write(payload)


    def _parsePacket(self, packetLength: int) -> None:
        """Skårhøj: void _parsePacket(uint16_t packetLength)"""

        # If packet is more than an ACK packet (= if its longer than 12 bytes header), lets parse it:
        indexPointer = self.atem.headerLen      # self.atem.headerLen bytes has already been read from the packet...
        while indexPointer < packetLength:
            # Read the length of segment (first word):
            self._udp.read(self._inBuf, self.atem.cmdHeaderLen)
            self._cmdLength = self._inBuf.getU16(0)
            self._cmdPointer = 0

            # Get the "command string", basically this is the 4 char variable name in the ATEM memory holding the various state values of the system:
            cmdStr = ''.join([chr(x) for x in [ self._inBuf[4], self._inBuf[5], self._inBuf[6], self._inBuf[7]]])

            if cmdStr in self.atem.commands:
                self.log.debug(f"Received: [{cmdStr}] ({self.atem.commands[cmdStr]})")
            else:
                self.log.debug(f"Received: UNKNOWN command [{cmdStr}]")

            # If length of segment larger than 8 (should always be...!)
            if self._cmdLength > self.atem.cmdHeaderLen:
                self._parseGetCommands(cmdStr)

                while self._read2InBuf():   # Empty, if not done yet.
                    pass

                indexPointer += self._cmdLength
            else:
                self.log.error(f"Bad CMD length ({self._cmdLength}), flushing input buffer")
                self._udp.flushInputBuffer()
                return


    def _parseGetCommands(self, cmdStr: str) -> None:
        """Skårhøj: virtual void _parseGetCommands(const char *cmdString)"""

        if cmdStr in self._cmdHandlers:
            try:
                self._cmdHandlers[cmdStr]["callback"](cmdStr)  # Call method

                # Avoid emitting events for handshake data
                if self.connected:
                    self._eventThreadEventQ.put({"name": "receive", "args": {
                        "switcher": self,
                        "cmd": cmdStr,
                        "cmdName": self.atem.commands[cmdStr] if cmdStr in self.atem.commands else ""
                        }})

            except ATEMException as e:
                self.log.warning(f"{str(e)} - processing [{cmdStr}]")
        else:
            self.log.warning(f"Received UNKNOWN command: [{cmdStr}]")


    def _read2InBuf(self, maxBytes: Optional[int] =None) -> bool:
        """Skårhøj: bool _read2InBuf(uint8_t maxBytes)"""

        if maxBytes is None:
            maxBytes = self.atem.inputBufferLength

        maxBytes = maxBytes if maxBytes <= self.atem.inputBufferLength else self.atem.inputBufferLength
        remainingBytes = self._cmdLength - self.atem.cmdHeaderLen - self._cmdPointer

        if remainingBytes > 0:
            if remainingBytes <= maxBytes:
                self._udp.read(self._inBuf, remainingBytes)
                self._cmdPointer += remainingBytes
                return False
            else:
                self._udp.read(self._inBuf, maxBytes)
                self._cmdPointer += maxBytes
                return True
        else:
            return False


    def _prepareCommandPacket(self, cmdString: str, cmdBytes: int, indexMatch: Optional[bool]=True) -> None:
        """Skårhøj: void _prepareCommandPacket(const char *cmdString, uint8_t cmdBytes, bool indexMatch=true)"""

        cmdStrPos = self.atem.headerLen + self._cBBO + self.atem.cmdStrOffset

        # First, in case of a command bundle, check if indexes are different OR if it's an entirely different command, then increase offset to accommodate new command:
        if self._cBundle:
            packetCmdString = self._outBuf[cmdStrPos:cmdStrPos+self.atem.cmdStrLen]
            if self._returnPacketLength > 0 and (not indexMatch or packetCmdString != cmdString):
                self._cBBO = self._returnPacketLength - self.atem.headerLen
        else:
            self._outBuf.reset()    # For command bundles, this is already done...

        self._returnPacketLength = self.atem.headerLen + self._cBBO + self.atem.cmdHeaderLen + cmdBytes

        # Because we increased length of command, we need to check for buffer overflow:
        if self._returnPacketLength > self.atem.outputBufferLength:
            raise ATEMException("Packet Buffer Overflow in the ATEM Library! Too long or too many commands bundled")

        # Copy Command String:
        if len(cmdString) == self.atem.cmdStrLen:
            self._outBuf.setString(cmdStrPos, self.atem.cmdStrLen, cmdString)
        else:
            raise ATEMException(f"BAD CMD [{cmdString}]: length ({len(cmdString)})" \
                            f" - should be {self.atem.cmdStrLen}")

        # Command length:
        commandLength = self.atem.cmdHeaderLen + cmdBytes
        self._outBuf.setU16(self.atem.headerLen + self._cBBO, commandLength)

        # Give control to user: set offset handler for output buffer
        self._outBuf.setUserOffsetCallback(lambda offset : self.atem.headerLen + self._cBBO + self.atem.cmdHeaderLen + offset)


    def _finishCommandPacket(self) -> None:
        """Skårhøj: void _finishCommandPacket()"""

        # Reset control to user: set offset handler for output buffer
        self._outBuf.setUserOffsetCallback(lambda offset : offset)

        if self._cBundle:
            self.log.warning("[_finishCommandPacket] ignoring attempt to finish command bundle, please use commandBundleEnd()")
            return

        self._setCommandHeader(self.atem.cmdFlags.ackRequest.value, self._returnPacketLength)
        self._sendCommand(self._returnPacketLength)
        self._returnPacketLength = 0
