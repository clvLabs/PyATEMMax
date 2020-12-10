---
layout: page
title: Docs - Methods - Set
permalink: /docs/methods/set/
---

The `set` methods allow changing switcher settings.

## List of set methods

### setAudioLevelsEnable
{% highlight python %}
setAudioLevelsEnable(enable:bool) -> None
{% endhighlight %}
Set Audio Levels Enable

        Args:
            enable (bool): On/Off

### setAudioMixerInputBalance
{% highlight python %}
setAudioMixerInputBalance(audioSource:ATEMConstant, balance:float) -> None
{% endhighlight %}
Set Audio Mixer Input Balance

        Args:
            audioSource: see ATEMAudioSources
            balance (float): -1.0-1.0: Left/Right Extremes

### setAudioMixerInputMixOption
{% highlight python %}
setAudioMixerInputMixOption(audioSource:ATEMConstant, mixOption:ATEMConstant) -> None
{% endhighlight %}
Set Audio Mixer Input Mix Option

        Args:
            audioSource: see ATEMAudioSources
            mixOption: see ATEMAudioMixerInputMixOptions

### setAudioMixerInputVolume
{% highlight python %}
setAudioMixerInputVolume(audioSource:ATEMConstant, db:float) -> None
{% endhighlight %}
Set Audio Mixer Input Volume

        Args:
            audioSource: see ATEMAudioSources
            db (float): volume in dB

### setAudioMixerMasterVolume
{% highlight python %}
setAudioMixerMasterVolume(db:float) -> None
{% endhighlight %}
Set Audio Mixer Master Volume

        Args:
            db (float): volume in dB

### setAudioMixerMonitorDim
{% highlight python %}
setAudioMixerMonitorDim(dim:bool) -> None
{% endhighlight %}
Set Audio Mixer Monitor Dim

        Args:
            dim (bool): On/Off

### setAudioMixerMonitorMonitorAudio
{% highlight python %}
setAudioMixerMonitorMonitorAudio(monitorAudio:bool) -> None
{% endhighlight %}
Set Audio Mixer Monitor Monitor Audio

        Args:
            monitorAudio (bool): On/Off

### setAudioMixerMonitorMute
{% highlight python %}
setAudioMixerMonitorMute(mute:bool) -> None
{% endhighlight %}
Set Audio Mixer Monitor Mute

        Args:
            mute (bool): On/Off

### setAudioMixerMonitorSolo
{% highlight python %}
setAudioMixerMonitorSolo(solo:bool) -> None
{% endhighlight %}
Set Audio Mixer Monitor Solo

        Args:
            solo (bool): On/Off

### setAudioMixerMonitorSoloInput
{% highlight python %}
setAudioMixerMonitorSoloInput(soloInput:ATEMConstant) -> None
{% endhighlight %}
Set Audio Mixer Monitor Solo Input

        Args:
            soloInput: see ATEMAudioSources

### setAudioMixerMonitorVolume
{% highlight python %}
setAudioMixerMonitorVolume(db:float) -> None
{% endhighlight %}
Set Audio Mixer Monitor Volume

        Args:
            db (float): volume in dB

### setAuxSourceInput
{% highlight python %}
setAuxSourceInput(auxChannel:ATEMConstant, input_:ATEMConstant) -> None
{% endhighlight %}
Set Aux Source Input

        Args:
            auxChannel: see ATEMAUXChannels
            input_: see ATEMVideoSources

### setCameraControlAutoFocus
{% highlight python %}
setCameraControlAutoFocus(camera:ATEMConstant) -> None
{% endhighlight %}
Set Camera Control Auto focus

        Args:
            camera: see ATEMCameras

### setCameraControlAutoIris
{% highlight python %}
setCameraControlAutoIris(camera:ATEMConstant) -> None
{% endhighlight %}
Set Camera Control Auto iris

        Args:
            camera: see ATEMCameras

### setCameraControlColorbars
{% highlight python %}
setCameraControlColorbars(camera:ATEMConstant, colorbars:int) -> None
{% endhighlight %}
Set Camera Control Colorbars

        Args:
            camera: see ATEMCameras
            colorbars: duration in secs (0=disable)

### setCameraControlComponentGain
{% highlight python %}
setCameraControlComponentGain(camera:ATEMConstant, gainR:float, gainG:float, gainB:float, gainY:float) -> None
{% endhighlight %}
Set Camera Control Component Gain

        Args:
            camera: see ATEMCameras
            gainR (float): 0.0-16.0
            gainG (float): 0.0-16.0
            gainB (float): 0.0-16.0
            gainY (float): 0.0-16.0

### setCameraControlContrast
{% highlight python %}
setCameraControlContrast(camera:ATEMConstant, contrast:float) -> None
{% endhighlight %}
Set Camera Control Contrast

        Args:
            camera: see ATEMCameras
            contrast (float): 0.0-100.0 (%)

### setCameraControlFocus
{% highlight python %}
setCameraControlFocus(camera:ATEMConstant, focus:int) -> None
{% endhighlight %}
Set Camera Control Focus

        Args:
            camera: see ATEMCameras
            focus (int): 0-65535

### setCameraControlGain
{% highlight python %}
setCameraControlGain(camera:ATEMConstant, gain:int) -> None
{% endhighlight %}
Set Camera Control Gain

        Args:
            camera: see ATEMCameras
            gain (int): 512: 0db, 1024: 6db, 2048: 12db, 4096: 18db

### setCameraControlGainB
{% highlight python %}
setCameraControlGainB(camera:ATEMConstant, gainB:float) -> None
{% endhighlight %}
Set Camera Control Gain B

        Args:
            camera: see ATEMCameras
            gainB (float): 0.0-16.0

### setCameraControlGainG
{% highlight python %}
setCameraControlGainG(camera:ATEMConstant, gainG:float) -> None
{% endhighlight %}
Set Camera Control Gain G

        Args:
            camera: see ATEMCameras
            gainG (float): 0.0-16.0

### setCameraControlGainR
{% highlight python %}
setCameraControlGainR(camera:ATEMConstant, gainR:float) -> None
{% endhighlight %}
Set Camera Control Gain R

        Args:
            camera: see ATEMCameras
            gainR (float): 0.0-16.0

### setCameraControlGainY
{% highlight python %}
setCameraControlGainY(camera:ATEMConstant, gainY:float) -> None
{% endhighlight %}
Set Camera Control Gain Y

        Args:
            camera: see ATEMCameras
            gainY (float): 0.0-16.0

### setCameraControlGamma
{% highlight python %}
setCameraControlGamma(camera:ATEMConstant, gammaR:float, gammaG:float, gammaB:float, gammaY:float) -> None
{% endhighlight %}
Set Camera Control Gamma

        Args:
            camera: see ATEMCameras
            gammaR (float): -1.0-1.0
            gammaG (float): -1.0-1.0
            gammaB (float): -1.0-1.0
            gammaY (float): -1.0-1.0

### setCameraControlGammaB
{% highlight python %}
setCameraControlGammaB(camera:ATEMConstant, gammaB:float) -> None
{% endhighlight %}
Set Camera Control Gamma B

        Args:
            camera: see ATEMCameras
            gammaB (float): -1.0-1.0

### setCameraControlGammaG
{% highlight python %}
setCameraControlGammaG(camera:ATEMConstant, gammaG:float) -> None
{% endhighlight %}
Set Camera Control Gamma G

        Args:
            camera: see ATEMCameras
            gammaG (float): -1.0-1.0

### setCameraControlGammaR
{% highlight python %}
setCameraControlGammaR(camera:ATEMConstant, gammaR:float) -> None
{% endhighlight %}
Set Camera Control Gamma R

        Args:
            camera: see ATEMCameras
            gammaR (float): -1.0-1.0

### setCameraControlGammaY
{% highlight python %}
setCameraControlGammaY(camera:ATEMConstant, gammaY:float) -> None
{% endhighlight %}
Set Camera Control Gamma Y

        Args:
            camera: see ATEMCameras
            gammaY (float): -1.0-1.0

### setCameraControlHue
{% highlight python %}
setCameraControlHue(camera:ATEMConstant, hue:float) -> None
{% endhighlight %}
Set Camera Control Hue

        Args:
            camera: see ATEMCameras
            hue (float): 0.0-359.9 degrees

### setCameraControlHueSaturation
{% highlight python %}
setCameraControlHueSaturation(camera:ATEMConstant, hue:float, saturation:float) -> None
{% endhighlight %}
Set Camera Control Hue/Saturation

        Args:
            camera: see ATEMCameras
            hue (float): 0.0-359.9 degrees
            saturation (float): 0.0-100.0 (%)

### setCameraControlIris
{% highlight python %}
setCameraControlIris(camera:ATEMConstant, iris:int) -> None
{% endhighlight %}
Set Camera Control Iris

        Args:
            camera: see ATEMCameras
            iris (int): 0-2048

### setCameraControlLift
{% highlight python %}
setCameraControlLift(camera:ATEMConstant, liftR:float, liftG:float, liftB:float, liftY:float) -> None
{% endhighlight %}
Set Camera Control Lift

        Args:
            camera: see ATEMCameras
            liftR (float): -1.0-1.0
            liftG (float): -1.0-1.0
            liftB (float): -1.0-1.0
            liftY (float): -1.0-1.0

### setCameraControlLiftB
{% highlight python %}
setCameraControlLiftB(camera:ATEMConstant, liftB:float) -> None
{% endhighlight %}
Set Camera Control Lift B

        Args:
            camera: see ATEMCameras
            liftB (float): -1.0-1.0

### setCameraControlLiftG
{% highlight python %}
setCameraControlLiftG(camera:ATEMConstant, liftG:float) -> None
{% endhighlight %}
Set Camera Control Lift G

        Args:
            camera: see ATEMCameras
            liftG (float): -1.0-1.0

### setCameraControlLiftR
{% highlight python %}
setCameraControlLiftR(camera:ATEMConstant, liftR:float) -> None
{% endhighlight %}
Set Camera Control Lift R

        Args:
            camera: see ATEMCameras
            liftR (float): -1.0-1.0

### setCameraControlLiftY
{% highlight python %}
setCameraControlLiftY(camera:ATEMConstant, liftY:float) -> None
{% endhighlight %}
Set Camera Control Lift Y

        Args:
            camera: see ATEMCameras
            liftY (float): -1.0-1.0

### setCameraControlLumMix
{% highlight python %}
setCameraControlLumMix(camera:ATEMConstant, lumMix:float) -> None
{% endhighlight %}
Set Camera Control Lum Mix

        Args:
            camera: see ATEMCameras
            lumMix (float):  0.0-100.0 (%)

### setCameraControlResetAll
{% highlight python %}
setCameraControlResetAll(camera:ATEMConstant) -> None
{% endhighlight %}
Set Camera Control Reset all

        Args:
            camera: see ATEMCameras

### setCameraControlSaturation
{% highlight python %}
setCameraControlSaturation(camera:ATEMConstant, saturation:float) -> None
{% endhighlight %}
Set Camera Control Saturation

        Args:
            camera: see ATEMCameras
            saturation (float):  0.0-100.0 (%)

### setCameraControlSharpeningLevel
{% highlight python %}
setCameraControlSharpeningLevel(camera:ATEMConstant, detail:ATEMConstant) -> None
{% endhighlight %}
Set Camera Control Detail level

        Args:
            camera: see ATEMCameras
            detail: see ATEMCamerControlSharpeningLevels

### setCameraControlShutter
{% highlight python %}
setCameraControlShutter(camera:ATEMConstant, shutter:float) -> None
{% endhighlight %}
Set Camera Control Shutter

        Args:
            camera: see ATEMCameras
            shutter (float): 1/50, 1/60, 1/75, 1/90, 1/100, 1/120, 1/150, 1/180, 1/250, 1/360, 1/500, 1/750, 1/1000, 1/1450, 1/2000

### setCameraControlVideomode
{% highlight python %}
setCameraControlVideomode(camera:ATEMConstant, fps:int, resolution:int, interlaced:int) -> None
{% endhighlight %}
Set Camera Control Video Mode

        Args:
            camera: see ATEMCameras
            fps (int): ?
            resolution (int): ?
            interlaced (int): ?

### setCameraControlWhiteBalance
{% highlight python %}
setCameraControlWhiteBalance(camera:ATEMConstant, whiteBalance:int) -> None
{% endhighlight %}
Set Camera Control White Balance

        Args:
            camera: see ATEMCameras
            whiteBalance(int): 3200: 3200K, 4500: 4500K, 5000: 5000K, 5600: 5600K, 6500: 6500K, 7500: 7500K

### setCameraControlZoomNormalized
{% highlight python %}
setCameraControlZoomNormalized(camera:ATEMConstant, zoomNormalized:float) -> None
{% endhighlight %}
Set Camera Control Zoom Normalized

        Args:
            camera: see ATEMCameras
            zoomNormalized (float): ?

### setCameraControlZoomSpeed
{% highlight python %}
setCameraControlZoomSpeed(camera:ATEMConstant, zoomSpeed:float) -> None
{% endhighlight %}
Set Camera Control Zoom

        Args:
            camera: see ATEMCameras
            zoomSpeed (float): 0.0-1.0

### setClipPlayerAtBeginning
{% highlight python %}
setClipPlayerAtBeginning(mediaPlayer:ATEMConstant, atBeginning:bool) -> None
{% endhighlight %}
Set Clip Player At Beginning

        Args:
            mediaPlayer: see ATEMMediaPlayers
            atBeginning (bool): On/Off

### setClipPlayerClipFrame
{% highlight python %}
setClipPlayerClipFrame(mediaPlayer:ATEMConstant, clipFrame:int) -> None
{% endhighlight %}
Set Clip Player Clip Frame

        Args:
            mediaPlayer: see ATEMMediaPlayers
            clipFrame (int): frame

### setClipPlayerLoop
{% highlight python %}
setClipPlayerLoop(mediaPlayer:ATEMConstant, loop:bool) -> None
{% endhighlight %}
Set Clip Player Loop

        Args:
            mediaPlayer: see ATEMMediaPlayers
            loop (bool): On/Off

### setClipPlayerPlaying
{% highlight python %}
setClipPlayerPlaying(mediaPlayer:ATEMConstant, playing:bool) -> None
{% endhighlight %}
Set Clip Player Playing

        Args:
            mediaPlayer: see ATEMMediaPlayers
            playing (bool): On/Off

### setColorGeneratorHue
{% highlight python %}
setColorGeneratorHue(colorGenerator:ATEMConstant, hue:float) -> None
{% endhighlight %}
Set Color Generator Hue

        Args:
            colorGenerator: see ATEMColorGenerators
            hue (float): 0.0-359.9 (degrees)

### setColorGeneratorLuma
{% highlight python %}
setColorGeneratorLuma(colorGenerator:ATEMConstant, luma:float) -> None
{% endhighlight %}
Set Color Generator Luma

        Args:
            colorGenerator: see ATEMColorGenerators
            luma (float): 0.0-100.0 (%)

### setColorGeneratorSaturation
{% highlight python %}
setColorGeneratorSaturation(colorGenerator:ATEMConstant, saturation:float) -> None
{% endhighlight %}
Set Color Generator Saturation

        Args:
            colorGenerator: see ATEMColorGenerators
            saturation (float): 0.0-100.0 (%)

### setDownConverterMode
{% highlight python %}
setDownConverterMode(mode:ATEMConstant) -> None
{% endhighlight %}
Set Down Converter Mode

        Args:
            mode: see ATEMDownConverterModes

### setDownstreamKeyerBottom
{% highlight python %}
setDownstreamKeyerBottom(keyer:ATEMConstant, bottom:float) -> None
{% endhighlight %}
Set Downstream Keyer Bottom

        Args:
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0

### setDownstreamKeyerClip
{% highlight python %}
setDownstreamKeyerClip(keyer:ATEMConstant, clip:float) -> None
{% endhighlight %}
Set Downstream Keyer Clip

        Args:
            keyer: see ATEMKeyersr 1-4
            clip (float): 0.0-100.0 (%)

### setDownstreamKeyerFillSource
{% highlight python %}
setDownstreamKeyerFillSource(keyer:ATEMConstant, fillSource:ATEMConstant) -> None
{% endhighlight %}
Set Downstream Keyer Fill Source

        Args:
            keyer: see ATEMKeyers
            fillSource: see ATEMVideoSources

### setDownstreamKeyerGain
{% highlight python %}
setDownstreamKeyerGain(keyer:ATEMConstant, gain:float) -> None
{% endhighlight %}
Set Downstream Keyer Gain

        Args:
            keyer: see ATEMKeyersr 1-4
            gain (float): 0.0-100.0 (%)

### setDownstreamKeyerInvertKey
{% highlight python %}
setDownstreamKeyerInvertKey(keyer:ATEMConstant, invertKey:bool) -> None
{% endhighlight %}
Set Downstream Keyer Invert Key(??)

        Args:
            keyer: see ATEMKeyers
            invertKey (bool): On/Off

### setDownstreamKeyerKeySource
{% highlight python %}
setDownstreamKeyerKeySource(keyer:ATEMConstant, keySource:ATEMConstant) -> None
{% endhighlight %}
Set Downstream Keyer Source

        Args:
            keyer: see ATEMKeyers
            keySource: see ATEMVideoSources

### setDownstreamKeyerLeft
{% highlight python %}
setDownstreamKeyerLeft(keyer:ATEMConstant, left:float) -> None
{% endhighlight %}
Set Downstream Keyer Left

        Args:
            keyer: see ATEMKeyers
            left (float): -9.0-9.0

### setDownstreamKeyerMasked
{% highlight python %}
setDownstreamKeyerMasked(keyer:ATEMConstant, masked:bool) -> None
{% endhighlight %}
Set Downstream Keyer Masked

        Args:
            keyer: see ATEMKeyers 1-4
            masked (bool): On/Off

### setDownstreamKeyerOnAir
{% highlight python %}
setDownstreamKeyerOnAir(keyer:ATEMConstant, onAir:bool) -> None
{% endhighlight %}
Set Downstream Keyer On Air

        Args:
            keyer: see ATEMKeyers
            onAir (bool): On/Off

### setDownstreamKeyerPreMultiplied
{% highlight python %}
setDownstreamKeyerPreMultiplied(keyer:ATEMConstant, preMultiplied:bool) -> None
{% endhighlight %}
Set Downstream Keyer Pre Multiplied

        Args:
            keyer: see ATEMKeyers
            preMultiplied (bool): On/Off

### setDownstreamKeyerRate
{% highlight python %}
setDownstreamKeyerRate(keyer:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Downstream Keyer Rate

        Args:
            keyer: see ATEMKeyers
        rate (int): 1-250 (frames)

### setDownstreamKeyerRight
{% highlight python %}
setDownstreamKeyerRight(keyer:ATEMConstant, right:float) -> None
{% endhighlight %}
Set Downstream Keyer Right

        Args:
            keyer: see ATEMKeyers
            right (float): -9.0-9.0

### setDownstreamKeyerTie
{% highlight python %}
setDownstreamKeyerTie(keyer:ATEMConstant, tie:bool) -> None
{% endhighlight %}
Set Downstream Keyer Tie

        Args:
            keyer: see ATEMKeyers
            tie (bool): On/Off

### setDownstreamKeyerTop
{% highlight python %}
setDownstreamKeyerTop(keyer:ATEMConstant, top:float) -> None
{% endhighlight %}
Set Downstream Keyer Top

        Args:
            keyer: see ATEMKeyers
            top (float): -9.0-9.0

### setFadeToBlackRate
{% highlight python %}
setFadeToBlackRate(mE:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Fade-To-Black Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)

### setInputExternalPortType
{% highlight python %}
setInputExternalPortType(videoSource:ATEMConstant, externalPortType:ATEMConstant) -> None
{% endhighlight %}
Set Input Properties External Port Type

        Args:
            videoSource: see ATEMVideoSources
            externalPortType: see ATEMExternalPortTypes

### setInputLongName
{% highlight python %}
setInputLongName(videoSource:ATEMConstant, longName:str) -> None
{% endhighlight %}
Set Input Properties Long Name

        Args:
            videoSource: see ATEMVideoSources
            longName(str): long name

### setInputShortName
{% highlight python %}
setInputShortName(videoSource:ATEMConstant, shortName:str) -> None
{% endhighlight %}
Set Input Properties Short Name

        Args:
            videoSource: see ATEMVideoSources
            shortName(str): short name

### setKeyChromaGain
{% highlight python %}
setKeyChromaGain(mE:ATEMConstant, keyer:ATEMConstant, gain:float) -> None
{% endhighlight %}
Set Key Chroma Gain

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            gain (float): 0.0-100.0 (%)

### setKeyChromaHue
{% highlight python %}
setKeyChromaHue(mE:ATEMConstant, keyer:ATEMConstant, hue:float) -> None
{% endhighlight %}
Set Key Chroma Hue

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            hue (float): 0.0-359.9 (degrees)

### setKeyChromaLift
{% highlight python %}
setKeyChromaLift(mE:ATEMConstant, keyer:ATEMConstant, lift:float) -> None
{% endhighlight %}
Set Key Chroma Lift

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lift (float): 0.0-100.0 (%)

### setKeyChromaNarrow
{% highlight python %}
setKeyChromaNarrow(mE:ATEMConstant, keyer:ATEMConstant, narrow:bool) -> None
{% endhighlight %}
Set Key Chroma Narrow

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            narrow (bool): On/Off

### setKeyChromaYSuppress
{% highlight python %}
setKeyChromaYSuppress(mE:ATEMConstant, keyer:ATEMConstant, ySuppress:float) -> None
{% endhighlight %}
Set Key Chroma Y Suppress

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            ySuppress (float): 0.0-100.0 (%)

### setKeyDVEBorderBevel
{% highlight python %}
setKeyDVEBorderBevel(mE:ATEMConstant, keyer:ATEMConstant, borderBevel:ATEMConstant) -> None
{% endhighlight %}
Set Key DVE Border Bevel

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevel: see ATEMBorderBevels

### setKeyDVEBorderBevelPosition
{% highlight python %}
setKeyDVEBorderBevelPosition(mE:ATEMConstant, keyer:ATEMConstant, borderBevelPosition:float) -> None
{% endhighlight %}
Set Key DVE Border Bevel Position

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevelPosition (float): 0.0-1.0

### setKeyDVEBorderBevelSoftness
{% highlight python %}
setKeyDVEBorderBevelSoftness(mE:ATEMConstant, keyer:ATEMConstant, borderBevelSoftness:float) -> None
{% endhighlight %}
Set Key DVE Border Bevel Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderBevelSoftness (float): 0.0-1.0

### setKeyDVEBorderEnabled
{% highlight python %}
setKeyDVEBorderEnabled(mE:ATEMConstant, keyer:ATEMConstant, borderEnabled:bool) -> None
{% endhighlight %}
Set Key DVE Border Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderEnabled (bool): On/Off

### setKeyDVEBorderHue
{% highlight python %}
setKeyDVEBorderHue(mE:ATEMConstant, keyer:ATEMConstant, borderHue:float) -> None
{% endhighlight %}
Set Key DVE Border Hue

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderHue (float): 0.0-359.9 (degrees)

### setKeyDVEBorderInnerSoftness
{% highlight python %}
setKeyDVEBorderInnerSoftness(mE:ATEMConstant, keyer:ATEMConstant, borderInnerSoftness:int) -> None
{% endhighlight %}
Set Key DVE Border Inner Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderInnerSoftness (int): 0-100 (%)

### setKeyDVEBorderInnerWidth
{% highlight python %}
setKeyDVEBorderInnerWidth(mE:ATEMConstant, keyer:ATEMConstant, borderInnerWidth:float) -> None
{% endhighlight %}
Set Key DVE Border Inner Width

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderInnerWidth (float): 0.0-16.0

### setKeyDVEBorderLuma
{% highlight python %}
setKeyDVEBorderLuma(mE:ATEMConstant, keyer:ATEMConstant, borderLuma:float) -> None
{% endhighlight %}
Set Key DVE Border Luma

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderLuma (float): 0.0-100.0 (%)

### setKeyDVEBorderOpacity
{% highlight python %}
setKeyDVEBorderOpacity(mE:ATEMConstant, keyer:ATEMConstant, borderOpacity:int) -> None
{% endhighlight %}
Set Key DVE Border Opacity

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOpacity (int): 0-100 (%)

### setKeyDVEBorderOuterSoftness
{% highlight python %}
setKeyDVEBorderOuterSoftness(mE:ATEMConstant, keyer:ATEMConstant, borderOuterSoftness:int) -> None
{% endhighlight %}
Set Key DVE Border Outer Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOuterSoftness (int): 0-100 (%)

### setKeyDVEBorderOuterWidth
{% highlight python %}
setKeyDVEBorderOuterWidth(mE:ATEMConstant, keyer:ATEMConstant, borderOuterWidth:float) -> None
{% endhighlight %}
Set Key DVE Border Outer Width

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderOuterWidth (float): 0.0-16.0

### setKeyDVEBorderSaturation
{% highlight python %}
setKeyDVEBorderSaturation(mE:ATEMConstant, keyer:ATEMConstant, borderSaturation:float) -> None
{% endhighlight %}
Set Key DVE Border Saturation

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            borderSaturation (float): 0.0-100.0 (%)

### setKeyDVEBottom
{% highlight python %}
setKeyDVEBottom(mE:ATEMConstant, keyer:ATEMConstant, bottom:float) -> None
{% endhighlight %}
Set Key DVE Bottom

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0

### setKeyDVELeft
{% highlight python %}
setKeyDVELeft(mE:ATEMConstant, keyer:ATEMConstant, left:float) -> None
{% endhighlight %}
Set Key DVE Left

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            left (float): -9.0-9.0

### setKeyDVELightSourceAltitude
{% highlight python %}
setKeyDVELightSourceAltitude(mE:ATEMConstant, keyer:ATEMConstant, lightSourceAltitude:int) -> None
{% endhighlight %}
Set Key DVE Light Source Altitude

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lightSourceAltitude (int): 10-100

### setKeyDVELightSourceDirection
{% highlight python %}
setKeyDVELightSourceDirection(mE:ATEMConstant, keyer:ATEMConstant, lightSourceDirection:float) -> None
{% endhighlight %}
Set Key DVE Light Source Direction

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            lightSourceDirection (float): 0.0-359.9 (degrees)

### setKeyDVEMasked
{% highlight python %}
setKeyDVEMasked(mE:ATEMConstant, keyer:ATEMConstant, masked:bool) -> None
{% endhighlight %}
Set Key DVE Masked

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            masked (bool): On/Off

### setKeyDVEPositionX
{% highlight python %}
setKeyDVEPositionX(mE:ATEMConstant, keyer:ATEMConstant, positionX:float) -> None
{% endhighlight %}
Set Key DVE Position X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionX (float): 0.0-1.0

### setKeyDVEPositionY
{% highlight python %}
setKeyDVEPositionY(mE:ATEMConstant, keyer:ATEMConstant, positionY:float) -> None
{% endhighlight %}
Set Key DVE Position Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionY (float): 0.0-1.0

### setKeyDVERate
{% highlight python %}
setKeyDVERate(mE:ATEMConstant, keyer:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Key DVE Rate

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers-4
            rate (int): 1-250 (frames)

### setKeyDVERight
{% highlight python %}
setKeyDVERight(mE:ATEMConstant, keyer:ATEMConstant, right:float) -> None
{% endhighlight %}
Set Key DVE Right

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            right (float): -9.0-9.0

### setKeyDVERotation
{% highlight python %}
setKeyDVERotation(mE:ATEMConstant, keyer:ATEMConstant, rotation:float) -> None
{% endhighlight %}
Set Key DVE Rotation

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            rotation (float): 0.0-359.9 (degrees)

### setKeyDVEShadow
{% highlight python %}
setKeyDVEShadow(mE:ATEMConstant, keyer:ATEMConstant, shadow:bool) -> None
{% endhighlight %}
Set Key DVE Shadow

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            shadow (bool): On/Off

### setKeyDVESizeX
{% highlight python %}
setKeyDVESizeX(mE:ATEMConstant, keyer:ATEMConstant, sizeX:float) -> None
{% endhighlight %}
Set Key DVE Size X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            sizeX (float): 0.0-1.0

### setKeyDVESizeY
{% highlight python %}
setKeyDVESizeY(mE:ATEMConstant, keyer:ATEMConstant, sizeY:float) -> None
{% endhighlight %}
Set Key DVE Size Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            sizeY (float): 0.0-1.0

### setKeyDVETop
{% highlight python %}
setKeyDVETop(mE:ATEMConstant, keyer:ATEMConstant, top:float) -> None
{% endhighlight %}
Set Key DVE Top

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            top (float): -9.0-9.0

### setKeyLumaClip
{% highlight python %}
setKeyLumaClip(mE:ATEMConstant, keyer:ATEMConstant, clip:float) -> None
{% endhighlight %}
Set Key Luma Clip

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            clip (float): 0.0-100.0 (%)

### setKeyLumaGain
{% highlight python %}
setKeyLumaGain(mE:ATEMConstant, keyer:ATEMConstant, gain:float) -> None
{% endhighlight %}
Set Key Luma Gain

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            gain (float): 0.0-100.0 (%)

### setKeyLumaInvertKey
{% highlight python %}
setKeyLumaInvertKey(mE:ATEMConstant, keyer:ATEMConstant, invertKey:bool) -> None
{% endhighlight %}
Set Key Luma Invert Key

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            invertKey (bool): On/Off

### setKeyLumaPreMultiplied
{% highlight python %}
setKeyLumaPreMultiplied(mE:ATEMConstant, keyer:ATEMConstant, preMultiplied:bool) -> None
{% endhighlight %}
Set Key Luma Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            preMultiplied (bool): On/Off

### setKeyPatternInvertPattern
{% highlight python %}
setKeyPatternInvertPattern(mE:ATEMConstant, keyer:ATEMConstant, invertPattern:bool) -> None
{% endhighlight %}
Set Key Pattern Invert Pattern

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            invertPattern (bool): On/Off

### setKeyPatternPattern
{% highlight python %}
setKeyPatternPattern(mE:ATEMConstant, keyer:ATEMConstant, pattern:ATEMConstant) -> None
{% endhighlight %}
Set Key Pattern Pattern

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            pattern: see ATEMPatternStyles

### setKeyPatternPositionX
{% highlight python %}
setKeyPatternPositionX(mE:ATEMConstant, keyer:ATEMConstant, positionX:float) -> None
{% endhighlight %}
Set Key Pattern Position X

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionX (float): 0.0-1.0

### setKeyPatternPositionY
{% highlight python %}
setKeyPatternPositionY(mE:ATEMConstant, keyer:ATEMConstant, positionY:float) -> None
{% endhighlight %}
Set Key Pattern Position Y

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            positionY (float): 0.0-1.0

### setKeyPatternSize
{% highlight python %}
setKeyPatternSize(mE:ATEMConstant, keyer:ATEMConstant, size:float) -> None
{% endhighlight %}
Set Key Pattern Size

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            size (float): 0.0-100.0 (%)

### setKeyPatternSoftness
{% highlight python %}
setKeyPatternSoftness(mE:ATEMConstant, keyer:ATEMConstant, softness:float) -> None
{% endhighlight %}
Set Key Pattern Softness

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            softness (float): 0.0-100.0 (%)

### setKeyPatternSymmetry
{% highlight python %}
setKeyPatternSymmetry(mE:ATEMConstant, keyer:ATEMConstant, symmetry:float) -> None
{% endhighlight %}
Set Key Pattern Symmetry

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            symmetry (float): 0.0-100.0 (%)

### setKeyerBottom
{% highlight python %}
setKeyerBottom(mE:ATEMConstant, keyer:ATEMConstant, bottom:float) -> None
{% endhighlight %}
Set Key Mask Bottom

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            bottom (float): -9.0-9.0

### setKeyerFillSource
{% highlight python %}
setKeyerFillSource(mE:ATEMConstant, keyer:ATEMConstant, fillSource:ATEMConstant) -> None
{% endhighlight %}
Set Key Fill Fill Source

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            fillSource: see ATEMVideoSources

### setKeyerFlyEnabled
{% highlight python %}
setKeyerFlyEnabled(mE:ATEMConstant, keyer:ATEMConstant, flyEnabled:bool) -> None
{% endhighlight %}
Set Key Type Fly Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            flyEnabled (bool): On/Off

### setKeyerFlyKeyFrame
{% highlight python %}
setKeyerFlyKeyFrame(mE:ATEMConstant, keyer:ATEMConstant, keyFrame:ATEMConstant) -> None
{% endhighlight %}
Set Keyer Fly Key Frame

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keyFrame: see ATEMKeyFrames

### setKeyerKeySource
{% highlight python %}
setKeyerKeySource(mE:ATEMConstant, keyer:ATEMConstant, keySource:ATEMConstant) -> None
{% endhighlight %}
Set Key Cut Key Source

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keySource: see ATEMVideoSources

### setKeyerLeft
{% highlight python %}
setKeyerLeft(mE:ATEMConstant, keyer:ATEMConstant, left:float) -> None
{% endhighlight %}
Set Key Mask Left

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            left (float): -9.0-9.0

### setKeyerMasked
{% highlight python %}
setKeyerMasked(mE:ATEMConstant, keyer:ATEMConstant, masked:bool) -> None
{% endhighlight %}
Set Key Mask Masked

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            masked (bool): On/Off

### setKeyerOnAirEnabled
{% highlight python %}
setKeyerOnAirEnabled(mE:ATEMConstant, keyer:ATEMConstant, enabled:bool) -> None
{% endhighlight %}
Set Keyer On Air Enabled

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            enabled (bool): On/Off

### setKeyerRight
{% highlight python %}
setKeyerRight(mE:ATEMConstant, keyer:ATEMConstant, right:float) -> None
{% endhighlight %}
Set Key Mask Right

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            right (float): -9.0-9.0

### setKeyerTop
{% highlight python %}
setKeyerTop(mE:ATEMConstant, keyer:ATEMConstant, top:float) -> None
{% endhighlight %}
Set Key Mask Top

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            top (float): -9.0-9.0

### setKeyerType
{% highlight python %}
setKeyerType(mE:ATEMConstant, keyer:ATEMConstant, type_:ATEMConstant) -> None
{% endhighlight %}
Set Key Type Type

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            type_: see ATEMKeyerTypes

### setMacroAction
{% highlight python %}
setMacroAction(macro:ATEMConstant, action:ATEMConstant) -> None
{% endhighlight %}
Set Macro Action Action

        Args:
            macro: see ATEMMacros (to stop, use macros.stop)
            action: see ATEMMacroActions

### setMacroAddPauseFrames
{% highlight python %}
setMacroAddPauseFrames(frames:int) -> None
{% endhighlight %}
Set Macro Add Pause Frames

        Args:
            frames (int): number of frames

### setMacroRunChangePropertiesLooping
{% highlight python %}
setMacroRunChangePropertiesLooping(looping:bool) -> None
{% endhighlight %}
Set Macro Run Change Properties Looping

        Args:
            looping (bool): On/Off

### setMediaPlayerSourceClipIndex
{% highlight python %}
setMediaPlayerSourceClipIndex(mediaPlayer:ATEMConstant, clipIndex:int) -> None
{% endhighlight %}
Set Media Player Source Clip Index

        Args:
            mediaPlayer: see ATEMMediaPlayers
            clipIndex (int): 0-x: Clip 1-x

### setMediaPlayerSourceStillIndex
{% highlight python %}
setMediaPlayerSourceStillIndex(mediaPlayer:ATEMConstant, stillIndex:int) -> None
{% endhighlight %}
Set Media Player Source Still Index

        Args:
            mediaPlayer: see ATEMMediaPlayers
            stillIndex (int): 0-x: Still 1-x

### setMediaPlayerSourceType
{% highlight python %}
setMediaPlayerSourceType(mediaPlayer:ATEMConstant, type_:ATEMConstant) -> None
{% endhighlight %}
Set Media Player Source Type

        Args:
            mediaPlayer: see ATEMMediaPlayers
            type_: see ATEMMediaPlayerSourceTypes

### setMediaPoolStorageClip1MaxLength
{% highlight python %}
setMediaPoolStorageClip1MaxLength(clip1MaxLength:int) -> None
{% endhighlight %}
Set Media Pool Storage Clip 1 Max Length

        Args:
            clip1MaxLength (int): frames

### setMultiViewerInputVideoSource
{% highlight python %}
setMultiViewerInputVideoSource(multiViewer:ATEMConstant, window:ATEMConstant, videoSource:ATEMConstant) -> None
{% endhighlight %}
Set MultiViewer Properties Video Source

        Args:
            multiViewer: see ATEMMultiViewers
            window: see ATEMWindows
            videoSource: see ATEMVideoSources

### setMultiViewerPropertiesLayout
{% highlight python %}
setMultiViewerPropertiesLayout(multiViewer:ATEMConstant, layout:ATEMConstant) -> None
{% endhighlight %}
Set MultiViewer Properties Layout

        Args:
            videoSource: see ATEMVideoSources
            layout: see ATEMMultiViewerLayouts

### setPreviewInputVideoSource
{% highlight python %}
setPreviewInputVideoSource(mE:ATEMConstant, videoSource:ATEMConstant) -> None
{% endhighlight %}
Set Preview Input Video Source

        Args:
            mE: see ATEMMixEffects
            videoSource: see ATEMVideoSources

### setProgramInputVideoSource
{% highlight python %}
setProgramInputVideoSource(mE:ATEMConstant, videoSource:ATEMConstant) -> None
{% endhighlight %}
Set Program Input Video Source

        Args:
            mE: see ATEMMixEffects
            videoSource: see ATEMVideoSources

### setResetAudioMixerPeaksInputSource
{% highlight python %}
setResetAudioMixerPeaksInputSource(inputSource:ATEMConstant) -> None
{% endhighlight %}
Set Reset Audio Mixer Peaks Input Source

        Args:
            inputSource: see ATEMAudioSources

### setResetAudioMixerPeaksMaster
{% highlight python %}
setResetAudioMixerPeaksMaster(master:bool) -> None
{% endhighlight %}
Set Reset Audio Mixer Peaks Master

        Args:
            master (bool): Yes/No

### setRunFlyingKeyKeyFrame
{% highlight python %}
setRunFlyingKeyKeyFrame(mE:ATEMConstant, keyer:ATEMConstant, keyFrame:ATEMConstant) -> None
{% endhighlight %}
Set Run Flying Key Key Frame

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyers
            keyFrame: see ATEMKeyFrames

### setRunFlyingKeyRuntoInfiniteindex
{% highlight python %}
setRunFlyingKeyRuntoInfiniteindex(mE:ATEMConstant, keyer:ATEMConstant, runtoInfiniteindex:int) -> None
{% endhighlight %}
Set Run Flying Key Run-to-Infinite-index

        Args:
            mE: see ATEMMixEffects
            keyer: see ATEMKeyerser 1-4
            runtoInfiniteindex (int): index

### setSuperSourceBorderBevel
{% highlight python %}
setSuperSourceBorderBevel(borderBevel:ATEMConstant) -> None
{% endhighlight %}
Set Super Source Border Bevel

        Args:
            borderBevel: see ATEMBorderBevels

### setSuperSourceBorderBevelPosition
{% highlight python %}
setSuperSourceBorderBevelPosition(borderBevelPosition:float) -> None
{% endhighlight %}
Set Super Source Border Bevel Position

        Args:
            borderBevelPosition (float): 0.0-1.0

### setSuperSourceBorderBevelSoftness
{% highlight python %}
setSuperSourceBorderBevelSoftness(borderBevelSoftness:float) -> None
{% endhighlight %}
Set Super Source Border Bevel Softness

        Args:
            borderBevelSoftness (float): 0.0-1.0

### setSuperSourceBorderEnabled
{% highlight python %}
setSuperSourceBorderEnabled(borderEnabled:bool) -> None
{% endhighlight %}
Set Super Source Border Enabled

        Args:
            borderEnabled (bool): On/Off

### setSuperSourceBorderHue
{% highlight python %}
setSuperSourceBorderHue(borderHue:float) -> None
{% endhighlight %}
Set Super Source Border Hue

        Args:
            borderHue (float): 0.0-359.9 (degrees)

### setSuperSourceBorderInnerSoftness
{% highlight python %}
setSuperSourceBorderInnerSoftness(borderInnerSoftness:int) -> None
{% endhighlight %}
Set Super Source Border Inner Softness

        Args:
            borderInnerSoftness (int): 0-100 (%)

### setSuperSourceBorderInnerWidth
{% highlight python %}
setSuperSourceBorderInnerWidth(borderInnerWidth:float) -> None
{% endhighlight %}
Set Super Source Border Inner Width

        Args:
            borderInnerWidth (float): 0.0-16.0

### setSuperSourceBorderLuma
{% highlight python %}
setSuperSourceBorderLuma(borderLuma:float) -> None
{% endhighlight %}
Set Super Source Border Luma

        Args:
            borderLuma (float): 0.0-100.0 (%)

### setSuperSourceBorderOuterSoftness
{% highlight python %}
setSuperSourceBorderOuterSoftness(borderOuterSoftness:int) -> None
{% endhighlight %}
Set Super Source Border Outer Softness

        Args:
            borderOuterSoftness (int): 0-100 (%)

### setSuperSourceBorderOuterWidth
{% highlight python %}
setSuperSourceBorderOuterWidth(borderOuterWidth:float) -> None
{% endhighlight %}
Set Super Source Border Outer Width

        Args:
            borderOuterWidth (float): 0.0-16.0

### setSuperSourceBorderSaturation
{% highlight python %}
setSuperSourceBorderSaturation(borderSaturation:float) -> None
{% endhighlight %}
Set Super Source Border Saturation

        Args:
            borderSaturation (float): 0.0-100.0 (%)

### setSuperSourceBoxParametersCropBottom
{% highlight python %}
setSuperSourceBoxParametersCropBottom(box:ATEMConstant, cropBottom:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Crop Bottom

        Args:
            box: see ATEMBoxes
            cropBottom (float): 0.0-18.0

### setSuperSourceBoxParametersCropLeft
{% highlight python %}
setSuperSourceBoxParametersCropLeft(box:ATEMConstant, cropLeft:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Crop Left

        Args:
            box: see ATEMBoxes
            cropLeft (float): 0.0-32.0

### setSuperSourceBoxParametersCropRight
{% highlight python %}
setSuperSourceBoxParametersCropRight(box:ATEMConstant, cropRight:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Crop Right

        Args:
            box: see ATEMBoxes
            cropRight (float): 0.0-32.0

### setSuperSourceBoxParametersCropTop
{% highlight python %}
setSuperSourceBoxParametersCropTop(box:ATEMConstant, cropTop:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Crop Top

        Args:
            box: see ATEMBoxes
            cropTop (float): 0.0-18.0

### setSuperSourceBoxParametersCropped
{% highlight python %}
setSuperSourceBoxParametersCropped(box:ATEMConstant, cropped:bool) -> None
{% endhighlight %}
Set Super Source Box Parameters Cropped

        Args:
            box: see ATEMBoxes
            cropped (bool): On/Off

### setSuperSourceBoxParametersEnabled
{% highlight python %}
setSuperSourceBoxParametersEnabled(box:ATEMConstant, enabled:bool) -> None
{% endhighlight %}
Set Super Source Box Parameters Enabled

        Args:
            box: see ATEMBoxes
            enabled (bool): On/Off

### setSuperSourceBoxParametersInputSource
{% highlight python %}
setSuperSourceBoxParametersInputSource(box:ATEMConstant, inputSource:ATEMConstant) -> None
{% endhighlight %}
Set Super Source Box Parameters Input Source

        Args:
            box: see ATEMBoxes
            inputSource: see ATEMVideoSources

### setSuperSourceBoxParametersPositionX
{% highlight python %}
setSuperSourceBoxParametersPositionX(box:ATEMConstant, positionX:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Position X

        Args:
            box: see ATEMBoxes
            positionX (float): -48.0-48.0

### setSuperSourceBoxParametersPositionY
{% highlight python %}
setSuperSourceBoxParametersPositionY(box:ATEMConstant, positionY:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Position Y

        Args:
            box: see ATEMBoxes
            positionY (float): -27.0-27.0

### setSuperSourceBoxParametersSize
{% highlight python %}
setSuperSourceBoxParametersSize(box:ATEMConstant, size:float) -> None
{% endhighlight %}
Set Super Source Box Parameters Size

        Args:
            box: see ATEMBoxes
            size (float): 0.07-1.0

### setSuperSourceClip
{% highlight python %}
setSuperSourceClip(clip:float) -> None
{% endhighlight %}
Set Super Source Clip

        Args:
            clip (float): 0.0-100.0 (%)

### setSuperSourceFillSource
{% highlight python %}
setSuperSourceFillSource(fillSource:ATEMConstant) -> None
{% endhighlight %}
Set Super Source Fill Source

        Args:
            fillSource: see ATEMVideoSources

### setSuperSourceForeground
{% highlight python %}
setSuperSourceForeground(foreground:bool) -> None
{% endhighlight %}
Set Super Source Foreground

        Args:
            foreground (bool): On/Off

### setSuperSourceGain
{% highlight python %}
setSuperSourceGain(gain:float) -> None
{% endhighlight %}
Set Super Source Gain

        Args:
            gain (float): 0.0-100.0 (%)

### setSuperSourceInvertKey
{% highlight python %}
setSuperSourceInvertKey(invertKey:bool) -> None
{% endhighlight %}
Set Super Source Invert Key

        Args:
            invertKey (bool): On/Off

### setSuperSourceKeySource
{% highlight python %}
setSuperSourceKeySource(keySource:ATEMConstant) -> None
{% endhighlight %}
Set Super Source Key Source

        Args:
            keySource: see ATEMVideoSources

### setSuperSourceLightSourceAltitude
{% highlight python %}
setSuperSourceLightSourceAltitude(lightSourceAltitude:int) -> None
{% endhighlight %}
Set Super Source Light Source Altitude

        Args:
            lightSourceAltitude (int): 10-100

### setSuperSourceLightSourceDirection
{% highlight python %}
setSuperSourceLightSourceDirection(lightSourceDirection:float) -> None
{% endhighlight %}
Set Super Source Light Source Direction

        Args:
            lightSourceDirection (float): 0.0-359.9 (degrees)

### setSuperSourcePreMultiplied
{% highlight python %}
setSuperSourcePreMultiplied(preMultiplied:bool) -> None
{% endhighlight %}
Set Super Source Pre Multiplied

        Args:
            preMultiplied (bool): On/Off

### setTransitionDVEClip
{% highlight python %}
setTransitionDVEClip(mE:ATEMConstant, clip:float) -> None
{% endhighlight %}
Set Transition DVE Clip

        Args:
            mE: see ATEMMixEffects
            clip (float): 0.0-100.0 (%)

### setTransitionDVEEnableKey
{% highlight python %}
setTransitionDVEEnableKey(mE:ATEMConstant, enableKey:bool) -> None
{% endhighlight %}
Set Transition DVE Enable Key

        Args:
            mE: see ATEMMixEffects
            enableKey (bool): On/Off

### setTransitionDVEFillSource
{% highlight python %}
setTransitionDVEFillSource(mE:ATEMConstant, fillSource:ATEMConstant) -> None
{% endhighlight %}
Set Transition DVE Fill Source

        Args:
            mE: see ATEMMixEffects
            fillSource: see ATEMVideoSources

### setTransitionDVEFlipFlop
{% highlight python %}
setTransitionDVEFlipFlop(mE:ATEMConstant, flipFlop:bool) -> None
{% endhighlight %}
Set Transition DVE FlipFlop

        Args:
            mE: see ATEMMixEffects
            flipFlop (bool): On/Off

### setTransitionDVEGain
{% highlight python %}
setTransitionDVEGain(mE:ATEMConstant, gain:float) -> None
{% endhighlight %}
Set Transition DVE Gain

        Args:
            mE: see ATEMMixEffects
            gain (float): 0.0-100.0 (%)

### setTransitionDVEInvertKey
{% highlight python %}
setTransitionDVEInvertKey(mE:ATEMConstant, invertKey:bool) -> None
{% endhighlight %}
Set Transition DVE Invert Key

        Args:
            mE: see ATEMMixEffects
            invertKey (bool): On/Off

### setTransitionDVEKeySource
{% highlight python %}
setTransitionDVEKeySource(mE:ATEMConstant, keySource:ATEMConstant) -> None
{% endhighlight %}
Set Transition DVE Key Source

        Args:
            mE: see ATEMMixEffects
            keySource: see ATEMVideoSources

### setTransitionDVEPreMultiplied
{% highlight python %}
setTransitionDVEPreMultiplied(mE:ATEMConstant, preMultiplied:bool) -> None
{% endhighlight %}
Set Transition DVE Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            preMultiplied (bool): On/Off

### setTransitionDVERate
{% highlight python %}
setTransitionDVERate(mE:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Transition DVE Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)

### setTransitionDVEReverse
{% highlight python %}
setTransitionDVEReverse(mE:ATEMConstant, reverse:bool) -> None
{% endhighlight %}
Set Transition DVE Reverse

        Args:
            mE: see ATEMMixEffects
            reverse (bool): On/Off

### setTransitionDVEStyle
{% highlight python %}
setTransitionDVEStyle(mE:ATEMConstant, style:ATEMConstant) -> None
{% endhighlight %}
Set Transition DVE Style

        Args:
            mE: see ATEMMixEffects
            style: see ATEMDVETransitionStyles

### setTransitionDipInput
{% highlight python %}
setTransitionDipInput(mE:ATEMConstant, input_:ATEMConstant) -> None
{% endhighlight %}
Set Transition Dip Input

        Args:
            mE: see ATEMMixEffects
            input_: see ATEMVideoSources

### setTransitionDipRate
{% highlight python %}
setTransitionDipRate(mE:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Transition Dip Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)

### setTransitionMixRate
{% highlight python %}
setTransitionMixRate(mE:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Transition Mix Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)

### setTransitionNextTransition
{% highlight python %}
setTransitionNextTransition(mE:ATEMConstant, nextTransition:int) -> None
{% endhighlight %}
Set Transition Style Next Transition

        Args:
            mE: see ATEMMixEffects
            nextTransition: see ATEMTransitionStyles

### setTransitionPosition
{% highlight python %}
setTransitionPosition(mE:ATEMConstant, position:int) -> None
{% endhighlight %}
Set Transition Preview Enabled

        Args:
            mE: see ATEMMixEffects
            position (int): 0-9999

### setTransitionPreviewEnabled
{% highlight python %}
setTransitionPreviewEnabled(mE:ATEMConstant, enabled:bool) -> None
{% endhighlight %}
Set Transition Preview Enabled

        Args:
            mE: see ATEMMixEffects
            enabled (bool): On/Off

### setTransitionStingerClip
{% highlight python %}
setTransitionStingerClip(mE:ATEMConstant, clip:float) -> None
{% endhighlight %}
Set Transition Stinger Clip

        Args:
            mE: see ATEMMixEffects
            clip (float): 0.0-100.0 (%)

### setTransitionStingerClipDuration
{% highlight python %}
setTransitionStingerClipDuration(mE:ATEMConstant, clipDuration:int) -> None
{% endhighlight %}
Set Transition Stinger Clip Duration

        Args:
            mE: see ATEMMixEffects
            clipDuration (int): frames

### setTransitionStingerGain
{% highlight python %}
setTransitionStingerGain(mE:ATEMConstant, gain:float) -> None
{% endhighlight %}
Set Transition Stinger Gain

        Args:
            mE: see ATEMMixEffects
            gain (float): 0.0-100.0 (%)

### setTransitionStingerInvertKey
{% highlight python %}
setTransitionStingerInvertKey(mE:ATEMConstant, invertKey:bool) -> None
{% endhighlight %}
Set Transition Stinger Invert Key

        Args:
            mE: see ATEMMixEffects
            invertKey (bool): On/Off

### setTransitionStingerMixRate
{% highlight python %}
setTransitionStingerMixRate(mE:ATEMConstant, mixRate:int) -> None
{% endhighlight %}
Set Transition Stinger Mix Rate

        Args:
            mE: see ATEMMixEffects
            mixRate (int): frames

### setTransitionStingerPreMultiplied
{% highlight python %}
setTransitionStingerPreMultiplied(mE:ATEMConstant, preMultiplied:bool) -> None
{% endhighlight %}
Set Transition Stinger Pre Multiplied

        Args:
            mE: see ATEMMixEffects
            preMultiplied (bool): On/Off

### setTransitionStingerPreRoll
{% highlight python %}
setTransitionStingerPreRoll(mE:ATEMConstant, preRoll:int) -> None
{% endhighlight %}
Set Transition Stinger Pre Roll

        Args:
            mE: see ATEMMixEffects
            preRoll (int): frames

### setTransitionStingerSource
{% highlight python %}
setTransitionStingerSource(mE:ATEMConstant, source:ATEMConstant) -> None
{% endhighlight %}
Set Transition Stinger Source

        Args:
            mE: see ATEMMixEffects
            source: see ATEMMediaPlayers

### setTransitionStingerTriggerPoint
{% highlight python %}
setTransitionStingerTriggerPoint(mE:ATEMConstant, triggerPoint:int) -> None
{% endhighlight %}
Set Transition Stinger Trigger Point

        Args:
            mE: see ATEMMixEffects
            triggerPoint (int): frames

### setTransitionStyle
{% highlight python %}
setTransitionStyle(mE:ATEMConstant, style:ATEMConstant) -> None
{% endhighlight %}
Set Transition Style

        Args:
            mE: see ATEMMixEffects
            style: see ATEMTransitionStyles

### setTransitionWipeFillSource
{% highlight python %}
setTransitionWipeFillSource(mE:ATEMConstant, fillSource:ATEMConstant) -> None
{% endhighlight %}
Set Transition Wipe Fill Source

        Args:
            mE: see ATEMMixEffects
            fillSource: see ATEMVideoSources

### setTransitionWipeFlipFlop
{% highlight python %}
setTransitionWipeFlipFlop(mE:ATEMConstant, flipFlop:bool) -> None
{% endhighlight %}
Set Transition Wipe FlipFlop

        Args:
            mE: see ATEMMixEffects
            flipFlop (bool): On/Off

### setTransitionWipePattern
{% highlight python %}
setTransitionWipePattern(mE:ATEMConstant, pattern:ATEMConstant) -> None
{% endhighlight %}
Set Transition Wipe Pattern

        Args:
            mE: see ATEMMixEffects
            pattern: see ATEMPatternStyles

### setTransitionWipePositionX
{% highlight python %}
setTransitionWipePositionX(mE:ATEMConstant, positionX:float) -> None
{% endhighlight %}
Set Transition Wipe Position X

        Args:
            mE: see ATEMMixEffects
            positionX (float): 0.0-1.0

### setTransitionWipePositionY
{% highlight python %}
setTransitionWipePositionY(mE:ATEMConstant, positionY:float) -> None
{% endhighlight %}
Set Transition Wipe Position Y

        Args:
            mE: see ATEMMixEffects
            positionY (float): 0.0-1.0

### setTransitionWipeRate
{% highlight python %}
setTransitionWipeRate(mE:ATEMConstant, rate:int) -> None
{% endhighlight %}
Set Transition Wipe Rate

        Args:
            mE: see ATEMMixEffects
            rate (int): 1-250 (frames)

### setTransitionWipeReverse
{% highlight python %}
setTransitionWipeReverse(mE:ATEMConstant, reverse:bool) -> None
{% endhighlight %}
Set Transition Wipe Reverse

        Args:
            mE: see ATEMMixEffects
            reverse (bool): On/Off

### setTransitionWipeSoftness
{% highlight python %}
setTransitionWipeSoftness(mE:ATEMConstant, softness:float) -> None
{% endhighlight %}
Set Transition Wipe Softness

        Args:
            mE: see ATEMMixEffects
            softness (float): 0.0-100.0 (%)

### setTransitionWipeSymmetry
{% highlight python %}
setTransitionWipeSymmetry(mE:ATEMConstant, symmetry:float) -> None
{% endhighlight %}
Set Transition Wipe Symmetry

        Args:
            mE: see ATEMMixEffects
            symmetry (float): 0.0-100.0 (%)

### setTransitionWipeWidth
{% highlight python %}
setTransitionWipeWidth(mE:ATEMConstant, width:float) -> None
{% endhighlight %}
Set Transition Wipe Width

        Args:
            mE: see ATEMMixEffects
            width (float): 0.0-100.0 (%)

### setVideoModeFormat
{% highlight python %}
setVideoModeFormat(format_:ATEMConstant) -> None
{% endhighlight %}
Set Video Mode Format

        Args:
            format_: see ATEMVideoModeFormats

