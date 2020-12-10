#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Macro
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class Macro():

    class RunStatus():
        class State():
            def __init__(self): # Macro.RunStatus.State
                self.running: bool = False
                self.waiting: bool = False

        def __init__(self): # Macro.RunStatus
            self.index: int = 0
            self.isLooping: bool = False
            self.state: Macro.RunStatus.State = Macro.RunStatus.State()


    class RecordingStatus():
        def __init__(self): # Macro.RecordingStatus
            self.index: int = 0
            self.isRecording: bool = False


    class Properties():
        def __init__(self): # Macro.Properties
            self.isUsed: bool = False
            self.name: str = ""


    class PropertiesList(ATEMValueDict[Properties]):
        def __init__(self): # Macro.PropertiesList
            super().__init__(Macro.Properties, ATEMProtocol.macros)


    class Pool():
        def __init__(self): # Macro.Pool
            self.banks: int = 0


    def __init__(self): # Macro
        self.properties: Macro.PropertiesList = Macro.PropertiesList()
        self.pool: Macro.Pool = Macro.Pool()
        self.recordingStatus: Macro.RecordingStatus = Macro.RecordingStatus()
        self.runStatus: Macro.RunStatus = Macro.RunStatus()
