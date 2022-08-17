#!/usr/bin/env python3
# coding: utf-8
"""
ATEMProtocol: Blackmagic ATEM protocol definitions.
Part of the PyATEMMax library.
"""

# pylint: disable=wildcard-import, unused-wildcard-import

from typing import Union

import math

from .ATEMProtocolEnums import *
from .ATEMException import ATEMException


class ATEMProtocol:
    """Blackmagic ATEM protocol definitions"""

    # ---------------------------------
    # Protocol events
    events: ATEMEvents = ATEMEvents()

    # ---------------------------------
    # Protocol settings

    # ATEM protocol standard UDP port
    UDPPort: int = 9910

    # Default timeout for full connection process
    defaultConnectionTimeout: float = 1.0

    # Default timeout for basic handshake
    defaultHandshakeTimeout: float = 0.1

    # ATEM protocol header command flags
    cmdFlags: ATEMHeaderCmdFlags = ATEMHeaderCmdFlags()

    # Size of packet buffers
    inputBufferLength: int = 10240
    outputBufferLength: int = 250

    # The maximum number of initialization packets.
    # By observation on a 2M/E 4K can be up to (not fixed!) 32. We allocate a f more then...
    maxInitPacketCount: int = 500

    # Field lengths/offsets

    # Size of packet header
    headerLen: int = 12

    # Size of command header (subpacket)
    cmdHeaderLen: int = 8

    # Size of command string (in command header)
    cmdStrLen: int = 4

    # Offset of command string (in command header)
    cmdStrOffset: int = 4

    # ---------------------------------
    # Switcher field value enumerations

    audioSources = ATEMAudioSources()
    audioMixerInputMixOptions = ATEMAudioMixerInputMixOptions()
    audioMixerInputTypes = ATEMAudioMixerInputTypes()
    audioMixerInputPlugTypes = ATEMAudioMixerInputPlugTypes()
    auxChannels = ATEMAUXChannels()
    borderBevels = ATEMBorderBevels()
    boxes = ATEMBoxes()
    camerControlSharpeningLevels = ATEMCamerControlSharpeningLevels()
    cameras = ATEMCameras()
    clipBanks = ATEMClipBanks()
    colorGenerators = ATEMColorGenerators()
    downConverterModes = ATEMDownConverterModes()
    dVETransitionStyles = ATEMDVETransitionStyles()
    dsks = ATEMDSKs()
    externalPortTypes = ATEMExternalPortTypes()
    keyers = ATEMKeyers()
    keyerTypes = ATEMKeyerTypes()
    keyFrames = ATEMKeyFrames()
    macroActions = ATEMMacroActions()
    macros = ATEMMacros()
    mediaPlayers = ATEMMediaPlayers()
    mediaPlayerSourceTypes = ATEMMediaPlayerSourceTypes()
    mixEffects = ATEMMixEffects()
    multiViewerLayouts = ATEMMultiViewerLayouts()
    multiViewers = ATEMMultiViewers()
    patternStyles = ATEMPatternStyles()
    stillBanks = ATEMStillBanks()
    switcherPortTypes = ATEMSwitcherPortTypes()
    transitionStyles = ATEMTransitionStyles()
    videoModeFormats = ATEMVideoModeFormats()
    videoSources = ATEMVideoSources()
    windows = ATEMWindows()


    # ---------------------------------
    # Protocol command names
    commands = {
        "_ver": 'Protocol Version',
        "_pin": 'Product Id',
        "Warn": 'Warning',
        "_top": 'Topology',
        "_MeC": 'Mix Effect Config',
        "_mpl": 'Media Players',
        "_MvC": 'Multi View Config',
        "_SSC": 'Super Source Config',
        "_TlC": 'Tally Channel Config',
        "_AMC": 'Audio Mixer Config',
        "_VMC": 'Video Mixer Config',
        "_MAC": 'Macro Pool',
        "Powr": 'Power',
        "DcOt": 'Down Converter',
        "VidM": 'Video Mode',
        "InPr": 'Input Properties',
        "MvPr": 'Multi Viewer Properties',
        "MvIn": 'Multi Viewer Input',
        "PrgI": 'Program Input',
        "PrvI": 'Preview Input',
        "TrSS": 'Transition',
        "TrPr": 'Transition Preview',
        "TrPs": 'Transition Position',
        "TMxP": 'Transition Mix',
        "TDpP": 'Transition Dip',
        "TWpP": 'Transition Wipe',
        "TDvP": 'Transition DVE',
        "TStP": 'Transition Stinger',
        "KeOn": 'Keyer On Air',
        "KeBP": 'Keyer Base',
        "KeLm": 'Key Luma',
        "KeCk": 'Key Chroma',
        "KePt": 'Key Pattern',
        "KeDV": 'Key DVE',
        "KeFS": 'Keyer Fly',
        "KKFP": 'Keyer Fly Key Frame',
        "DskB": 'Downstream Keyer (B)',
        "DskP": 'Downstream Keyer (P)',
        "DskS": 'Downstream Keyer (S)',
        "FtbP": 'Fade-To-Black',
        "FtbS": 'Fade-To-Black State',
        "ColV": 'Color Generator',
        "AuxS": 'Aux Source',
        "CCdP": 'Camera Control',
        "RCPS": 'Clip Player',
        "MPCE": 'Media Player Source',
        "MPSp": 'Media Pool Storage',
        "MPCS": 'Media Player Clip Source',
        "MPAS": 'Media Player Audio Source',
        "MPfe": 'Media Player Still Files',
        "MRPr": 'Macro Run Status',
        "MPrp": 'Macro Properties',
        "MRcS": 'Macro Recording Status',
        "SSrc": 'Super Source',
        "SSBP": 'Super Source Box Parameters',
        "AMIP": 'Audio Mixer Input',
        "AMMO": 'Audio Mixer Master',
        "AMmO": 'Audio Mixer Monitor',
        "AMLv": 'Audio Mixer Levels',
        "AMTl": 'Audio Mixer Tally',
        "TlIn": 'Tally By Index',
        "TlSr": 'Tally By Source',
        "Time": 'Last State Change Time Code',
        'LKST': 'Lock State',
        'PLCK': 'Acquire Media Lock',
        'LKOB': 'Lock Obtained',
        'LOCK': 'Set Lock State',
        'FTDE': 'Data Transfer Error',
        'FTUA': 'Data Transfer Ack',
        'FTSD': 'Data Transfer to Switcher',
        'FTSU': 'Data Transfer Request',
        'RXMS': 'HyperDeck Settings Get',

        # These commands are not really unknown,
        #   but they are not implemented

        # Documented as (?) in Skårhøj's protocol definition
        "CCdo": "Not implemented: Camera Control Options(?)",

        # Possibly from future versions of the protocol / not found in Skårhøj's protocol
        '_DVE': 'Not implemented: _DVE',
        'AMHP': 'Not implemented: AMHP',
        'AMPP': 'Not implemented: AMPP',
        'ATMP': 'Not implemented: ATMP',
        'CAMI': 'Not implemented: Audio Mixer Input',
        'CAMM': 'Not implemented: Audio Mixer Master',
        'CAMm': 'Not implemented: Audio Mixer Monitor',
        'CAuS': 'Not implemented: Aux Source',
        'CClV': 'Not implemented: Color Generator',
        'CCmd': 'Not implemented: Camera Control',
        'CCst': 'Not implemented: CCst',
        'CDsC': 'Not implemented: Downstream Keyer',
        'CDsF': 'Not implemented: Downstream Keyer',
        'CDsG': 'Not implemented: Downstream Keyer',
        'CDsL': 'Not implemented: Downstream Keyer',
        'CDsM': 'Not implemented: Downstream Keyer',
        'CDsR': 'Not implemented: Downstream Keyer',
        'CDsT': 'Not implemented: Downstream Keyer',
        'CInL': 'Not implemented: Input Properties',
        'CKCk': 'Not implemented: Key Chroma',
        'CKDV': 'Not implemented: Key DVE',
        'CKeC': 'Not implemented: Key Cut',
        'CKeF': 'Not implemented: Key Fill',
        'CKLm': 'Not implemented: Key Luma',
        'CKMs': 'Not implemented: Key Mask',
        'CKOn': 'Not implemented: Keyer On Air',
        'CKPt': 'Not implemented: Key Pattern',
        'CKTp': 'Not implemented: Key Type',
        'CMPA': 'Not implemented: Media Pool Clear Audio',
        'CMPC': 'Not implemented: Media Pool Clear Clip',
        'CMPr': 'Not implemented: Change Macro Properties',
        'CMPS': 'Not implemented: Media Pool Storage',
        'CMvI': 'Not implemented: Multi Viewer Input',
        'CMvP': 'Not implemented: Multi Viewer Properties',
        'CPgI': 'Not implemented: Program Input',
        'CPvI': 'Not implemented: Preview Input',
        'CSBP': 'Not implemented: Super Source Box Parameters',
        'CSSc': 'Not implemented: Super Source',
        'CSTL': 'Not implemented: Media Pool Clear Still',
        'CTDp': 'Not implemented: Transition Dip',
        'CTDv': 'Not implemented: Transition DVE',
        'CTMx': 'Not implemented: Transition Mix',
        'CTPr': 'Not implemented: Transition Preview',
        'CTPs': 'Not implemented: Transition Position',
        'CTSt': 'Not implemented: Transition Stinger',
        'CTTp': 'Not implemented: Transition',
        'CTWp': 'Not implemented: Transition Wipe',
        'CVdM': 'Not implemented: Video Mode',
        'DAut': 'Not implemented: Auto',
        'DCut': 'Not implemented: Cut',
        'DDsA': 'Not implemented: Downstream Keyer Auto',
        'FtbA': 'Not implemented: Fade-To-Black',
        'FtbC': 'Not implemented: Fade-To-Black',
        'FTCD': 'Not implemented: Data Transfer Upload Continue',
        'FTDa': 'Not implemented: Data Transfer Data',
        'FTDC': 'Not implemented: Data Transfer Completed',
        'FTFD': 'Not implemented: Data File Description',
        'InCm': 'Not implemented: Initialization Completed',
        'MAct': 'Not implemented: Macro Action',
        'MMOP': 'Not implemented: MMOP',
        'MPSS': 'Not implemented: Media Player Source',
        'MRCP': 'Not implemented: Macro Run Change Properties',
        'MSlp': 'Not implemented: Macro Add Pause',
        'MSRc': 'Not implemented: Macro Start Recording',
        'MvVM': 'Not implemented: MvVM',
        'PZCS': 'Not implemented: PZCS',
        'RAMP': 'Not implemented: Reset Audio Mixer Peaks',
        'RFlK': 'Not implemented: Run Flying Key',
        'RXCC': 'Not implemented: RXCC',
        'RXCP': 'Not implemented: RXCP',
        'RXSS': 'Not implemented: RXSS',
        'SALN': 'Not implemented: Audio Levels',
        'SCPS': 'Not implemented: Clip Player',
        'SFKF': 'Not implemented: Keyer Fly',
        'SMPC': 'Not implemented: Set Media Player Clip Description',
        'SPtM': 'Not implemented: SPtM',
        'SPZS': 'Not implemented: SPZS',
        'SRcl': 'Not implemented: Clear Startup State',
        'SRsv': 'Not implemented: Save Startup State',
        'TlFc': 'Not implemented: TlFc',
        'TMIP': 'Not implemented: TMIP',
        'V3sl': 'Not implemented: V3sl',
        'VuMC': 'Not implemented: VuMC',
        'VuMo': 'Not implemented: VuMo',
    }


    # ---------------------------------
    # Utility methods

    @staticmethod
    def audioWord2Db(input_: int) -> float:
        """Skårhøj: float audioWord2Db(uint16_t input)"""

        # -48 to +6 output
        if input_ <= 32:
            return -60

        return math.log10(input_/(1<<11) / 16.0) * 20.0


    @staticmethod
    def audioDb2Word(input_: float) -> int:
        """Skårhøj: uint16_t audioDb2Word(float input)"""

        # -48 to +6 input
        return int(math.pow(10, input_/20.0) * 16.0 * (1<<11))


    @staticmethod
    def getVideoSrc(source: Union[ATEMConstant, str, int]) -> int:
        """Get a video source"""

        foundsrc = None

        if isinstance(source, ATEMConstant):
            foundsrc = source.value
        elif isinstance(source, str):
            found = ATEMProtocol.videoSources.byName(source)
            if found:
                foundsrc = found.value
        else: # int
            foundsrc = source

        if foundsrc is None:
            raise ATEMException(f"{source} ({type(source)}) is not a valid source")

        return foundsrc


    @staticmethod
    def getAudioSrc(source: Union[ATEMConstant, str, int]) -> int:
        """Get an audio source"""

        foundsrc = None

        if isinstance(source, ATEMConstant):
            foundsrc = source.value
        elif isinstance(source, str):
            found = ATEMProtocol.audioSources.byName(source)
            if found:
                foundsrc = found.value
        else: # int
            foundsrc = source

        if foundsrc is None:
            raise ATEMException(f"{source} ({type(source)}) is not a valid source")

        return foundsrc
