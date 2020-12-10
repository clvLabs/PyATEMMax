#!/usr/bin/env python3
# coding: utf-8
"""
ATEMValueDict: Blackmagic ATEM switcher: Base classes for value dictionaries
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring, wildcard-import, unused-wildcard-import

from typing import Any, Optional, TypeVar, Generic

from .ATEMUtils import getEmptyDict
from .ATEMConstant import ATEMConstant, ATEMConstantList
from .ATEMException import ATEMException


ITEMTYPE = TypeVar('ITEMTYPE')

class ATEMValueDict(Generic[ITEMTYPE]):
    def __init__(self, itemClass: Any, itemDict: ATEMConstantList):
        self.itemClass = itemClass
        self.itemDict = itemDict
        self._data = getEmptyDict(itemClass, itemDict)

    def __getitem__(self, itemKey: Any) -> ITEMTYPE:
        _key: Optional[Any] = None

        if isinstance(itemKey, int):
            _key = self.itemDict.byValue(itemKey)
        elif isinstance(itemKey, str):
            _key = self.itemDict.byName(itemKey)
        elif isinstance(itemKey, ATEMConstant):
            _key = itemKey

        if _key is None:
            raise ATEMException(f"{itemKey} ({type(itemKey)}) is not a valid key for {self.itemClass.__name__}[]")

        return self._data[_key]
