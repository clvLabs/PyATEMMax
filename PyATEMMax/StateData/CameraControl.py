#!/usr/bin/env python3
# coding: utf-8
"""
PyATEMMax state data: CameraControl
Part of the PyATEMMax library.
"""

# pylint: disable=missing-class-docstring

from PyATEMMax.ATEMProtocol import ATEMProtocol
from PyATEMMax.ATEMValueDict import ATEMValueDict

class CameraControl():

    class Gain():
        def __init__(self): # CameraControl.Gain
            self.value: int = 0
            self.b: float = 0.0
            self.g: float = 0.0
            self.r: float = 0.0
            self.y: float = 0.0


    class Gamma():
        def __init__(self): # CameraControl.Gamma
            self.b: float = 0.0
            self.g: float = 0.0
            self.r: float = 0.0
            self.y: float = 0.0


    class Lift():
        def __init__(self): # CameraControl.Lift
            self.b: float = 0.0
            self.g: float = 0.0
            self.r: float = 0.0
            self.y: float = 0.0


    class Zoom():
        def __init__(self): # CameraControl.Zoom
            self.normalized: float = 0.0
            self.speed: float = 0.0


    def __init__(self): # CameraControl
        self.colorbars: int = 0
        self.contrast: int = 0
        self.focus: int = 0
        self.gain: CameraControl.Gain = CameraControl.Gain()
        self.gamma: CameraControl.Gamma = CameraControl.Gamma()
        self.hue: float = 0.0
        self.iris: int = 0
        self.lift: CameraControl.Lift = CameraControl.Lift()
        self.lumMix: float = 0.0
        self.saturation: float = 0.0
        self.sharpeningLevel: int = 0
        self.shutter: float = 0.0
        self.whiteBalance: int = 0
        self.zoom: CameraControl.Zoom = CameraControl.Zoom()


class CameraControlList(ATEMValueDict[CameraControl]):
    def __init__(self):
        super().__init__(CameraControl, ATEMProtocol.cameras)
