#!/usr/bin/env python3
# coding: utf-8
"""
ATEMBuffer: Blackmagic ATEM buffer manager class
Part of the PyATEMMax library.
"""

# pyright: reportGeneralTypeIssues=false, reportUnknownVariableType=false

from typing import List, Callable, Union

import struct

from .ATEMException import ATEMException


class ATEMBuffer():
    """ATEM Buffer manager"""


    # #######################################################################
    #
    #  Initialization
    #

    def __init__(self, size:int):
        """Create a buffer

        Args:
            size (int): size of the buffer
        """

        self._buf: List[int]
        self.size = size
        self._userOffsetCallback: Callable[[int], int]
        self._userOffsetCallbackSet: bool = False
        self.reset()


    def setUserOffsetCallback(self, callback: Callable[[int], int]) -> None:
        """Set the callback used to calculate buffer offsets.

        This is needed to be able to dynamically calculate the offset
         for output buffers having the commandOffsetBundle in account.

        The callback receives an offset(int) and returns an offset(int).

        Args:
            callback (Callable[[int], int]): function (or lambda) to call
        """

        self._userOffsetCallback = callback
        self._userOffsetCallbackSet = True



    # #######################################################################
    #
    #  List methods
    #

    def __getitem__(self, i: Union[int, slice]) -> Union[int, List[int]]:
        return self._buf.__getitem__(i)


    def __setitem__(self, i: Union[int, slice], v: int) -> None:
        return self._buf.__setitem__(i, v)

    def pop(self, i: int = ...) -> int:
        """Remove the byte at the given position in the list, and return it (default last)"""

        return self._buf.pop(i)

    def append(self, v: int) -> None:
        """Append byte to buffer"""

        self._buf.append(v)

    def __len__(self) -> int:
        return len(self._buf)


    # #######################################################################
    #
    #  Methods
    #

    def reset(self, size:int = -1):
        """Reset the buffer

        Args:
            size (int): size of the buffer
        """

        if size != -1:
            self.size = size

        self._buf = [0 for _ in range(self.size)]


    def _getFormatChar(self, signed: bool, bits: int) -> str:
        """Get format character for struct.pack/unpack"""

        fmtChr = ''
        if bits == 8:
            fmtChr = 'b'
        elif bits == 16:
            fmtChr = 'h'
        elif bits == 32:
            fmtChr = 'l'
        elif bits == 64:
            fmtChr = 'q'
        else:
            raise ATEMException(f"_getFormatChar(): Invalid number of bits ({bits}) requested")

        if not signed:
            fmtChr = fmtChr.upper()

        return f'!{fmtChr}'
        # return fmtChr



    # #######################################################################
    #
    #  Basic value type management
    #

    def getInt(self, offset: int, signed: bool, bits: int) -> int:
        """Get an integer"""

        if self._userOffsetCallbackSet:
            bufferIndex = self._userOffsetCallback(offset)
        else:
            bufferIndex = offset

        numBytes = int(bits/8)

        if 0 < bufferIndex >= (self.size - numBytes):
            raise ATEMException(f"ATEMBuffer.getInt(): Can't get" \
                            f" {'S' if signed else 'U'}{bits}" \
                            f" @offset[{offset}]" \
                            f" - buffIndex[{bufferIndex}]" \
                            f" - numBytes[{numBytes}]" \
                            f" - buffLen[{self.size}]")

        packedValue = bytes(self._buf[bufferIndex:bufferIndex+numBytes])

        return struct.unpack(self._getFormatChar(signed, bits), packedValue)[0]


    def setInt(self, offset: int, signed: bool, bits: int, value: int) -> None:
        """Set an integer"""

        if self._userOffsetCallbackSet:
            bufferIndex = self._userOffsetCallback(offset)
        else:
            bufferIndex = offset

        numBytes = int(bits/8)

        if 0 < bufferIndex >= (self.size - numBytes):
            raise ATEMException(f"ATEMBuffer.setInt(): Can't set" \
                            f" {'S' if signed else 'U'}{bits}" \
                            f" @offset[{offset}]" \
                            f" value[{value:X}]" \
                            f" - buffIndex[{bufferIndex}]" \
                            f" - numBytes[{numBytes}]" \
                            f" - buffLen[{self.size}]")

        packedValue = struct.pack(self._getFormatChar(signed, bits), value)

        self._buf[bufferIndex:bufferIndex+numBytes] = list(packedValue)


    def changeInt(self, offset: int, signed: bool, bits: int, func: Callable[[int], int]) -> None:
        """Change an integer"""

        value = func(self.getInt(offset, signed, bits))
        self.setInt(offset, signed, bits, value)


    def getFlag(self, offset: int, signed: bool, bits: int, bit: int) -> bool:
        """Get an individual bit in an integer"""

        return True if (self.getInt(offset, signed, bits) & 1<<bit) else False


    def setFlag(self, offset: int, signed: bool, bits: int, bit: int) -> None:
        """Set an individual bit in an integer"""

        self.changeInt(offset, signed, bits, lambda v: v | 1<<bit)


    def getFloat(self, offset: int, signed: bool, bits: int, factor: int) -> float:
        """Get a floating point integer"""

        return self.getInt(offset, signed, bits) / factor


    def setFloat(self, offset: int, signed: bool, bits: int, factor: int, value: float) -> None:
        """Set a floating point integer"""

        return self.setInt(offset, signed, bits, int(value*factor))


    def getString(self, offset: int, numBytes: int) -> str:
        """Get a string"""

        if self._userOffsetCallbackSet:
            bufferIndex = self._userOffsetCallback(offset)
        else:
            bufferIndex = offset

        if 0 < bufferIndex >= (self.size - numBytes):
            raise ATEMException(f"ATEMBuffer.getString(): Can't set string" \
                            f" @offset[{offset}]" \
                            f" - buffIndex[{bufferIndex}]" \
                            f" - numBytes[{numBytes}]" \
                            f" - buffLen[{self.size}]")

        valueBuff = []
        index = bufferIndex
        while index < (bufferIndex + numBytes) and self._buf[index]:
            valueBuff.append(self._buf[index])
            index += 1

        cstring = bytes(valueBuff).decode('utf8', "ignore")
        return cstring



    def setString(self, offset: int, numBytes: int, value: str) -> None:
        """Set a string"""

        if self._userOffsetCallbackSet:
            bufferIndex = self._userOffsetCallback(offset)
        else:
            bufferIndex = offset

        if 0 < bufferIndex >= (self.size - numBytes):
            raise ATEMException(f"ATEMBuffer.setString(): Can't set string" \
                            f" @offset[{offset}]" \
                            f" - buffIndex[{bufferIndex}]" \
                            f" - numBytes[{numBytes}]" \
                            f" - buffLen[{self.size}]")

        buf = value.encode('utf8')
        buf += bytes([0 for _ in range(numBytes)])
        buf = buf[:numBytes]

        self._buf[bufferIndex:bufferIndex+numBytes-1] = list(buf)


    # #######################################################################
    #
    #  Integer
    #

    # -----------------------------------------------------------------------
    #
    #  get
    #

    def getU8(self, offset: int) -> int:
        """Get an U8 integer"""

        return self.getInt(offset, False, 8)

    def getS8(self, offset: int) -> int:
        """Get an S8 integer"""

        return self.getInt(offset, True, 8)

    def getU16(self, offset: int) -> int:
        """Get an U16 integer"""

        return self.getInt(offset, False, 16)

    def getS16(self, offset: int) -> int:
        """Get an S16 integer"""

        return self.getInt(offset, True, 16)

    def getU32(self, offset: int) -> int:
        """Get an U32 integer"""

        return self.getInt(offset, False, 32)

    def getS32(self, offset: int) -> int:
        """Get an S32 integer"""

        return self.getInt(offset, True, 32)

    def getU64(self, offset: int) -> int:
        """Get an U64 integer"""

        return self.getInt(offset, False, 64)

    def getS64(self, offset: int) -> int:
        """Get an S64 integer"""

        return self.getInt(offset, True, 64)

    # -----------------------------------------------------------------------
    #
    #  set
    #

    def setU8(self, offset: int, value: int) -> None:
        """Set an U8 integer"""

        self.setInt(offset, False, 8, value)

    def setS8(self, offset: int, value: int) -> None:
        """Set an S8 integer"""

        self.setInt(offset, True, 8, value)

    def setU16(self, offset: int, value: int) -> None:
        """Set an U16 integer"""

        self.setInt(offset, False, 16, value)

    def setS16(self, offset: int, value: int) -> None:
        """Set an S16 integer"""

        self.setInt(offset, True, 16, value)

    def setU32(self, offset: int, value: int) -> None:
        """Set an U32 integer"""

        self.setInt(offset, False, 32, value)

    def setS32(self, offset: int, value: int) -> None:
        """Set an S32 integer"""

        self.setInt(offset, True, 32, value)

    def setU64(self, offset: int, value: int) -> None:
        """Set an U64 integer"""

        self.setInt(offset, False, 64, value)

    def setS64(self, offset: int, value: int) -> None:
        """Set an S64 integer"""

        self.setInt(offset, True, 64, value)

    # -----------------------------------------------------------------------
    #
    #  change
    #

    def changeU8(self, offset: int, func: Callable[[int], int]) -> None:
        """Change an U8 integer"""

        self.changeInt(offset, False, 8, func)

    def changeU16(self, offset: int, func: Callable[[int], int]) -> None:
        """Change an U16 integer"""

        self.changeInt(offset, False, 16, func)

    def changeU32(self, offset: int, func: Callable[[int], int]) -> None:
        """Change an U32 integer"""

        self.changeInt(offset, False, 32, func)

    def changeU64(self, offset: int, func: Callable[[int], int]) -> None:
        """Change an U64 integer"""

        self.changeInt(offset, False, 64, func)


    # -----------------------------------------------------------------------
    #
    #  set flag
    #

    def getU8Flag(self, offset: int, bit: int) -> bool:
        """Get an individual bit in an U8 integer"""

        return self.getFlag(offset, False, 8, bit)

    def getU16Flag(self, offset: int, bit: int) -> bool:
        """Get an individual bit in an U16 integer"""

        return self.getFlag(offset, False, 16, bit)

    def getU32Flag(self, offset: int, bit: int) -> bool:
        """Get an individual bit in an U32 integer"""

        return self.getFlag(offset, False, 32, bit)

    def getU64Flag(self, offset: int, bit: int) -> bool:
        """Get an individual bit in an U64 integer"""

        return self.getFlag(offset, False, 64, bit)


    def setU8Flag(self, offset: int, bit: int) -> None:
        """Set an individual bit in an U8 integer"""

        self.setFlag(offset, False, 8, bit)

    def setU16Flag(self, offset: int, bit: int) -> None:
        """Set an individual bit in an U16 integer"""

        self.setFlag(offset, False, 16, bit)

    def setU32Flag(self, offset: int, bit: int) -> None:
        """Set an individual bit in an U32 integer"""

        self.setFlag(offset, False, 32, bit)

    def setU64Flag(self, offset: int, bit: int) -> None:
        """Set an individual bit in an U64 integer"""

        self.setFlag(offset, False, 64, bit)
