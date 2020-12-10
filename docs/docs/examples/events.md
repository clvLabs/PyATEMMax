---
layout: page
title: Docs - Examples - events
permalink: /docs/examples/events/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/events.py)

This example is a simple demo of the events in the library:
```
$ python3 events.py -h
[Mon Dec  7 03:38:41 2020] PyATEMMax demo script: events
usage: events.py [-h] [-i INTERVAL] ip

positional arguments:
  ip                    switcher IP address

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        wait INTERVAL seconds between changes, default: 1.0
```

It tries to connect to the specified ip and once a second it changes `PGM`/`PVW` to random values between 1 and 8 every `INTERVAL` seconds, while showing information about received data.

```
$ python3 events.py 192.168.1.111
[Mon Dec  7 03:37:30 2020] PyATEMMax demo script: events
[Mon Dec  7 03:37:30 2020] Changing PGM/PVW on ATEM switcher at 192.168.1.111 every 1.0 seconds
[Mon Dec  7 03:37:30 2020] Waiting for connection
[Mon Dec  7 03:37:30 2020] Trying to connect to switcher at 192.168.1.111
[Mon Dec  7 03:37:31 2020] Connected to switcher at 192.168.1.111
[Mon Dec  7 03:37:31 2020] Changing PGM
[Mon Dec  7 03:37:31 2020] Changing PVW
[Mon Dec  7 03:37:31 2020] Received [Time]: Last State Change Time Code
[Mon Dec  7 03:37:31 2020] Received [TlIn]: Tally By Index
[Mon Dec  7 03:37:31 2020] Received [TlSr]: Tally By Source
[Mon Dec  7 03:37:31 2020] Received [PrgI]: Program Input
[Mon Dec  7 03:37:31 2020] Received [PrvI]: Preview Input
[Mon Dec  7 03:37:32 2020] Received [Time]: Last State Change Time Code
[Mon Dec  7 03:37:32 2020] Changing PGM
[Mon Dec  7 03:37:32 2020] Changing PVW
[Mon Dec  7 03:37:32 2020] Received [Time]: Last State Change Time Code
[Mon Dec  7 03:37:32 2020] Received [TlIn]: Tally By Index
[Mon Dec  7 03:37:32 2020] Received [TlSr]: Tally By Source
[Mon Dec  7 03:37:32 2020] Received [PrvI]: Preview Input
[Mon Dec  7 03:37:33 2020] Changing PGM
[Mon Dec  7 03:37:33 2020] Changing PVW
[Mon Dec  7 03:37:33 2020] Received [Time]: Last State Change Time Code
[Mon Dec  7 03:37:33 2020] Received [TlIn]: Tally By Index
[Mon Dec  7 03:37:33 2020] Received [TlSr]: Tally By Source
[Mon Dec  7 03:37:33 2020] Received [PrgI]: Program Input
[Mon Dec  7 03:37:33 2020] Received [PrvI]: Preview Input
...
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""events.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

from typing import Dict, Any

import argparse
import time
import random
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: events")

DEFAULT_INTERVAL = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-i', '--interval',
                    help=f'wait INTERVAL seconds between changes, default: {DEFAULT_INTERVAL}',
                    default=DEFAULT_INTERVAL,
                    type=float)
args = parser.parse_args()

print(f"[{time.ctime()}] Changing PGM/PVW on ATEM switcher at {args.ip} every {args.interval} seconds")
{% endhighlight %}

At this point, the event handlers are defined.

All events receive a `params` dictionary, which in all cases will contain a `switcher` item containing a reference to the switcher object generating the event (to allow using a single event handler for multiple `ATEMMax` instances).

Some events include extra information.

{% highlight python %}
# #######################################################################
#
# PyATEMMax Events
#

def onConnectAttempt(params: Dict[Any, Any]) -> None:
    """Called when a connection is attempted"""

    print(f"[{time.ctime()}] Trying to connect to switcher at {params['switcher'].ip}")


def onConnect(params: Dict[Any, Any]) -> None:
    """Called when the switcher is connected"""

    print(f"[{time.ctime()}] Connected to switcher at {params['switcher'].ip}")


def onDisconnect(params: Dict[Any, Any]) -> None:
    """Called when the switcher disconnects"""

    print(f"[{time.ctime()}] DISCONNECTED from switcher at {params['switcher'].ip}")


def onReceive(params: Dict[Any, Any]) -> None:
    """Called when data is received from the switcher"""

    print(f"[{time.ctime()}] Received [{params['cmd']}]: {params['cmdName']}")
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
{% endhighlight %}

After creating the switcher object, event handlers are registered:

{% highlight python %}
switcher.registerEvent(switcher.atem.events.connectAttempt, onConnectAttempt)
switcher.registerEvent(switcher.atem.events.connect, onConnect)
switcher.registerEvent(switcher.atem.events.disconnect, onDisconnect)
switcher.registerEvent(switcher.atem.events.receive, onReceive)
{% endhighlight %}

Then, the script connects to the switcher and enters an infinite loop changing `PGM` and `PVW` if the switcher is connected:

{% highlight python %}
switcher.connect(args.ip)

while True:
    if switcher.connected:
        print(f"[{time.ctime()}] Changing PGM")
        switcher.setProgramInputVideoSource(0, random.randint(1,8))

        print(f"[{time.ctime()}] Changing PVW")
        switcher.setPreviewInputVideoSource(0, random.randint(1,8))

    time.sleep(args.interval)
{% endhighlight %}

This allows for an easy fit of the library in GUI apps. Just register your event handlers and forget about the switcher :)
