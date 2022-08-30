---
layout: page
title: Docs - Examples - change-settings
permalink: /docs/examples/change-settings/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/change-settings.py)

This script connects to a switcher and changes a few settings at once.
```
$ python3 change-settings.py -h
[Tue Nov 24 22:36:06 2020] PyATEMMax demo script: change-settings
usage: change-settings.py [-h] [-v MASTERVOLUME] [-w PREVIEW] [-p PROGRAM]
                          [-m MIXEFFECT]
                          ip

positional arguments:
  ip                    switcher IP address

optional arguments:
  -h, --help            show this help message and exit
  -v MASTERVOLUME, --mastervolume MASTERVOLUME
                        master volume (dB)
  -w PREVIEW, --preview PREVIEW
                        set preview video source
  -p PROGRAM, --program PROGRAM
                        set program video source
  -m MIXEFFECT, --mixeffect MIXEFFECT
                        select mix effect (0/1), default 0
```


```
$ python3 change-settings.py 192.168.1.111 -v 1.7 -p 3 -w 2
[Tue Nov 24 22:37:26 2020] PyATEMMax demo script: change-settings
[Tue Nov 24 22:37:26 2020] Changing settings in 192.168.1.111
[Tue Nov 24 22:37:26 2020] - Master volume: 1.7db
[Tue Nov 24 22:37:26 2020] - PGM Video source: 3 on m/e 0
[Tue Nov 24 22:37:26 2020] - PVW Video source: 2 on m/e 0
[Tue Nov 24 22:37:26 2020] Starting settings update
[Tue Nov 24 22:37:26 2020] Connecting to 192.168.1.111
[Tue Nov 24 22:37:26 2020] Settings updated on ATEM Television Studio HD at 192.168.1.111
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](./index.md))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""change-settings.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import sys
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: change-settings")

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-v', '--mastervolume', help=f'master volume (dB)', type=float)
parser.add_argument('-w', '--preview', help=f'set preview video source', type=int)
parser.add_argument('-p', '--program', help=f'set program video source', type=int)
parser.add_argument('-m', '--mixeffect', help=f'select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

if args.mastervolume is None and args.program is None and args.preview is None:
    print(f"[{time.ctime()}] Please specify a value to change (see help)")
    sys.exit(1)

print(f"[{time.ctime()}] Changing settings in {args.ip}")

if args.mastervolume is not None:
    print(f"[{time.ctime()}] - Master volume: {args.mastervolume}db")

if args.program is not None:
    print(f"[{time.ctime()}] - PGM Video source: {args.program} on m/e {args.mixeffect}")

if args.preview is not None:
    print(f"[{time.ctime()}] - PVW Video source: {args.preview} on m/e {args.mixeffect}")

switcher = PyATEMMax.ATEMMax()
count = 0

print(f"[{time.ctime()}] Starting settings update")
print(f"[{time.ctime()}] Connecting to {args.ip}")
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created the script waits for connection:

{% highlight python %}
switcher.connect(args.ip)
if switcher.waitForConnection(infinite=False):
{% endhighlight %}

Once connected, the provided values are used to change the switcher settings.

{% highlight python %}
    if args.mastervolume is not None:
        switcher.setAudioMixerMasterVolume(args.mastervolume)

    if args.program is not None:
        switcher.setProgramInputVideoSource(args.mixeffect, args.program)

    if args.preview is not None:
        switcher.setPreviewInputVideoSource(args.mixeffect, args.preview)

    print(f"[{time.ctime()}] Settings updated on {switcher.atemModel} at {args.ip}")
    count += 1
{% endhighlight %}

If `waitForConnection()` returned `False` the script displays an error message.

{% highlight python %}
else:
    print(f"[{time.ctime()}] ERROR: no response from {args.ip}")
{% endhighlight %}

And finally the switcher connection is closed

{% highlight python %}
switcher.disconnect()
{% endhighlight %}


## Stripped down version

{% highlight python %}
import PyATEMMax

switcher = PyATEMMax.ATEMMax()
switcher.connect("192.168.1.111")
if switcher.waitForConnection(infinite=False):
    switcher.setAudioMixerMasterVolume(0)
    switcher.setProgramInputVideoSource(0, 1)
    switcher.setPreviewInputVideoSource(0, 2)
    print("Settings updated")
else:
    print("ERROR: no response from switcher")
switcher.disconnect()
{% endhighlight %}
