#!/usr/bin/env python3
# coding: utf-8
"""
ATEMutils: PyATEMMAx internal utility methods.
Part of the PyATEMMax library.
"""

from typing import Dict, Tuple, Iterable, Any

import time

from .ATEMConstant import ATEMConstantList


def highLowBytes(val: int) -> Tuple[int, int]:
    """Get splitted high/low bytes

    Args:
        val: value to split

    Returns:
        high/low values
    """

    return divmod(val, 0x100)


def highByte(val: int) -> int:
    """Get high byte

    Args:
        val: input value

    Returns:
        high byte
    """

    return highLowBytes(val)[0]


def lowByte(val: int) -> int:
    """Get low byte

    Args:
        val: input value

    Returns:
        low byte
    """

    return highLowBytes(val)[1]


def word(hibyte: int, lobyte: int) -> int:
    """Build a word (16-bit) from 2 bytes

    Args:
        hibyte: high part of the word
        lobyte: low part of the word

    Returns:
        16-bit word
    """

    return (hibyte * 256) + lobyte


def hexStr(buf: Iterable[int]) -> str:
    """Build a hex representation of a buffer

    Args:
        buf : buffer

    Returns:
        hex representation of the buffer
    """

    bufStr = ''
    if buf:
        for b in buf:
            bufStr += f'{b:02x} '
    return bufStr.strip()


def getEmptyDict(value: Any, refDict: ATEMConstantList) -> Any:
    """Generate an empty list filled with an initial value

    Args:
        value: value used to fill the list
        count: amount of items

    Returns:
        filled list
    """

    if isinstance(value, type):
        newDict: Dict[str, Any] = {refDict[k]: value() for k in refDict}
    else:
        newDict = {refDict[k]: value for k in refDict}

    return newDict


def hasTimedOut(_time: float, timeout: float) -> bool:
    """Check if an amount of time has elapsed

    Args:
        _time (int): start time
        timeout (int): number of seconds

    Returns:
        bool: True if timeout has elapsed

    Skårhøj:
        bool hasTimedOut(unsigned long time, unsigned long timeout)
    """

    return time.time() > (_time + timeout)


def boolBit(value: int, bit: int) -> bool:
    """Read a bit from value and return as bool

    Args:
        value (int): value to check
        bit (int): bit number

    Returns:
        bool: True if bit is set, else False
    """

    return True if value & 1<<bit else False


def mapValue(value:float, minFrom:float, maxFrom:float, minTo:float, maxTo:float):
    """Map a value from a range to another one"""

    rangeFrom = maxFrom - minFrom
    rangeTo = maxTo - minTo
    scaled = (value - minFrom) / rangeFrom
    return minTo + (scaled * rangeTo)
