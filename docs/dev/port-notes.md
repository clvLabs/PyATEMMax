---
layout: page
title: /dev - Port from original Arduino libraries
permalink: /dev/port-notes/
---


The original library code can be found at [SKAARHOJ-Open-Engineering GitHub repo][skaarhoj-repo].

In the original version, features are split in several libraries (`ATEMbase`, `ATEMext`, `ATEMmax`, `ATEMmin`, `ATEMstd`, `ATEMuni`) as program space is a valuable resource when compiling for Arduino or other MCU platforms.

This library tries to reproduce the features of `ATEMmax` by translating the original code of `ATEMbase` and `ATEMmax`.
* `ATEMbase` has been ported as `ATEMConnectionManager`.
* `ATEMmax` has been ported as `ATEMMax`.

The intention has been to mantain the code as similar to the original as I could, so anybody that has used the original libraries before should be able to use this version with no problems. This has not been always possible due to both differences between C and Python and differences between Arduino and PC (memory limitations, etc). Also, I have to recognize that in a few cases I've let myself go and made some change _here and there_.

Some details:
* Fixed local port number for UDP connections has been deprecated, so the ported library won't have it.
* Renamed `connect()` as `_connect()`.
* Renamed `begin()` as `connect()`.
* Added `disconnect()`.
* Added `ping()`.
* Most `getXXX()` methods have been omitted in favor of the use of the `ATEMMax.data` class members (variables).
* Known non-implemented protocol commands can be differenced from unknown/malformed commands.
* Stored information for all 20 cameras in `Camera Control` instead of 8 in the Arduino version.
* Python's `logging` has been used instead of the original serial output.
* Protocol definitions have been moved to a new module: `ATEMProtocol`.
* Several modules have been added and some have been renamed.
* Buffer sizes have been increased, as a PC has a lot more of memory and can handle bigger input buffers.
* Some code related to buffer handling has been adapted.
* In certain situations the code has been slightly "pythonized" (sometimes keeping the original code structure made things uglier, sometimes it was too easy and cheap to add nice features :).

[skaarhoj-repo]: https://github.com/kasperskaarhoj/SKAARHOJ-Open-Engineering
