#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Power
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring


class Power():
    class Status():
        def __init__(self): # Power.Status
            self.main: bool = False
            self.backup: bool = False


    def __init__(self): # Power
        self.status:Power.Status = Power.Status()
