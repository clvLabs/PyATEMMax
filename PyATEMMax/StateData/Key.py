#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Key
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class Key():

    class Luma():
        def __init__(self): # Key.Luma
            self.clip: float = 0.0
            self.gain: float = 0.0
            self.invertKey: bool = False
            self.preMultiplied: bool = False

    class Pattern():
        class Position(): # Key.Pattern.Position
            def __init__(self):
                self.x: float = 0.0
                self.y: float = 0.0


        def __init__(self): # Key.Pattern
            self.invertPattern: bool = False
            self.pattern: ATEMConstant = ATEMConstant()
            self.position: Key.Pattern.Position = Key.Pattern.Position()
            self.size: float = 0.0
            self.softness: float = 0.0
            self.symmetry: float = 0.0


    class DVE():
        class Border():
            class Bevel():
                def __init__(self): # Key.DVE.Border.Bevel
                    self.type: ATEMConstant = ATEMConstant()
                    self.position: float = 0.0
                    self.softness: float = 0.0


            class Inner():
                def __init__(self): # Key.DVE.Border.Inner
                    self.softness: int = 0
                    self.width: float = 0.0


            class Outer():
                def __init__(self): # Key.DVE.Border.Outer
                    self.softness: int = 0
                    self.width: float = 0.0


            def __init__(self): # Key.DVE.Border
                self.enabled: bool = False
                self.hue: float = 0.0
                self.luma: float = 0.0
                self.opacity: int = 0
                self.saturation: float = 0.0
                self.bevel: Key.DVE.Border.Bevel = Key.DVE.Border.Bevel()
                self.inner: Key.DVE.Border.Inner = Key.DVE.Border.Inner()
                self.outer: Key.DVE.Border.Outer = Key.DVE.Border.Outer()


        class LightSource():
            def __init__(self): # Key.DVE.LightSource
                self.altitude: int = 0
                self.direction: float = 0.0


        class Position():
            def __init__(self): # Key.DVE.Position
                self.x: float = 0.0
                self.y: float = 0.0


        class Size():
            def __init__(self): # Key.DVE.Size
                self.x: float = 0.0
                self.y: float = 0.0


        def __init__(self): # Key.DVE
            self.border:Key.DVE.Border = Key.DVE.Border()
            self.bottom: float = 0.0
            self.left: float = 0.0
            self.lightSource: Key.DVE.LightSource = Key.DVE.LightSource()
            self.masked: bool = False
            self.position: Key.DVE.Position = Key.DVE.Position()
            self.rate: int = 0
            self.right: float = 0.0
            self.rotation: float = 0.0
            self.shadow: bool = False
            self.size: Key.DVE.Size = Key.DVE.Size()
            self.top: float = 0.0


    class Chroma():
        def __init__(self): # Key.Chroma
            self.gain: float = 0.0
            self.hue: float = 0.0
            self.lift: float = 0.0
            self.narrow: bool = False
            self.ySuppress: float = 0.0


    def __init__(self): # Key
        self.chroma:Key.Chroma = Key.Chroma()
        self.dVE:Key.DVE = Key.DVE()
        self.luma: Key.Luma = Key.Luma()
        self.pattern: Key.Pattern = Key.Pattern()


class MixEffectKeyList(ATEMValueDict[Key]):
    def __init__(self):
        super().__init__(Key, ATEMProtocol.keyers)


class KeyList(ATEMValueDict[MixEffectKeyList]):
    def __init__(self):
        super().__init__(MixEffectKeyList, ATEMProtocol.mixEffects)
