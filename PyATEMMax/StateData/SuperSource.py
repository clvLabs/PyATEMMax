#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: SuperSource
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring


from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict


class SuperSource():


    class BoxParameters():

        class Crop():
            def __init__(self): # SuperSource.BoxParameters.Crop
                self.bottom: float = 0.0
                self.left: float = 0.0
                self.right: float = 0.0
                self.top: float = 0.0


        class Position():
            def __init__(self): # SuperSource.BoxParameters.Position
                self.x: float = 0.0
                self.y: float = 0.0


        def __init__(self): # SuperSource.BoxParameters
            self.crop: SuperSource.BoxParameters.Crop = SuperSource.BoxParameters.Crop()
            self.cropped: bool = False
            self.enabled: bool = False
            self.inputSource: ATEMConstant = ATEMConstant()
            self.position: SuperSource.BoxParameters.Position = SuperSource.BoxParameters.Position()
            self.size: float = 0.0


    class BoxParametersList(ATEMValueDict[BoxParameters]):
        def __init__(self): # SuperSource.BoxParametersList
            super().__init__(SuperSource.BoxParameters, ATEMProtocol.boxes)


    class Border():
        class Bevel():
            def __init__(self): # SuperSource.Border.Bevel
                self.value: ATEMConstant = ATEMConstant()
                self.position: float = 0.0
                self.softness: float = 0.0


        class Inner():
            def __init__(self): # SuperSource.Border.Inner
                self.softness: int = 0
                self.width: float = 0.0


        class Outer():
            def __init__(self): # SuperSource.Border.Outer
                self.softness: int = 0
                self.width: float = 0.0


        def __init__(self): # SuperSource.Border
            self.enabled: bool = False
            self.hue: float = 0.0
            self.luma: float = 0.0
            self.saturation: float = 0.0
            self.bevel: SuperSource.Border.Bevel = SuperSource.Border.Bevel()
            self.inner: SuperSource.Border.Inner = SuperSource.Border.Inner()
            self.outer: SuperSource.Border.Outer = SuperSource.Border.Outer()


    class LightSource():
        def __init__(self): # SuperSource.LightSource
            self.altitude: int = 0
            self.direction: float = 0.0


    class Config():
        def __init__(self): # SuperSource.Config
            self.boxes: int = 0


    def __init__(self): # SuperSource
        self.border:SuperSource.Border = SuperSource.Border()
        self.clip: float = 0.0
        self.config:SuperSource.Config = SuperSource.Config()
        self.boxParameters:SuperSource.BoxParametersList = SuperSource.BoxParametersList()
        self.fillSource: ATEMConstant = ATEMConstant()
        self.foreground: bool = False
        self.gain: float = 0.0
        self.invertKey: bool = False
        self.keySource: ATEMConstant = ATEMConstant()
        self.lightSource:SuperSource.LightSource = SuperSource.LightSource()
        self.preMultiplied: bool = False
