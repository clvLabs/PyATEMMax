#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: Keyer
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMConstant import ATEMConstant
from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class Keyer():
    class Fly():
        class KeyFrame():
            class Border():

                class Bevel():
                    def __init__(self): # Keyer.Fly.KeyFrame.Border.Bevel
                        self.position: float = 0.0
                        self.softness: float = 0.0


                class Inner():
                    def __init__(self): # Keyer.Fly.KeyFrame.Border.Inner
                        self.softness: int = 0
                        self.width: float = 0.0


                class Outer():
                    def __init__(self): # Keyer.Fly.KeyFrame.Border.Outer
                        self.softness: int = 0
                        self.width: float = 0.0


                def __init__(self): # Keyer.Fly.KeyFrame.Border
                    self.bevel: Keyer.Fly.KeyFrame.Border.Bevel = Keyer.Fly.KeyFrame.Border.Bevel()
                    self.hue: float = 0.0
                    self.inner: Keyer.Fly.KeyFrame.Border.Inner = Keyer.Fly.KeyFrame.Border.Inner()
                    self.luma: float = 0.0
                    self.opacity: int = 0
                    self.outer: Keyer.Fly.KeyFrame.Border.Outer = Keyer.Fly.KeyFrame.Border.Outer()
                    self.saturation: float = 0.0


            class LightSource():
                def __init__(self): # Keyer.Fly.KeyFrame.LightSource
                    self.altitude: int = 0
                    self.direction: float = 0.0


            class Position():
                def __init__(self): # Keyer.Fly.KeyFrame.Position
                    self.x: float = 0.0
                    self.y: float = 0.0


            class Size():
                def __init__(self): # Keyer.Fly.KeyFrame.Size
                    self.x: float = 0.0
                    self.y: float = 0.0


            def __init__(self): # Keyer.Fly.KeyFrame
                self.border: Keyer.Fly.KeyFrame.Border = Keyer.Fly.KeyFrame.Border()
                self.bottom: float = 0.0
                self.left: float = 0.0
                self.lightSource: Keyer.Fly.KeyFrame.LightSource = Keyer.Fly.KeyFrame.LightSource()
                self.position: Keyer.Fly.KeyFrame.Position = Keyer.Fly.KeyFrame.Position()
                self.right: float = 0.0
                self.rotation: float = 0.0
                self.size: Keyer.Fly.KeyFrame.Size = Keyer.Fly.KeyFrame.Size()
                self.top: float = 0.0


        class KeyFrameList(ATEMValueDict[KeyFrame]):
            def __init__(self): # Keyer.Fly.KeyFrameList
                super().__init__(Keyer.Fly.KeyFrame, ATEMProtocol.keyFrames)


        class IsAtKeyFrame():
            def __init__(self): # Keyer.Fly.IsAtKeyFrame
                self.a:bool = False
                self.b:bool = False
                self.full:bool = False
                self.runToInfinite:bool = False


        def __init__(self): # Keyer.Fly
            self.enabled: bool = False
            self.isASet: bool = False
            self.isAtKeyFrame: Keyer.Fly.IsAtKeyFrame = Keyer.Fly.IsAtKeyFrame()
            self.isBSet: bool = False
            self.keyFrame: Keyer.Fly.KeyFrameList = Keyer.Fly.KeyFrameList()
            self.runtoInfiniteindex: int = 0

    class OnAir():
        def __init__(self): # Keyer.OnAir
            self.enabled: bool = False


    def __init__(self): # Keyer
        self.bottom: float = 0.0
        self.fillSource: ATEMConstant = ATEMConstant()
        self.fly: Keyer.Fly = Keyer.Fly()
        self.keySource: ATEMConstant = ATEMConstant()
        self.left: float = 0.0
        self.masked: bool = False
        self.onAir:Keyer.OnAir = Keyer.OnAir()
        self.right: float = 0.0
        self.top: float = 0.0
        self.type: ATEMConstant = ATEMConstant()


class MixEffectKeyerList(ATEMValueDict[Keyer]):
    def __init__(self):
        super().__init__(Keyer, ATEMProtocol.keyers)


class KeyerList(ATEMValueDict[MixEffectKeyerList]):
    def __init__(self):
        super().__init__(MixEffectKeyerList, ATEMProtocol.mixEffects)
