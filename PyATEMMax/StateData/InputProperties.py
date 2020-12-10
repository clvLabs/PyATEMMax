#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: InputProperties
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMValueDict import ATEMValueDict


class InputProperties():
    class ExternalPortTypes():
        def __init__(self): # InputProperties.ExternalPortTypes
            self.sdi: bool = False
            self.hdmi: bool = False
            self.component: bool = False
            self.composite: bool = False
            self.sVideo: bool = False


    class Availability():
        def __init__(self): # InputProperties.Availability
            self.auxiliary: bool = False
            self.multiviewer: bool = False
            self.superSourceArt: bool = False
            self.superSourceBox: bool = False
            self.keySourcesEverywhere: bool = False


    class MEAvailability():
        def __init__(self): # InputProperties.MEAvailability
            self.mE1FillSources: bool = False
            self.mE2FillSources: bool = False


    def __init__(self): # InputProperties
        self.availability: InputProperties.Availability = InputProperties.Availability()
        self.availableExternalPortTypes: InputProperties.ExternalPortTypes = InputProperties.ExternalPortTypes()
        self.externalPortType: ATEMConstant = ATEMConstant()
        self.longName: str = ""
        self.mEAvailability: InputProperties.MEAvailability = InputProperties.MEAvailability()
        self.portType: ATEMConstant = ATEMConstant()
        self.shortName: str = ""


class InputPropertiesList(ATEMValueDict[InputProperties]):
    def __init__(self):
        super().__init__(InputProperties, ATEMProtocol.videoSources)
