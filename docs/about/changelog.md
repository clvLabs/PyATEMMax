---
layout: page
title: About - Changelog
permalink: /about/changelog/
---

## 1.0b8 (2022-08-17)
* Fixed [issue #14](https://github.com/clvLabs/PyATEMMax/issues/14): execMacroStopRecording not working.
* Fixed the range of the `zoomSpeed` parameter in `setCameraControlZoomSpeed()` ([issue #18](https://github.com/clvLabs/PyATEMMax/issues/18)).
* Added new (optional) parameters to `execMacroRecord()` so macro name and description can be specified ([issue #15](https://github.com/clvLabs/PyATEMMax/issues/15)).

## 1.0b7 (2022-01-25)
* Fixed `Super Source Box` message byte order. [PR #13](https://github.com/clvLabs/PyATEMMax/pull/13) -  Thank you [Sergey](https://github.com/s-kol-gg) !

## 1.0b6 (2021-12-01)
* Some documentation fixes
* Fixed wrong byte index in _handleSSBP ([issue #9](https://github.com/clvLabs/PyATEMMax/issues/9)) - Thank you [kellyzdude](https://github.com/kellyzdude) !
* Increased number of available aux channels to 32 - Thank you Jan Görgen ! (using ATEM Constellation 8K)

## 1.0b5 (2021-09-28)
* Protect against empty packed values ([issue #4](https://github.com/clvLabs/PyATEMMax/issues/4)) - Thank you [slampants](https://github.com/slampants) !

## 1.0b4 (2021-05-16)
* Fixed bug in `ATEMSetterMethods.setTransitionWipePattern()` ([issue #5](https://github.com/clvLabs/PyATEMMax/issues/5))

## 1.0b3 (2021-02-23)
* Fixed bug in `ATEMProtocol.getVideoSrc/getAudioSrc()` ([issue #3](https://github.com/clvLabs/PyATEMMax/issues/3))

## 1.0b2 (2021-01-25)
* Fixed bug in `ATEMBuffer.getFlag()` ([issue #2](https://github.com/clvLabs/PyATEMMax/issues/2))

## 1.0b1 (2020-12-10)
* First release.
* Ported original code.
* Moved protocol info to `ATEMProtocol`.
* Moved switcher state to `ATEMSwitcherState`.
* Moved `set` methods to `ATEMSetterMethods`.
* Created `StateData` class tree.
* Added threads to handle communications.
* Created documentation.
* Created Python package.

## 0.0 (2020-11-16)
* Started development.
