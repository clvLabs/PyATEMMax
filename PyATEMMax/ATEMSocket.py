#!/usr/bin/env python3
# coding: utf-8
"""
ATEMsocket: A socket that simulates the behaviour of Arduino's socket
to keep the ATEMConnectionManager class as close as possible to the original.
Part of the PyATEMMax library.
"""

from typing import Any, List, Optional, Union

import socket
import logging

from .ATEMProtocol import ATEMProtocol
from .ATEMUtils import hexStr


class ATEMUDPSocket():
    """
    This class emulates the behaviour of Arduino's UDP socket.

    Its purpose is to keep the code as close as possible to the original.
    """

    def __init__(self):
        """Create a ATEMUDPSocket object."""

        self.log = logging.getLogger('ATEMsocket')
        self.log.debug("Initializing")
        self.setLogLevel(logging.CRITICAL)  # Initially silent

        super().__init__()

        self.atem: ATEMProtocol = ATEMProtocol()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setblocking(False)

        self.connected = False

        self._buffer = []


    def connect(self, ip: str) -> None:
        """
        Connect to a specified IP address and port.

        From: https://www.arduino.cc/en/Reference/ClientConnect
        """

        if self.connected:
            self.log.debug("Closing previous connection")
            self.stop()

        port = self.atem.UDPPort
        address = (ip, port)
        self.log.info(f"Connecting to {ip}:{port}")
        self._socket.connect(address)
        self.connected = True


    def stop(self) -> Any:
        """
        Disconnect from the server.

        From: https://www.arduino.cc/en/Reference/ClientStop
        """

        if self.connected:
            # No need to close an UDP socket in Python, and
            #  it does close the file descriptor...
            # self._socket.close()
            self.connected = False

        self.flushInputBuffer()


    def parsePacket(self) -> int:
        """
        Check for the presence of a UDP packet.

        parsePacket() must be called before reading the buffer.

        Returns:
            number of available bytes

        From: https://www.arduino.cc/en/Reference/EthernetUDPParsePacket
        """

        try:
            data, _ = self._socket.recvfrom(10240)
        except socket.error:
            data = []

        if data:
            self._buffer.extend(data)
            self.log.debug(f"Received {len(data)} new bytes [{hexStr(data)}] - " \
                            f" {self.available()} bytes available")

        return self.available()


    def available(self):
        """
        Get the number of bytes (characters) available for reading from the buffer.

        This is data that's already arrived.

        From: https://www.arduino.cc/en/Reference/EthernetUDPAvailable
        """

        return len(self._buffer)


    def read(self, buffer: List[int], maxSize: Optional[int] =None):
        """
        Read UDP data from the specified buffer.

        If no arguments are given, it will return the next character in the buffer.

        From: https://www.arduino.cc/en/Reference/EthernetUDPRead
        """

        # Clear buffer before receiving
        buffer[:] = []

        # Get data from the internal buffer
        count = 0
        maxCount = maxSize if maxSize else 9999999999999
        while count < maxCount:
            if self.available():
                buffer.append(self._buffer.pop(0))
                count += 1
            else:
                break

        return count


    def write(self, payload: Union[List[int], bytes], length: Optional[int] =None):
        """
        Write data to the server the client is connected to.

        This data is sent as a byte or series of bytes.

        From: https://www.arduino.cc/en/Reference/ClientWrite
        """

        if isinstance(payload, List):
            outbuf = bytes(payload)
        else:
            outbuf = payload

        outbuf = outbuf[:length] if length else outbuf

        self.log.debug(f"Sending buffer [{hexStr(outbuf)}]")
        return self._socket.send(outbuf)


    def flushInputBuffer(self):
        """Flush the input buffer"""

        oldbuffer = [b for b in self._buffer]
        self._buffer = []

        self.log.debug(f"Buffer flushed. Data: [{hexStr(oldbuffer)}]")
        return oldbuffer


    def peek(self):
        """Get a copy of the input buffer"""

        return [b for b in self._buffer]


    def setLogLevel(self, level: int) -> None:
        """
        Set the logging output level.

        Args:
            level (int): logging level as per Python's logging library
        """

        self.log.setLevel(level)
