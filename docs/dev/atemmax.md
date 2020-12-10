---
layout: page
title: /dev - ATEMMax
permalink: /dev/atemmax/
---

## Composition of the ATEMMax object

To keep the code organized, the contents of the `ATEMMax` class have been split into several modules.
* `ATEMSwitcherState`: switcher state data objects.
* `ATEMSetterMethods`: setter methods for data.
* `ATEMCommandHandlers`: protocol message handlers.

`ATEMMax` derives from:
* `ATEMConnectionManager` to expose methods as `connect()` and `waitForConnection()`
* `ATEMSwitcherState` to expose data members as `audioMixer` and `programInput`
* `ATEMSetterMethods` to expose setter methods as `setAudioMixerMasterVolume`

And uses `ATEMCommandHandlers` by composition because command handlers do not need to be exposed.
