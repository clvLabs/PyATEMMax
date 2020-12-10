#!/usr/bin/env python3
# coding: utf-8
"""
ATEMConstant: Blackmagic ATEM protocol definitions - constant value base class
Part of the PyATEMMax library.
"""

from typing import Any, Optional, Union

from .ATEMException import ATEMException


class ATEMConstant:
    """Meta-class to generate constant values"""

    def __init__(self, name: str = "", value: Any = None):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"PyATEMMax.ATEMProtocolEnums.ATEMConstant(name={self.name}, value={self.value})"

    def __format__(self, format_spec: str) -> str:
        return format(str(self), format_spec)


class ATEMConstantList:
    """Meta-class to generate value lists"""


    class Iterator:
        """Iterator for ATEMConstantList"""

        def __init__(self, class_: Any):
            self._values = class_._values
            self._keylist = list(class_._values.keys())
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < len(self._keylist):
                key = self._keylist[self._index]
                value = self._values[key]
                self._index += 1
                return value
            raise StopIteration


    def __init__(self):
        self._values = {
                prop: self.__getattribute__(prop)
                for prop in self.__class__.__dict__
                if isinstance(self.__getattribute__(prop), ATEMConstant)
            }


    def __len__(self):
        return len(self._values)


    def __getitem__(self, item: Union[ATEMConstant, str, int]) -> Any:
        key: str

        if isinstance(item, ATEMConstant):
            found = self._byValue(item)
            if found is None:
                raise ATEMException(f"Wrong value for {self.__class__.__name__}: [{item}] ({type(item)})")
            else:
                key = found.name
        elif isinstance(item, str):
            found = self.byName(item)
            if found is None:
                raise ATEMException(f"Wrong value for {self.__class__.__name__}: [{item}] ({type(item)})")
            key = item
        else: # int
            found = self._byValue(item)
            if found is None:
                raise ATEMException(f"Wrong value for {self.__class__.__name__}: [{item}] ({type(item)})")
            else:
                key = found.name

        return self._values[key]     # retval hit TypeValue o como sea de typing


    def __iter__(self):
        return ATEMConstantList.Iterator(self)


    def __next__(self):
        pass


    def getName(self, value: Union[ATEMConstant, int]) -> str:
        """Get ATEMConstant name from value"""

        found = self._byValue(value)
        return found.name if found else ""


    def byName(self, name: str) -> Optional[Any]:
        """Get ATEMConstant name from name"""

        return self._values[name]


    def _byValue(self, value: Union[ATEMConstant, int]) -> Optional[ATEMConstant]:
        """Get ATEMConstant item from value"""

        if isinstance(value, ATEMConstant):
            value = value.value
        found = None
        for k in self._values:
            v = self._values[k].value
            if v == value:
                found = self._values[k]
                break
        return found


    def byValue(self, value: Union[ATEMConstant, int]) -> ATEMConstant:
        """Get ATEMConstant item from value"""

        found = self._byValue(value)
        return found if found else ATEMConstant()
