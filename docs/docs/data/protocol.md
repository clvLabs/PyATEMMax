---
layout: page
title: Docs - Data - Protocol constants
permalink: /docs/data/protocol/
---

The `atem` member in `ATEMMax` is an `ATEMProtocol` object, containing constant value definitions for the ATEM protocol.

{% highlight python %}
>>> print(switcher.atem.UDPPort.value)
9910
>>> print(switcher.atem.videoSources.mediaPlayer1.value)
3010
>>> print(switcher.atem.videoModeFormats.f1080p50.value)
12
{% endhighlight %}

## Value enumerations

A lot of efforts have been put into making the library _Intellisense friendly_ and helping the library user with the overwhelming amount of setting values you can find in the protocol.

Instead of using numbers extracted from the [ATEM Potocol][skaarhoj-bmdprotocol] to identify cameras, videoSources, etc... you can use things like:

* Video sources
    * `switcher.atem.videoSources.input1`
    * `switcher.atem.videoSources.colorBars`
    * `switcher.atem.videoSources.mediaPlayer1`
* Audio sources
    * `switcher.atem.audioSources.input1`
    * `switcher.atem.audioSources.xlr`
    * `switcher.atem.audioSources.mic1`
* Video mode formats
    * `switcher.atem.videoModeFormats.f525i59_94_ntsc_16_9`
    * `switcher.atem.videoModeFormats.f720p50`
    * `switcher.atem.videoModeFormats.f1080p50`
* Down converter modes
    * `switcher.atem.downConverterModes.centerCut`
    * `switcher.atem.downConverterModes.letterBox`
    * `switcher.atem.downConverterModes.anamorphic`

As you start typing the collection name, your editor should show you a list of valid value names.

## ATEMConstant

All these protocol values are stored as `ATEMConstant` objects.

* An `ATEMConstant` object consists of a `name` and a `value`.
* If you print an `ATEMConstant` you will get its name (string)
* If you want to get the *raw* numeric value, use `ATEMConstant.value`

With these `ATEMConstant`s you can choose how you want to provide parameters for methods:
* Using the provided protocol constants
{% highlight python %}
switcher.setProgramInputVideoSource(switcher.atem.mixEffects.mixEffect1, switcher.atem.videoSources.mediaPlayer1)
{% endhighlight %}
* Using ATEM protocol integer values
{% highlight python %}
switcher.setProgramInputVideoSource(0, 3010)
{% endhighlight %}
* Using strings representing the values in the respective lists
{% highlight python %}
switcher.setProgramInputVideoSource("mixEffect1", "mediaPlayer1")
{% endhighlight %}

It works the same way when getting data values:
* Using the provided protocol constants
{% highlight python %}
switcher.programInput[switcher.atem.mixEffects.mixEffect1].videoSource
{% endhighlight %}
* Using ATEM protocol integer values
{% highlight python %}
switcher.programInput[0].videoSource
{% endhighlight %}
* Using strings representing the values in the respective lists
{% highlight python %}
switcher.programInput["mixEffect1"].videoSource
{% endhighlight %}

## Value lists


### swicher.atem.videoSources
* `black`
* `input1..40`
* `colorBars`
* `color1`
* `color2`
* `mediaPlayer1`
* `mediaPlayer1..4Key`
* `key1..16Mask`
* `dsk1..4Mask`
* `superSource`
* `superSource2`
* `cleanFeed1..4`
* `auxilary1..24`
* `mE1..4Prog`
* `mE1..4Prev`
* `input1Direct`


### swicher.atem.audioSources
* `input1..20`
* `xlr`
* `aes_ebu`
* `rca`
* `mic1..2`
* `mp1..4`


### swicher.atem.downConverterModes
* `centerCut`
* `letterBox`
* `anamorphic`


### swicher.atem.videoModeFormats
* `f525i59_94_ntsc`
* `f625i_50_pal`
* `f525i59_94_ntsc_16_9`
* `f625i_50_pal_16_9`
* `f720p50`
* `f720p59_94`
* `f1080i50`
* `f1080i59_94`
* `f1080p23_98`
* `f1080p24`
* `f1080p25`
* `f1080p29_97`
* `f1080p50`
* `f1080p59_94`
* `f2160p23_98`
* `f2160p24`
* `f2160p25`
* `f2160p29_97`


### swicher.atem.externalPortTypes
* `internal`
* `sdi`
* `hdmi`
* `composite`
* `component`
* `sVideo`


### swicher.atem.switcherPortTypes
* `external`
* `black`
* `colorBars`
* `colorGenerator`
* `mediaPlayerFill`
* `mediaPlayerKey`
* `superSource`
* `externalDirect`
* `mEOutput`
* `auxiliary`
* `mask`
* `multiviewer`


### swicher.atem.multiViewerLayouts
* `top`
* `bottom`
* `left`
* `right`


### swicher.atem.transitionStyles
* `mix`
* `dip`
* `wipe`
* `dVE`
* `sting`


### swicher.atem.keyerTypes
* `luma`
* `chroma`
* `pattern`
* `dVE`


### swicher.atem.borderBevels
* `no`
* `inOut`
* `in_`
* `out`


### swicher.atem.mediaPlayerSourceTypes
* `still`
* `clip`


### swicher.atem.audioMixerInputTypes
* `externalVideo`
* `mediaPlayer`
* `externalAudio`


### swicher.atem.audioMixerInputPlugTypes
* `internal`
* `sdi`
* `hdmi`
* `component`
* `composite`
* `sVideo`
* `xlr`
* `aes_ebu`
* `rca`


### swicher.atem.audioMixerInputMixOptions
* `off`
* `on`
* `afv`


### swicher.atem.dVETransitionStyles
* `swooshTopLeft`
* `swooshTop`
* `swooshTopRight`
* `swooshLeft`
* `swooshRight`
* `swooshBottomLeft`
* `swooshBottom`
* `swooshBottomRight`
* `spinCCWTopRight`
* `spinCWTopLeft`
* `spinCCWBottomRight`
* `spinCWBottomLeft`
* `spinCWTopRight`
* `spinCCWTopLeft`
* `spinCWBottomRight`
* `spinCCWBottomLeft`
* `squeezeTopLeft`
* `squeezeTop`
* `squeezeTopRight`
* `squeezeLeft`
* `squeezeRight`
* `squeezeBottomLeft`
* `squeezeBottom`
* `squeezeBottomRight`
* `pushTopLeft`
* `pushTop`
* `pushTopRight`
* `pushLeft`
* `pushRight`
* `pushBottomLeft`
* `pushBottom`
* `pushBottomRight`
* `graphicCWSpin`
* `graphicCCWSpin`
* `graphicLogoWipe`


### swicher.atem.patternStyles
* `leftToRightBar`
* `topToBottomBar`
* `horizontalBarnDoor`
* `verticalBarnDoor`
* `cornersInFourBox`
* `rectangleIris`
* `diamondIris`
* `circleIris`
* `topLeftBox`
* `topRightBox`
* `bottomRightBox`
* `bottomLeftBox`
* `topCentreBox`
* `rightCentreBox`
* `bottomCentreBox`
* `leftCentreBox`
* `topLeftDiagonal`
* `topRightDiagonal`


### swicher.atem.camerControlSharpeningLevels
* `off`
* `low`
* `medium`
* `high`


### swicher.atem.macroActions
* `runMacro`
* `stopMacro`
* `stopRecording`
* `insertWaitForUser`
* `continueMacro`
* `deleteMacro`


### swicher.atem.keyFrames
* `a`
* `b`
* `full`
* `runToInfinite`



### swicher.atem.mixEffects
* `mixEffect1..4`


### swicher.atem.multiViewers
* `multiViewer1..2`


### swicher.atem.windows
* `window1..10`


### swicher.atem.keyers
* `keyer1..4`


### swicher.atem.dSKs
* `dsk1..2`


### swicher.atem.colorGenerators
* `colorGenerator1..2`


### swicher.atem.auxChannels
* `auxChannel1..6`


### swicher.atem.cameras
* `camera1..20`


### swicher.atem.mediaPlayers
* `mediaPlayer1..4`


### swicher.atem.clipBanks
* `clipBank1..2`


### swicher.atem.stillBanks
* `stillBank1..32`


### swicher.atem.macros
* `stop`
* `macro1..100`


### swicher.atem.boxes
* `box1..4`


[skaarhoj-bmdprotocol]: http://skaarhoj.com/fileadmin/BMDPROTOCOL.html
