#!/usr/bin/env python3
# coding: utf-8
"""
ATEMProtocolEnums: Blackmagic ATEM protocol definitions - value enumerations
Part of the PyATEMMax library.
"""

from .ATEMConstant import ATEMConstant, ATEMConstantList


# #######################################################################
#
# Events
#

class ATEMEvents:
    """Events emitted by the library"""

    connectAttempt:str = 'connectAttempt'
    connect:str = 'connect'
    disconnect:str = 'disconnect'
    receive:str = 'receive'
    warning:str = 'warning'


# #######################################################################
#
# Named lists
#


class ATEMHeaderCmdFlags(ATEMConstantList):
    """Protocol header command flags list"""

    ackRequest = ATEMConstant('ackRequest', 0x1)               # Please acknowledge reception of this packet...
    helloPacket = ATEMConstant('helloPacket', 0x2)             # This is a handshake packet
    resend = ATEMConstant('resend', 0x4)                       # This is a resent information
    requestNextAfter = ATEMConstant('requestNextAfter', 0x8)   # I'm requesting you to resend something to me.
    ack = ATEMConstant('ack', 0x10)                            # Packet is ACK to packetId (byte 4-5) ackRequest


class ATEMVideoSources(ATEMConstantList):
    """VideoSource list"""

    black = ATEMConstant('black', 0)

    input1 = ATEMConstant('input1', 1)
    input2 = ATEMConstant('input2', 2)
    input3 = ATEMConstant('input3', 3)
    input4 = ATEMConstant('input4', 4)
    input5 = ATEMConstant('input5', 5)
    input6 = ATEMConstant('input6', 6)
    input7 = ATEMConstant('input7', 7)
    input8 = ATEMConstant('input8', 8)
    input9 = ATEMConstant('input9', 9)
    input10 = ATEMConstant('input10', 10)
    input11 = ATEMConstant('input11', 11)
    input12 = ATEMConstant('input12', 12)
    input13 = ATEMConstant('input13', 13)
    input14 = ATEMConstant('input14', 14)
    input15 = ATEMConstant('input15', 15)
    input16 = ATEMConstant('input16', 16)
    input17 = ATEMConstant('input17', 17)
    input18 = ATEMConstant('input18', 18)
    input19 = ATEMConstant('input19', 19)
    input20 = ATEMConstant('input20', 20)
    input21 = ATEMConstant('input21', 21)
    input22 = ATEMConstant('input22', 22)
    input23 = ATEMConstant('input23', 23)
    input24 = ATEMConstant('input24', 24)
    input25 = ATEMConstant('input25', 25)
    input26 = ATEMConstant('input26', 26)
    input27 = ATEMConstant('input27', 27)
    input28 = ATEMConstant('input28', 28)
    input29 = ATEMConstant('input29', 29)
    input30 = ATEMConstant('input30', 30)
    input31 = ATEMConstant('input31', 31)
    input32 = ATEMConstant('input32', 32)
    input33 = ATEMConstant('input33', 33)
    input34 = ATEMConstant('input34', 34)
    input35 = ATEMConstant('input35', 35)
    input36 = ATEMConstant('input36', 36)
    input37 = ATEMConstant('input37', 37)
    input38 = ATEMConstant('input38', 38)
    input39 = ATEMConstant('input39', 39)
    input40 = ATEMConstant('input40', 40)

    colorBars = ATEMConstant('colorBars', 1000)

    color1 = ATEMConstant('color1', 2001)
    color2 = ATEMConstant('color2', 2002)

    mediaPlayer1 = ATEMConstant('mediaPlayer1', 3010)
    mediaPlayer1Key = ATEMConstant('mediaPlayer1Key', 3011)
    mediaPlayer2 = ATEMConstant('mediaPlayer2', 3020)
    mediaPlayer2Key = ATEMConstant('mediaPlayer2Key', 3021)
    mediaPlayer3 = ATEMConstant('mediaPlayer3', 3030)
    mediaPlayer3Key = ATEMConstant('mediaPlayer3Key', 3031)
    mediaPlayer4 = ATEMConstant('mediaPlayer4', 3040)
    mediaPlayer4Key = ATEMConstant('mediaPlayer4Key', 3041)

    key1Mask = ATEMConstant('key1Mask', 4010)
    key2Mask = ATEMConstant('key2Mask', 4020)
    key3Mask = ATEMConstant('key3Mask', 4030)
    key4Mask = ATEMConstant('key4Mask', 4040)
    key5Mask = ATEMConstant('key5Mask', 4050)
    key6Mask = ATEMConstant('key6Mask', 4060)
    key7Mask = ATEMConstant('key7Mask', 4070)
    key8Mask = ATEMConstant('key8Mask', 4080)
    key9Mask = ATEMConstant('key9Mask', 4090)
    key10Mask = ATEMConstant('key10Mask', 4100)
    key11Mask = ATEMConstant('key11Mask', 4110)
    key12Mask = ATEMConstant('key12Mask', 4120)
    key13Mask = ATEMConstant('key13Mask', 4130)
    key14Mask = ATEMConstant('key14Mask', 4140)
    key15Mask = ATEMConstant('key15Mask', 4150)
    key16Mask = ATEMConstant('key16Mask', 4160)

    dsk1Mask = ATEMConstant('dsk1Mask', 5010)
    dsk2Mask = ATEMConstant('dsk2Mask', 5020)
    dsk3Mask = ATEMConstant('dsk3Mask', 5030)
    dsk4Mask = ATEMConstant('dsk4Mask', 5040)

    superSource = ATEMConstant('superSource', 6000)
    superSource2 = ATEMConstant('superSource2', 6001)

    cleanFeed1 = ATEMConstant('cleanFeed1', 7001)
    cleanFeed2 = ATEMConstant('cleanFeed2', 7002)
    cleanFeed3 = ATEMConstant('cleanFeed3', 7003)
    cleanFeed4 = ATEMConstant('cleanFeed4', 7004)

    auxilary1 = ATEMConstant('auxilary1', 8001)
    auxilary2 = ATEMConstant('auxilary2', 8002)
    auxilary3 = ATEMConstant('auxilary3', 8003)
    auxilary4 = ATEMConstant('auxilary4', 8004)
    auxilary5 = ATEMConstant('auxilary5', 8005)
    auxilary6 = ATEMConstant('auxilary6', 8006)

    auxilary7 = ATEMConstant('auxilary7', 8007)
    auxilary8 = ATEMConstant('auxilary8', 8008)
    auxilary9 = ATEMConstant('auxilary9', 8009)
    auxilary10 = ATEMConstant('auxilary10', 8010)
    auxilary11 = ATEMConstant('auxilary11', 8011)
    auxilary12 = ATEMConstant('auxilary12', 8012)
    auxilary13 = ATEMConstant('auxilary13', 8013)
    auxilary14 = ATEMConstant('auxilary14', 8014)
    auxilary15 = ATEMConstant('auxilary15', 8015)
    auxilary16 = ATEMConstant('auxilary16', 8016)
    auxilary17 = ATEMConstant('auxilary17', 8017)
    auxilary18 = ATEMConstant('auxilary18', 8018)
    auxilary19 = ATEMConstant('auxilary19', 8019)
    auxilary20 = ATEMConstant('auxilary20', 8020)
    auxilary21 = ATEMConstant('auxilary21', 8021)
    auxilary22 = ATEMConstant('auxilary22', 8022)
    auxilary23 = ATEMConstant('auxilary23', 8023)
    auxilary24 = ATEMConstant('auxilary24', 8024)

    mE1Prog = ATEMConstant('mE1Prog', 10010)
    mE1Prev = ATEMConstant('mE1Prev', 10011)
    mE2Prog = ATEMConstant('mE2Prog', 10020)
    mE2Prev = ATEMConstant('mE2Prev', 10021)
    mE3Prog = ATEMConstant('mE3Prog', 10030)
    mE3Prev = ATEMConstant('mE3Prev', 10031)
    mE4Prog = ATEMConstant('mE4Prog', 10040)
    mE4Prev = ATEMConstant('mE4Prev', 10041)

    input1Direct = ATEMConstant('input1Direct', 11001)


class ATEMAudioSources(ATEMConstantList):
    """AudioSource list"""

    input1 = ATEMConstant('input1', 1)
    input2 = ATEMConstant('input2', 2)
    input3 = ATEMConstant('input3', 3)
    input4 = ATEMConstant('input4', 4)
    input5 = ATEMConstant('input5', 5)
    input6 = ATEMConstant('input6', 6)
    input7 = ATEMConstant('input7', 7)
    input8 = ATEMConstant('input8', 8)
    input9 = ATEMConstant('input9', 9)
    input10 = ATEMConstant('input10', 10)
    input11 = ATEMConstant('input11', 11)
    input12 = ATEMConstant('input12', 12)
    input13 = ATEMConstant('input13', 13)
    input14 = ATEMConstant('input14', 14)
    input15 = ATEMConstant('input15', 15)
    input16 = ATEMConstant('input16', 16)
    input17 = ATEMConstant('input17', 17)
    input18 = ATEMConstant('input18', 18)
    input19 = ATEMConstant('input19', 19)
    input20 = ATEMConstant('input20', 20)

    xlr = ATEMConstant('xlr', 1001)
    aes_ebu = ATEMConstant('aes_ebu', 1101)
    rca = ATEMConstant('rca', 1201)

    mic1 = ATEMConstant('mic1', 1301)
    mic2 = ATEMConstant('mic2', 1302)

    mp1 = ATEMConstant('mp1', 2001)
    mp2 = ATEMConstant('mp2', 2002)
    mp3 = ATEMConstant('mp3', 2003)
    mp4 = ATEMConstant('mp4', 2004)


class ATEMDownConverterModes(ATEMConstantList):
    """DownConverterMode list"""

    centerCut = ATEMConstant('centerCut', 0)
    letterBox = ATEMConstant('letterBox', 1)
    anamorphic = ATEMConstant('anamorphic', 2)


class ATEMVideoModeFormats(ATEMConstantList):
    """VideoModeFormat list"""

    f525i59_94_ntsc = ATEMConstant('f525i59_94_ntsc', 0)            # 525i59.94 NTSC
    f625i_50_pal = ATEMConstant('f625i_50_pal', 1)                  # 625i 50 PAL
    f525i59_94_ntsc_16_9 = ATEMConstant('f525i59_94_ntsc_16_9', 2)  # 525i59.94 NTSC 16:9
    f625i_50_pal_16_9 = ATEMConstant('f625i_50_pal_16_9', 3)        # 625i 50 PAL 16:9
    f720p50 = ATEMConstant('f720p50', 4)                            # 720p50
    f720p59_94 = ATEMConstant('f720p59_94', 5)                      # 720p59.94
    f1080i50 = ATEMConstant('f1080i50', 6)                          # 1080i50
    f1080i59_94 = ATEMConstant('f1080i59_94', 7)                    # 1080i59.94
    f1080p23_98 = ATEMConstant('f1080p23_98', 8)                    # 1080p23.98
    f1080p24 = ATEMConstant('f1080p24', 9)                          # 1080p24
    f1080p25 = ATEMConstant('f1080p25', 10)                         # 1080p25
    f1080p29_97 = ATEMConstant('f1080p29_97', 11)                   # 1080p29.97
    f1080p50 = ATEMConstant('f1080p50', 12)                         # 1080p50
    f1080p59_94 = ATEMConstant('f1080p59_94', 13)                   # 1080p59.94
    f2160p23_98 = ATEMConstant('f2160p23_98', 14)                   # 2160p23.98
    f2160p24 = ATEMConstant('f2160p24', 15)                         # 2160p24
    f2160p25 = ATEMConstant('f2160p25', 16)                         # 2160p25
    f2160p29_97 = ATEMConstant('f2160p29_97', 17)                   # 2160p29.97


class ATEMExternalPortTypes(ATEMConstantList):
    """ExternalPortType list"""

    internal = ATEMConstant('internal', 0)
    sdi = ATEMConstant('sdi', 1)
    hdmi = ATEMConstant('hdmi', 2)
    composite = ATEMConstant('composite', 3)
    component = ATEMConstant('component', 4)
    sVideo = ATEMConstant('sVideo', 5)


class ATEMSwitcherPortTypes(ATEMConstantList):
    """SwitcherPortType list"""

    external = ATEMConstant('external', 0)
    black = ATEMConstant('black', 1)
    colorBars = ATEMConstant('colorBars', 2)
    colorGenerator = ATEMConstant('colorGenerator', 3)
    mediaPlayerFill = ATEMConstant('mediaPlayerFill', 4)
    mediaPlayerKey = ATEMConstant('mediaPlayerKey', 5)
    superSource = ATEMConstant('superSource', 6)
    externalDirect = ATEMConstant('externalDirect', 6)
    mEOutput = ATEMConstant('mEOutput', 128)
    auxiliary = ATEMConstant('auxiliary', 129)
    mask = ATEMConstant('mask', 130)
    multiviewer = ATEMConstant('multiviewer', 131)


class ATEMMultiViewerLayouts(ATEMConstantList):
    """MultiViewerLayout list"""

    top = ATEMConstant('top', 0)
    bottom = ATEMConstant('bottom', 1)
    left = ATEMConstant('left', 2)
    right = ATEMConstant('right', 3)


class ATEMTransitionStyles(ATEMConstantList):
    """TransitionStyle list"""

    mix = ATEMConstant('mix', 0)
    dip = ATEMConstant('dip', 1)
    wipe = ATEMConstant('wipe', 2)
    dVE = ATEMConstant('dVE', 3)
    sting = ATEMConstant('sting', 4)


class ATEMKeyerTypes(ATEMConstantList):
    """KeyerType list"""

    luma = ATEMConstant('luma', 0)
    chroma = ATEMConstant('chroma', 1)
    pattern = ATEMConstant('pattern', 2)
    dVE = ATEMConstant('dVE', 3)


class ATEMBorderBevels(ATEMConstantList):
    """BorderBevel list"""

    no = ATEMConstant('no', 0)
    inOut = ATEMConstant('inOut', 1)
    in_ = ATEMConstant('in_', 2)     # Sorry, Python stuff...
    out = ATEMConstant('out', 3)


class ATEMMediaPlayerSourceTypes(ATEMConstantList):
    """MediaPlayerSourceType list"""

    still = ATEMConstant('still', 1)
    clip = ATEMConstant('clip', 2)


class ATEMAudioMixerInputTypes(ATEMConstantList):
    """AudioMixerInputType list"""

    externalVideo = ATEMConstant('externalVideo', 0)
    mediaPlayer = ATEMConstant('mediaPlayer', 1)
    externalAudio = ATEMConstant('externalAudio', 2)


class ATEMAudioMixerInputPlugTypes(ATEMConstantList):
    """AudioMixerInputPlugType list"""

    internal = ATEMConstant('internal', 0)
    sdi = ATEMConstant('sdi', 1)
    hdmi = ATEMConstant('hdmi', 2)
    component = ATEMConstant('component', 3)
    composite = ATEMConstant('composite', 4)
    sVideo = ATEMConstant('sVideo', 5)
    xlr = ATEMConstant('xlr', 32)
    aes_ebu = ATEMConstant('aes_ebu', 64)
    rca = ATEMConstant('rca', 128)


class ATEMAudioMixerInputMixOptions(ATEMConstantList):
    """AudioMixerInputMixOption list"""

    off = ATEMConstant('off', 0)
    on = ATEMConstant('on', 1)
    afv = ATEMConstant('afv', 2)


class ATEMDVETransitionStyles(ATEMConstantList):
    """DVETransitionStyle list"""

    swooshTopLeft = ATEMConstant('swooshTopLeft', 0)
    swooshTop = ATEMConstant('swooshTop', 1)
    swooshTopRight = ATEMConstant('swooshTopRight', 2)
    swooshLeft = ATEMConstant('swooshLeft', 3)
    swooshRight = ATEMConstant('swooshRight', 4)
    swooshBottomLeft = ATEMConstant('swooshBottomLeft', 5)
    swooshBottom = ATEMConstant('swooshBottom', 6)
    swooshBottomRight = ATEMConstant('swooshBottomRight', 7)

    spinCCWTopRight = ATEMConstant('spinCCWTopRight', 13)
    spinCWTopLeft = ATEMConstant('spinCWTopLeft', 8)
    spinCCWBottomRight = ATEMConstant('spinCCWBottomRight', 15)
    spinCWBottomLeft = ATEMConstant('spinCWBottomLeft', 10)
    spinCWTopRight = ATEMConstant('spinCWTopRight', 9)
    spinCCWTopLeft = ATEMConstant('spinCCWTopLeft', 12)
    spinCWBottomRight = ATEMConstant('spinCWBottomRight', 11)
    spinCCWBottomLeft = ATEMConstant('spinCCWBottomLeft', 14)

    squeezeTopLeft = ATEMConstant('squeezeTopLeft', 16)
    squeezeTop = ATEMConstant('squeezeTop', 17)
    squeezeTopRight = ATEMConstant('squeezeTopRight', 18)
    squeezeLeft = ATEMConstant('squeezeLeft', 19)
    squeezeRight = ATEMConstant('squeezeRight', 20)
    squeezeBottomLeft = ATEMConstant('squeezeBottomLeft', 21)
    squeezeBottom = ATEMConstant('squeezeBottom', 22)
    squeezeBottomRight = ATEMConstant('squeezeBottomRight', 23)

    pushTopLeft = ATEMConstant('pushTopLeft', 24)
    pushTop = ATEMConstant('pushTop', 25)
    pushTopRight = ATEMConstant('pushTopRight', 26)
    pushLeft = ATEMConstant('pushLeft', 27)
    pushRight = ATEMConstant('pushRight', 28)
    pushBottomLeft = ATEMConstant('pushBottomLeft', 29)
    pushBottom = ATEMConstant('pushBottom', 30)
    pushBottomRight = ATEMConstant('pushBottomRight', 31)

    graphicCWSpin = ATEMConstant('graphicCWSpin', 32)
    graphicCCWSpin = ATEMConstant('graphicCCWSpin', 33)
    graphicLogoWipe = ATEMConstant('graphicLogoWipe', 34)


class ATEMPatternStyles(ATEMConstantList):
    """PatternStyle list"""

    leftToRightBar = ATEMConstant('leftToRightBar', 0)
    topToBottomBar = ATEMConstant('topToBottomBar', 1)
    horizontalBarnDoor = ATEMConstant('horizontalBarnDoor', 2)
    verticalBarnDoor = ATEMConstant('verticalBarnDoor', 3)
    cornersInFourBox = ATEMConstant('cornersInFourBox', 4)
    rectangleIris = ATEMConstant('rectangleIris', 5)
    diamondIris = ATEMConstant('diamondIris', 6)
    circleIris = ATEMConstant('circleIris', 7)
    topLeftBox = ATEMConstant('topLeftBox', 8)
    topRightBox = ATEMConstant('topRightBox', 9)
    bottomRightBox = ATEMConstant('bottomRightBox', 10)
    bottomLeftBox = ATEMConstant('bottomLeftBox', 11)
    topCentreBox = ATEMConstant('topCentreBox', 12)
    rightCentreBox = ATEMConstant('rightCentreBox', 13)
    bottomCentreBox = ATEMConstant('bottomCentreBox', 14)
    leftCentreBox = ATEMConstant('leftCentreBox', 15)
    topLeftDiagonal = ATEMConstant('topLeftDiagonal', 16)
    topRightDiagonal = ATEMConstant('topRightDiagonal', 17)


class ATEMCamerControlSharpeningLevels(ATEMConstantList):
    """CamerControlSharpeningLevel list"""

    off = ATEMConstant('off', 0)
    low = ATEMConstant('low', 1)
    medium = ATEMConstant('medium', 2)
    high = ATEMConstant('high', 3)


class ATEMMacroActions(ATEMConstantList):
    """MacroAction list"""

    runMacro = ATEMConstant('runMacro', 0)
    stopMacro = ATEMConstant('stopMacro', 1)
    stopRecording = ATEMConstant('stopRecording', 2)
    insertWaitForUser = ATEMConstant('insertWaitForUser', 3)
    continueMacro = ATEMConstant('continueMacro', 4)
    deleteMacro = ATEMConstant('deleteMacro', 5)


class ATEMKeyFrames(ATEMConstantList):
    """KeyFrame list"""

    a = ATEMConstant('a', 1)
    b = ATEMConstant('b', 2)
    full = ATEMConstant('full', 3)
    runToInfinite = ATEMConstant('runToInfinite', 4)


# #######################################################################
#
# Value range lists
#

class ATEMMixEffects(ATEMConstantList):
    """MixEffect list"""

    mixEffect1 = ATEMConstant('mixEffect1', 0)
    mixEffect2 = ATEMConstant('mixEffect2', 1)
    mixEffect3 = ATEMConstant('mixEffect3', 2)
    mixEffect4 = ATEMConstant('mixEffect4', 3)


class ATEMMultiViewers(ATEMConstantList):
    """MultiViewer list"""

    multiViewer1 = ATEMConstant('multiViewer1', 0)
    multiViewer2 = ATEMConstant('multiViewer2', 1)


class ATEMWindows(ATEMConstantList):
    """Window list"""

    window1 = ATEMConstant('window1', 0)
    window2 = ATEMConstant('window2', 1)
    window3 = ATEMConstant('window3', 2)
    window4 = ATEMConstant('window4', 3)
    window5 = ATEMConstant('window5', 4)
    window6 = ATEMConstant('window6', 5)
    window7 = ATEMConstant('window7', 6)
    window8 = ATEMConstant('window8', 7)
    window9 = ATEMConstant('window9', 8)
    window10 = ATEMConstant('window10', 9)


class ATEMKeyers(ATEMConstantList):
    """Keyer list"""

    keyer1 = ATEMConstant('keyer1', 0)
    keyer2 = ATEMConstant('keyer2', 1)
    keyer3 = ATEMConstant('keyer3', 2)
    keyer4 = ATEMConstant('keyer4', 3)


class ATEMDSKs(ATEMConstantList):
    """DSK list"""

    dsk1 = ATEMConstant('dsk1', 0)
    dsk2 = ATEMConstant('dsk2', 1)


class ATEMColorGenerators(ATEMConstantList):
    """ColorGenerator list"""

    colorGenerator1 = ATEMConstant('colorGenerator1', 0)
    colorGenerator2 = ATEMConstant('colorGenerator2', 1)


class ATEMAUXChannels(ATEMConstantList):
    """AUXChannel list"""

    auxChannel1 = ATEMConstant('auxChannel1', 0)
    auxChannel2 = ATEMConstant('auxChannel2', 1)
    auxChannel3 = ATEMConstant('auxChannel3', 2)
    auxChannel4 = ATEMConstant('auxChannel4', 3)
    auxChannel5 = ATEMConstant('auxChannel5', 4)
    auxChannel6 = ATEMConstant('auxChannel6', 5)


class ATEMCameras(ATEMConstantList):
    """Camera list"""

    camera1 = ATEMConstant('camera1', 1)
    camera2 = ATEMConstant('camera2', 2)
    camera3 = ATEMConstant('camera3', 3)
    camera4 = ATEMConstant('camera4', 4)
    camera5 = ATEMConstant('camera5', 5)
    camera6 = ATEMConstant('camera6', 6)
    camera7 = ATEMConstant('camera7', 7)
    camera8 = ATEMConstant('camera8', 8)
    camera9 = ATEMConstant('camera9', 9)
    camera10 = ATEMConstant('camera10', 10)
    camera11 = ATEMConstant('camera11', 11)
    camera12 = ATEMConstant('camera12', 12)
    camera13 = ATEMConstant('camera13', 13)
    camera14 = ATEMConstant('camera14', 14)
    camera15 = ATEMConstant('camera15', 15)
    camera16 = ATEMConstant('camera16', 16)
    camera17 = ATEMConstant('camera17', 17)
    camera18 = ATEMConstant('camera18', 18)
    camera19 = ATEMConstant('camera19', 19)
    camera20 = ATEMConstant('camera20', 20)


class ATEMMediaPlayers(ATEMConstantList):
    """MediaPlayer list"""

    mediaPlayer1 = ATEMConstant('mediaPlayer1', 0)
    mediaPlayer2 = ATEMConstant('mediaPlayer2', 1)
    mediaPlayer3 = ATEMConstant('mediaPlayer3', 2)
    mediaPlayer4 = ATEMConstant('mediaPlayer4', 3)


class ATEMClipBanks(ATEMConstantList):
    """ClipBank list"""

    clipBank1 = ATEMConstant('clipBank1', 0)
    clipBank2 = ATEMConstant('clipBank2', 1)


class ATEMStillBanks(ATEMConstantList):
    """StillBank list"""

    stillBank1 = ATEMConstant('stillBank1', 0)
    stillBank2 = ATEMConstant('stillBank2', 1)
    stillBank3 = ATEMConstant('stillBank3', 2)
    stillBank4 = ATEMConstant('stillBank4', 3)
    stillBank5 = ATEMConstant('stillBank5', 4)
    stillBank6 = ATEMConstant('stillBank6', 5)
    stillBank7 = ATEMConstant('stillBank7', 6)
    stillBank8 = ATEMConstant('stillBank8', 7)
    stillBank9 = ATEMConstant('stillBank9', 8)
    stillBank10 = ATEMConstant('stillBank10', 9)
    stillBank11 = ATEMConstant('stillBank11', 10)
    stillBank12 = ATEMConstant('stillBank12', 11)
    stillBank13 = ATEMConstant('stillBank13', 12)
    stillBank14 = ATEMConstant('stillBank14', 13)
    stillBank15 = ATEMConstant('stillBank15', 14)
    stillBank16 = ATEMConstant('stillBank16', 15)
    stillBank17 = ATEMConstant('stillBank17', 16)
    stillBank18 = ATEMConstant('stillBank18', 17)
    stillBank19 = ATEMConstant('stillBank19', 18)
    stillBank20 = ATEMConstant('stillBank20', 19)
    stillBank21 = ATEMConstant('stillBank21', 20)
    stillBank22 = ATEMConstant('stillBank22', 21)
    stillBank23 = ATEMConstant('stillBank23', 22)
    stillBank24 = ATEMConstant('stillBank24', 23)
    stillBank25 = ATEMConstant('stillBank25', 24)
    stillBank26 = ATEMConstant('stillBank26', 25)
    stillBank27 = ATEMConstant('stillBank27', 26)
    stillBank28 = ATEMConstant('stillBank28', 27)
    stillBank29 = ATEMConstant('stillBank29', 28)
    stillBank30 = ATEMConstant('stillBank30', 29)
    stillBank31 = ATEMConstant('stillBank31', 30)
    stillBank32 = ATEMConstant('stillBank32', 31)


class ATEMMacros(ATEMConstantList):
    """Macro list"""

    stop = ATEMConstant('stop', 0xFFFF)
    macro1 = ATEMConstant('macro1', 0)
    macro2 = ATEMConstant('macro2', 1)
    macro3 = ATEMConstant('macro3', 2)
    macro4 = ATEMConstant('macro4', 3)
    macro5 = ATEMConstant('macro5', 4)
    macro6 = ATEMConstant('macro6', 5)
    macro7 = ATEMConstant('macro7', 6)
    macro8 = ATEMConstant('macro8', 7)
    macro9 = ATEMConstant('macro9', 8)
    macro10 = ATEMConstant('macro10', 9)
    macro11 = ATEMConstant('macro11', 10)
    macro12 = ATEMConstant('macro12', 11)
    macro13 = ATEMConstant('macro13', 12)
    macro14 = ATEMConstant('macro14', 13)
    macro15 = ATEMConstant('macro15', 14)
    macro16 = ATEMConstant('macro16', 15)
    macro17 = ATEMConstant('macro17', 16)
    macro18 = ATEMConstant('macro18', 17)
    macro19 = ATEMConstant('macro19', 18)
    macro20 = ATEMConstant('macro20', 19)
    macro21 = ATEMConstant('macro21', 20)
    macro22 = ATEMConstant('macro22', 21)
    macro23 = ATEMConstant('macro23', 22)
    macro24 = ATEMConstant('macro24', 23)
    macro25 = ATEMConstant('macro25', 24)
    macro26 = ATEMConstant('macro26', 25)
    macro27 = ATEMConstant('macro27', 26)
    macro28 = ATEMConstant('macro28', 27)
    macro29 = ATEMConstant('macro29', 28)
    macro30 = ATEMConstant('macro30', 29)
    macro31 = ATEMConstant('macro31', 30)
    macro32 = ATEMConstant('macro32', 31)
    macro33 = ATEMConstant('macro33', 32)
    macro34 = ATEMConstant('macro34', 33)
    macro35 = ATEMConstant('macro35', 34)
    macro36 = ATEMConstant('macro36', 35)
    macro37 = ATEMConstant('macro37', 36)
    macro38 = ATEMConstant('macro38', 37)
    macro39 = ATEMConstant('macro39', 38)
    macro40 = ATEMConstant('macro40', 39)
    macro41 = ATEMConstant('macro41', 40)
    macro42 = ATEMConstant('macro42', 41)
    macro43 = ATEMConstant('macro43', 42)
    macro44 = ATEMConstant('macro44', 43)
    macro45 = ATEMConstant('macro45', 44)
    macro46 = ATEMConstant('macro46', 45)
    macro47 = ATEMConstant('macro47', 46)
    macro48 = ATEMConstant('macro48', 47)
    macro49 = ATEMConstant('macro49', 48)
    macro50 = ATEMConstant('macro50', 49)
    macro51 = ATEMConstant('macro51', 50)
    macro52 = ATEMConstant('macro52', 51)
    macro53 = ATEMConstant('macro53', 52)
    macro54 = ATEMConstant('macro54', 53)
    macro55 = ATEMConstant('macro55', 54)
    macro56 = ATEMConstant('macro56', 55)
    macro57 = ATEMConstant('macro57', 56)
    macro58 = ATEMConstant('macro58', 57)
    macro59 = ATEMConstant('macro59', 58)
    macro60 = ATEMConstant('macro60', 59)
    macro61 = ATEMConstant('macro61', 60)
    macro62 = ATEMConstant('macro62', 61)
    macro63 = ATEMConstant('macro63', 62)
    macro64 = ATEMConstant('macro64', 63)
    macro65 = ATEMConstant('macro65', 64)
    macro66 = ATEMConstant('macro66', 65)
    macro67 = ATEMConstant('macro67', 66)
    macro68 = ATEMConstant('macro68', 67)
    macro69 = ATEMConstant('macro69', 68)
    macro70 = ATEMConstant('macro70', 69)
    macro71 = ATEMConstant('macro71', 70)
    macro72 = ATEMConstant('macro72', 71)
    macro73 = ATEMConstant('macro73', 72)
    macro74 = ATEMConstant('macro74', 73)
    macro75 = ATEMConstant('macro75', 74)
    macro76 = ATEMConstant('macro76', 75)
    macro77 = ATEMConstant('macro77', 76)
    macro78 = ATEMConstant('macro78', 77)
    macro79 = ATEMConstant('macro79', 78)
    macro80 = ATEMConstant('macro80', 79)
    macro81 = ATEMConstant('macro81', 80)
    macro82 = ATEMConstant('macro82', 81)
    macro83 = ATEMConstant('macro83', 82)
    macro84 = ATEMConstant('macro84', 83)
    macro85 = ATEMConstant('macro85', 84)
    macro86 = ATEMConstant('macro86', 85)
    macro87 = ATEMConstant('macro87', 86)
    macro88 = ATEMConstant('macro88', 87)
    macro89 = ATEMConstant('macro89', 88)
    macro90 = ATEMConstant('macro90', 89)
    macro91 = ATEMConstant('macro91', 90)
    macro92 = ATEMConstant('macro92', 91)
    macro93 = ATEMConstant('macro93', 92)
    macro94 = ATEMConstant('macro94', 93)
    macro95 = ATEMConstant('macro95', 94)
    macro96 = ATEMConstant('macro96', 95)
    macro97 = ATEMConstant('macro97', 96)
    macro98 = ATEMConstant('macro98', 97)
    macro99 = ATEMConstant('macro99', 98)
    macro100 = ATEMConstant('macro100', 99)


class ATEMBoxes(ATEMConstantList):
    """Box list"""

    box1 = ATEMConstant('box1', 0)
    box2 = ATEMConstant('box2', 1)
    box3 = ATEMConstant('box3', 2)
    box4 = ATEMConstant('box4', 3)
