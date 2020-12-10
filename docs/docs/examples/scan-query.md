---
layout: page
title: Docs - Examples - scan-query
permalink: /docs/examples/scan-query/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/scan-query.py)

This example scans a whole nework range (1-254) searching for ATEM switchers and reads some settings:
```
$ python3 scan-query.py -h
[Tue Nov 24 22:28:52 2020] PyATEMMax demo script: scan-query
usage: scan-query.py [-h] [-m MIXEFFECT] range

positional arguments:
  range                 IP address range (e.g) 192.168.1

optional arguments:
  -h, --help            show this help message and exit
  -m MIXEFFECT, --mixeffect MIXEFFECT
                        select mix effect (0/1), default 0
```

It tries to connect to all the addresses in the range, reads a few settings and reports result.
```
$ python3 scan-query.py 192.168.1
[Tue Nov 24 22:30:07 2020] PyATEMMax demo script: scan-query
[Tue Nov 24 22:30:07 2020] Scanning network range 192.168.1.* for ATEM switchers
[Tue Nov 24 22:30:19 2020] ATEM Television Studio HD found at 192.168.1.111 - Master Volume: 0.0dB - PVW: CAM1 - PGM: HPDK
[Tue Nov 24 22:30:33 2020] FINISHED: 1 ATEM switchers found.

```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""scan-query.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: scan-query")

parser = argparse.ArgumentParser()
parser.add_argument('range', help='IP address range (e.g) 192.168.1')
parser.add_argument('-m', '--mixeffect', help=f'select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

print(f"[{time.ctime()}] Scanning network range {args.range}.* for ATEM switchers")
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created and the hit count is initialized:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
count = 0
{% endhighlight %}

After that, a loop starts for values (1-254):

{% highlight python %}
for i in range(1,255):
{% endhighlight %}

* The corresponding ip address is built

{% highlight python %}
    ip = f"{args.range}.{i}"
    print(f"[{time.ctime()}] Checking {ip}", end="\r")
{% endhighlight %}

* The script tries to connect to the switcher and shows a message if the connection could be established. See the parameters in `waitForConnection()`
    * `infinite=False` means we don't want to wait forever. The library will use the default wait time.
    * `waitForFullHandshake=False` means we want to stop waiting as soon as the first message has been received from the switcher (because we're doing a `scan`, we just care about connectivity, not data)

{% highlight python %}
    switcher.connect(ip)
    if switcher.waitForConnection(infinite=False, waitForFullHandshake=False):
{% endhighlight %}

* If this first wait succeeds it means we received a response to the initial connection request.
* At this point we can keep on waiting for the complete reception of the data snapshot from the switcher.
    * `infinite=False` means we don't want to wait forever. The library will use the default wait time.
    * `waitForFullHandshake` is `True` by default, which means we want to wait until the whole set of switcher settings has been received.

{% highlight python %}
        # If the switcher answered the handshake we can wait a bit longer...
        if switcher.waitForConnection(infinite=False):
{% endhighlight %}

* Once the switcher data has been received, data can be read and displayed

{% highlight python %}
            # Now we have all switcher settings!
            pvw = switcher.previewInput[args.mixeffect].videoSource
            pgm = switcher.programInput[args.mixeffect].videoSource
            pvwName = switcher.inputProperties[pvw].shortName
            pgmName = switcher.inputProperties[pgm].shortName

            print(f"[{time.ctime()}] {switcher.atemModel} found at {ip}"
                    f" - Master Volume: {switcher.audioMixer.master.volume}dB"
                    f" - PVW: {pvwName}"
                    f" - PGM: {pgmName}" )
            count += 1
    switcher.disconnect()

print(f"[{time.ctime()}] FINISHED: {count} ATEM switchers found.")
{% endhighlight %}


## Stripped down version

{% highlight python %}
import PyATEMMax

switcher = PyATEMMax.ATEMMax()

for i in range(1,255):
    ip = f"192.168.1.{i}"
    print(f"Checking {ip}", end="\r")

    switcher.connect(ip)
    if switcher.waitForConnection(infinite=False, waitForFullHandshake=False):
        if switcher.waitForConnection(infinite=False):
            pvw = switcher.previewInput[0].videoSource
            pgm = switcher.programInput[0].videoSource
            pvwName = switcher.inputProperties[pvw].shortName
            pgmName = switcher.inputProperties[pgm].shortName

            print(f"{switcher.atemModel} found at {ip}"
                    f" - Master Volume: {switcher.audioMixer.master.volume}dB"
                    f" - PVW: {pvwName}"
                    f" - PGM: {pgmName}" )
    switcher.disconnect()
{% endhighlight %}
