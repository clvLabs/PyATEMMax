#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Topology
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring


class Topology():
    def __init__(self): # Topology
        self.auxBusses: int = 0
        self.colorGenerators: int = 0
        self.downstreamKeyers: int = 0
        self.dVEs: int = 0
        self.hasSDOutput: bool = False
        self.mEs: int = 0
        self.sources: int = 0
        self.stingers: int = 0
        self.superSources: int = 0
