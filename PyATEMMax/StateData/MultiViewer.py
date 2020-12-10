#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: MultiViewer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class MultiViewer():

    class Properties():
        def __init__(self): # MultiViewer.Properties
            self.layout: ATEMConstant = ATEMConstant()


    class PropertiesList(ATEMValueDict[Properties]):
        def __init__(self): # MultiViewer.PropertiesList
            super().__init__(MultiViewer.Properties, ATEMProtocol.multiViewers)


    class InputWindow():
        def __init__(self): # MultiViewer.InputWindow
            self.videoSource: ATEMConstant = ATEMConstant()


    class InputWindowList(ATEMValueDict[InputWindow]):
        def __init__(self): # MultiViewer.InputWindowList
            super().__init__(MultiViewer.InputWindow, ATEMProtocol.windows)


    class InputList(ATEMValueDict[InputWindowList]):
        def __init__(self): # MultiViewer.InputList
            super().__init__(MultiViewer.InputWindowList, ATEMProtocol.multiViewers)


    class Config():
        def __init__(self): # MultiViewer.Config
            self.multiViewers: int = 0


    def __init__(self): # MultiViewer
        self.config: MultiViewer.Config = MultiViewer.Config()
        self.input: MultiViewer.InputList = MultiViewer.InputList()
        self.properties: MultiViewer.PropertiesList = MultiViewer.PropertiesList()
