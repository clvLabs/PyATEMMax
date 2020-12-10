---
layout: page
title: Docs - Examples - change-settings-multi
permalink: /docs/examples/change-settings-multi/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/change-settings-multi.py)

This script connects to a predefined list of switchers and changes a few settings at once.
```
$ python3 change-settings-multi.py -h
[Tue Nov 24 22:50:20 2020] PyATEMMax demo script: change-settings-multi
usage: change-settings-multi.py [-h] [-v MASTERVOLUME] [-w PREVIEW]
                                [-p PROGRAM] [-m MIXEFFECT]

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
$ python3 change-settings-multi.py -v 0.0 -m 1 -p 1 -w 2
[Tue Nov 24 22:51:17 2020] PyATEMMax demo script: change-settings-multi
[Tue Nov 24 22:51:17 2020] Changing settings in all switchers
[Tue Nov 24 22:51:17 2020] - Master volume: 0.0db
[Tue Nov 24 22:51:17 2020] - PGM Video source: 1 on m/e 1
[Tue Nov 24 22:51:17 2020] - PVW Video source: 2 on m/e 1
[Tue Nov 24 22:51:17 2020] Starting settings update
[Tue Nov 24 22:51:18 2020] ERROR: no response from 192.168.1.110
[Tue Nov 24 22:51:18 2020] Settings updated on ATEM Television Studio HD at 192.168.1.111
[Tue Nov 24 22:51:19 2020] ERROR: no response from 192.168.1.112
[Tue Nov 24 22:51:20 2020] ERROR: no response from 192.168.1.113
[Tue Nov 24 22:51:21 2020] ERROR: no response from 192.168.1.114
[Tue Nov 24 22:51:22 2020] ERROR: no response from 192.168.1.115
[Tue Nov 24 22:51:22 2020] FINISHED: 1/6 switchers updated.
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""change-settings-multi.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import sys
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: change-settings-multi")
{% endhighlight %}

In this example, a custom switcher ip list is created:

{% highlight python %}
SWITCHERS =  [
    "192.168.1.110",
    "192.168.1.111",
    "192.168.1.112",
    "192.168.1.113",
    "192.168.1.114",
    "192.168.1.115",
]

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--mastervolume', help=f'master volume (dB)', type=float)
parser.add_argument('-w', '--preview', help=f'set preview video source', type=int)
parser.add_argument('-p', '--program', help=f'set program video source', type=int)
parser.add_argument('-m', '--mixeffect', help=f'select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

if args.mastervolume is None and args.program is None and args.preview is None:
    print(f"[{time.ctime()}] Please specify a value to change (see help)")
    sys.exit(1)

print(f"[{time.ctime()}] Changing settings in all switchers")

if args.mastervolume is not None:
    print(f"[{time.ctime()}] - Master volume: {args.mastervolume}db")

if args.program is not None:
    print(f"[{time.ctime()}] - PGM Video source: {args.program} on m/e {args.mixeffect}")

if args.preview is not None:
    print(f"[{time.ctime()}] - PVW Video source: {args.preview} on m/e {args.mixeffect}")
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created and the hit count is initialized:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
count = 0
count = 0
{% endhighlight %}

After that, a loop starts for all configured switchers:

{% highlight python %}
print(f"[{time.ctime()}] Starting settings update")
for ip in SWITCHERS:
    print(f"[{time.ctime()}] Connecting to {ip}", end="\r")
count = 0
{% endhighlight %}

* The script tries to connect to the switcher:

{% highlight python %}
    switcher.connect(ip)
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

        print(f"[{time.ctime()}] Settings updated on {switcher.atemModel} at {ip}")
        count += 1
{% endhighlight %}

If `waitForConnection()` returned `False` the script displays an error message.

{% highlight python %}
    else:
        print(f"[{time.ctime()}] ERROR: no response from {ip}")
{% endhighlight %}

And finally the switcher connection is closed

{% highlight python %}
    switcher.disconnect()

print(f"[{time.ctime()}] FINISHED: {count}/{len(SWITCHERS)} switchers updated.")
{% endhighlight %}


## Stripped down version

{% highlight python %}
import PyATEMMax

SWITCHERS =  [
    "192.168.1.110",
    "192.168.1.111",
    "192.168.1.112",
    "192.168.1.113",
    "192.168.1.114",
    "192.168.1.115",
]

switcher = PyATEMMax.ATEMMax()
for ip in SWITCHERS:
    switcher.connect(ip)
    if switcher.waitForConnection(infinite=False):
        switcher.setAudioMixerMasterVolume(0.0)
        switcher.setProgramInputVideoSource(0, 1)
        switcher.setPreviewInputVideoSource(0, 2)
        print(f"Settings updated on {switcher.atemModel} at {ip}")
    else:
        print(f"ERROR: no response from {ip}")
    switcher.disconnect()
{% endhighlight %}
