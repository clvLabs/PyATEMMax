---
layout: page
title: Docs - Examples - tally-str
permalink: /docs/examples/tally-str/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/tally-str.py)

This example uses a different (maybe easier) way to access tally information.

```
$ python3 tally-str.py -h
[Sat Nov 28 15:39:18 2020] PyATEMMax demo script: tally-str
usage: tally-str.py [-h] [-m MIXEFFECT] ip source

positional arguments:
  ip                    switcher IP address
  source                video source number

optional arguments:
  -h, --help            show this help message and exit
  -m MIXEFFECT, --mixeffect MIXEFFECT
                        select mix effect (0/1), default 0
```

It connects to the specified switcher and keeps listening for `PGM`/`PVW` changes to show tally changes for the selected source. Note that in this case, the `preview` input is also watched *at the same price* (or less):

```
$ python3 tally.py 192.168.1.111 5
[Sat Nov 28 15:39:41 2020] PyATEMMax demo script: tally-str
[Sat Nov 28 15:39:41 2020] Connecting to switcher at 192.168.1.111
[Sat Nov 28 15:39:41 2020] Connected, tally 5 is [PVW]
[Sat Nov 28 15:39:41 2020] Watching for tally changes on videoSource 5
[Sat Nov 28 15:39:45 2020] tally 5 is [PGM]
[Sat Nov 28 15:39:48 2020] tally 5 is [PVW]
[Sat Nov 28 15:39:51 2020] tally 5 is []
[Sat Nov 28 15:39:53 2020] tally 5 is [PVW]
[Sat Nov 28 15:39:55 2020] tally 5 is [PGM]
[Sat Nov 28 15:39:56 2020] tally 5 is [PGM][PVW]
[Sat Nov 28 15:39:59 2020] tally 5 is [PGM]
[Sat Nov 28 15:40:01 2020] tally 5 is [PGM][PVW]
[Sat Nov 28 15:40:05 2020] tally 5 is [PGM]
[Sat Nov 28 15:40:06 2020] tally 5 is [PVW]
[Sat Nov 28 15:40:08 2020] tally 5 is []
[Sat Nov 28 15:40:12 2020] tally 5 is [PVW]
[Sat Nov 28 15:40:14 2020] tally 5 is [PGM]
...
```


## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""tally-str.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: tally-str")

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('source', help='video source number', type=int)
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()
{% endhighlight %}

Connect to the switcher and wait for the connection process to finish:

{% highlight python %}
# Connect to the switcher
print(f"[{time.ctime()}] Connecting to switcher at {args.ip}")
switcher = PyATEMMax.ATEMMax()
switcher.connect(args.ip)
switcher.waitForConnection()
{% endhighlight %}

Once it's connected to the switcher it can get information on the selected videoSource for `PGM`/`PVW`.

To do this, it uses `switcher.tally.bySource.flags[]`, a dictionary of `Tally.Flags` objects.

A `Tally.Flags` object can be used in two ways:
* Getting individual `bool` flag values: `tally.program`
* Getting a string representation of the flags: `str(tally)`

{% highlight python %}
# Show initial tally state
tally = switcher.tally.bySource.flags[args.source]
last_tally_str = str(tally)
print(f"[{time.ctime()}] Connected, tally {args.source} is {last_tally_str}")
{% endhighlight %}

From this point on, the script just keeps on asking for the same data and comparing it to see if it has changed. To make it easier to compare, the script uses the string version. Once it knows if anything has changed, it can check the individual tally flags.

{% highlight python %}
# Loop forever watching for changes
print(f"[{time.ctime()}] Watching for tally changes on videoSource {args.source}")
while True:
    # Watch for tally changes
    tally = switcher.tally.bySource.flags[args.source]
    tally_str = str(tally)
    if tally_str != last_tally_str:
        print(f"[{time.ctime()}] Tally {args.source} is {tally_str}")

        # Demonstrate the use of individual tally flags
        if tally.program:
            print(f"[{time.ctime()}] Source {args.source} is on air !!!!")

        last_tally_str = tally_str

    time.sleep(0.01)     # Avoid hogging processor...
{% endhighlight %}


## Stripped down version

{% highlight python %}
import time
import PyATEMMax

SOURCE = 5

switcher = PyATEMMax.ATEMMax()
switcher.connect("192.168.1.111")
switcher.waitForConnection()

last_tally_str = str(switcher.tally.bySource.flags[SOURCE])
print(f"Connected, tally {SOURCE} is {last_tally_str}")

while True:
    tally_str = str(switcher.tally.bySource.flags[SOURCE])
    if tally_str != last_tally_str:
        print(f"Tally {SOURCE} is {tally_str}")
        last_tally_str = tally_str

    time.sleep(0.01)     # Avoid hogging processor...
{% endhighlight %}
