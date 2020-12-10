---
layout: page
title: Docs - Data - Switcher State
permalink: /docs/data/state/
---

The `ATEMMax` object provides information about both the connection status and the switcher state.

## Switcher connection

* `started` (bool): `True` if `connect()` has been called.
* `switcherAlive` (bool): Set to `True` on first UDP packet reception from the switcher.
* `handshakeStarted` (bool): Set to `True` when `ATEMMax` closes the `HELLO` interaction and starts waiting for the initial data snapshot.
* `connected` (bool): Set to `True` when the initial data snapshot is finished and *normal operation* starts.
* `ip` (str): IP address of the switcher.


## Switcher state

### Data structure

Settings are organized in a tree-like structure, for easier access. Examples:
* `switcher.videoMode.format`
* `switcher.audioMixer.master.volume`
* `switcher.audioMixer.input[audioSource].volume`
* `switcher.cameraControl[camera].lift.r`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.outer.softness`

### Value lists

When a node in the value tree is a list, it can be indexed using an `ATEMConstant`.

These 3 statements are equivalent:

{% highlight python %}
switcher.audioMixer.input[switcher.atem.audioSources.mic1].volume
switcher.audioMixer.input[1301].volume
switcher.audioMixer.input["mic1"].volume
{% endhighlight %}

See the [Data - Protocol - ATEMConstant](../protocol#atemconstant) section for more info.

### Mapped values

In most cases the *raw* values received from the switcher are converted to *real world* values. Examples:

Audio volumes are expressed in dB, no conversions required:
{% highlight python %}
switcher.setAudioMixerMasterVolume(1.8)
decibels = switcher.audioMixer.master.volume
{% endhighlight %}

Gamma values in `cameraControl` are interpreted as `float` values ranging from -1.0 to 1.0, instead of the original -8192 to 8192 *raw* range:
{% highlight python %}
switcher.setCameraControlGammaR("camera1", 0.7)
gamma = self.data.cameraControl["camera1"].gamma.r
{% endhighlight %}

Hue value in `cameraControl` is interpreted as a `float` value ranging from 0.0 to 359.9 degrees, instead of the original -2048 to 2048 *raw* range:
{% highlight python %}
switcher.setCameraControlHue("camera1", 90.5)
hue = self.data.cameraControl["camera1"].hue
{% endhighlight %}


### Enumerated values

When a setting corresponds to an enumerated value, the option name can be extracted by converting it to a string or getting its `name` member:
{% highlight python %}
formatname = f"Current video format: {switcher.videoMode.format}"
formatname = "Current video format: " + str(switcher.videoMode.format)
formatname = "Current video format: " + switcher.videoMode.format.name
{% endhighlight %}

### State tree

This is the complete list of settings stored in the `ATEMMax` object:

#### general
* `switcher.atemModel`
* `switcher.warningText`

#### audioMixer
* `switcher.audioMixer.config.audioChannels`
* `switcher.audioMixer.config.hasMonitor`
* `switcher.audioMixer.input[audioSource].balance`
* `switcher.audioMixer.input[audioSource].fromMediaPlayer`
* `switcher.audioMixer.input[audioSource].mixOption`
* `switcher.audioMixer.input[audioSource].plugtype`
* `switcher.audioMixer.input[audioSource].type`
* `switcher.audioMixer.input[audioSource].volume`
* `switcher.audioMixer.levels.master.left`
* `switcher.audioMixer.levels.master.peak.left`
* `switcher.audioMixer.levels.master.peak.right`
* `switcher.audioMixer.levels.master.right`
* `switcher.audioMixer.levels.monitor`
* `switcher.audioMixer.levels.numSources`
* `switcher.audioMixer.levels.sources[audioSources[a]].left`
* `switcher.audioMixer.levels.sources[audioSources[a]].peak.left`
* `switcher.audioMixer.levels.sources[audioSources[a]].peak.right`
* `switcher.audioMixer.levels.sources[audioSources[a]].right`
* `switcher.audioMixer.master.volume`
* `switcher.audioMixer.monitor.dim`
* `switcher.audioMixer.monitor.monitorAudio`
* `switcher.audioMixer.monitor.mute`
* `switcher.audioMixer.monitor.solo`
* `switcher.audioMixer.monitor.soloInput`
* `switcher.audioMixer.monitor.volume`
* `switcher.audioMixer.tally.numSources`
* `switcher.audioMixer.tally.sources[audioSource].isMixedIn`

#### auxSource
* `switcher.auxSource[aUXChannel].input`

#### cameraControl
* `switcher.cameraControl[camera].colorbars`
* `switcher.cameraControl[camera].contrast`
* `switcher.cameraControl[camera].focus`
* `switcher.cameraControl[camera].gain.b`
* `switcher.cameraControl[camera].gain.g`
* `switcher.cameraControl[camera].gain.r`
* `switcher.cameraControl[camera].gain.value`
* `switcher.cameraControl[camera].gain.y`
* `switcher.cameraControl[camera].gamma.b`
* `switcher.cameraControl[camera].gamma.g`
* `switcher.cameraControl[camera].gamma.r`
* `switcher.cameraControl[camera].gamma.y`
* `switcher.cameraControl[camera].hue`
* `switcher.cameraControl[camera].iris`
* `switcher.cameraControl[camera].lift.b`
* `switcher.cameraControl[camera].lift.g`
* `switcher.cameraControl[camera].lift.r`
* `switcher.cameraControl[camera].lift.y`
* `switcher.cameraControl[camera].lumMix`
* `switcher.cameraControl[camera].saturation`
* `switcher.cameraControl[camera].sharpeningLevel`
* `switcher.cameraControl[camera].shutter`
* `switcher.cameraControl[camera].whiteBalance`
* `switcher.cameraControl[camera].zoom.normalized`
* `switcher.cameraControl[camera].zoom.speed`

#### clipPlayer
* `switcher.clipPlayer[mediaPlayer].atBeginning`
* `switcher.clipPlayer[mediaPlayer].clipFrame`
* `switcher.clipPlayer[mediaPlayer].loop`
* `switcher.clipPlayer[mediaPlayer].playing`

#### colorGenerator
* `switcher.colorGenerator[colorGenerator].hue`
* `switcher.colorGenerator[colorGenerator].luma`
* `switcher.colorGenerator[colorGenerator].saturation`

#### downConverter
* `switcher.downConverter.mode`

#### downstreamKeyer
* `switcher.downstreamKeyer[dsk].bottom`
* `switcher.downstreamKeyer[dsk].clip`
* `switcher.downstreamKeyer[dsk].fillSource`
* `switcher.downstreamKeyer[dsk].framesRemaining`
* `switcher.downstreamKeyer[dsk].gain`
* `switcher.downstreamKeyer[dsk].inTransition`
* `switcher.downstreamKeyer[dsk].invertKey`
* `switcher.downstreamKeyer[dsk].isAutoTransitioning`
* `switcher.downstreamKeyer[dsk].keySource`
* `switcher.downstreamKeyer[dsk].left`
* `switcher.downstreamKeyer[dsk].masked`
* `switcher.downstreamKeyer[dsk].onAir`
* `switcher.downstreamKeyer[dsk].preMultiplied`
* `switcher.downstreamKeyer[dsk].rate`
* `switcher.downstreamKeyer[dsk].right`
* `switcher.downstreamKeyer[dsk].tie`
* `switcher.downstreamKeyer[dsk].top`

#### fadeToBlack
* `switcher.fadeToBlack[mE].rate`
* `switcher.fadeToBlack[mE].state.framesRemaining`
* `switcher.fadeToBlack[mE].state.fullyBlack`
* `switcher.fadeToBlack[mE].state.inTransition`

#### inputProperties
* `switcher.inputProperties[videoSource].availability.auxiliary`
* `switcher.inputProperties[videoSource].availability.keySourcesEverywhere`
* `switcher.inputProperties[videoSource].availability.multiviewer`
* `switcher.inputProperties[videoSource].availability.superSourceArt`
* `switcher.inputProperties[videoSource].availability.superSourceBox`
* `switcher.inputProperties[videoSource].availableExternalPortTypes.component`
* `switcher.inputProperties[videoSource].availableExternalPortTypes.composite`
* `switcher.inputProperties[videoSource].availableExternalPortTypes.hdmi`
* `switcher.inputProperties[videoSource].availableExternalPortTypes.sdi`
* `switcher.inputProperties[videoSource].availableExternalPortTypes.sVideo`
* `switcher.inputProperties[videoSource].externalPortType`
* `switcher.inputProperties[videoSource].longName`
* `switcher.inputProperties[videoSource].mEAvailability.mE1FillSources`
* `switcher.inputProperties[videoSource].mEAvailability.mE2FillSources`
* `switcher.inputProperties[videoSource].portType`
* `switcher.inputProperties[videoSource].shortName`

#### key
* `switcher.key[mE][keyer].chroma.gain`
* `switcher.key[mE][keyer].chroma.hue`
* `switcher.key[mE][keyer].chroma.lift`
* `switcher.key[mE][keyer].chroma.narrow`
* `switcher.key[mE][keyer].chroma.ySuppress`
* `switcher.key[mE][keyer].dVE.border.bevel.position`
* `switcher.key[mE][keyer].dVE.border.bevel.softness`
* `switcher.key[mE][keyer].dVE.border.bevel.type`
* `switcher.key[mE][keyer].dVE.border.enabled`
* `switcher.key[mE][keyer].dVE.border.hue`
* `switcher.key[mE][keyer].dVE.border.inner.softness`
* `switcher.key[mE][keyer].dVE.border.inner.width`
* `switcher.key[mE][keyer].dVE.border.luma`
* `switcher.key[mE][keyer].dVE.border.opacity`
* `switcher.key[mE][keyer].dVE.border.outer.softness`
* `switcher.key[mE][keyer].dVE.border.outer.width`
* `switcher.key[mE][keyer].dVE.border.saturation`
* `switcher.key[mE][keyer].dVE.bottom`
* `switcher.key[mE][keyer].dVE.left`
* `switcher.key[mE][keyer].dVE.lightSource.altitude`
* `switcher.key[mE][keyer].dVE.lightSource.direction`
* `switcher.key[mE][keyer].dVE.masked`
* `switcher.key[mE][keyer].dVE.position.x`
* `switcher.key[mE][keyer].dVE.position.y`
* `switcher.key[mE][keyer].dVE.rate`
* `switcher.key[mE][keyer].dVE.right`
* `switcher.key[mE][keyer].dVE.rotation`
* `switcher.key[mE][keyer].dVE.shadow`
* `switcher.key[mE][keyer].dVE.size.x`
* `switcher.key[mE][keyer].dVE.size.y`
* `switcher.key[mE][keyer].dVE.top`
* `switcher.key[mE][keyer].luma.clip`
* `switcher.key[mE][keyer].luma.gain`
* `switcher.key[mE][keyer].luma.invertKey`
* `switcher.key[mE][keyer].luma.preMultiplied`
* `switcher.key[mE][keyer].pattern.invertPattern`
* `switcher.key[mE][keyer].pattern.pattern`
* `switcher.key[mE][keyer].pattern.position.x`
* `switcher.key[mE][keyer].pattern.position.y`
* `switcher.key[mE][keyer].pattern.size`
* `switcher.key[mE][keyer].pattern.softness`
* `switcher.key[mE][keyer].pattern.symmetry`

#### keyer
* `switcher.keyer[mE][keyer].bottom`
* `switcher.keyer[mE][keyer].fillSource`
* `switcher.keyer[mE][keyer].fly.enabled`
* `switcher.keyer[mE][keyer].fly.isASet`
* `switcher.keyer[mE][keyer].fly.isAtKeyFrame.a`
* `switcher.keyer[mE][keyer].fly.isAtKeyFrame.b`
* `switcher.keyer[mE][keyer].fly.isAtKeyFrame.full`
* `switcher.keyer[mE][keyer].fly.isAtKeyFrame.runToInfinite`
* `switcher.keyer[mE][keyer].fly.isBSet`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.bevel.position`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.bevel.softness`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.hue`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.inner.softness`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.inner.width`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.luma`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.opacity`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.outer.softness`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.outer.width`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].border.saturation`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].bottom`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].left`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].lightSource.altitude`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].lightSource.direction`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].position.x`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].position.y`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].right`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].rotation`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].size.x`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].size.y`
* `switcher.keyer[mE][keyer].fly.keyFrame[keyFrame].top`
* `switcher.keyer[mE][keyer].fly.runtoInfiniteindex`
* `switcher.keyer[mE][keyer].keySource`
* `switcher.keyer[mE][keyer].left`
* `switcher.keyer[mE][keyer].masked`
* `switcher.keyer[mE][keyer].onAir.enabled`
* `switcher.keyer[mE][keyer].right`
* `switcher.keyer[mE][keyer].top`
* `switcher.keyer[mE][keyer].type`

#### lastStateChange
* `switcher.lastStateChange.timeCode.frame`
* `switcher.lastStateChange.timeCode.hour`
* `switcher.lastStateChange.timeCode.minute`
* `switcher.lastStateChange.timeCode.second`

#### macro
* `switcher.macro.pool.banks`
* `switcher.macro.properties[macroIndex].isUsed`
* `switcher.macro.properties[macroIndex].name`
* `switcher.macro.recordingStatus.index`
* `switcher.macro.recordingStatus.isRecording`
* `switcher.macro.runStatus.index`
* `switcher.macro.runStatus.isLooping`
* `switcher.macro.runStatus.state.running`
* `switcher.macro.runStatus.state.waiting`

#### mediaPlayer
* `switcher.mediaPlayer.audioSource[clipBank].fileName`
* `switcher.mediaPlayer.audioSource[clipBank].isUsed`
* `switcher.mediaPlayer.clipBanks`
* `switcher.mediaPlayer.clipSource[clipBank].fileName`
* `switcher.mediaPlayer.clipSource[clipBank].frames`
* `switcher.mediaPlayer.clipSource[clipBank].isUsed`
* `switcher.mediaPlayer.source[mediaPlayer].clipIndex`
* `switcher.mediaPlayer.source[mediaPlayer].stillIndex`
* `switcher.mediaPlayer.source[mediaPlayer].type`
* `switcher.mediaPlayer.stillBanks`
* `switcher.mediaPlayer.stillFile[stillBank].fileName`
* `switcher.mediaPlayer.stillFile[stillBank].isUsed`

#### mediaPoolStorage
* `switcher.mediaPoolStorage.clip1MaxLength`
* `switcher.mediaPoolStorage.clip2MaxLength`

#### mixEffect
* `switcher.mixEffect.config[mE].keyers`

#### multiViewer
* `switcher.multiViewer.config.multiViewers`
* `switcher.multiViewer.input[multiViewer][windowIndex].videoSource`
* `switcher.multiViewer.properties[multiViewer].layout`

#### power
* `switcher.power.status.backup`
* `switcher.power.status.main`

#### previewInput
* `switcher.previewInput[mE].videoSource`

#### programInput
* `switcher.programInput[mE].videoSource`

#### protocolVersion
* `switcher.protocolVersion.major`
* `switcher.protocolVersion.minor`

#### superSource
* `switcher.superSource.border.bevel.position`
* `switcher.superSource.border.bevel.softness`
* `switcher.superSource.border.bevel.value`
* `switcher.superSource.border.enabled`
* `switcher.superSource.border.hue`
* `switcher.superSource.border.inner.softness`
* `switcher.superSource.border.inner.width`
* `switcher.superSource.border.luma`
* `switcher.superSource.border.outer.softness`
* `switcher.superSource.border.outer.width`
* `switcher.superSource.border.saturation`
* `switcher.superSource.boxParameters[box].crop.bottom`
* `switcher.superSource.boxParameters[box].crop.left`
* `switcher.superSource.boxParameters[box].crop.right`
* `switcher.superSource.boxParameters[box].crop.top`
* `switcher.superSource.boxParameters[box].cropped`
* `switcher.superSource.boxParameters[box].enabled`
* `switcher.superSource.boxParameters[box].inputSource`
* `switcher.superSource.boxParameters[box].position.x`
* `switcher.superSource.boxParameters[box].position.y`
* `switcher.superSource.boxParameters[box].size`
* `switcher.superSource.clip`
* `switcher.superSource.config.boxes`
* `switcher.superSource.fillSource`
* `switcher.superSource.foreground`
* `switcher.superSource.gain`
* `switcher.superSource.invertKey`
* `switcher.superSource.keySource`
* `switcher.superSource.lightSource.altitude`
* `switcher.superSource.lightSource.direction`
* `switcher.superSource.preMultiplied`

#### tally
* `switcher.tally.byIndex.flags[a].preview`
* `switcher.tally.byIndex.flags[a].program`
* `switcher.tally.byIndex.sources`
* `switcher.tally.bySource.flags[videoSource].preview`
* `switcher.tally.bySource.flags[videoSource].program`
* `switcher.tally.bySource.sources`
* `switcher.tally.channelConfig.tallyChannels`

#### topology
* `switcher.topology.auxBusses`
* `switcher.topology.colorGenerators`
* `switcher.topology.downstreamKeyers`
* `switcher.topology.dVEs`
* `switcher.topology.hasSDOutput`
* `switcher.topology.mEs`
* `switcher.topology.sources`
* `switcher.topology.stingers`
* `switcher.topology.superSources`

#### transition
* `switcher.transition[mE].dip.input`
* `switcher.transition[mE].dip.rate`
* `switcher.transition[mE].dVE.clip`
* `switcher.transition[mE].dVE.enableKey`
* `switcher.transition[mE].dVE.fillSource`
* `switcher.transition[mE].dVE.flipFlop`
* `switcher.transition[mE].dVE.gain`
* `switcher.transition[mE].dVE.invertKey`
* `switcher.transition[mE].dVE.keySource`
* `switcher.transition[mE].dVE.preMultiplied`
* `switcher.transition[mE].dVE.rate`
* `switcher.transition[mE].dVE.reverse`
* `switcher.transition[mE].dVE.style`
* `switcher.transition[mE].framesRemaining`
* `switcher.transition[mE].inTransition`
* `switcher.transition[mE].mix.rate`
* `switcher.transition[mE].nextTransition.background`
* `switcher.transition[mE].nextTransition.key1`
* `switcher.transition[mE].nextTransition.key2`
* `switcher.transition[mE].nextTransition.key3`
* `switcher.transition[mE].nextTransition.key4`
* `switcher.transition[mE].nextTransitionNext.background`
* `switcher.transition[mE].nextTransitionNext.key1`
* `switcher.transition[mE].nextTransitionNext.key2`
* `switcher.transition[mE].nextTransitionNext.key3`
* `switcher.transition[mE].nextTransitionNext.key4`
* `switcher.transition[mE].position`
* `switcher.transition[mE].preview.enabled`
* `switcher.transition[mE].stinger.clip`
* `switcher.transition[mE].stinger.clipDuration`
* `switcher.transition[mE].stinger.gain`
* `switcher.transition[mE].stinger.invertKey`
* `switcher.transition[mE].stinger.mixRate`
* `switcher.transition[mE].stinger.preMultiplied`
* `switcher.transition[mE].stinger.preRoll`
* `switcher.transition[mE].stinger.source`
* `switcher.transition[mE].stinger.triggerPoint`
* `switcher.transition[mE].style`
* `switcher.transition[mE].styleNext`
* `switcher.transition[mE].wipe.fillSource`
* `switcher.transition[mE].wipe.flipFlop`
* `switcher.transition[mE].wipe.pattern`
* `switcher.transition[mE].wipe.position.x`
* `switcher.transition[mE].wipe.position.y`
* `switcher.transition[mE].wipe.rate`
* `switcher.transition[mE].wipe.reverse`
* `switcher.transition[mE].wipe.softness`
* `switcher.transition[mE].wipe.symmetry`
* `switcher.transition[mE].wipe.width`

#### videoMixer
* `switcher.videoMixer.config.modes.f1080i50`
* `switcher.videoMixer.config.modes.f1080i59_94`
* `switcher.videoMixer.config.modes.f1080p23_98`
* `switcher.videoMixer.config.modes.f1080p24`
* `switcher.videoMixer.config.modes.f1080p25`
* `switcher.videoMixer.config.modes.f1080p29_97`
* `switcher.videoMixer.config.modes.f1080p50`
* `switcher.videoMixer.config.modes.f1080p59_94`
* `switcher.videoMixer.config.modes.f2160p23_98`
* `switcher.videoMixer.config.modes.f2160p24`
* `switcher.videoMixer.config.modes.f2160p25`
* `switcher.videoMixer.config.modes.f2160p29_97`
* `switcher.videoMixer.config.modes.f525i59_94_NTSC`
* `switcher.videoMixer.config.modes.f525i59_94_NTSC_16_9`
* `switcher.videoMixer.config.modes.f625i_50_PAL`
* `switcher.videoMixer.config.modes.f625i_50_PAL_16_9`
* `switcher.videoMixer.config.modes.f720p50`
* `switcher.videoMixer.config.modes.f720p59_94`

#### videoMode
* `switcher.videoMode.format`
