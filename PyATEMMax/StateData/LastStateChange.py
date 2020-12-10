#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: LastStateChange
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring


class LastStateChange():

    class TimeCode():
        def __init__(self): # LastStateChange.TimeCode
            self.hour: int = 0
            self.minute: int = 0
            self.second: int = 0
            self.frame: int = 0

        def __str__(self):
            return f"{self.hour:02}:{self.minute:02}:{self.second:02}:{self.frame:02}"

        def __format__(self, format_spec: str) -> str:
            return format(str(self), format_spec)

    def __init__(self): # LastStateChange
        self.timeCode: LastStateChange.TimeCode = LastStateChange.TimeCode()
