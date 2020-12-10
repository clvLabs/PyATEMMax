#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: ProtocolVersion
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring, wildcard-import, unused-wildcard-import


class ProtocolVersion():
    def __init__(self):
        self.major: int = 0
        self.minor: int = 0

    def __str__(self):
        return f"v{self.major}.{self.minor}"

    def __format__(self, format_spec: str) -> str:
        return format(str(self), format_spec)
